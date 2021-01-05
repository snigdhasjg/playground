from html.parser import HTMLParser

import requests

url = 'https://tracking.dtdc.com/ctbs-tracking/customerInterface.tr'

param = {
    'submitName': 'showCITrackingDetails',
    'cType': 'Consignment',
    'cnNo': 'B91876888'
}

parser = HTMLParser()
content = requests.get(url, param).content
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
parsed_html = BeautifulSoup(content)
text = parsed_html.body.find('div', attrs={'class': 'widget widget-table action-table'})\
    .find('div', attrs={'class': 'widget-content'})
print(text.text)

if __name__ == '__main__':
    pass
