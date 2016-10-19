这是 The Django Book 中文版（http://djangobook.py3k.cn/2.0/）的随书CODE,是本人学习的学习过程，
由于第一次使用Github,可能有不规范，对访问者产生的困扰还望谅解。

在随书CODING过程中，我会记录一些问题，以及解决方法在这里
2016-10-19 \t\n
1、书中提供的MySQLdb的驱动地址：http://www.djangoproject.com/r/python-mysql，这里只能下载到WIN32的驱动，
如果是64位系统，需要另外自己去找64位的驱动，百度MySQL-python-1.2.3.win-amd64-py2.7.exe，可以下载。这里直接
使用pip install mysql-python,会报错的；所以选择下载单独程序做安装。
