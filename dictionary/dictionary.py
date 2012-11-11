from sys import exit
from bs4 import BeautifulSoup
import urllib2


  
def search_for((lang, word_to_find)):

  if lang == 'spanish' or lang == 'espanol':
    url = 'http://es.thefreedictionary.com/%s' %  word_to_find
    search_for_class = 'runseg'

  elif lang == 'english' or lang =='ingles':
    url = 'http://thefreedictionary.com/%s' %  word_to_find
    search_for_class = 'ds-list'

  elif lang == 'italian' or lang == 'italien':
    url = 'http://it.thefreedictionary.com/%s' % word_to_find
    search_for_class = 'runseg'

  else:
    print 'Language not supported'
    exit()

  req = urllib2.urlopen(url)
  data = req.read()
  req.close()

  soup = BeautifulSoup(data)


  word_body = soup.find_all('div', class_ = search_for_class)

  print '\n',word_to_find, '\n\n'

  if word_body:
    for text in word_body:
      print text.get_text()
  else:
    print "Word not found"
