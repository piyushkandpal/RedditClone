import webapp2
import cgi
from utils import escape_html
from validate import valid_username,valid_pwd,valid_email

form_signup = """
<!DOCTYPE html>

<html>
  <head>
    <title>SignUp</title>
  </head>

  <body>
    <h2>SignUp</h2>
    <form method="post">
    <label>
        Username
        <input type="text" name="uname" value="%(uname)s">
    </label>
    <div style="color:red">%(err_user)s</div>
    <br>
    <label>
        Password
        <input type="text" name="pwd" value="%(pwd)s">
    </label>
    <div style="color:red">%(err_pwd)s</div>
    <br>
    <label>
        Verify Password
        <input type="text" name="vpwd" value="%(vpwd)s">
    </label>
    <div style="color:red">%(err_vpwd)s</div>
    <br>
    <label>
        Email (optional)
        <input type="text" name="email" value="%(email)s">
    </label>
    <div style="color:red">%(err_email)s</div>
    <br>
      <input type="submit">
    </form>
  </body>

</html>
"""
ERR_INVALID_USER = "That was not a valid username"
ERR_INVALID_PWD = "That was not a valid password"
ERR_INVALID_EMAIL = "That was not a valid email"
ERR_PWD_MISMATCH = "Your passwords didn't match"

# persist valid username in every scenario
# remove wrong/mismatched passwords
class UserProfile:
    def __init__(self,uname=None,pwd=None,email=None):
        self.uname = uname
        self.pwd = pwd
        self.email = email
    
    def getUname(self):
        return self.uname

    def setUname(self,name):
        self.uname = name

    def getpwd(self):
        return self.pwd

    def setpwd(self,name):
        self.pwd = pwd
    
    def getEmail(self):
        return self.email

    def setUname(self,email):
        self.email = email

class Form:
    def __init__(self,form,*fields):
        self.form = form
        self.fields = fields

    def getFormStr(self):
        return self.form

    def getFields(self):
        for self.fields

class SignUpForm(Form):
    def __init__(self,userpf,*error):
        self.form = form_signup 
        self.userpf = userpf
        err_uname,err_pwd,err_vpwd, = error
        
        super(SignUpForm,self).__init__(self.form,userpf,*err)
    

class SignUpHandler(webapp2.RequestHandler):
    def write_form(self,uname="",pwd="",vpwd="",email=""):
        self.response.write(form_signup%
                {"uname":escape_html(uname),
                 "pwd":escape_html(pwd),
                 "vpwd":escape_html(vpwd),
                 "email":escape_html(email)
                 "error_uname":err_
                })
    
    def get(self):
        self.write_form()
    
    def post(self):
        uname = self.request.get('uname')
        pwd = self.request.get('pwd')
        vpwd = self.request.get('vpwd')
        email = self.request.get('email')
        valid_uname = valid_username(uname)
        valid_pwd = valid_pwd(pwd)
        valid_vpwd = False
        if vpwd == valid_pwd:
            valid_vpwd = True
        
        if not valid_uname:
            self.write_form(uname,"","","")
        elif not valid_pwd: 
            self.write_form(uname,"","","")
        elif not valid_vpwd:
            self.write_form(uname,"","","")
        else:
            # redirect it to "/unit2/welcome?username=piyush"
            self.response.write(form_%
                {"uname":escape_html(flip_text)})
        
application = webapp2.WSGIApplication([
    ('/unit2/signup', SignUpHandler),], debug=True)
