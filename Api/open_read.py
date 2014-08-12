import json
def function_json():
	
	#
	fo = open('test.json','r')
	file_input = json.load(fo)
	fo.close()

	#
	for entry_dicttionary in file_input:

		#
		price = entry_dicttionary['price']
		item = entry_dicttionary['item']
		print len(item)
		if entry_dicttionary 
		



function_json()
