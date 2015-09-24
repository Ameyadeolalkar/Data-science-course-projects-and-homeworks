'''
OPTIONAL WEB SCRAPING HOMEWORK

First, define a function that accepts an IMDb ID and returns a dictionary of
movie information: title, star_rating, description, content_rating, duration.
The function should gather this information by scraping the IMDb website, not
by calling the OMDb API. (This is really just a wrapper of the web scraping
code we wrote above.)

For example, get_movie_info('tt0111161') should return:

{'content_rating': 'R',
 'description': u'Two imprisoned men bond over a number of years...',
 'duration': 142,
 'star_rating': 9.3,
 'title': u'The Shawshank Redemption'}

Then, open the file imdb_ids.txt using Python, and write a for loop that builds
a list in which each element is a dictionary of movie information.

Finally, convert that list into a DataFrame.
'''

from bs4 import BeautifulSoup
import requests
import pandas as pd
def get_movie_info(id):
    d={}
    r=requests.get('http://www.imdb.com/title/'+id+'/')   
    b = BeautifulSoup(r.text)
    d['content_rating'] = b.find(name='meta',attrs={'itemprop':'contentRating'})['content']
    d['description'] = b.find(name='p',attrs={'itemprop':'description'}).text
    info = b.find(name='time',attrs={'itemprop':'duration'}).text.strip()[:-4]
    d['duration'] = int(info)
    star = b.find(name='div',attrs={'class':'titlePageSprite star-box-giga-star'}).text.strip()
    d['star_rating'] = float(star)
    d['title'] = b.find(name='span',attrs={'class':'itemprop','itemprop':'name'}).text
    print d
    
get_movie_info('tt0111161') 
titles = []
info = []
with open('imdb_ids.txt') as f:
    for line in f:
        titles.append(line.strip())
print titles

for id in titles:
    pd.DataFrame(get_movie_info(id))
    