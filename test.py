import re

URL = r"https://boston.craigslist.org/gbs/apa/d/somerville-august-inman-union-sq-luxury/7636135906.html"
expression = r"(?<=\/)(\d*?)(?=\.)"

match = re.search(expression, URL)

if match:
    print("found", match.group())
else:
    print("did not find")
