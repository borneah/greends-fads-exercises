import urllib.request

from urllib.request import urlopen

url1 = "http://olympus.realpython.org/profiles/aphrodite"

page1 = urlopen(url1)

page1

html_bytes = page1.read()
html = html_bytes.decode("utf-8")

