'''
app.py by Poonnada 20/5/2022
'''
from flask import Flask, render_template
app=Flask(__name__)


# Route ไปที่ Index HTML
@app.route("/")
def index():
    name = "John Doe"
    description = "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."
    return render_template("index.html",name = name , description = description)


# Route ไปที่ About
@app.route("/about")
def about():
    product={"name":"AI","sur":"BUU"}
    return render_template("about.html",product=product)



@app.route("/user/<name>")
def user(name):
    return f"<h1> Hi {name} </h1>"


if __name__=="__main__":
    app.run()
