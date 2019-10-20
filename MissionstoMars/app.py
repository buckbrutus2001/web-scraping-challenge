from flask import Flask, render_template, redirect
import pymongo
import scrape


app = Flask(__name__)


# Create connection variable
# conn = 'mongodb://localhost:27017'
# Pass connection to the pymongo instance.
client = pymongo.MongoClient()

mars_mongo = client.mission_to_mars_db


@app.route('/')
def home():
    
    mars_data = mars_mongo.db.mars_collection.find_one()
    return  render_template('index.html', mars_data=mars_data)


@app.route('/scrape')
def web_scrape():

    mars_data = mars_mongo.db.mars_data
    mars_data = scrape.scrape()
    mars_mongo.mars_collection.update(
        {},
        mars_data,
        upsert=True
    )
    return  redirect('/')


if __name__ == "__main__":
    app.run(debug=True)