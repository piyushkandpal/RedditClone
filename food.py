import os
import webapp2
import jinja2

hidden_html = """
<input type="hidden" name="food" value="%s">
"""
item_html = "<li>%s</li>"

shoppinglist_html="""
<br>
<br>
<h2>Shopping list</h2>
<ul>
%s
</ul>
"""
template_dir = os.path.join(
        os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(
        loader = jinja2.FileSystemLoader(template_dir))

class Handler(webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.write(*a,**kw)

    def render_str(self,template,**params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self,template,**kw):
        self.write(self.render_str(template, **kw))

        
class MainPage(Handler):
    def get(self):
        n = self.request.get("n")
        if n:
            n = int(n)
        self.render('shopping_list.html',n=n)
        """
        output_hidden = ""
        items = self.request.get_all("food")
        if items:
            output_items = ""
            for item in items:
                output_hidden += hidden_html % item
                output_items += item_html % item
            output_shopping = shoppinglist_html % output_items
            output += output_shopping
        output = output % output_hidden
        self.write(output)
        """
application = webapp2.WSGIApplication([
    ('/unit2/food', MainPage),], debug=True)




