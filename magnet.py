from urllib import unquote
import re

class magnet(object):

    match_xt = re.compile('xt=([^&]*)').search
    match_dn = re.compile('dn=([^&]*)').search
    
    def __init__(self, url):
        # TODO: check magnet url
        self.url = url

    @property
    def xt(self):
        m = self.match_xt(self.url)
        return m.group(1) if m else ''

    @property
    def dn(self):
        m = self.match_dn(self.url)
        return unquote(m.group(1)) if m else ''

def test_xt(urls):
    return [magnet(url).xt for url in urls]

def test_dn(urls):
    return [magnet(url).dn for url in urls]

if __name__ == '__main__':
    with open('magnets.txt') as f:
        urls = [url.strip() for url in f.readlines()]
    print test_xt(urls)[-2]
    print test_dn(urls)[-1]
    pass
