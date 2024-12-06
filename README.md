API文件夹是后端接口文件采用FastApi，python开发，进去运行main.py文件即可运行接口
！！注意：里面database.py是连接数据库的里面连接的时候需要改为自己的用户名和密码
可以在出现的连接后加上 /docs，例如：http://127.0.0.1:8000/docs到浏览器可以看到所有接口

my_text文件夹是用vue2，element-ui设计的页面（页面长得不是很好看）
暂时还没有设置路由守卫
前端启动使用 npm run serve
还得下载element-ui的包，可到官网看

datas.sql文件是创建的本地的数据库使用的navicate，导入就可以了
其中users表有用户列表最后is_admin字段为1则是管理员用户可以自己在数据库添加一个管理员

后面上传几张截图分别是一些界面展示
在imags文件夹中
