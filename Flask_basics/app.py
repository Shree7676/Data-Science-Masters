from flask import Flask, render_template, request, jsonify

app=Flask(__name__)

# @app.route("/")
# def check():
#     return render_template("index.html")

# @app.route("/shree_main",methods=['POST'])
# def get_data():
#     if (request.method=="POST"):
#         un=request.form['un']
#         pw=request.form['pw']
#         data="your username is {} and your password is {}".format(un,pw)

#     return render_template("results.html",result=data)

@app.route("/through_postman",methods=['POST'])
def get_data_through_postman():
    if (request.method=="POST"):
        un=request.json['un']
        pw=request.json['pw']
        data="your username is {} and your password is {}".format(un,pw)

    return jsonify(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
