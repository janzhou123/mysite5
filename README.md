这是 The Django Book 中文版自己的随书CODE,也是本人学习的学习过程，
由于第一次使用Github,可能有不规范，对访问者产生的困扰还望谅解。<br>
<br>
The Django Book 中文版：http://djangobook.py3k.cn/2.0/<br>
我现在看的是一个2.3M的PDF文件，名字是：Django_中文教程.pdf，我会以看到此PDF哪一页提交代码，以备自己后面查看<br>
<br>
在随书CODING过程中，我会记录一些问题，以及解决方法在这里；还有一些自己觉值得记录的东西<br>
### 2016-10-19<br />
2016-10-19<br>
1、书中提供的MySQLdb的驱动地址：http://www.djangoproject.com/r/python-mysql
    这里只能下载到WIN32的驱动，如果是64位系统，需要另外自己去找64位的驱动，百度MySQL-python-1.2.3.win-amd64-py2.7.exe，可以下载。这里直接
    使用pip install mysql-python,会报错的；所以选择下载单独程序做安装。另外如果想在venv中安装MySqldb,pip不成功的话，可以直接将安装成功的
    文件拷贝到venv目录中，可以使用pip uninstall mysql-python获得需要拷贝的文件清单<br>
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
    pip freeze > requirements.txt    生成环境配置文件<br>
    pip install -r requirements.txt  根据文件安装配置<br>
<br>
4、测试数据库是否连接正常<br>
    from django.db import connection<br>
    cursor = connection.cursor()  没有错误返回则正常<br>
<br>
5、HttpRequest对象包含当前请求URL的一些信息：<br>
request.path 除域名以外的请求路径，以正斜杠开头 "/hello/"<br>
request.get_host() 主机名（比如，通常所说的域名） "127.0.0.1:8000"or"www.example.com"<br>
request.get_full_path()请求路径，可能包含查询字符串 "/hello/?print=true"<br>
request.is_secure() 如果通过HTTPS访问，则此方法返回True， 否则返回False True或者 False<br>
有关request的其它信息：<br>
request.META 是一个Python字典，包含了所有本次HTTP请求的Header信息<br>
HTTP_REFERER，进站前链接网页，如果有的话。 （请注意，它是REFERRER的笔误。）
HTTP_USER_AGENT，用户浏览器的user-agent字符串，如果有的话。 例如："Mozilla/5.0 (X11; U; Linux i686; fr‐FR; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17".
REMOTE_ADDR客户端IP，如："12.345.67.89"。(如果申请是经过代理服务器的话，那么它可能是以逗号分割的多个IP地址，如："12.345.67.89,23.456.78.90"。)