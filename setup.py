from setuptools import setup


setup(name='harder',
      version='0.01',
      description='Reinforcement Learning Utils',
      url='http://github.com/storborg/funniest',
      author='Jeremi Kaczmarczyk',
      author_email='jeremi.kaczmarczyk@gmail.com',
      license='MIT',
      packages=['harder'],
      install_requires=[
          'gym', 'nupmy', 'scipy'
      ],
zip_safe=False)