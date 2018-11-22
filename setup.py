from setuptools import setup

setup(name='pytabfmt',
      version='0.1',
      description='formatter class for emitting latex tables',
      url='http://github.com/amlimaye/pytabfmt',
      author='Aditya Limaye',
      author_email='aditya.limaye@gmail.com',
      license='MIT',
      packages=['pytabfmt'],
      zip_safe=False,
      setup_requires=['pytest-runner'],
      tests_require=['pytest'])
