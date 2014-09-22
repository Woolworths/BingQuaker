#python3.3 works for Bing then I'll make it google when I can be fucked
#the main search has not been implemented yet, resultCount() and getUrls() works fine though
#MADE FOR EDUCATION PURPOSES, DO NOT USE!
from urllib.request import urlopen
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from django.utils.encoding import smart_str

class Core(object):
    #NOTE, this is not using the API therefore the max results you can get it 10
    def __init__(self, q, numResults=10, displayResults=True):
        self.q = smart_str(q)
        self.numResults = int(numResults)
        self.displayResults = bool(displayResults)
        # here is where we open url and make it into a bs4 object
        self.encode = urlencode({'q' : self.q})
        self.full_url = "http://www.bing.com/search?%s" % (self.encode)
        self.url = urlopen(self.full_url)
        self.html = BeautifulSoup(self.url)
    def __search__(self, resultType='search'):
        results = []
        html = self.html
        if(resultType == 'search'):
            for res in html.ol.find_all('li', attrs={'class': 'b_algo'}):
                res = res.find('div', attrs={'class': 'b_caption'})
                res = res.find('p')
                text = res.get_text()
                results.append(smart_str(text))
        elif(resultType == 'resultCount'):
            sbCount = html.find('span', attrs={'class': 'sb_count'})
            sbCount = sbCount.get_text()[:-8]
            results.append(smart_str(sbCount))
        elif(resultType == 'getUrls'):
            for url in html.ol.find_all('cite'):
                cleanUrl = url.get_text()
                results.append(smart_str(cleanUrl))
        #trim list
        if(resultType == 'search' or resultType == 'getUrls'): del results[self.numResults:]
        
        if(self.displayResults==True): print(results)
        elif(self.displayResults==False): return(results)        
    def search(self):
        self.__search__(resultType='search')
    def resultCount(self):
        self.__search__(resultType='resultCount')
    def getUrls(self):
        self.__search__(resultType='getUrls')

    def displayInfo(self, debug=False):
        print("q= %s" % (str(self.q)))
        print("numResults= %s" % (str(self.numResults)))
        if(debug==True):
            print("full_url= %s" % (str(self.full_url)))

def main():
    #remember you can only fetch 10 results (line 9)
    app = Core('SEARCH-TERM-IN-HERE', numResults=10, displayResults=True)
    app.search()
    #app.displayInfo(debug=True)
    #app.resultCount()
    app.getUrls()
if __name__ == "__main__":
    main()