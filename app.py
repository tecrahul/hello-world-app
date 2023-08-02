from flask import Flask, jsonify
import pymysql.cursors
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MySQL connection details
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')

@app.before_request
def before_request():
    g.db = pymysql.connect(host=MYSQL_HOST,
                           user=MYSQL_USER,
                           password=MYSQL_PASSWORD,
                           db=MYSQL_DB,
                           cursorclass=pymysql.cursors.DictCursor)

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/id/<int:id>')
def get_student(id):
    try:
        with connection.cursor() as cursor:
            # Query the database
            sql = "SELECT * FROM Students WHERE Id = %s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()

            if result:
                return jsonify(result), 200
            else:
                return jsonify({'error': 'Student not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Database error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
