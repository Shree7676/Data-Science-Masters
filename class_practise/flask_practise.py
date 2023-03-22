from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/")
@app.route("/hel_world")
def hel_world():
    return "<h1> Hello world 0</h1>"

@app.route("/Helloa_world")
def hel_world1():
    return "<h1> Hello world 1 </h1>"

@app.route("/hw")
def hel_world2():
    return "<h1> Hello world 2</h1>"

@app.route("/test2")
def test2():
    data= request.args.get("x") 
    return "this is the input that u entered {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")