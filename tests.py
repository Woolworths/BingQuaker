from core import Search
import threading
'''
FOR YOU IT WOULD BE:
from BingQuaker.core import Search
'''

app = Search('hello kitty')
count = threading.Thread(target=app.resultCount(displayResults=True))
autocorrect = threading.Thread(target=app.autocorrect(displayResults=True))
headline = threading.Thread(target=app.headline(displayResults=True))
search = threading.Thread(target=app.search(numResults=1))
getUrls = threading.Thread(target=app.getUrls(displayResults=True, numResults=4))

#alternatively:

#app.resultCount(displayResults=True)
#app.headline(displayResults=False, numResults=3)
#app.search(numResults=1)
#app.getUrls(displayResults=True, numResults=4)