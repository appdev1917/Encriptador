from setuptools import setup, find_packages
setup(
  name = 'Encriptador',         # How you named your package folder (MyLib)
  packages = find_packages(),   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='gpl-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Encriptador y desencriptador de archivos utilizando la AESCrypt',   # Give a short description about your library
  author = 'app.dev1917',                   # Type in your name
  author_email = 'app.dev1917@outlook.com',      # Type in your E-Mail
  url = 'https://github.com/appdev1917/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/appdev1917/Encriptador/archive/1.0.1.tar.gz',    # I explain this later on
  keywords = ['ENCRIPTADOR','DESENCRIPTADOR'],   # Keywords that define your package best
  python_requires='>=3.5, <4', 
  install_requires=[            # I get to this in a second
          'pyAesCrypt',
          'tkinter',
          'PIL'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
