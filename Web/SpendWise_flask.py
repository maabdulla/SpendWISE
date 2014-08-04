import json
from flask import Flask, request, redirect
app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def Submit():
	Namee = request.form['name']
	Birth = request.form['username']
	Quote = request.form['email']  

	
	return 



if __name__ == "__main__":
	app.debug = True
	app.run()
