#python3.3 bing the I'll make it google when i can be fucked!
# __search__() does all the work
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.utils.encoding import smart_str

class Core(object):
    def __init__(self, q, numResults=10, displayResults=True):
        self.q = smart_str(q)
        self.numResults = int(numResults)
        self.displayResults = bool(displayResults)
        # here is where we open url and make it into a bs4 object
        self.full_url = "http://www.bing.com/search?q=%s" % (self.q)
        self.url = urlopen(self.full_url)
        self.html = BeautifulSoup(self.url)
    def __search__(self, resultType='search'):
        results = []
        html = self.html
        if(resultType == 'search'):
            pass
        elif(resultType == 'resultCount'):
            sbCount = html.find('span', attrs={'class': 'sb_count'})
            sbCount = sbCount.get_text()[:-8]
            results.append(sbCount) 
        elif(resultType == 'getUrls'):
            for url in html.ol.find_all('cite'):
                cleanUrl = url.get_text()
                results.append(cleanUrl)
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
    letssee = Core('google', numResults=5, displayResults=True)
    #letssee.displayInfo(debug=True)
    letssee.resultCount()
    letssee.getUrls()
if __name__ == "__main__":
    main()