from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def hello_world():
    return "<p> HELLO FROM THE APP! </p>"

@app.route("/health")
def health():
    return jsonify(
        status = "UP"
    )

@app.route("/details")
def details():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 80)