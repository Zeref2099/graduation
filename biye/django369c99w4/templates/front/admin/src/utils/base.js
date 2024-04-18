const base = {
    get() {
        return {
            url : "http://localhost:8080/django369c99w4/",
            name: "django369c99w4",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于Django的招聘数据分析可视化系统"
        } 
    }
}
export default base
