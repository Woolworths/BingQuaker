from core import Search
'''
from the file 'core.py', import the class 'Core'
for you it would be:
from BingQuaker.core import Core
'''
app = Search('Hello Kitty')
app.resultCount(displayResults=True)
app.headline(displayResults=False, numResults=3)
app.search(numResults=1)
app.getUrls(displayResults=True, numResults=4)
app.debug()