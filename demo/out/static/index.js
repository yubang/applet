// 这里填充每一个页面的数据（一个字典）
var html_and_css_and_js_data = {"/404": {"title": "\u5c0f\u7a0b\u5e8f\u9996\u9875", "html": "\u4f3c\u4e4e\u4f60\u8bbf\u95ee\u4e86\u4e00\u4e2a\u9519\u8bef\u9875\u9762\uff01", "css": "", "js": ""}, "/abc": {"title": "\u5c0f\u7a0b\u5e8f\u9996\u9875", "html": "<app-test></app-test>", "css": "", "js": "console.log(\"welcome\")\nnew Vue({\n    el: \"#html\"\n})"}, "/debug": {"title": "\u5c0f\u7a0b\u5e8f\u9996\u9875", "html": "", "css": "", "js": ""}};

// 404页面地址
var not_found_path = "/404";

// 路由处理
function goto_url(url){
    if(html_and_css_and_js_data[url]){
        $("#css").html(html_and_css_and_js_data[url]['css']);
        $("#html").html(html_and_css_and_js_data[url]['html']);
        $("#js").html(html_and_css_and_js_data[url]['js']);
        $("#loading").hide();
    }else{
        if(html_and_css_and_js_data[not_found_path]){
            $("#css").html(html_and_css_and_js_data[not_found_path]['css']);
            $("#html").html(html_and_css_and_js_data[not_found_path]['html']);
            $("#js").html(html_and_css_and_js_data[not_found_path]['js']);
            $("#loading").hide();
        }else{
            alert("你访问的页面已经被吃掉了！");
        }
    }
}

// 组件js

            var html_App_e452db5c49091461a7e10760bdfc4a9b = {"html": "<div>\n    <a href=\"/debug\">a\u6807\u7b7e</a>\n</div>"};
            function App_e452db5c49091461a7e10760bdfc4a9b(){
                this.data = function(){
    return {};
}

this.props = function(){
    return [];
}

this.methods = function(){
    return {}
}
            }
            var app_e452db5c49091461a7e10760bdfc4a9b = new App_e452db5c49091461a7e10760bdfc4a9b();
            // 注册组件
            Vue.component('app-test', {
              template: html_App_e452db5c49091461a7e10760bdfc4a9b['html'],
              data: app_e452db5c49091461a7e10760bdfc4a9b.data,
              methods: app_e452db5c49091461a7e10760bdfc4a9b.methods(),
              props: app_e452db5c49091461a7e10760bdfc4a9b.props()
            })
        

$(document).ready(function(){
    goto_url(window.location.pathname);
});