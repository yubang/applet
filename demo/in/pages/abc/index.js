function app_init(){
    app.init({
        "data": {t: "测试来的"},
        "api": {
            "url": "/api",
            success: function(d){return {t: d['data']}},
            method: "GET"
        }
    });
    console.log("welcome");
}