from modules import display,api
def inpmsg(message, limit_value=tuple()):
    '''
    inspect input message is valid or not
    :param message:sting type  to display
    :param limit_value:
    :return:input
    '''
    is_null_flag = True
    while is_null_flag:
        display.colordisplay(message, "blue")
        input_value = input().strip()
        if not input_value:
            display.colordisplay("Input is empty!", "red")
            continue
        elif input_value not in limit_value:
            display.colordisplay("Input is invalid,please retry!","red")
            continue
        else:
            if input_value == 'q':
                exit()
            return input_value
def login(role):
    '''
    user sign in and sign up ,if sign in successfully,return user
    :return:
    '''
    role_dic = {"students":"2","teachers":"1","admin":"0",}
    choice = inpmsg("[1.sign in]\n[2.sign up]",('1','2'))
    if choice == '1':#sign in
        user_inp = input("\033[1;34;1mPlease input username:\033[0m").strip()
        psd_inp = input("\033[1;34;1mPlease input password:\033[0m").strip()
        user_info = api.users_op(user_inp,psd_inp,'read')
        if user_inp in user_info:
            if psd_inp == user_info[user_inp][0]:#password right
                if role_dic.get(role) == user_info[user_inp][1]:#match role
                    print("\033[1;31;1mSing in successfully!\033[0m")
                    return user_inp
                else:
                    print("\033[1;31;1mRole not match!!!\033[0m")
            else:
                print("\033[1;31;1m Wrong password!\033[0m")
        else:
            print("\033[1;31;1mCan not find user!\033[0m")

    else:#sign up
        user_inp = input("\033[1;34;1mPlease input username:\033[0m").strip()
        psd_inp = input("\033[1;34;1mPlease input password:\033[0m").strip()
        role = inpmsg("Input role [1.students  2.teachers]>>:",('1','2'))
        user_info = api.users_op(user_inp, psd_inp, 'read')
        if user_inp in user_info:
            print("\033[1;31;1mUser already exists!\033[0m")
        if role == '1' or role == '2':
            api.users_op(user_inp, psd_inp,'write',role)
        else:
            api.users_op(user_inp, psd_inp, 'write')
    return None
