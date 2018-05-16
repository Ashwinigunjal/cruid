from flask import Fask, redirect, url_for
app=Flask(__name__)

@app.route('/admin') 
def hello_admin():
	return "hello admin"

@app.route('/guest/<name>')
def hello_guest(name):
	return "Hello %s as guest"%guest

@app.route('/user/<name>')
def hello_user(name):
	if name == 'admin':
		return redirect(url_for('hello_admin'))

	else:
		return redirect(url_for('hello_guest', name=name))


if __name__ == '__main__':
	app.run(debug=True)