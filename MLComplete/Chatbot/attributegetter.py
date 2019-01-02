from nltk.tag import StanfordNERTagger
from pycorenlp import StanfordCoreNLP
from nltk import sent_tokenize, word_tokenize
from marisa_trie import Trie
import re
import datetime
import os
nlp = StanfordCoreNLP('http://localhost:9000')


#def getattributes(uinput,context,attributes):
    
#    if context.name.startswith('IntentComplete'):
#        return attributes, uinput
#    else:

#        files = os.listdir('./entities/')
#        entities = {}
#        for fil in files:
#            lines = open('./entities/'+fil).readlines()
#            for i, line in enumerate(lines):
#                lines[i] = line[:-1]
#            entities[fil[:-4]] = lines

#        matches = {}

#        for entity in entities:
#            entities[entity]
#            for entity in entities:
#                print entities
#            uinput = re.sub(match,r'$person',uinput,flags=re.IGNORECASE)


#        continue

#        uinput_tokenized = word_tokenize(uinput)
#        if context.name=='FirstGreeting':
#            names,matches = getNames(uinput,context,matches)
#            # uinput_tokenized = replaceNames(uinput_tokenized, context)   
#            if names!=[]:
#                attributes['PassengerName'] = names[0]

#            # print matches,"after checking names"
#            cities_trie, cities_dict = loadCities('./data/cities.dat')
#            attributes,matches = getlocation(uinput,cities_trie,cities_dict,context,attributes,matches)
#            # uinput_tokenized = replacelocation(uinput.split(),cities_trie, cities_dict, context)
#            # print matches,"after checking location"
#            attributes,matches = getdate(uinput,context,attributes,matches)
#            # uinput_tokenized = getdate(uinput.split(),context,attributes,True)
#            # print matches,"after replacing date"

#            # print uinput



#            for match in matches['Name']:
#                uinput = re.sub(match,r'$person',uinput,flags=re.IGNORECASE)

#            for match in matches['Date']:
#                uinput = re.sub(match,r'$date',uinput,flags=re.IGNORECASE)

#            for match in matches['Location']:
#                uinput = re.sub(match,r'$location',uinput,flags=re.IGNORECASE)
            
#            return attributes,uinput
#            # cleaned_input = replaceplaceholders(uinput)

#        if '_'.join(context.name.split('_')[2:])=='From':
#            cities_trie, cities_dict = loadCities('./data/cities.dat')
#            attributes,matches = getlocation(uinput,cities_trie, cities_dict, context,attributes,matches)

#        if '_'.join(context.name.split('_')[2:])=='To':
#            cities_trie, cities_dict = loadCities('./data/cities.dat')
#            attributes,matches = getlocation(uinput,cities_trie, cities_dict, context,attributes,matches)

#        if '_'.join(context.name.split('_')[2:])=='Date':
#            attributes,matches = getdate(uinput,context,attributes,matches)

#        if '_'.join(context.name.split('_')[2:])=='PassengerName':
#            names,matches = getNames(uinput, context,matches)   
#            if names!=[]:
#                attributes['PassengerName'] = names[0]
                

#        return attributes, uinput
