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
    
    
def produce_url(netloc, path):
    scheme = "https"
    url_tuple = (scheme, netloc, path, "", "", "")
    return urllib.parse.urlunparse(url_tuple)

def get_freq_words(url):
    # Gets the most frequent words in a website and returns the most frequent words
    # that are not common English words (using a defined list of common words)
    common_words = ["to","of","in","for","on","with","at","by","from","up","about",
                    "into","over","after","the","and","a","that","I","it","not","he",
                    "as","you","this","but","his","they","her","she","or","an",
                    "will","my","one","all","would","there","their"]
    r = requests.get(url)

    soup = BeautifulSoup(r.content)

    text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))

    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
    # prints most common words staring at most frequent, removing list of common words
    ret = []
    for val in c.most_common():
        add = True
        for word in common_words:
            if val[0] == word:
                add = False
        if add == True:
            ret.append((val[0], val[1]))
    return(ret)