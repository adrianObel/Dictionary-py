from sys import exit
from bs4 import BeautifulSoup
import urllib2
import commands

# If no language is passed as argument get System language
def search_one(word_to_find):
  # Dummy language and encoding
  language = 'English'
  encoding = 'enc'

  data = commands.getoutput('locale')
  data = data.split('\n')
  for locale in data:
    if locale.split('=')[0] == 'LANG':
      language = locale.split('=')[1].split('.')[0]

  lang = language[:2]
  search_web((lang, word_to_find))

def search_two(lang, word_to_find):
  search_web((lang, word_to_find))


def search_web((lang, word_to_find)):

  if lang == 'es':
    url = 'http://es.thefreedictionary.com/%s' %  word_to_find
    search_for_class = 'runseg'

  elif lang == 'en':
    url = 'http://thefreedictionary.com/%s' %  word_to_find
    search_for_class = 'ds-list'

  elif lang == 'it':
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
