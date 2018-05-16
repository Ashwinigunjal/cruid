from flask import Flask,render_template, request

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/result.html', methods=['POST','GET'])
def result():
	if request.method=='POST':
		result=request.form
		print result
		return render_template('result.html' ,result=result)


if __name__ == '__main__':
	app.run()