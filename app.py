from flask import Flask, render_template, url_for, render_template, request, redirect
from password import get_random_alphanumeric_string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asecret!'

@app.route('/index')
def home():
    return render_template('index.html')

@app.route("/base", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        category = request.form["category"]
        return redirect(url_for("password", usr=category))
    else:
        return render_template("base.html")

@app.route("/<usr>")
def password(usr):
    opt = []
    for option in range(0,3):
        opt.append(get_random_alphanumeric_string(5, usr))
    return f"<h1>{usr}</h1>\n Here is your random password!\
         Choose from any of the 3:\n <h3>{opt[0]}</h3> \n\
         <h3>{opt[1]}</h3> \n\
             <h3>{opt[2]}</h3>"


if __name__ == "__main__":
    app.run(debug=True)
    
