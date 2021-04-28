from setuptools import setup, find_packages

setup(
  name = 'conformer',
  packages = find_packages(),
  version = '0.2.5',
  license='MIT',
  description = 'The convolutional module from the Conformer paper',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/conformer',
  keywords = ['transformers', 'artificial intelligence', 'transformer'],
  install_requires=[
      'einops',
      'torch'
  ],
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
  ],
)
