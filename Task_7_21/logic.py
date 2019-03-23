from flask import Blueprint
from flask import request
from flask import jsonify
import Task_7_21.utils as utils


convert = Blueprint('convert', __name__)


# convert
@convert.route('/convert', methods=['GET', 'POST'])
def do_convert():
    val1_name = request.form["val1_name"]
    val2_name = request.form["val2_name"]
    try:
        count = int(request.form["count"])
    except Exception as e:
        return jsonify(error=True, answer=str(e))
    data = utils.valute_provider.get_valute_data()
    if val1_name == val2_name:
        return str(count)
    return jsonify(error=False, answer=str(data[val1_name][0] / data[val2_name][0] * data[val1_name][1]))
