from distutils.core import setup

setup(name='palindrome',
      version='1.0',
      py_modules=['palindrome'],
      #metadata
      author="Devashish Nigam",
      author_email="thyanchor@gmail.com",
      description="Finding Palindrome nums",
      license="MIT",
      keywords="example",
      )


# C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome>python -m venv palindrome_env
#
# C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome>cd palindrome_env/Scripts
#
# C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome\palindrome_env\Scripts>activate
#
# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome\palindrome_env\Scripts>

# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome\palindrome_env\Scripts>cd ..
#
# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome\palindrome_env>cd ..
#
# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome>python setup.py install
# running install
# running build
# running build_py
# copying palindrome.py -> build\lib
# running install_lib
# copying build\lib\palindrome.py -> C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome\palindrome_env\Lib\site-packages
# byte-compiling C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome\palindrome_env\Lib\site-packages\palindrome.py to palindrome.cpython-37.pyc
# running install_egg_info
# Removing C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome\palindrome_env\Lib\site-packages\palindrome-1.0-py3.7.egg-info
# Writing C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome\palindrome_env\Lib\site-packages\palindrome-1.0-py3.7.egg-info
#
# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome>


# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome>cd ..
#
#
# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice>python
# Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import palindrome
# >>> palindrome.__file__
# 'C:\\Users\\dnigam\\PycharmProjects\\PlurasightPractice\\palindrome\\palindrome_env\\lib\\site-packages\\palindrome.py'
# >>>
# >>> exit()
#
# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice>cd palindrome
# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome>dir
#  Volume in drive C is WINDOWS
#  Volume Serial Number is AA35-5E2C
#
#  Directory of C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome
#
# 09-04-2020  02:19    <DIR>          .
# 09-04-2020  02:19    <DIR>          ..
# 09-04-2020  02:13    <DIR>          build
# 09-04-2020  02:14               326 palindrome.py
# 09-04-2020  02:08    <DIR>          palindrome_env
# 09-04-2020  02:19             2,368 setup.py
#                2 File(s)          2,694 bytes
#                4 Dir(s)  287,529,353,216 bytes free
#
# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome>

############################################################################################
# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome>python setup.py sdist --format zip
# running sdist
# running check
# warning: check: missing required meta-data: url
#
# warning: sdist: manifest template 'MANIFEST.in' does not exist (using default file list)
#
# warning: sdist: standard file not found: should have one of README, README.txt, README.rst
#
# writing manifest file 'MANIFEST'
# creating palindrome-1.0
# making hard links in palindrome-1.0...
# hard linking palindrome.py -> palindrome-1.0
# hard linking setup.py -> palindrome-1.0
# creating dist
# creating 'dist\palindrome-1.0.zip' and adding 'palindrome-1.0' to it
# adding 'palindrome-1.0\palindrome.py'
# adding 'palindrome-1.0\PKG-INFO'
# adding 'palindrome-1.0\setup.py'
# removing 'palindrome-1.0' (and everything under it)
#
# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome>

# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome>cd dist
#
# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome\dist>dir
#  Volume in drive C is WINDOWS
#  Volume Serial Number is AA35-5E2C
#
#  Directory of C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome\dist
#
# 09-04-2020  02:25    <DIR>          .
# 09-04-2020  02:25    <DIR>          ..
# 09-04-2020  02:25             1,557 palindrome-1.0.zip
#                1 File(s)          1,557 bytes
#                2 Dir(s)  287,526,146,048 bytes free
#
# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome\dist>

# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome\dist>pip install palindrome-1.0.zip
# Processing c:\users\dnigam\pycharmprojects\plurasightpractice\palindrome\dist\palindrome-1.0.zip
# Installing collected packages: palindrome
#   Found existing installation: palindrome 1.0
# Cannot uninstall 'palindrome'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
# You are using pip version 10.0.1, however version 20.0.2 is available.
# You should consider upgrading via the 'python -m pip install --upgrade pip' command.
#
# (palindrome_env) C:\Users\dnigam\PycharmProjects\PlurasightPractice\palindrome\dist>
