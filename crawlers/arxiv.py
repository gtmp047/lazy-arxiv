import xmltodict
from typing import List
import requests
from collections import OrderedDict
from typing import Dict

try:
    from urllib.parse import urljoin, urlencode
except ImportError:
    from urlparse import urlparse
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def get_first(val: list):
    if val and isinstance(val, list):
        return val[0]
    return val



class ArxivCrawler:
    def __init__(self, search_query: str):
        query = self.build_query_string(search_query)
        self.query_url = f'http://export.arxiv.org/api/query?{query}'
        self.raw_data = xmltodict.parse(urlopen(self.query_url).read())
        self.parsed_data = ArxivCrawler.get_entry_infos(self.raw_data.get('feed').get('entry'),search_query )

    @staticmethod
    def build_data_line(arxiv: OrderedDict)-> Dict:
        return f"{arxiv.get('query')}\n{arxiv.get('id')}"

    @staticmethod
    def _get_authors(item: OrderedDict):
        if isinstance(item, list):
            return [i.get('name') for i in item]
        else:
            return [item.get('name')]


    @staticmethod
    def _get_categories( item: OrderedDict):
        if isinstance(item, list):
            return [i.get('@term') for i in item]
        else:
            return [item.get('@term')]

    @staticmethod
    def get_entry_infos(entry_list: List, query:str):
        res = []
        for i, item in enumerate(entry_list):
            item['query'] = query
            item['author'] =  ArxivCrawler._get_categories(item['author'])
            item['pdf_link'] = get_first([i.get('@href') for i in item['link'] if i.get('@type') == 'application/pdf'])
            item['category'] = ArxivCrawler._get_categories(item['category'])
            item['text'] = ArxivCrawler.build_data_line(item)
            item['pdf_file_b'] = '0'
            #todo very slow method Need to rethink

            # with requests.session() as sess:
            #     item['pdf_file_b'] = sess.get(item['pdf_link']).text.encode('utf-8')
            res.append(item)
        return res

    def build_query_string(self, search_query: str, start: int = 0, max_results: int = 10,
                           sortBy: str = 'submittedDate', sortOrder: str = 'descending'):
        data = {
            'search_query': search_query,
            'start': start,
            'max_results': max_results,
            'sortBy': sortBy,
            'sortOrder': sortOrder,
        }
        return urlencode(data)

if __name__ == '__main__':
    ArxivCrawler('image segmentation')