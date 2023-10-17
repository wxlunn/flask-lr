from flask import *
import pymongo

client=pymongo.MongoClient("")
db=client.member_system
print("db connect successfully")

app = Flask(__name__,
            static_folder="public",
            static_url_path="/")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def memeber():
    return render_template("member.html")

@app.route("/error")
def error():
    msg = request.args.get("msg", "error occur, please contact us")
    return render_template("error.html", msg=msg)

app.secret_key="any string"
app.run()