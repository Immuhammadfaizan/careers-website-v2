from flask import Blueprint, jsonify

bp = Blueprint('performance', __name__)

@bp.route('/speedtest', methods=['GET'])
def speed_test():
    # Placeholder: Implement your speed test logic here
    return jsonify({"speed": "500ms"})
