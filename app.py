from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>張博的中央機房</p>"

if __name__=='__main__':
    app.run(host='127.0.0.1', port=5000)