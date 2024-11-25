from Flask import Flask, render_template, request, redirect, url_for
import os
import pickle

app = Flask(__name__)

TODO_FILE = 'todo_list.pkl'

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'rb') as f:
            return pickle.load(f)
    return []

def save_todos():
    with open(TODO_FILE, 'wb') as f:
        pickle.dump(todo_list, f)

todo_list = load_todos()

@app.route('/')
def index():
    return render_template('index.html', todos=todo_list)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    if "@" not in email:
        return redirect(url_for('index', error="Invalid email"))

    if priority not in ['Low', 'Medium', 'High']:
        return redirect(url_for('index', error="Invalid priority"))

    todo_list.append({'task': task, 'email': email, 'priority': priority})
    
    save_todos()  # Save the list after adding a new item
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear():
    global todo_list
    todo_list = []  # Clear the global list
    save_todos()  # Save the cleared list
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>', methods=['GET'])
def delete(item_id):
    if 0 <= item_id < len(todo_list):
        todo_list.pop(item_id)
        save_todos()  # Save the updated list
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)