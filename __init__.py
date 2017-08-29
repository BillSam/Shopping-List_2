from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template("index.html")

@app.route('/about/')
def about():
	return render_template("about.html")


@app.route('/services/')
def services():
	return render_template("services.html")

@app.route('/login/')
def login():
	return render_template("login.html")

@app.route('/signup/')
def signup():
	return render_template("signup.html")

@app.route('/list/')
def list():
	return render_template("list.html")


if __name__ == "__main__":
	app.run()
