from distutils.core import setup


setup(name='sub', version='0.7',
      py_modules=['test', 'Map', 'NaverMaps', 'NaverSearch', 'telegram', 'TimeTable', 'Graph'],
      package_data=['bak.png', 'Linemap.jpg', 'Title.png']
      )