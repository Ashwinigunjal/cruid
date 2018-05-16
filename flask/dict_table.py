from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
   dict = {'Physics':50,'Chemistry':60,'Mathematics':70, 'Marathi':80, 'History':80, 'Drawing':95}
   return render_template('table.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)