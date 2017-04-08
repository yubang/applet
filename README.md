# applet
一个简化前后端分离的小工具，类似于微信小程序的打包编译


##### 安装
下载代码到本地，然后用pip install -r requirements.txt安装需要的依赖，然后运行python index.py即可

##### 修改项目代码地址和输出目录地址

只需要修改根目录的config.json即可

applet_dir_path为代码地址

build_dir_path为输出目录地址


##### 项目信息配置

每个项目的根目录必须有一个index.json文件

* pages是一个字典数组，每一个字典描述一个页面，url是浏览器上面对应的url，path对应的是页面代码文件夹
* title是页面默认的标题
* components是一个字典数组，每一个字典定义一个组件，name是组件名字，path是组件代码目录
* 404是指没有匹配路由的时候请求那一个地址，与上面pages定义相关联
* own_css_list是字符串列表，表明要引入哪些css
* own_js_list是字符串列表，表明要引入哪些js

##### 更多

* 可以参考项目的demo目录
* 还有疑问可以发送邮件到：yubang93@gmail.com