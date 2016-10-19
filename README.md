这是 The Django Book 中文版的随书CODE,是本人学习的学习过程，
由于第一次使用Github,可能有不规范，对访问者产生的困扰还望谅解。<br>
<br>
The Django Book 中文版：http://djangobook.py3k.cn/2.0/<br>
我现在看的是一个2.3M的PDF文件，名字是：Django_中文教程.pdf，我会以看到此PDF哪一页提交代码，以备自己后面查看<br>
<br>
在随书CODING过程中，我会记录一些问题，以及解决方法在这里<br>
2016-10-19<br>
<br>
1、书中提供的MySQLdb的驱动地址：http://www.djangoproject.com/r/python-mysql
这里只能下载到WIN32的驱动，如果是64位系统，需要另外自己去找64位的驱动，百度MySQL-python-1.2.3.win-amd64-py2.7.exe，可以下载。这里直接
使用pip install mysql-python,会报错的；所以选择下载单独程序做安装。<br>
<br>
2、Django版本问题，非常要注意书籍所使用软件的版本问题；本书使用的是1.1版，我使用的是1.10版，所以这会给后面的学习带来
很多的麻烦。我不打算更改Django的版本了，后面有问题解决好了：）<br>
<br>
3、记录一些 manag.py的命令<br>
django‐admin.py startproject mysite   创建名称为  mysite 的项目  <br>
python manage.py help                   帮助<br>
python manage.py runserver          启动服务<br>
python manage.py runserver 8080 启动服务并改变服务端口<br>
python manage.py shell                  启动交互界面<br>
python manage.py startapp books  在`` mysite`` 项目文件下输入下面的命令来创建`` books`` app<br>
python manage.py validate              命令验证模型的有效性(这个命令貌似在1.10版本里面没有了)<br>
数据库新建表或者修改表：<br>
python manage.py makemigrations rango  更改模型，修改数据库，产生migrations   第一步<br>
python manage.py migrate  将生成的migrations执行到目的数据库                         第二步<br>
python manage.py createsuperuser  创建管理员,用以登陆后台admin<br>
<br>
pip freeze > requirements.txt    生成环境配置文件<br>
pip install -r requirements.txt  根据文件安装配置<br>
