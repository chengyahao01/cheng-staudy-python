from flask import Flask, request, jsonify
from config import USERNAME, PASSWORD

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username == USERNAME and password == PASSWORD:
        return jsonify({"message": "登录成功"}), 200
    else:
        return jsonify({"message": "登录失败"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 