from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

import os

with app.app_context():
    print("Database location:", db.engine.url.database)
    print("Absolute path:", os.path.abspath(db.engine.url.database))


# Todo table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(300), default="")
    priority = db.Column(db.String(20), nullable=False, default="Medium")
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)


# Display pending and completed tasks
@app.route("/")
def home():
    pending = Todo.query.filter_by(is_completed=False).all()
    completed = Todo.query.filter_by(is_completed=True).all()

    return render_template(
        "index.html",
        pending=pending,
        completed=completed
    )


# Add a new task
@app.route("/add", methods=["POST"])
def add_todo():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    priority = request.form.get("priority")
    due_date = request.form.get("due_date")

    if not title or not due_date:
        return "Title and due date are required.", 400

    if len(title) > 150 or len(description) > 300:
        return "Title or description is too long.", 400

    if priority not in ["High", "Medium", "Low"]:
        return "Invalid priority.", 400

    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        return "Invalid due date.", 400

    task = Todo(
        title=title,
        description=description,
        priority=priority,
        due_date=due_date
    )

    db.session.add(task)
    db.session.commit()

    return redirect(url_for("home"))


# Mark a task completed or pending
@app.route("/toggle/<int:id>", methods=["POST"])
def toggle_todo(id):
    task = db.session.get(Todo, id)

    if task is None:
        return "Task not found.", 404

    task.is_completed = not task.is_completed
    db.session.commit()

    return redirect(url_for("home"))


# Update an existing task
@app.route("/update/<int:id>", methods=["POST"])
def update_todo(id):
    task = db.session.get(Todo, id)

    if task is None:
        return "Task not found.", 404

    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    priority = request.form.get("priority")
    due_date = request.form.get("due_date")

    if not title or not due_date:
        return "Title and due date are required.", 400

    if len(title) > 150 or len(description) > 300:
        return "Title or description is too long.", 400

    if priority not in ["High", "Medium", "Low"]:
        return "Invalid priority.", 400

    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        return "Invalid due date.", 400

    task.title = title
    task.description = description
    task.priority = priority
    task.due_date = due_date

    db.session.commit()

    return redirect(url_for("home"))


# Delete a task
@app.route("/delete/<int:id>", methods=["POST"])
def delete_todo(id):
    task = db.session.get(Todo, id)

    if task is None:
        return "Task not found.", 404

    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("home"))


# Create the database and start Flask
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(port=5001, debug=True)

import os

with app.app_context():
    print("Database location:", db.engine.url.database)
    print("Absolute path:", os.path.abspath(db.engine.url.database))
