#!/usr/bin/env python3

import os
import json


def main():

    # print("Content-Type: application/json")
    print("Content-type: text/html")
    print()                             # end of headers

    # print(json.dumps(dict(os.environ), indent=2))
    # print(f"<p>QUERY_STRING: {os.environ['QUERY_STRING']}</p>")
    print(f"<p>HTTP_USER_AGENT: {os.environ['HTTP_USER_AGENT']}</p>")



if __name__ == '__main__':
    main()
