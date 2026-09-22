from flask import Flask ,render_template,request,jsonify
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/todo",methods=["GET","POST"])
def todo():
    print(request.method)
    if request.method=="POST":
        data={"id":request.form.get("id"),
        "task":request.form.get("task_name"),
        "date":request.form.get("due_date"),
        "status":request.form.get("status")}

        print(data)
        return jsonify({'Task Name':data})


if __name__=="__main__":
    app.run(port=5000,debug="True")