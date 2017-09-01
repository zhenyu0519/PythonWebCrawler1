'''
Created on 2017Äê8ÔÂ31ÈÕ

@author: NUC
'''


class UrlManager(object):
    
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
    #add one new url to manager
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    #add some new urls to manager
    def add_new_urls(self, urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)

    #if the manager has new url
    def has_new_url(self):
        return len(self.new_urls)!=0

    #get a new url to craw from manager
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


    
    
    
    
    
    
    
    



