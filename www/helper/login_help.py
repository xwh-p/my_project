from flask import render_template, g

from www.helper.session_help import Session



def my_before_request(fn):
    def warp():
        if not Session.is_user_exist():
            # g.user = None
            print('第一次请求。。。。。。。')
            return render_template('login.html')
        # g.user = Session.get_user()
        fn()
        print(Session.get_user(),'登陆状态')
    return warp
    # g.current_industry = Session.get_user_indstry()
