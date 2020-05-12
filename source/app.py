from flask import Flask, render_template
from datetime import datetime
from flask import request
from flask import jsonify
import psycopg2 as pg
from db import Banco
import os

username = os.environ['DB_USER']
passwd = os.environ['DB_PASSWORD']
pg_host = os.environ['DB_HOST']
pg_port = os.environ['DB_PORT']
db_name= os.environ['DB_NAME']


prod = Banco(username, passwd, db_name, pg_host, pg_port)

prod.execute_query("""
             CREATE TABLE IF NOT EXISTS users (
             id serial PRIMARY KEY,
             name VARCHAR(30) NOT NULL,
             username VARCHAR(40) NOT NULL UNIQUE,
             email VARCHAR(60) NOT NULL UNIQUE,
             password VARCHAR(200) NOT NULL,
             registerdate TIMESTAMP,
             isAdmin BOOLEAN DEFAULT False);""")

app = Flask(__name__)

@app.route('/singup', methods = ['POST'])
def create_user():
    content = request.get_json()
    name = content['user']
    username = content['username']
    password = content['password']
    email = content['email']
    isadmin = content['isadmin']
    insert = "INSERT INTO users (name, username, email, password, registerdate, isAdmin) VALUES ('{}', '{}', '{}', '{}', current_timestamp, '{}')".format(name, username, email, password, isadmin)
    print(insert)
    prod.execute_query(insert)
    return 'Usuário criado com sucesso', 200

@app.route('/getuser/<string:username>', methods = ['GET'])
def get_user(username):
    query = "Select name, email, password from users where username = '{}'".format(username)
    user = prod.select_query(query)
    name = user[0][0]
    email = user[0][1]
    senha = user[0][2]
    data = {
        "name":name,
        "email":email,
        "senha":senha 
    }
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)   