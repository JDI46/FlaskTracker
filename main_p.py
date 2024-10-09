from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/home")
def base():
    return render_template("home.html")

@app.route('/blog')
def home():
    return render_template('admin_page.html')



# @app.route('/messageme')
# me():
#     return render_template('messageme.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/admin_page")
def user():
    return render_template("admin_page.html")

if __name__ == "__main__":
    app.run(debug=True)