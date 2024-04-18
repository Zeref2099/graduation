<template>
<div class="content" :style='{"minHeight":"100vh","width":"100%","padding":"30px","background":"url(http://codegen.caihongy.cn/20240406/b4e984e90fb34e1cb7a7aac463fb85da.png) no-repeat center top / cover","height":"auto"}'>
	<!-- notice -->
	<!-- title -->
	<div class="text" :style='{"margin":"50px auto","fontSize":"24px","color":"rgb(51, 51, 51)","textAlign":"center","fontWeight":"bold"}'>欢迎使用 {{this.$project.projectName}}</div>
	<!-- statis -->
	<div :style='{"margin":"0 0 20px 0","alignItems":"center","justifyContent":"center","display":"flex"}'>
		<div :style='{"boxShadow":"0 1px 6px rgba(0,0,0,.3)","margin":"0 10px","borderRadius":"4px","display":"flex"}' v-if="isAuth('yonghu','首页总数')">
			<div :style='{"width":"80px","alignItems":"center","background":"rgba(44, 55, 66,1)","justifyContent":"center","display":"flex","height":"80px"}'>
				<span class="icon iconfont icon-shenhe9" :style='{"color":"#fff","fontSize":"24px"}'></span>
			</div>
			<div :style='{"width":"160px","alignItems":"center","flexDirection":"column","justifyContent":"center","display":"flex"}'>
				<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"20px","color":"#333","fontWeight":"bold","height":"24px"}'>{{yonghuCount}}</div>
				<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"16px","color":"#666","height":"24px"}'>用户总数</div>
			</div>
		</div>
		<div :style='{"boxShadow":"0 1px 6px rgba(0,0,0,.3)","margin":"0 10px","borderRadius":"4px","display":"flex"}' v-if="isAuth('zhiwei','首页总数')">
			<div :style='{"width":"80px","alignItems":"center","background":"rgba(44, 55, 66,1)","justifyContent":"center","display":"flex","height":"80px"}'>
				<span class="icon iconfont icon-zhangjie18" :style='{"color":"#fff","fontSize":"24px"}'></span>
			</div>
			<div :style='{"width":"160px","alignItems":"center","flexDirection":"column","justifyContent":"center","display":"flex"}'>
				<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"20px","color":"#333","fontWeight":"bold","height":"24px"}'>{{zhiweiCount}}</div>
				<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"16px","color":"#666","height":"24px"}'>职位总数</div>
			</div>
		</div>
	</div>
	<!-- statis -->
	

	
	<!-- echarts -->
