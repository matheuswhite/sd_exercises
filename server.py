from flask import Flask
from flask import request
from flask import abort
import json
app = Flask(__name__)

#run server in localhost
#FLASK_APP=server.py flask run

#run server in IPv6
#FLASK_APP=server.py flask run --host=your-ipv6

@app.route('/')
def index():
	return 'My awersome page!'


@app.route('/university', methods=['GET'])
def get():
	with open('content.json', 'r') as json_file:
		json_data = json.load(json_file)
	text = '<html><body><pre>'
	for university in json_data["university"]:
		text += university + "\n"
	text += '</pre></body></html>'
	return text


@app.route('/university', methods=['POST'])
def post():
	with open('content.json', 'r+') as json_file:
		json_data = json.load(json_file)
		json_data["university"].append(request.form['name'])
		json_file.seek(0)
		json_file.write(json.dumps(json_data))
		json_file.truncate()
	return 'Content Update!'


@app.route('/university', methods=['PUT'])
def put():
	with open('content.json', 'r+') as json_file:
		json_data = json.load(json_file)
		i = request.form['index']
		name = request.form['name']

		if int(i) >= len(json_data['university']):
			json_data["university"].append(name)
		else:
			json_data['university'][int(i)] = name

		json_file.seek(0)
		json_file.write(json.dumps(json_data))
		json_file.truncate()
	return 'Content Update!'


@app.route('/university/<int:i>', methods=['DELETE'])
def delete(i):
	with open('content.json', 'r+') as json_file:
		json_data = json.load(json_file)

		if i < len(json_data['university']):
			university = json_data['university'][i]
			json_data["university"].remove(university)
			json_file.seek(0)
			json_file.write(json.dumps(json_data))
			json_file.truncate()
			return 'Content Update!'
		else:
			abort(404)
