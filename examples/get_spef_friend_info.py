from full_code import *

id=input("ID: ")
name=friends.username(id)
nickname=friends.nickname(id)
avatar=friends.avatar(id)
if not name==None:
    print(str(name) + " - " + str(id) + " - " + str(nickname) + " - " + str(avatar))
