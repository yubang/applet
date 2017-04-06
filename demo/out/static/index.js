// 这里填充每一个页面的数据（一个字典）
var html_and_css_and_js_data = {"/abc": {"title": "\u5c0f\u7a0b\u5e8f\u9996\u9875", "html": "123", "css": "", "js": ""}, "/debug": {"title": "\u5c0f\u7a0b\u5e8f\u9996\u9875", "html": "", "css": "", "js": ""}};

// 路由处理
function goto_url(url){
    if(html_and_css_and_js_data[url]){
        $("#css").html(html_and_css_and_js_data[url]['css']);
        $("#html").html(html_and_css_and_js_data[url]['html']);
        $("#loading").hide();
    }else{
        alert("404");
    }
}

$(document).ready(function(){
    goto_url(window.location.pathname);
});