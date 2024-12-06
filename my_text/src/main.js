//引入Vue
import Vue from 'vue'
//引入App
import App from './App.vue'
//引入VueRouter
import VueRouter from 'vue-router'
//引入路由器
import router from './router'



import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

// // 按需引入
// import { MenuItemGroup, Row, Col, Button, Input, Dialog, Form,FormItem, Table, TableColumn, Alert, Container, Header, Aside, Main, Menu, Submenu, MenuItem, MessageBox } from 'element-ui';

// // 按需引入
// Vue.component(Button.name, Button);
// Vue.component(Input.name, Input);
// Vue.component(Dialog.name, Dialog);
// Vue.component(Form.name, Form);
// Vue.component(FormItem.name, FormItem);
// Vue.component(Table.name, Table);
// Vue.component(TableColumn.name, TableColumn);
// Vue.component(Alert.name, Alert);
// Vue.component(Container.name, Container);
// Vue.component(Header.name, Header);
// Vue.component(Aside.name, Aside);
// Vue.component(Main.name, Main);
// Vue.component(Menu.name, Menu);
// Vue.component(Submenu.name, Submenu);
// Vue.component(MenuItem.name, MenuItem);
// Vue.component(MenuItemGroup.name, MenuItemGroup);

// Vue.component(Row.name, Row);
// Vue.component(Col.name, Col);
// Vue.component(MessageBox.name, MessageBox);


//关闭Vue的生产提示
Vue.config.productionTip = false
//应用插件
Vue.use(VueRouter)

//创建vm
new Vue({
	el:'#app',
	render: h => h(App),
	router:router
})
