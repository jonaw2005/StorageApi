import json

from flask import Flask, jsonify, request
from StorageApi import StorageHandler

app = Flask(__name__)

handler = StorageHandler.StorageHandler
#StorageHandler.StorageHandler
data = {"items":{"coords":{"x#1":{"y#1": "Schraube M2", "y#2": 0, "y#3": "Bauteil #358986"}, "x#2":{"y#1": "Schraube M3", "y#2": "Mutter H7", "y#3": "Bauteil #358986"}, "x#3":{"y#1": "Schraube M4", "y#2": 0, "y#3": "Bauteil #358986"}, "x#4":{"y#1": "Schraube M6", "y#2": "kugellager d5mm", "y#3": "Bauteil #358986"}}}, "connection":{"ip": "127.0.0.1", "port": 5000, "endpoint": "/"}, "time": "20.10.2023"}

@app.route("/")
def test():
    return "<h1>Test!</h1>"

@app.route("/all_items")
def items():
    #data = handler.allItems()
    return jsonify(data)

@app.route("/einlagern", methods=['POST'])
def einlagern():
    # {'x': x, 'y': y, 'description': desc, 'amount': num}
    data = request.json
    x = data.get("x")
    y = data.get("y")
    desc = data.get("description")
    amount = data.get("amount")

    if not handler.checkReady():
        return jsonify({'status': 'in use'})

    data_ret = handler.putItem(x,y,desc,amount)

    return jsonify(data_ret)

@app.route("/auslagern", methods=['POST'])
def auslagern():
    # {'x': x, 'y': y, 'description': desc, 'amount': num}
    data = request.json
    x = data.get("x")
    y = data.get("y")


    if not handler.checkReady():
        return jsonify({'status': 'in use'})

    data_ret = handler.takeItem(x,y)
    return jsonify(data_ret)

@app.route("/umlagern", methods=['POST'])
def umlagern():
    # {'prevX': prevX, 'prevY': prevY, 'newX': newX, 'newY': newY}
    data = request.json
    prevX = data.get("prevX")
    prevY = data.get("prevY")
    newX = data.get("newX")
    newY = data.get("newY")

    if not handler.checkReady():
        return jsonify({'status': 'in use'})

    data_ret = handler.relocateItem()
    return "<h1>"+str(data_ret)+"</h1>"

@app.route("/status")
def status():
    data_ret = handler.getStatus()
    return jsonify(data_ret)

@app.route("/reset")
def reset():
    data_ret = StorageHandler.StorageHandler.resetCrane()
    return jsonify(data_ret)