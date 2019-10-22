from flask import Flask, render_template, redirect
import pymongo
import scrape


app = Flask(__name__)


# Create connection variable
conn = 'mongodb://localhost:27017'
# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

mars_db = client.mission_to_mars_db



@app.route('/')
def home():
    
    mars = mars_db.db.mars_collection.find_one()
    return  render_template('index.html', mars=mars)


@app.route('/scrape')
def web_scrape():

    mars = mars_db.db.mars_collection
    mars_scraped = scrape.scrape()
    mars.update(
        {},
        mars_scraped,
        upsert=True
    )
    return  redirect('/')


if __name__ == "__main__":
    app.run(debug=True)