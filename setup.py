try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'Dictionary for terminal'
, 'author': ['Adrian Obelmejias', 'Roger Gonzalez', 'Stefan Maric']
, 'author_email': ['obeladrian@gmail.com', 'rogergonzalez21@gmail.com','alexstefan92@gmail.com']
, 'url': 'https://github.com/adrianObel/Dictionary-py'
, 'version': '0.2'
, 'install_requires':['BeautifulSoup4','nose']
, 'packages': ['dictionary']
, 'scripts': ['bin/dictpy']
, 'name': 'Dictionary-py'
}

setup(**config)