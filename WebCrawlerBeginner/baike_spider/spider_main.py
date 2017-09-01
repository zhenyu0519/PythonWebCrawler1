#coding: utf8
'''
Created on 2017年8月31日

@author: Jeffery
'''
from baike_spider import url_manager, html_downloader, html_outputer,\
    html_parser


class SpiderMain(object):
    #Inilize the components object in constructor
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        #to record the current url number
        count = 1
        #add the root_url to url manager
        self.urls.add_new_url(root_url)
        #when url manager has new url then loop
        while self.urls.has_new_url():
            try:
                #get the new url
                new_url = self.urls.get_new_url()
                print 'craw %d: %s' % (count, new_url)
                #download the url to html container
                html_cont = self.downloader.download(new_url)
                #parser the url data and get the new url list and data.
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                #add the url to url manager
                self.urls.add_new_urls(new_urls)
                #collect the data
                self.outputer.collect_data(new_data)
                if(count == 1000):
                    break
                
                count = count + 1
            except:
                print 'craw failed!'
            
            
            
        self.outputer.output_html()
    
    



if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    #create spider
    obj_spider = SpiderMain()
    #run spider
    obj_spider.craw(root_url)