from flask import Flask, render_template, Markup
import pymongo
import mission_to_mars

conn = 'mongodb://127.0.0.1:27017'
client = pymongo.MongoClient(conn)

db = client.mars_DB

app = Flask(__name__)

@app.route('/')
def index():
    '''Query db for mars data, and display'''
    mars_data = list(db.mars_collection.find())
    mars_data[0]['table_html']=Markup(mars_data[0]['table_html'])
    return render_template('index.html', data = mars_data[0])

@app.route('/scrape')
def scrape():
    '''Scrape mars data from internet, store into db'''
    mars_data =  mission_to_mars.scrape()
    db.mars_collection.drop()
    db.mars_collection.insert_one(mars_data)
    mars_data = list(db.mars_collection.find())
    mars_data[0]['table_html']=Markup(mars_data[0]['table_html'])
    return render_template('index.html', data = mars_data[0])

if __name__=='__main__':
    app.run(debug=True)