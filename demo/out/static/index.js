// 这里填充每一个页面的数据（一个字典）
var html_and_css_and_js_data = {"/404": {"title": "\u5c0f\u7a0b\u5e8f\u9996\u9875", "html": "\u4f3c\u4e4e\u4f60\u8bbf\u95ee\u4e86\u4e00\u4e2a\u9519\u8bef\u9875\u9762\uff01", "css": "", "js": "app.init({});"}, "/abc": {"title": "\u5c0f\u7a0b\u5e8f\u9996\u9875", "html": "<app-test v-bind:t=\"t\"></app-test>", "css": "", "js": "app.init({\n        \"data\": {t: \"\u6d4b\u8bd5\u6765\u7684\"},\n        \"api\": {\n            \"url\": \"/api\",\n            success: function(d){return {t: d['data']}},\n            method: \"GET\"\n        }\n    });\n    console.log(\"welcome\");"}, "/debug": {"title": "\u5c0f\u7a0b\u5e8f\u9996\u9875", "html": "", "css": "", "js": "app.init({})"}};

// 404页面地址
var not_found_path = "/404";

// js name
var js_label_name = "js_";
var js_label_index = 0;

// 路由处理
function goto_url(url){
    if(html_and_css_and_js_data[url]){
        $("#css").html(html_and_css_and_js_data[url]['css']);
        $("#html").html(html_and_css_and_js_data[url]['html']);

        $("#" + js_label_name + js_label_index).remove();
        js_label_index++;
        $("body").append('<script id="'+js_label_name + js_label_index+'">'+html_and_css_and_js_data[url]['js']+'</script>');
    }else{
        if(html_and_css_and_js_data[not_found_path]){
            $("#css").html(html_and_css_and_js_data[not_found_path]['css']);
            $("#html").html(html_and_css_and_js_data[not_found_path]['html']);
            $("#" + js_label_name + js_label_index).remove();
            js_label_index++;
            $("body").append('<script id="'+js_label_name + js_label_index+'">'+html_and_css_and_js_data[not_found_path]['js']+'</script>');
        }else{
            alert("你访问的页面已经被吃掉了！");
        }
    }
}

// 组件js

            var html_App_e452db5c49091461a7e10760bdfc4a9b = {"html": "<div>\n    <a href=\"/debug\">{{ t }}</a>\n</div>"};
            function App_e452db5c49091461a7e10760bdfc4a9b(){
                this.data = function(){
    return {"t": "ceshi"};
}

this.props = function(){
    return ["t"];
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
        

// app内置的方法
function Applet(){

    this.vm = null;

    // 是否显示loading
    this.show_loading = function(sign){
        if(sign){
            $("#html").hide();
            $("#loading").show();
        }else{
            $("#html").show();
            $("#loading").hide();
        }
    }

    this.render = function(d){
        var that = this;
        this.vm = new Vue({
            el: '#html',
            data: d['data'] || {},
            methods: d['methods'] || {},
            mounted: function(){
                that.show_loading(false);
            }
        });
    }

    // 渲染页面
    this.init = function(vue_data){
        // 显示loadin动画
        this.show_loading(true);

        var api = vue_data['api'] || {};
        // 获取api数据
        var api_url = api['url'] || null;
        var api_data = api['data'] || {};
        var api_method = api['method'] || "GET";
        var api_headers = api['headers'] || {};
        var success = api['success'] || function(d){return d;}
        var error = api['error'] || function(){}

        if(api_url == null){
            this.render(vue_data);
        }else{
            var that = this;
            $.ajax({
                url: api_url,
                type: api_method,
                headers: api_headers,
                data: api_data,
                success: function(d){
                    vue_data['data'] = success(d);
                    that.render(vue_data);
                },
                error: function(){
                    error();
                    that.render(vue_data);
                }
            });

        }

    }

    // 无刷新跳转页面
    this.goto = function(url){
        window.history.pushState({},0,url);
         goto_url(url);
    }

}

var app = new Applet();

$(document).ready(function(){
    goto_url(window.location.pathname);
});