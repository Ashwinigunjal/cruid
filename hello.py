from flask import Flask
app = Flask(__name__)

# @app.route('/hello/<int:10>')
# def hello_name(name):
   # return 'Hello %d!' % name

@app.route('/blog/<int:id>')
def number(id):
	return 'Hello %d'%id

@app.route('/blog1/<float:id1>')
def number1(id1):
	return 'Hello %f'%id1

if __name__ == '__main__':
   app.run('127.0.0.1',5000,debug=True)