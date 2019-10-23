from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/scrape_mars_app")


@app.route("/")
def index():
    marslinks = mongo.db.marslinks.find_one()
    return render_template("index.html", marslinks=marslinks)


@app.route("/scrape")
def scraper():
    marslinks = mongo.db.marslinks
    marslinks_data = scrape_mars.scrape()
    marslinks.update({}, marslinks_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)