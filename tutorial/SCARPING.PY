import yieldfrom.urllib.request
from bs4 import BeautifulSoup

test_url="https://www.amazon.com/"

data_url = yieldfrom.urllib.request.urlopen(test_url)
read_html = data_url.read()
data_url.close()

print(read_html)
