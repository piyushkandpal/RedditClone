import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PWD_RE re.compile(r"^.{3,20}$") 
EMAIL_RE= re.compile(r"^[\S]+@[\S]+\.[\S]+$") 

def valid_username(username):
    return username and USER_RE.match(username)

def valid_pwd(pwd):
    return pwd and PWD_RE.match(pwd)

def valid_email(email):
    return email and EMAIL_RE.match(pwd)
