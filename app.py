from flask import Flask, redirect, request, url_for, render_template
app = Flask(__name__)


@app.route('/')
def intro1():
    return "<h1>Hello World</h1>"


@app.route('/hello/<user>')
def intro(user):
    return render_template('hello.html', name=user)


@app.route('/success/<name>')
def success(name):
    return "Yo man, we know how to link html and worked with name " + name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)
