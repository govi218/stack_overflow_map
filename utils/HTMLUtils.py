import urllib
from HyperlinkParser import HyperlinkParser

def extract_url_path(url):
    return urllib.parse.urlparse(url).path

def extract_url_netloc(url):
    return urllib.parse.urlparse(url).netloc

def word_in_list(word,lst):
    for elem in lst:
        if word in elem:
            return True
    return False

def is_same_netloc(url1,url2):
    netloc1 = extract_url_netloc(url1)
    netloc2 = extract_url_netloc(url2)
    return netloc1 == netloc2

def is_linked(url1, url2):
    html = get_html(url1)
    parser = HyperlinkParser()
    parser.feed(html)
    url1_links = parser.links
    url2_path = extract_url_path(url2)
    for link in url1_links:
        if url2 in link:
            return True
        if url2_path in link:
            return True
    return False

def get_html(url):
    website = urllib.request.urlopen(url)
    html = website.read().decode()
    return html