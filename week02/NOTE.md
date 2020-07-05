学习笔记
结合上周学习内容梳理下scrapy框架的流程
1.当SPIDER要爬取某URL地址的页面时，需使用该URL构造一个Request对象，提交给ENGINE。
2.ENGINE将Request对象传给SCHEDULER，SCHEDULER对URL进行去重，按某种算法进行排队，之后的某个时刻SCHEDULER将其出队，将处理好的Request对象返回给ENGINE。
3.ENGINE将SCHEDULER处理后的Request对象发送给DOWNLOADER下载页面。
4.DOWNLOADER根据MIDDLEWARE的规则，使用Request对象中的URL地址发送一次HTTP请求到网站服务器，之后用服务器返回的HTTP响应构造出一个Response对象，其中包含页面的HTML文本。DOWNLOADER将结果Resopnse对象传给ENGINE。
5.ENGINE将Response对象发送给SPIDER的页面解析函数（构造Request对象时指定）进行处理，页面解析函数从页面中提取数据，封装成Item后提交给ENGINE。
6.ENGINE将Item送往ITEMPIPELINES进行处理，最终以某种数据格式写入文件（csv，json）或者存储到数据库中。

pymysql学习
fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
mysql的游标建立之时，就自动开始了一个隐形的数据库事务。
commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。
爬虫中间件
下载中间件（Downloader Middlewares） 位于scrapy引擎和下载器之间的一层组件。
1.引擎将请求传递给下载器过程中， 下载中间件可以对请求进行一系列处理。比如设置请求的 User-Agent，设置代理等
2.在下载器完成将Response传递给引擎中，下载中间件可以对响应进行一系列处理。比如进行gzip解压等

user-agent池
作用：尽可能多的将scrapy工程中的请求伪装成不同类型的浏览器身份。
操作流程：
1.在下载中间件中拦截请求
2.将拦截到的请求的请求头信息中的UA进行篡改伪装
3.在配置文件中开启下载中间件

代理池
作用：尽可能多的将scrapy工程中的请求的·设置成不同的。
操作流程：
在下载中间件中拦截请求
将拦截到的请求的IP修改成某一代理IP
在配置文件中开启下载中间件

这一周的课程，前半部分可以理解，需要多写代码，多练习来巩固；对于爬虫中间件和代理池这一块还是没有特别理解，需要后续再多看几遍的老师的视频和参考一些书籍来弄懂。


