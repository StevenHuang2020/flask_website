# -*- encoding: utf-8 -*-
# Date: 11/Jan/2022
# Author: Steven Huang, Auckland, NZ
# License: MIT License
"""
Description: Flask website main app

Start server with Python:
$ python run.py

Or start server with flask cmd:
1. open cmd
2. $ set FLASK_APP=main.py
   $ set FLASK_DEBUG=1
3. $ flask run


Reference courses:
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=1
"""

# from first_website import app
from first_website import create_app

app = create_app()


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
