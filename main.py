from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/music")
def music():
    return render_template("music.html")


@app.route("/movies")
def movies():
    return render_template("movies.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/shows")
def shows():
    return render_template("shows.html")

if __name__ == "__main__":
    app.run(debug=True)