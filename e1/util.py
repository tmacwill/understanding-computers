from flask import jsonify

def json_success():
    return jsonify({ 'success': True })
