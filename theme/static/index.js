// 这里填充每一个页面的数据（一个字典）
var html_and_css_and_js_data = %(html_and_css_and_js_json)s;

// 404页面地址
var not_found_path = "%(not_found_path)s";

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
%(component_js)s

$(document).ready(function(){
    goto_url(window.location.pathname);
});