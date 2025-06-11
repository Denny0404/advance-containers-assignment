from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Database config from environment variables
db_config = {
    'host': os.environ.get('DB_HOST', 'db'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', 'password'),
    'database': os.environ.get('DB_NAME', 'users_db')
}

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (first_name, last_name) VALUES (%s, %s)",
                   (data['first_name'], data['last_name']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User created'}), 201

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return jsonify(result if result else {'error': 'User not found'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
