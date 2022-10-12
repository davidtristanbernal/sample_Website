from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/home")
def home():
   return render_template("index.html")

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/contact")
def contact():
   return render_template("contact.html")

@app.route("/friends")
def friends():
   return render_template("friends.html")

@app.route("/registration")
def registration():
   return render_template("registration.html")

@app.route("/login")
def login():
   return render_template("login.html")

@app.route('/verify',methods = ['POST', 'GET'])
def verify():
    if request.method == 'POST':
        userid = request.form['nm']
        return render_template('login_details.html',uid = userid)
    else:
        userid = request.args.get('nm')
        return render_template('login_details.html',uid = userid)

@app.route('/register',methods = ['POST','GET'])
def register():
    if request.method == 'POST':
        result = request.form

    return render_template("register_details.html", result=result)

if __name__ == "__main__":
   app.run()