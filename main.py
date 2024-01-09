import json
from flask import Flask, jsonify, request

from db import add_spacesallocation, get_spaces, add_spaces, get_spacesallocation,space_allocated_deleted, space_deleted

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


# Creating Space Allocation
@app.route('/spaceallocation', methods=['POST', 'GET'])
def spaceallocation():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        add_spacesallocation(request.get_json())
        data = json.loads(request.data)
        aid = data.get('bay_id')
        return  jsonify({"status": "success",
                        "message": "space allocated successfully ",
                        "data": aid}), 200

    return get_spacesallocation()

# Endpoint for deleting a allocated bay
@app.route("/deleteAllocatedBay/<id>", methods=["DELETE"])
def spaceAllocated_deleted(id):
        try:
            space_allocated_deleted(id)
            return jsonify({"status": "success",
                            "message": "allocated bay deleted successfully",
                            "data": {}}), 200
        except Exception as error:
            return jsonify({"status": "error",
                           "message": "bad request"}), 400
        
# Endpoint for deleting a space 
@app.route("/deleteSpace/<id>", methods=["DELETE"])
def delete_space(id):
        try:
            space_deleted(id)
            return jsonify({"status": "success",
                            "message": "Space deleted successfully",
                            "data": {}}), 200
        except Exception as error:
            return jsonify({"status": "error",
                           "message": "bad request"}), 400
        

if __name__ == '__main__':
    app.run(debug=True)
