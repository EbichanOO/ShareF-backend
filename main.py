import json, sqlite3

from flask import Flask, jsonify, request
app = Flask(__name__)

dbname = 'object.db'

@app.route("/")
def helloWorld():
    return "Hello, World!"

@app.route('/init/db', methods=['GET'])
def initDB():
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()

        cur.execute(
            'drop table if exists OBJECT'
        )

        # create table
        cur.execute(
            'create table OBJECT(objID integer primary key autoincrement,context string,x float,y float,z float,xTurn float,yTurn float)'
        )

        # create datas
        sql = 'INSERT INTO OBJECT(context,x,y,z,xTurn,yTurn) VALUES(?,?,?,?,?,?)'
        cur.execute(sql, ["hoge", 1,1,1,1,1])
        
        conn.commit()
    return "ok"

@app.route('/get/object/all', methods=['GET'])
def initObject():
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()
        sendData = {"data":[{'context':d[1], 'x':d[2], 'y':d[3], 'z':d[4], 'x-turn':d[5],'y-turn':d[6]} for d in cur.execute('select * from OBJECT')]}

    return jsonify(sendData)

@app.route('/add/object', methods=['POST'])
def addObject():
    getData = [request.form['context'], float(request.form['x']), float(request.form['y']), float(request.form['z']), float(request.form['x-turn']), float(request.form['y-turn'])]
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()

        cur.execute('INSERT INTO OBJECT(context,x,y,z,xTurn,yTurn) VALUES(?,?,?,?,?,?)', getData)
        conn.commit()
    return "ok"

if __name__=="__main__":
    app.run(host="0.0.0.0")