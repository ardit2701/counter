from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/success')
def success_1():
    return "success"

@app.route('/hello/ardit')
def hello_1():
    name = 'ardit'
    return "Hello " + name

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)   