from sys import argv
from bs4 import BeautifulSoup
import urllib2

script, word_to_find = argv

url = "http://es.thefreedictionary.com/%s" %  word_to_find

req = urllib2.urlopen(url)
data = req.read()
req.close()

soup = BeautifulSoup(data)


word_body = soup.find_all('div', class_ = "runseg")


print word_to_find, "\n\n"

for text in word_body:
  print text.get_text()