from flask import Flask
from flask import render_template
from Task_7_21.logic import convert
import Task_7_21.utils as utils

# init
app = Flask(__name__, template_folder="pages")
utils.valute_provider.update()
# reg convert func
app.register_blueprint(convert)


# main page
@app.route('/')
def index():
    return render_template("main.html", valutes=utils.valute_provider.get_valute_names())


if __name__ == '__main__':
    app.run()
