from flask import Flask, jsonify, request

from db import add_spacesallocation, get_spaces, add_spaces, get_spacesallocation

app = Flask(__name__)

@app.route('/space', methods=['POST', 'GET'])
def space():

    if request.method == 'POST':
        try:
            add_spaces(request.get_json())
            return jsonify({"status": "success",
                        "message": "Space added successfully",
                        "data": {}}), 200
        except Exception as error: 
            return jsonify({"status": "error",
                           "message": "bad request"}), 400
    if request.method == 'GET':
        try:
            return get_spaces()
        except Exception as error: 
            return jsonify({"status": "error",
                           "message": "bad request"}), 400 


@app.route('/spaceallocation', methods=['POST', 'GET'])
def spaceallocation():
    if request.method == 'POST':
       # bayID = request.form['bay_id']
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        add_spacesallocation(request.get_json())
        return  jsonify({"status": "success",
                        "message": "space allocated successfully ",
                        "data": {}}), 200

    return get_spacesallocation()

if __name__ == '__main__':
    app.run(debug=True)
