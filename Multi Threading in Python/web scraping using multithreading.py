'''
Web scraping is a I/O bound operations in which we wait for resoponse from a server.
It involves numerous network requests to obtain data from web.

'''
'''
https://python.langchain.com/docs/introduction/

https://python.langchain.com/docs/concepts/

https://python.langchain.com/docs/tutorials/

'''
import threading
from bs4 import BeautifulSoup 
import requests

urls = [
    "https://python.langchain.com/docs/introduction/",
    "https://python.langchain.com/docs/concepts/",
    "https://python.langchain.com/docs/tutorials/"
]