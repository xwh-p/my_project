from flask import Flask, Blueprint, render_template, jsonify, request



widget = Blueprint('widget', __name__)

# app = Flask(__name__)

@widget.route('/widget/')
def widget_func():
    return render_template('widgets.html')


@widget.route('/')
def index():
    return render_template('index.html')


@widget.route('/a/')
def root1():
    print('他来了。。。。。。。。。。。')
    return jsonify({"name":["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],
                    'data':[5, 20, 36, 10, 10, 20]})



# if __name__ == '__main__':
#     app.run()