from flask import Flask,render_template

app = Flask(__name__)

events =[
    {
        'title' : 'TestEvent',
        'start' : '2022-10-18',
        'end': '',
        'url': ''
    },
    {
        'title' : 'TestEvent2',
        'start' : '2022-10-18',
        'end': '2022-12-10',
        'url': ''
    }
]

@app.route("/")
def hello_world():
    return render_template('add.html')

@app.route('/cal')
def cal():
    return render_template("cal.html")

if __name__ == "__main__":
    app.run(debug=True,port=5000)