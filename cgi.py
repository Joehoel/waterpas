#!/usr/bin/python3

import datetime

# print HTTP header
print("Content-type: text/plain\n")

# dynamic body
print("een python CGI script")
print(datetime.datetime.now())

# done
print("Einde script")
