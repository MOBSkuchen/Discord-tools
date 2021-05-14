from full_code import *

for id in friends.ids():
    name=friends.username(id)
    if not name==None:
        print(name + "-" + id)
