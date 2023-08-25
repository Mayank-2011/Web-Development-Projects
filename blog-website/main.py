from flask import Flask, render_template
import requests

app = Flask(__name__)

url = ("https://api.npoint.io/d09a4b72e3be8429943a")
response = requests.get(url)
all_posts = response.json()

@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def blog(num):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == num:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)