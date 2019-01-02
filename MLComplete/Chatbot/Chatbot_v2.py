from generatengrams import ngrammatch
from Contexts import *
import json
from Intents import *
import random
import os
import re
import pandas as pd

def check_actions(current_intent, attributes, context): 
    print("Chatbot_v2_check_actions")
    action_performed = current_intent.action
    if current_intent.action == 'GetMobileIssues':
        menuoptions = getAttributeValue(attributes, "menuoptions")

        subMenuOptions = getSubMenuOptions(menuoptions)
        if len(subMenuOptions) == 0:
            action_performed = 'No options found as per your choice, Please try with another combination.'
        else:
            action_performed = "Found the following Sub-Menu options for you \n" + "\n".join(subMenuOptions)
    
    #elif if required

    context = IntentComplete()
    return action_performed, context

def getAttributeValue(attributes, key):
    print("Chatbot_v2_getAttributeValue")
    value = str(attributes[key])
    value = value.strip().lower()

    return value

def getSubMenuOptions(menuOption):
     print("Chatbot_v2_getSubMenuOptions")
     fn_tolower = lambda x : x.lower().strip()

     subMenuOptions = pd.read_csv('Chatbot/database/SubMenuOptionsList.csv', converters={'Option': fn_tolower})
     query = "Option == '" + menuOption + "'";

     selectedOption = subMenuOptions.query(query)

     if len(selectedOption) == 0: # No Options found
        return []
     else:
        return list(selectedOption["SubMenuOptions"])

def check_required_params(current_intent, attributes, context):
    print("Chatbot_v2_check_required_params")
    '''Collects attributes pertaining to the current intent'''
    for para in current_intent.params:
        if para.required:
            if para.name not in attributes:
                #Example of where the context is born, implemented in Contexts.py
                if para.name=='RegNo':
                    context = GetRegNo()
                if para.name == 'letter':
                    context = GetLetter()
                if para.name == 'numerology':
                    context = GetNumerlogy()
                #returning a random prompt frmo available choices.
                return random.choice(para.prompts), context

    return None, context

def input_processor(user_input, context, attributes, intent):  
    print("Chatbot_v2_input_processor")
    # uinput = TextBlob(user_input).correct().string
    
    #update the attributes, abstract over the entities in user input
    attributes, cleaned_input = getattributes(user_input, context, attributes)
    
    return attributes, cleaned_input

def loadIntent(path, intent):
    print("Chatbot_v2_loadIntent: Path:"+path+"     Intent:"+intent)
    with open(path) as fil:
        dat = json.load(fil)
        intent = dat[intent]
        return Intent(intent['intentname'],intent['Parameters'], intent['actions'])

def intentIdentifier(clean_input, context,current_intent):
    print("Chatbot_v2_IntentIdentifier")
    if context.active == False:
        return current_intent

    clean_input = clean_input.lower()
    
    #Scoring Algorithm, can be changed.
    scores = ngrammatch(clean_input)
    
    #choosing here the intent with the highest score
    scores = sorted_by_second = sorted(scores, key=lambda tup: tup[1])

    # If current intent is not none, stick with the ongoing intent else select an intent.
    if current_intent == None:
        if clean_input == 'mobile':
            current_intent = loadIntent('Chatbot/params/newparams.cfg', 'MobileTroubleShooting')
        elif clean_input == "baby":
            current_intent = loadIntent('Chatbot/params/newparams.cfg', 'BabyNameSuggestion')
        elif clean_input == 'restaurant':
            current_intent = loadIntent('Chatbot/params/newparams.cfg', 'RestaurantBooking')
        else:
            current_intent = loadIntent('Chatbot/params/newparams.cfg', scores[-1][0])
        
    return current_intent

