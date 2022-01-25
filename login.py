#!/usr/bin/env python3

import cgi
import cgitb
import secret
import os
from http.cookies import SimpleCookie

from templates import login_page, secret_page, after_login_incorrect


def main():

  form = cgi.FieldStorage()
  username = form.getfirst("username")
  password = form.getfirst("password")

  form_ok = username == secret.username and password == secret.password

  # set up cookie
  cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
  cookie_username = None
  cookie_password = None
  if cookie.get("username"):
    cookie_username = cookie.get("username").value
  if cookie.get("password"):
    cookie_password = cookie.get("password").value

  cookie_ok = cookie_username == secret.username and cookie_password == secret.password

  if cookie_ok:
    username = cookie_username
    password = cookie_password

  print("Content-Type: text/html")
  
  if form_ok:
    # set cookie if login info is correct
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

  print()     # end of header lines

  # login page
  if not username and not password:
    print(login_page())
  elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
  else:
    print(after_login_incorrect())


if __name__ == '__main__':
  cgitb.enable()    # display errors in the browser
  main()