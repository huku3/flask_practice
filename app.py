from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "Hello Flask"


@app.route("/hiraizumi")
def hiraizumi():
    return "やっほー平泉"


@app.route("/user/<name>")
def heyName(name):
    return f"HI!{name}"


# @app.route("/user/<name>/<age>")
# def userAge(name, age):
#     return f"{name}は{age}です"


# from flasl import render_template
@app.route("/html")
def html():
    # return "<h1>Hello Html</h1>"
    return render_template("index.html")


@app.route("/html/<aaa>")
def htmlName(aaa):
    return render_template("name.html", bbb=aaa)


@app.route("/html/<name>/<age>")
def userAge1(name, age):
    return render_template("age.html", name=name, age=age)


# from flask import request
@app.route("/query")
def query():
    BBB = request.args.get("AAA")
    return BBB


# http://127.0.0.1.5000/query?AAA=XXX


app.run()


if __name__ == "__main__":
    app.run(debug=True)
