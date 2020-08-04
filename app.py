from flask import Flask, render_template, url_for, render_template, request, redirect
from password import get_random_alphanumeric_string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asecret!'

@app.route('/')
def hello():
    return get_random_alphanumeric_string(6)

@app.route('/generatepassword')
def getpassword():
    return get_random_alphanumeric_string(6)

@app.route('/index')
def home():
    return render_template('index.html')

@app.route("/base", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("base.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>" + get_random_alphanumeric_string(6) + f"<h1>{usr}</h1>" + get_random_alphanumeric_string(6) + f"<h1>{usr}</h1>" + get_random_alphanumeric_string(6)

if __name__ == "__main__":
    app.run(debug=True)
    