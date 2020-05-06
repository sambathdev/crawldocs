import scrapy

class PostsSpider(scrapy.Spider):
    name = 'posts'
    start_urls = [
    
    ]
    f=open("urlslistshort.txt", "r")
    urllist = f.readlines()
    for url in urllist:
      start_urls.append(url)
      print('jkjl99999: ', url)
    print('pppppppppppp', start_urls)

    def parse(self, response):
      strStore = ''
      filename = ''
      className = [
        'Article__Headline__Title',
        'story-body__h1',
      ]
      for title in response.css('body'):
        strTitle = title.css('p ::text').getall()
        for i in strTitle:
          strStore += i
          # strStore += '\n'
      # fileName Config
      filename = response.css('.Article__Headline__Title::text').get()
      docTitle = filename + '\n'
      filename = filename.strip()
      # while ' ' in filename:
      #   filename = filename.replace(' ', '')
      b = ':!./,;)(*`-_#%+=$^& ?\''
      for char in b:
        filename = filename.replace(char,"")
      doc = open('docs/%s.txt' %filename, 'w') 
      doc.write(docTitle)
      doc.write(strStore)
      doc.close() 