from flask import Flask
import pymongo

client=pymongo.MongoClient("...")

app = Flask(__name__,
            static_folder="public",
            static_url_path="/")

@app.route('/')
def index():
    return "Hello"

app.secret_key="any string"
app.run()