from flask import Flask, render_template,jsonify,url_for

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/boot/')
def boot():
    return render_template('ajax_demo.html')


@app.route('/a/')
def root1():
    return jsonify({"name":["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],
                    'data':[5, 20, 36, 10, 10, 20]})




if __name__ == "__main__":
    app.run()


