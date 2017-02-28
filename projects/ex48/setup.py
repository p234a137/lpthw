try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config ={
        'description': 'Exercise 48 Lexicon',
        'author': 'R2 D2',
        'url': 'URL to get at it.',
        'download_url': 'Where to download it.',
        'author_email':'p234a137@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex48'],
        'scripts': [],
        'name': 'Lexicon'
}

setup(**config)
