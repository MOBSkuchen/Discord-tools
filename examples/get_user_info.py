from full_code import *

name=info.name()
avatar=info.avatar()
all=info.getallraw()
email=info.email()
phone=info.phone()
lang=info.lang()
id=info.id()
print(f"NAME: {name} \n"
      f"EMAIL: {email} \n"
      f"ID: {id} \n"
      f"PHONE: {phone} \n"
      f"AVATAR_URL: {avatar} \n"
      f"LANGUAGE: {lang} \n"
      f"ALL: {all}")
