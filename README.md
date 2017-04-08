# applet
一个简化前后端分离的小工具，类似于微信小程序的打包编译


##### 安装
下载代码到本地，然后用pip install -r requirements.txt安装需要的依赖，然后运行python index.py即可

##### 修改项目代码地址和输出目录地址

只需要修改根目录的config.json即可

applet_dir_path为代码地址

build_dir_path为输出目录地址


##### 项目信息配置

每个项目的根目录必须有一个index.json文件，每一个页面的js必须提供一个app_init方法作为初始化函数

* pages是一个字典数组，每一个字典描述一个页面，url是浏览器上面对应的url，path对应的是页面代码文件夹
* title是页面默认的标题
* components是一个字典数组，每一个字典定义一个组件，name是组件名字，path是组件代码目录
* 404是指没有匹配路由的时候请求那一个地址，与上面pages定义相关联
* own_css_list是字符串列表，表明要引入哪些css
* own_js_list是字符串列表，表明要引入哪些js

##### 一些扩展的js方法

// 渲染页面，代替new Vue({...})

app.init(字典);

字典参数含义如下：

data：相当于vue的data参数

api：一个字典（可选），字典允许的key为url，data，method，headers，success，error

* url：需要请求的url
* data：请求参数
* method：GET，POST，请求类型
* headers：请求带上的heaaders
* success：请求成功回调函数，一个参数，获取到的数据，需要返回一个vue允许的data参数
* error：请求失败回调函数，需要返回vue允许的data参数

// vue对象（需要执行过app.init(字典);）

app.vm

// 无刷新跳转页面

app.goto(url)

##### 更多

* 可以参考项目的demo目录
* 还有疑问可以发送邮件到：yubang93@gmail.com