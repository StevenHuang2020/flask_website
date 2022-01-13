# -*- encoding: utf-8 -*-
# Date: 13/Jan/2022
# Author: Steven Huang, Auckland, NZ
# License: MIT License
"""
Description: PostgreSQL db
"""
from flask_sqlalchemy import SQLAlchemy

class WebsiteDB():
    def __init__(self, app):
        db = SQLAlchemy(app)


def main():
    pass

if __name__ == "__main__":
    main()
