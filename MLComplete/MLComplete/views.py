"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from MLComplete import app
import pyodbc
import pandas as pd

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )



@app.route('/testapi/<name>')
def testapi(name):
    """Renders the home page."""
    return name


@app.route('/enternewurl')
def new_student():
   return render_template('urlbank.html')

@app.route('/addurl',methods = ['POST', 'GET'])
def addrec():
    return 'record successfully added'

#cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                      "Server=EXLRH053L;"
#                      "Database=WebCrawling;"
#                      "Trusted_Connection=yes;")

#@app.route('/geturltypes',methods = ['POST', 'GET'])
#def geturltypes():
#    cursor = cnxn.cursor()
#    query = 'SELECT * FROM UrlType'
#    df = pd.read_sql(query,cnxn)
#    return df.to_json(orient='records')

#@app.route('/geturls',methods = ['POST', 'GET'])
#def geturls():
#    cursor = cnxn.cursor()
#    query = 'SELECT * FROM Url'
#    df = pd.read_sql(query,cnxn)
#    return df.to_json(orient='records')

#@app.route('/getkeywords',methods = ['POST', 'GET'])
#def getkeywords():
#    cursor = cnxn.cursor()
#    query = 'SELECT * FROM Keyword'
#    df = pd.read_sql(query,cnxn)
#    return df.to_json(orient='records')


#@app.route('/inserturltype/<type>',methods = ['POST','GET'])
#def inserturltype(type):
#    cursor = cnxn.cursor()
#    query = "INSERT INTO [dbo].[UrlType]([Name]) VALUES ('"+type+"')"
#    cursor.execute(query)

#    cnxn.commit()
#    cursor.close()
#    cnxn.close()
#    return 'Url Type added successfully'

#@app.route('/inserturl/<name>/<navigationsteps>/<downloadlink>/<urlTypeId>',methods = ['POST','GET'])
#def inserturl(name,navigationsteps,downloadlink,urlTypeId):
#    cursor = cnxn.cursor()
#    query = "INSERT INTO [dbo].[Url]([Name],[NavigationSteps],[DownloadLink],[UrlTypeId]) VALUES ('"+name+"','"+navigationsteps+"','"+downloadlink+"','"+urlTypeId+"')"
#    cursor.execute(query)

#    cnxn.commit()
#    cursor.close()
#    cnxn.close()
#    return 'Url added successfully'

#@app.route('/insertkeyword/<keyword>/<synonyms>',methods = ['POST','GET'])
#def insertkeyword(keyword,synonyms):
#    cursor = cnxn.cursor()
#    query = "INSERT INTO [dbo].[Keyword] ([Name],[Synonyms]) VALUES('"+keyword+"','"+synonyms+"')"
#    cursor.execute(query)

#    cnxn.commit()
#    cursor.close()
#    cnxn.close()
#    return 'Keyword added successfully'



#@app.route('/updateurltype/<id>/<type>',methods = ['POST','GET'])
#def updateUrl(id,type):
#    cursor = cnxn.cursor()
#    query = "Update [dbo].[UrlType] SET [Name]='"+type+"' where Id="+id
#    cursor.execute(query)

#    cnxn.commit()
#    cursor.close()
#    cnxn.close()
#    return 'UrlType updated successfully'


#@app.route('/updateurl/<id>/<name>/<navigationsteps>/<downloadlink>/<urlTypeId>',methods = ['POST','GET'])
#def updateurl(id,name,navigationsteps,downloadlink,urlTypeId):
#    cursor = cnxn.cursor()
#    query = "Update [dbo].[Url] set [Name]='"+name+"',[NavigationSteps]='"+navigationsteps+"',[DownloadLink]='"+downloadlink+"',[UrlTypeId]='"+urlTypeId+"' where Id = '"+id+"'"
#    cursor.execute(query)

#    cnxn.commit()
#    cursor.close()
#    cnxn.close()
#    return 'Url updated successfully'

#@app.route('/updatekeyword/<id>/<name>/<synonyms>',methods = ['POST','GET'])
#def updatekeyword(id,name,synonyms):
#    cursor = cnxn.cursor()
#    query = "Update [dbo].[Keyword] set [Name]='"+name+"',[Synonyms]='"+synonyms+"' where Id = '"+id+"'"
#    cursor.execute(query)

#    cnxn.commit()
#    cursor.close()
#    cnxn.close()
#    return 'Keyword updated successfully'



#@app.route('/deleteurltype/<id>',methods = ['POST','GET'])
#def deleteurltype(id):
#    cursor = cnxn.cursor()
#    query = "Delete from [dbo].[UrlType] where Id="+id
#    cursor.execute(query)

#    cnxn.commit()
#    cursor.close()
#    cnxn.close()
#    return 'UrlType deleted successfully'


#@app.route('/deleteurl/<id>',methods = ['POST','GET'])
#def deleteurl(id):
#    cursor = cnxn.cursor()
#    query = "Delete from [dbo].[Url] where Id="+id
#    cursor.execute(query)

#    cnxn.commit()
#    cursor.close()
#    cnxn.close()
#    return 'Url deleted successfully'

#@app.route('/deletekeyword/<id>',methods = ['POST','GET'])
#def deletekeyword(id):
#    cursor = cnxn.cursor()
#    query = "Delete from [dbo].[Keyword] where Id = '"+id+"'"
#    cursor.execute(query)

#    cnxn.commit()
#    cursor.close()
#    cnxn.close()
#    return 'Keyword deleted successfully'