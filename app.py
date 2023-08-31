from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Todo

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///todos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'oh-so-secret'

app.app_context().push()

connect_db(app)

@app.route('/api/todos')
def list_todos():
    all_todos = [todo.serialize() for todo in Todo.query.all()]
    return jsonify(all_todos)