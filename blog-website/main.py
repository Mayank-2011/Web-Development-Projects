from flask import Flask, render_template, request
import requests
import smtplib


def send_email(data):
    my_email = "your email"
    password = "your app password"
    with smtplib.SMTP("your smtp server", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: New Message\n\nName: {data['username']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
        )


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


@app.route("/contact", methods=['GET', "POST"])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data)
        return render_template("contact.html", message="Successfully sent your message.")
    return render_template("contact.html", message="Contact Me")


@app.route("/post/<int:num>")
def blog(num):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == num:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
