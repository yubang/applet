// 这里填充每一个页面的数据（一个字典）
var html_and_css_and_js_data = %(html_and_css_and_js_json)s;

// 路由处理
function goto_url(url){
    if(html_and_css_and_js_data[url]){
        $("#css").html(html_and_css_and_js_data[url]['css']);
        $("#html").html(html_and_css_and_js_data[url]['html']);
        $("#js").html(html_and_css_and_js_data[url]['js']);
        $("#loading").hide();
    }else{
        alert("404");
    }
}

$(document).ready(function(){
    goto_url(window.location.pathname);
});