import cgi

def escape_html(s):
    return cgi.escape(s,quote=True)

def convert_rot(text):
    t=[]
    for i in text:
        if i.isalpha():
            asc=ord(i)
            if asc in range(65,91):
                if asc+13 < 91:
                    asc+=13
                else:
                    asc-=13
            elif asc in range(97,123):
                if asc+13 < 123:
                    asc+=13
                else:
                    asc-=13
            t.append(chr(asc))
        else:
            t.append(i)
    return ''.join(t)

months=["January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "Novemeber",
              "December"]

month_abbvs = dict((m[:3].lower(),m) for m in months)

def valid_month(month):
    if month and len(month)>=3:
        return month_abbvs.get(month[:3].lower())

def valid_day(day):
    if day and day.isdigit():
        if 0 < int(day) <=31:
            return day

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year>1900 and year<2020:
            return year

