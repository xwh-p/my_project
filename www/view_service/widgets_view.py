from random import randrange
from flask import Flask, Blueprint, render_template, jsonify, request, redirect, url_for, g, session
from pyecharts.charts import Bar
from pyecharts import options as opts

from www.helper.login_help import my_before_request
from www.helper.session_help import Session
from www.helper.user_dict import check_user

widget = Blueprint('widget', __name__)
login1 = Blueprint('login1', __name__)



@widget.before_request
def before_request():
    if not Session.is_user_exist():

        print('第一次请求。。。。。。。')
        return render_template('login.html')
    g.user = Session.get_user()
    print(Session.get_user(),'登陆状态')
    # g.current_industry = Session.get_user_indstry()


@widget.route('/widget/')
def widget_func():
    print(g.user,'----------g.user')
    return render_template('widgets.html')


@widget.route('/')
def index():
    # return render_template('bj.html')
    return render_template('index.html')


@widget.route('/a/')
def root1():
    print('他来了。。。。。。。。。。。')
    return jsonify({"name":["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],
                    'data':[5, 20, 36, 10, 10, 20],'msg':200})



@widget.route('/echar/')
def echart_test():
    return render_template('echar_test.html')



def bar_base():
    c = Bar()
    c.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    c.add_yaxis("商家A", [randrange(0, 100) for _ in range(6)],color='blue')
    c.add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
    c.set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))

    return c


@widget.route("/barChart/")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()

# login
@login1.route("/login/")
def login():
    return render_template('login.html')



@login1.route("/login_out/")
def login_out():
    session.clear()
    return redirect(url_for('login1.login'))



@login1.route("/login_check/",methods=['post','get'])
def login_check():
    if request.method == 'POST':
        user = request.form.get('userid')
        password = request.form.get('password')

        if check_user(user,password):
            Session.set_user(user)
            # return redirect(url_for('widget.widget_func'))
            return redirect('/')

    return render_template('login.html')



# session.permanent = True  # 开启session存储持久化
# app.permanent_session_lifttime = timedelta(minutes=1)  # 存活一分钟
# session['name'] = 'zhangsan'
