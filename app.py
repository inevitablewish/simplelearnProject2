from flask import Flask, jsonify
app = Flask(__name__)

count = 0

@app.route('/hello')
def hello():
    greeting = "Hello Mohsin! You are doing Project 2 of simplilearn"
    return greeting

@app.route('/count', methods=["GET"])
def getCount():
    global count
    count += 1
    user = ['Mohsin', 'Andrew', 'Sharon']
    while count < 3:
        return str(user[count])
    count=0
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)