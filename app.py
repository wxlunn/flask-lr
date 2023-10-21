from flask import *
import pymongo

# mongodb init
client=pymongo.MongoClient("mongodb url")
db=client.member_system
print("db connect successfully")

# server init
app = Flask(__name__,
            static_folder="static",
            static_url_path="/static")

app.secret_key="any string"

# homepage
@app.route("/")
def index():
    return render_template("index.html")

# member page
@app.route("/member")
def memeber():
    if "nickname" in session:
        return render_template("member.html")
    else:
        return redirect("/")

# error page
@app.route("/error")
def error():
    msg = request.args.get("msg", "error occur, please contact us")
    return render_template("error.html", msg=msg)

# handle signup func
@app.route("/signup", methods=["POST"])
def signup():
    # receive data from frontend signup
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

# handle signin func
@app.route("/signin", methods=["POST"])
def signin():
    email = request.form["email"]
    password = request.form["password"]
    collection = db.user
    result=collection.find_one({
        "$and":[
        {"email":email},
        {"password":password}
        ]
    })
    if result == None:
        return redirect("/error?meg=Email or Password is wrong")
    session["nickname"] = result["nickname"]
    return redirect("/member")

# handle signout dunc
@app.route("/signout")
def signout():
    del session["nickname"]
    return redirect("/")

app.run()