import scrape_mars
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect

app = Flask(__name__) 

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")


@app.route("/")
def index():

   
    infomars = mongo.db.collection.find_one()
    return render_template("index.html", dict_web=infomars)


    

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_info = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_info, upsert=True)

    # Redirect back to home page
    return redirect("/")

    #return render_template("index.html", dict_web=dict_web)

if __name__ == "__main__":
    app.run(debug=True)
