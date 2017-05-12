import translitru

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'translitru',
    'description': 'Transliteration for Russian language by predefined rules (GOST 7.79-2000, ISO 9-1995, U.S. State Department)',
    'packages': ['translitru'],
    'version': translitru.__version__,
    'author': 'Vitaly Zagorovskiy',
    'url': 'https://github.com/vzagorovskiy/translit-ru',
    'download_url': 'https://github.com/vzagorovskiy/translit-ru/archive/master.zip',
    'author_email': 'vzagorovskiy@gmail.com',
    'install_requires': [],
    'scripts': [],
    'license': 'MIT',
    'keywords': ['transliteration', 'transliterate'],
}

setup(**config)
