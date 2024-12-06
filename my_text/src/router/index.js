// 该文件专门用于创建整个应用的路由器
import VueRouter from 'vue-router'
//引入组件
import MyLogin from '@/pages/MyLogin.vue'
import UserEnroll from '@/pages/UserEnroll.vue'
import MyHome from '@/pages/MyHome.vue'
import MyIndex from '@/pages/MyIndex.vue'
import MyAdmin from '@/pages/MyAdmin.vue'
import MyOrdinary from '@/pages/MyOrdinary.vue'
import MyClass from '@/pages/MyClass.vue'
import MyStudents from '@/pages/MyStudents.vue'
import MyScore from '@/pages/MyScore.vue'
import OrdinaryClass from '@/pages/OrdinaryClass.vue'
import OrdinaryScore from '@/pages/OrdinaryScore.vue'
import OrdinaryStudent from '@/pages/OrdinaryStudent.vue'

//创建并暴露一个路由器
export default new VueRouter({
	routes:[
		{
            name:'Enroll',
			path:'/enroll',
			component:UserEnroll,
		},
        {
            name:'Login',
			path:'/login',
			component:MyLogin,
		},
        {
            name:'MyHome',
            path:'/MyHome',
            component:MyHome
        },
        {
            name:'MyIndex',
            path:'/MyIndex',
            component:MyIndex
        },
        {
            name:'MyAdmin',
            path:'/MyAdmin',
            component:MyAdmin,
            children: [
                {
                    path: 'MyClass',
                    name: 'MyClass',
                    component: MyClass
                },
                {
                    path: 'MyScore',
                    name: 'MyScore',
                    component: MyScore
                },
                {
                    path: 'MyStudents',
                    name: 'MyStudents',
                    component: MyStudents
                }
            ]

        },
        {
            name:'MyOrdinary',
            path:'/MyOrdinary',
            component:MyOrdinary,
            children: [
                {
                    path: 'OrdinaryClass',
                    name: 'OrdinaryClass',
                    component: OrdinaryClass
                },
                {
                    path: 'OrdinaryScore',
                    name: 'OrdinaryScore',
                    component: OrdinaryScore
                },
                {
                    path: 'OrdinaryStudent',
                    name: 'OrdinaryStudent',
                    component: OrdinaryStudent
                }
            ]
        },
          // 添加默认路由
        { path: '/',
          redirect: '/MyHome' } // 重定向根路径到登录页面
	]
})
