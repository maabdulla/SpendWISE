import json

from flask import Flask, request, redirect
app = Flask(__name__)



#
#
@app.route('/contact', methods=['POST'])
def Submit():
	user_name = request.form['username']
	email_address = request.form['email']
	user_message = request.form['user_message']  

	json_text = {'name': user_name, 'email': email_address, 'user_message': user_message}

	final_json = json.dumps(json_text)
	return final_json



#
#
@app.route('/1page_wise', methods=['POST'])
def Submit1():
	email_address = request.form['your_name']
	user_message = request.form['the_birth'] 
	interest_ = request.form['interest']

 

	json_text = {'the_birth': user_message, 'your_name': email_address, 'interest': interest_}

	final_json = json.dumps(json_text)
	return final_json


#
#
@app.route('/2page_wise', methods=['POST'])
def Submit2():
	money = request.form['amount']

 
	json_text = {'amount': money}

	final_json = json.dumps(json_text)
	return final_json






if __name__ == "__main__":
	app.debug = True
	app.run()
