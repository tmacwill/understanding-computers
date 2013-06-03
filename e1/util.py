from flask import jsonify

def json_success(data={}):
    data['success'] = True
    return jsonify(data)
