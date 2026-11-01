import flask, datetime, flask_cors

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route("/")
def s():
    return datetime.datetime.now().ctime(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
