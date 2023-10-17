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

@app.route("/signup", method=["POST"])
def signup():
    # receive data from frontend 
    nickname = request.form["nickname"]
    email = request.form["email"]
    password = request.form["password"]

    # db check and write
    collection = db.user
    result=collection.find_one({
        "email":email
    })
    if result != None:
        return redirect("/error?meg=email has been used")
    
    collection.insert_one({
        "nickname":nickname,
        "email":email,
        "password":password
    })

    return redirect('/')


app.secret_key="any string"
app.run()