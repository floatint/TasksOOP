import functools

from flask import Blueprint
from flask import request
from flask import jsonify
import Task_7_21.utils as utils


convert = Blueprint('convert', __name__)


def return_json(view):
    @functools.wraps(view)
    def wrapped_view(**values):
        return jsonify(view(**values))
    return wrapped_view


# convert
@convert.route('/convert', methods=['GET', 'POST'])
@return_json
def do_convert():
    val1_name = request.form["val1_name"]
    val2_name = request.form["val2_name"]
    try:
        count = int(request.form["count"])
    except Exception as e:
        return {"error": True, "message": str(e)}
    data = utils.valute_provider.get_valute_data()
    if val1_name == val2_name:
        return {"error": False, "answer": count}
    return {"error": False, "answer": data[val1_name][0] * count / data[val2_name][0]}
