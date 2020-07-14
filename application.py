from flask import Flask,request,render_template,redirect

app=Flask(__name__)

todos=[]

@app.route("/")
  def taks()
    return render_template("tasks.html",todos=todos)
    
@app.route("/add",method=["GET","POST"])
  if request.method=="GET"
    return render_tmeplate("add.html")
  else
    todo=request.form.get("task")
    todos.append(todo)
    return redirect("/")
    
