from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/2e981f92d41b89c9c5c0")
all_posts = response.json()

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<id>")
def show_post(id):
    requested_post = None
    for post in all_posts:
        if post["id"] == id:
            requested_post = post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)