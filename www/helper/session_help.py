from flask import session, g


class Session:
    @staticmethod
    def get_user():
        if 'user' in session:
            return session['user']
        else:
            return None

    @staticmethod
    def set_user(val):

        session['user'] = val

    @staticmethod
    def set_user_indstry(val):
        session['current_industry'] = val

    @staticmethod
    def get_user_indstry():
        if 'current_industry' in session:
            return session['current_industry']
        else:
            return None

    @staticmethod
    def set_user_tags(val):
        session['user']['mytags'] = val

    @staticmethod
    def is_user_exist():
        return 'user' in session
