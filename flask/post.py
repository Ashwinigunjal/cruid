from flask import Flask, url_for, request,redirect
app=Flask(__name__)

@app.route('/success/<name>')
def success(name):
	return "<h1 style='color:green'>Welcome User %s</h1>"%name

@app.route('/fail/<name>')
def fail(name):
	return "<h1 style='color:green'>Welcome User fail %s</h1>"%name


@app.route('/login',methods=['POST','GET'])
def login():
	print "I am in login"
	if request.method == 'POST':
		print "I am in if"
		user=request.form['name']

		password=request.form['pass']
		print user
		print password	
		return redirect(url_for('success',name=user))

	elif request.method == 'GET':
		print "I am in if"
		user=request.args.get('name')

		password=request.args.get('pass')
		print user
		print password	
		return redirect(url_for('fail',name=user))


if __name__ == '__main__':
	app.run(debug=True)