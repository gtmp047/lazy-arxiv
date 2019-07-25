try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import xmltodict

url = 'http://export.arxiv.org/api/query?search_query=all:segmentation&start=0&max_results=10'
data = urlopen(url).read()
a = xmltodict.parse(data)
print(data)
