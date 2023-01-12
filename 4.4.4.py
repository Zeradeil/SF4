login_list = [
   'root',
   'username1'
   ]

password_list = {
   'root': '1q2w3e4r',
   'username1': 'qwerty123'
}

username = input('Введите логин:\n')

if username in login_list:
    userpswd = input('Введите пароль:\n')
    if userpswd == password_list[username]:
        print("входите")
    else:
        print("Пароль введен неверно")
else:
    print("Логие введен неверно")
