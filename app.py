import flask

app=flask(__name__)

@app.route("/home")
def home():
    return "hello prjwal"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=1234)
