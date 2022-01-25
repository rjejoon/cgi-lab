#!/usr/bin/env python3

import os

import cgi
import cgitb


def main():

    form = cgi.FieldStorage()

    print("Content-Type: text/html")    
    print()                             # blank line, end of headers

    print("<html>")

    print("<head>")
    print("<title>CGI Program</title>")
    print("</head>")

    print("<body>")
    print("Hello, world!")

    print("</body>")
    print("</html>")




if __name__ == '__main__':
    cgitb.enable()      # display errors occured in web browsers
    main()
