
    
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
  def index2():
    return render_template("index.html")


@app.route("/reactapp")
  def reactapp():
    return render_template("reactapp.html")
