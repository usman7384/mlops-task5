from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongodb:27017/')
db = client['webapp_db']
collection = db['user_info']

@app.route('/store-info', methods=['POST'])
def store_info():
    name = request.form['name']
    email = request.form['email']
    user_info = {'name': name, 'email': email}
    result = collection.insert_one(user_info)
    return jsonify({'message': 'Data stored successfully!', 'id': str(result.inserted_id)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