def getattributes(uinput,context,attributes):
    print("Chatbot_v2_getattributes")
    '''This function marks the entities in user input, and updates
    the attributes dictionary'''
    #Can use context to context specific attribute fetching
    if context.name.startswith('IntentComplete'):
        return attributes, uinput
    else:
        #Code can be optimised here, loading the same files each time suboptimal 
        files = os.listdir('Chatbot/entities/')
        entities = {}
        for fil in files:
            if fil.endswith('.dat'):
                lines = open('Chatbot/entities/'+fil).readlines()
                for i, line in enumerate(lines):
                    lines[i] = line[:-1]
                entities[fil[:-4]] = '|'.join(lines)

        #Extract entity and update it in attributes dict
        for entity in entities:
            for i in entities[entity].split('|'):
                if i.lower() in uinput.lower() and entity not in attributes.keys():
                    attributes[entity] = i

        # Convert Male,Boy and Female/Girl to M/F
        for att in attributes:
            # print(att + ' : ' + attributes[att])
            if att.lower() == 'gender':
                attributes[att] = selectGenderType(attributes[att])
            
        for entity in entities:
            uinput = re.sub(entities[entity],r'$'+entity,uinput,flags=re.IGNORECASE)

        #Example of where the context is being used to do conditional branching.
        if context.name=='GetRegNo' and context.active:
            print(attributes)
            match = re.search('[0-9]+', uinput)
            if match:
                uinput = re.sub('[0-9]+', '$regno', uinput)
                attributes['RegNo'] = match.group()
                context.active = False

        # REGEX to get a single letter for baby name's starting character
        if context.name == 'GetLetter' and context.active:
            matched_char = re.search('[a-z]', uinput.lower())
            if matched_char:
                uinput = re.sub('[a-zA-Z]', '$letter', uinput.lower())
                attributes['letter'] = matched_char.group()
                context.active = False

        # REGEX to find the selected number.
        if context.name == 'GetNumerology' and context.active:
            matchedNumber = re.search('[0-9]', uinput)
            if matchedNumber:
                uinput = re.sub('[0-9]', '$numerology', uinput)
                attributes['numerology'] = matchedNumber.group()
                context.active = False

        return attributes, uinput

# In[ ]:

def selectGenderType(gender):
    print("Chatbot_v2_selectGenderType")
    if gender.lower() == "male" or gender.lower() == "boy" or gender.lower() == "m":
        return 'M'
    else:
        return 'F'

class Session:
    def __init__(self, attributes=None, active_contexts=[FirstGreeting(), IntentComplete() ]):
        print("Chatbot_v2_init: Self ")
        '''Initialise a default session'''
        
        #Active contexts not used yet, can use it to have multiple contexts
        self.active_contexts = active_contexts
        
        #Contexts are flags which control dialogue flow, see Contexts.py        
        self.context = FirstGreeting()
        
        #Intent tracks the current state of dialogue
        #self.current_intent = First_Greeting()
        self.current_intent = None
        
        #attributes hold the information collected over the conversation
        self.attributes = {}
       
    #unused   
    def update_contexts(self):
        '''Not used yet, but is intended to maintain active contexts'''
        for context in self.active_contexts:
            if context.active:
                context.decrease_lifespan()

    def reply(self, user_input):
        print("Chatbot_v2_reply: Self ")
        
        self.attributes, clean_input = input_processor(user_input, self.context, self.attributes, self.current_intent)
        
        self.current_intent = intentIdentifier(clean_input, self.context, self.current_intent)
        
        prompt, self.context = check_required_params(self.current_intent, self.attributes, self.context)

        #prompt being None means all parameters satisfied, perform the intent action
        if prompt is None:
            if self.context.name != 'IntentComplete':
                prompt, self.context = check_actions(self.current_intent, self.attributes, self.context)
        
        #Resets the state after the Intent is complete
        if self.context.name == 'IntentComplete':
            self.attributes = {}
            self.context = FirstGreeting()
            self.current_intent = None
        
        return prompt


# In[ ]:


# session = Session()
def restart():
    print("Chatbot_v2_restart")
    print('BOT: Hi! How may I assist you?')
    session = Session()
    while True:
        inp = input('User: ')
        if inp == 'restart' or inp == 'Restart':
            print("Restarting")
            if session.current_intent is not None:
                session.current_intent.active = False
                session.context = IntentComplete()
                session.reply(inp)

            print('BOT: Hi! How may I assist you?')
            inp = input('User: ')

        print('BOT: ', session.reply(inp), '\t\t(Type "restart" to restart)')

restart()
