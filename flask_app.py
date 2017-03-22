from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/<msg>", methods=['GET', 'POST'])
def server(msg):
    return str(msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0')