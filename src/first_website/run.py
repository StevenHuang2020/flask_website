# -*- encoding: utf-8 -*-
# Date: 11/Jan/2022
# Author: Steven Huang, Auckland, NZ
# License: MIT License
"""
Description: Flask test
Start server with flask cmd:
1. open cmd
2. $ set FLASK_APP=main.py
   $ set FLASK_DEBUG=1
3. $ flask run

Start server with Python:
$ python run.py

Reference courses:
https://www.youtube.com/watch?v=803Ei2Sq-Zs&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=7
"""

from first_website import app


# def to_pretty_json(value):
#     return json.dumps(value, sort_keys=True,
#                       indent=2, separators=(',', ': '))


def main():
    # app.jinja_env.filters['tojson_pretty'] = to_pretty_json
    app.run(debug=True)


if __name__ == "__main__":
    main()
