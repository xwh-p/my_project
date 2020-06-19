from flask import render_template, g, redirect, url_for

from www import create_app
from www.helper.session_help import Session

app = create_app()



# @app.before_request
# def before_request():
#     if not Session.is_user_exist():
#         # g.user = None
#         print('第一次请求。。。。。。。')
#         return render_template('login.html')
#     g.user = Session.get_user()
#     print(Session.get_user(),'登陆状态')
#     # g.current_industry = Session.get_user_indstry()




@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html'),404

# gunicorn run:app -c gunicorn_conf.py



