from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<int:n>')
def greater(n):
    if n>10:
        return("The Number is great")
    if n<=10:
        return("The Number is not so great")
    return jsonify('result')

if __name__ == "__main__":
    app.run(debug=True)