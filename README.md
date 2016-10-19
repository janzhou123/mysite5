这是 The Django Book 中文版的随书CODE,是本人学习的学习过程，
由于第一次使用Github,可能有不规范，对访问者产生的困扰还望谅解。<br>
<br>
The Django Book 中文版：http://djangobook.py3k.cn/2.0/<br>
<br>
在随书CODING过程中，我会记录一些问题，以及解决方法在这里<br>
2016-10-19<br>
<br>
1、书中提供的MySQLdb的驱动地址：http://www.djangoproject.com/r/python-mysql，这里只能下载到WIN32的驱动，
如果是64位系统，需要另外自己去找64位的驱动，百度MySQL-python-1.2.3.win-amd64-py2.7.exe，可以下载。这里直接
使用pip install mysql-python,会报错的；所以选择下载单独程序做安装。<br>
<br>
2、版本问题，非常要注意书籍所使用软件的版本问题；本书使用的是1.1版，我使用的是1.10版，所以这会给后面的学习带来
很多的麻烦。<br>
<br>