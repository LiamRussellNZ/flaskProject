from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello, World! Hoory this works'

@app.route('/hello/', methods = ['GET'])
def helloUser():
    name = request.args.get("name", None)
    return f'Hello, {name}'