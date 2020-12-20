import flask
from flask import request, jsonify
from flask_cors import CORS
CORS(app)
import config

app = flask.Flask(__name__)

con = mysql.connector.connect(
        host=config.mysql["host"],
        port=3306,
        user=config.mysql["user"],
        password=config.mysql["password"],
        database=config.mysql["database"])
dataCursor = con.cursor()

@app.route('/register', methods=['POST'])
def register():
    
    sql = f"insert into data (endpoint,p256dh,auth,latitude,longitude) values(%s,%s,%s,%s,%s)"
    tupl = (request.json['endpoint'],request.json['p256dh'],request.json['auth'],request.json['latitude'],request.json['longitude'])
    dataCursor.execute(sql,tupl)
    con.commit()
    return jsonify({'success':True})

app.run()
