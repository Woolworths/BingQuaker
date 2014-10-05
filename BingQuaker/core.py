# MADE ONLY FOR EDUCATIONAL PURPOSES, DO NOT USE AS SCRAPING DATA MAY BE ILLEGAL!
# The program works fine however headline() is still being implemeted.
# make it so it can grab more than 10 request by going to page 2
from urllib.request import urlopen, Request
from urllib.parse import urlencode, quote_plus
from bs4 import BeautifulSoup
from django.utils.encoding import smart_str
import threading, random

browsers = ['Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3',
           'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
           'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
           'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1',
           'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1',
           'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
           'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)',
           'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)',
           'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)',
           'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
           'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)',
           'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51']
referrer = ['http://www.google.com/?q=',
           'http://www.usatoday.com/search/results?q=',
           'http://engadget.search.aol.com/search?q=',
           'https://www.bing.com']

class Search(threading.Thread):
    #NOTE, this is not using the API therefore the max results you can get it 10
    def __init__(self, q):
        self.q = q
        self.url = "https://www.bing.com"
        # here is where we open url and make it into a bs4 object
        self.query = quote_plus(self.q)
        self.fullUrl = "https://www.bing.com/search?q=%s" % (self.query)

        req = Request(self.fullUrl)        
        req.add_header('User-Agent', random.choice(browsers))
        req.add_header('Accept-Language', 'en-US,en;q=0.5')
        req.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
        req.add_header('Cache-Control', 'no-cache')
        req.add_header('Referer', random.choice(referrer))

        resp = urlopen(req)
        html = resp.read()
        self.html = BeautifulSoup(html)
        
    def __search__(self, resultType='search', *args, **kwargs):
        results = []
        displayResults = kwargs.get('displayResults')
        numResults = kwargs.get('numResults')
        
        html = self.html
        if(resultType == 'search'):
            for res in html.find_all('li', attrs={'class': 'b_algo'}):
                res = res.find('div', attrs={'class': 'b_caption'})
                res = res.find('p')
                text = res.get_text()
                results.append(smart_str(text))
        elif(resultType == 'resultCount'):
            sbCount = html.find('span', attrs={'class': 'sb_count'})
            sbCount = sbCount.get_text()[:-8]
            results.append(smart_str(sbCount))
        elif(resultType == 'getUrls'):
            for url in html.find_all('li', attrs={'class': 'b_algo'}):
                url = url.find('div', attrs={'class': 'b_attribution'})
                url = url.find('cite')
                cleanUrl = url.get_text()
                results.append(smart_str(cleanUrl))
        #trim list
        if(resultType == 'search' or resultType == 'getUrls' or resultType == 'headline'): del results[numResults:]
        
        if(displayResults==True): print(results)
        elif(displayResults==False): return(results)

    def resultCount(self, displayResults=True):
        self.__search__(resultType='resultCount', displayResults=displayResults)    
    def autocorrect(self, displayResults=True):
        pass    
    def headline(self, numResults=10, displayResults=True):
        pass
    def search(self, numResults=10, displayResults=True):
        self.__search__(resultType='search', numResults=numResults, displayResults=displayResults)
    def getUrls(self, numResults=10, displayResults=True):
        self.__search__(resultType='getUrls', numResults=numResults, displayResults=displayResults)

    def debug(self):
        print('q= "%s"' % (str(self.q)))
        print('full_url= "%s"' % (str(self.fullUrl)))

def usage():
    print('USAGE:')
    print('from BingQuaker.core import Search')
    print("app = Search('QUERY') - numResults and displayResults are optional")
    print('app.resultCount(displayResults=True) - Prints how many results the query returns')
    print('app.autocorrect(displayResults=False) - If the word is spelt wrong, returns the correct suggestion')
    print('app.headline(displayResults=False, numResults=3) - Returns the top 3 headlines')
    print('app.search(displayResults=False, numResults=6) - Returns the top 6 main information (unless you set displayResults to False)')
    print('app.getUrls(displayResults=True, numResults=2) - Prints the top 2 urls from the page')
    print('app.debug() - Displays information about things (meant for debugging)')
    print('SEE TESTS.PY FOR MORE!')
    print('SEE TESTS.PY FOR MORE!')
    print('SEE TESTS.PY FOR MORE!')

if __name__ == "__main__":
    usage()