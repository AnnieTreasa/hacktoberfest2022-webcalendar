from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/cal')
def cal():
    return render_template("cal.html")

if __name__ == "__main__":
    app.run(debug=True,port=5000)