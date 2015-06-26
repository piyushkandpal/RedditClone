import webapp2
import cgi
from utils import escape_html,valid_day,valid_month,valid_year

form_birth="""
<form method="post">
    What is your birth date?
    <br>
    <label>Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label>Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label>Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color:red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self,error="",month="",day="",year=""):
        self.response.write(form_birth%{"error":error,
                                        "month":escape_html(month),
                                        "day":escape_html(day),
                                        "year":escape_html(year)})
    def get(self):
        self.write_form()
    
    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')
        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)
        print user_month,user_day,user_year
        if not (month and day and year):
            self.write_form('not a valid date',user_month,user_day,user_year)
        else:
            self.redirect("/thanks")

class TestHandler(webapp2.RequestHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)
        
class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks!Its a valid entry")
        
application = webapp2.WSGIApplication([
    ('/helloworld', MainPage),('/testform', TestHandler),('/thanks',ThanksHandler)], debug=True)
