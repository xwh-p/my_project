


user_dict = {'user':'1234','user1':'1234'}
def check_user(user,password):

    if user not in user_dict:
        return False

    if user_dict['user'] != password:
        return False
    return True



