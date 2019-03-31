import requests
import os
import datetime
class Ingester:
   def __init__(self, type , sourceUrl, targetFileName):
      self.type = type
      self.sourceUrl = sourceUrl
      self.targetFileName = targetFileName
   def ingestRssFeed(self):
      resp = requests.get(self.sourceUrl)
      with open(self.targetFileName,'wb') as f:
        f.write(resp.content)
homePath = os.environ['APPHOME']
tz = str(datetime.datetime.utcnow())
I = Ingester('RSS','http://export.arxiv.org/rss/cs', homePath + '/Landing/cs_'+ tz +'.xml')
I.ingestRssFeed()
