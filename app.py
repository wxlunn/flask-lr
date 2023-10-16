from flask import Flask
import pymongo

client=pymongo.MongoClient("mongodb+srv://root:root0320@trainingcluster.ymqgddi.mongodb.net/?retryWrites=true&w=majority")

app = Flask(__name__,
            static_folder="public",
            static_url_path="/")

@app.route('/')
def index():
    return "Hello"

app.secret_key="any string"
app.run()