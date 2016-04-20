from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Hello World!'
def index():
    return '<h1>Hello World!</h1>'

    if __name__ == '__main__':
            app.run(debug=True)

