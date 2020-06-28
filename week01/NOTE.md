《git的操作笔记》
cd /E 切换目录
mkdir git 新建git文件夹
cd git 进入到git文件夹
ls -al 查看文件夹下的文件
git init 初始化git文件夹
git config --global user.name "gtzheng163" 配置用户
git config --global user.email "gtzheng@163.com" 配置用户邮箱
git config --global --list 查看配置的用户和邮箱

工作区，暂存区，仓库
创建learn_git.txt文件
git status 查看状态
git add learn_git.txt 加载到缓存区（git add .）加载所有
git commit -m "create learn_git file" 提交到仓库
git log 查看变更日志

创建仓库
选择SSH协议
git remote add origin git@github.com:gtzheng163/learn_git.git 连接远程仓库
git remote 查看是否连接成功
ssh-keygen -t rsa -C "gtzheng@163.com" 配置ssh公私钥
cd ../.ssh 切换到.ssh目录下
cat ...pub 查看公钥密码
浏览器设置新增ssh
ssh -T git@github.com 远程连接git
cd /e/learn_git 切换到仓库目录下
git push -u origin master 推送仓库文件到远程

《Python环境变量的配置》
where python3.7 查看Python安装路径
pip3 install ... 第三方库的安装
临时替换
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

永久替换
先升级 pip：pip3 install pip -U/python -m pip install --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip config set install.trusted-host pypi.tuna.tsinghua.edu.cn

A环境生成pip freeze requirements.txt
B环境克隆A环境pip install -r requirements.txt

创建虚拟环境并激活
python -m venv envir1/python -m venv envir2 创建在当前目录下
envir1/Scripts/activate 激活虚拟环境envir1
envir2/Scripts/activate 激活虚拟环境envir2

《requests》
requests.request() 构造一个请求，支撑以下各方法的基础方法
requests.get() 获取HTML网页的主要方法，对应于HTTP的GET
requests.head() 获取HTML网页头信息的方法，对应于HTTP的HEAD

1.为什么requests中需要添加headers？
在爬虫的时候，如果不添加请求头，可能网站会阻止一个用户的登陆，此时我们就需要添加请求头来进行模拟浏览网页

《beautifulsoup》
soup=beautifulsoup(解析内容,解析器)
常用解析器：html.parser,lxml,xml,html5lib
有时候需要安装安装解析器：比如pip3 install lxml

find( name , attrs , recursive , text , **kwargs ):根据参数来找出对应的标签,但只返回第一个符合条件的结果
find_all( name , attrs , recursive , text , **kwargs ):根据参数来找出对应的标签,但只返回所有符合条件的结果

筛选条件参数介绍：
name：为标签名,根据标签名来筛选标签
attrs:为属性,，根据属性键值对来筛选标签，赋值方式可以为:属性名=值,attrs={属性名:值}（但由于class是python关键字，需要使用class_）
text：为文本内容，根据指定文本内容来筛选出标签，（单独使用text作为筛选条件，只会返回text，所以一般与其他条件配合使用）
recursive：指定筛选是否递归，当为False时，不会在子结点的后代结点中查找，只会查找子结点

对于scrapy框架目前有个大概的了解，对其原理和使用还有点模糊，后续还得继续看老师视频和参考相关文档来理解。