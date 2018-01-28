from distutils.core import setup
setup(
  name = 'libsubcard',
  packages = ['libsubcard'],
  version = '0.1',
  description = 'A unofficial lib for (at the moment german) subcard data',
  author = 'Alexander Eisele',
  author_email = 'git@eiselecloud.de',
  url = 'https://github.com/derEisele/libSubcard',
  download_url = 'https://github.com/derEisele/libSubcard/archive/0.1.tar.gz',
  keywords = ['api'],
  install_requires=[
    'requests>=1.0',
  ],
  classifiers = [],
  )
