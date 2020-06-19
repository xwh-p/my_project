from flask import Flask

# from www.views import test, test2, power_view
from www.view_service.widgets_view import widget, login1


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('/Users/xingwenhao/Desktop/flask_demo/config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # app.register_blueprint(test.t)
    # app.register_blueprint(test2.t1)
    # app.register_blueprint(power_view.new_old_pow)
    app.register_blueprint(widget)
    app.register_blueprint(login1)
    return app
