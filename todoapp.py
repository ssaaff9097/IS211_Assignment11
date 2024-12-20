from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    if "@" not in email or priority not in ['Low', 'Medium', 'High']:
        return redirect(url_for('index'))
    
    todo_list.append({'task': task, 'email': email, 'priority': priority})
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear():
    global todo_list
    todo_list.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



