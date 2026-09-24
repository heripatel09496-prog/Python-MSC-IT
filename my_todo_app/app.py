from flask import Flask ,render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Use an in-memory database for clean, fast classroom testing
# (To save to a real file, use: 'sqlite:///students.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect SQLAlchemy to Flask
db = SQLAlchemy(app)

print(" Step 1 Complete: Database successfully connected to Flask!")

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)       # Unique ID
    task_name = db.Column(db.String(100), nullable=False)   # Name cannot be blank
    due_date= db.Column(db.String(100), nullable=False) # Course name
    status= db.Column(db.String(50))                    # Grade (e.g. 'A+', 'B')

    def __repr__(self):
        return (f"<Todo #{self.id}: {self.task_name} ({self.due_date}) - Status: {self.status}>")

print(" Step 2 Complete: Todo model defined!")  

@app.route("/")
def home():
    return render_template("index.html")


    
@app.route("/add",methods=['POST'])
def add_todo():
    todo_name=request.form.get("task_name")
    due_date=request.form.get("due_date")
    status=request.form.get("status")
   
    with app.app_context():
        #1.Create a Student object
        t1=Todo(
            task_name=todo_name,
            status=status,
            due_date=due_date
            )
        #2. Stage and save
        db.session.add(t1)
        db.session.commit()  
        
        return jsonify({
            "message": "Todo  added successfully",
            "id": t1.id,
            "task_name":t1.task_name,
            "due_date":t1.due_date,
            "status":t1.status

        })
@app.route("/get", methods=["GET"])
def get_todo():
    todo=Todo.query.all()
    result=[]
    for t2 in todo:
        result.append({
            "id":t2.task_name,
            "task_name": t2.due_date,
            "status":t2.status
        })
    return jsonify(result)

@app.route("/put/<int:id>",methods=["PUT"])
def  todo_update(id):
    todo=Todo.query.get(id)
    if todo is None:
        return jsonify({"message": "Todo not found"}),404
    data=request.get_json()
    todo.task_name=data.get("task_name",todo.task_name)
    todo.due_date=data.get("due_date",todo.due_date)
    todo.status=data.get("status",todo.status)

    db.session.commit()
    return jsonify({
    "message": "Todo update successfully",
    "id":todo.id,
    "task_name": todo.task_name,
    "due_date": todo.due_date,
    "status":todo.status
})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run( port=5001,debug=True)

