import webapp2
import cgi
from utils import escape_html,convert_rot
import os
import jinja2

form_rot="""
<form method="post">
    <input type="text" name="rot" value="%(rot)s">
    <br>
    <input type="submit">
</form>
"""
form = """
<!DOCTYPE html>

<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="rot" style="height: 100px; width: 400px;">%(rot)s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
"""
template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(
                                template_dir) ,autoscape = True)
def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.write(render_str(template,**kw))
    
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

class Rot13Handler(BaseHandler):
    def write_form(self,rot=""):
        self.response.write(form%
            {"rot":escape_html(rot)})
    
    def get(self):
        self.write_form()
    
    def post(self):
        rot = self.request.get('rot')
        if not rot:
            self.write_form()
        else:
            flip_text = convert_rot(rot)
            print flip_text
            self.response.write(form%
            {"rot":escape_html(flip_text)})
        
application = webapp2.WSGIApplication([
    ('/unit2/rot13', Rot13Handler),], debug=True)
