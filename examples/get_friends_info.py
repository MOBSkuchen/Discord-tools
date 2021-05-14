from full_code import *

for id in friends.ids():
    name=friends.username(id)
    nickname=friends.nickname(id)
    avatar=friends.avatar(id)
    if not name==None:
        print(str(name) + " - " + str(id) + " - " + str(nickname) + " - " + str(avatar))