</div>
</template>
<script>
//0
import router from '@/router/router-static'
import * as echarts from 'echarts'
export default {
	data() {
		return {
            yonghuCount: 0,
            zhiweiCount: 0,
		};
	},
	mounted(){
		this.init();
		this.getyonghuCount();
		this.getzhiweiCount();
	},
	methods:{
		init(){
			if(this.$storage.get('Token')){
			this.$http({
				url: `${this.$storage.get('sessionTable')}/session`,
				method: "get"
			}).then(({ data }) => {
				if (data && data.code != 0) {
				router.push({ name: 'login' })
				}
			});
			}else{
				router.push({ name: 'login' })
			}
		},
		getyonghuCount() {
			this.$http({
				url: `yonghu/count`,
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code == 0) {
					this.yonghuCount = data.data
				}
			})
		},
		getzhiweiCount() {
			this.$http({
				url: `zhiwei/count`,
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code == 0) {
					this.zhiweiCount = data.data
				}
			})
		},
  }
};
</script>
<style lang="scss" scoped>
    .cardView {
        display: flex;
        flex-wrap: wrap;
        width: 100%;

        .cards {
            display: flex;
            align-items: center;
            width: 100%;
            margin-bottom: 10px;
            justify-content: center;
            .card {
                width: calc(25% - 20px);
                margin: 0 10px;
                /deep/.el-card__body{
                    padding: 0;
                }
            }
        }
    }
	
	// 日历
	.calendar td .text {
				border-radius: 12px;
				flex-direction: column;
				background: #fff;
				display: flex;
				width: 100%;
				justify-content: center;
				align-items: center;
				height: 100%;
			}
	.calendar td .text:hover {
				background: rgba(78,110,242,.1);
			}
	.calendar td .text .new {
				color: #000;
				font-size: 24px;
				line-height: 1.4;
			}
	.calendar td .text .old {
				color: #666;
				font-size: 16px;
				line-height: 1.4;
			}
	.calendar td.festival .text {
				border-radius: 12px;
				flex-direction: column;
				background: rgba(235,51,51,.05);
				display: flex;
				width: 100%;
				justify-content: center;
				align-items: center;
				height: 100%;
			}
	.calendar td.festival .text:hover {
				background: rgba(78,110,242,.1);
			}
	.calendar td.festival .text .new {
				color: #000;
				font-size: 24px;
				line-height: 1.4;
			}
	.calendar td.festival .text .old {
				color: #666;
				font-size: 16px;
				line-height: 1.4;
			}
	.calendar td.other .text {
				border-radius: 12px;
				flex-direction: column;
				background: #fff;
				display: flex;
				width: 100%;
				justify-content: center;
				align-items: center;
				opacity: 0.3;
				height: 100%;
			}
	.calendar td.other .text:hover {
				background: rgba(78,110,242,.1);
			}
	.calendar td.other .text .new {
				color: #000;
				font-size: 24px;
				line-height: 1.4;
			}
	.calendar td.other .text .old {
				color: #666;
				font-size: 16px;
				line-height: 1.4;
			}
	.calendar td.today .text {
				border-radius: 12px;
				flex-direction: column;
				color: #fff;
				background: rgb(64, 158, 255);
				display: flex;
				width: 100%;
				justify-content: center;
				align-items: center;
				height: 100%;
			}
	.calendar td.today .text:hover {
				background: rgba(64, 158, 255,.5);
			}
	.calendar td.today .text .new {
				color: inherit;
				font-size: 24px;
				line-height: 1.4;
			}
	.calendar td.today .text .old {
				color: inherit;
				font-size: 16px;
				line-height: 1.4;
			}
	
	// echarts1
	.type1 .echarts1 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 100%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type1 .echarts1:hover {
			}
	// echarts2
	.type2 .echarts1 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 49%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type2 .echarts1:hover {
			}
	.type2 .echarts2 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 49%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type2 .echarts2:hover {
			}
	// echarts3
	.type3 .echarts1 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 100%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type3 .echarts1:hover {
			}
	.type3 .echarts2 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 49%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type3 .echarts2:hover {
			}
	.type3 .echarts3 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 49%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type3 .echarts3:hover {
			}
	// echarts4
	.type4 .echarts1 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 49%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type4 .echarts1:hover {
			}
	.type4 .echarts2 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 49%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type4 .echarts2:hover {
			}
	.type4 .echarts3 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 49%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type4 .echarts3:hover {
			}
	.type4 .echarts4 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 49%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type4 .echarts4:hover {
			}
	// echarts5
	.type5 .echarts1 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 100%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type5 .echarts1:hover {
			}
	.type5 .echarts2 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 49%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type5 .echarts2:hover {
			}
	.type5 .echarts3 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 49%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type5 .echarts3:hover {
			}
	.type5 .echarts4 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 49%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type5 .echarts4:hover {
			}
	.type5 .echarts5 {
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 2px 8px rgba(0,0,0,.1);
				margin: 10px 0;
				background: rgba(255,255,255,1);
				width: 49%;
				position: relative;
				transition: 0.3s;
				height: 400px;
			}
	.type5 .echarts5:hover {
			}
	
	.echarts-flag-2 {
	  display: flex;
	  flex-wrap: wrap;
	  justify-content: space-between;
	  padding: 10px 20px;
	  background: rebeccapurple;
	
	  &>div {
	    width: 32%;
	    height: 300px;
	    margin: 10px 0;
	    background: rgba(255,255,255,.1);
	    border-radius: 8px;
	    padding: 10px 20px;
	  }
	}
</style>
