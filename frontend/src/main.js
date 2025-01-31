import "./assets/main.css";

import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import { autoAnimatePlugin } from "@formkit/auto-animate/vue";
import App from "./App.vue";
import ordersSearch from "./pages/ordersSearch.vue";
import Home from "./pages/Home.vue";
import Favorites from "./pages/Favorites.vue";
import Product from "./pages/Product.vue";
import Cart from "./pages/Cart.vue";
import OrderDetails from "./pages/OrderDetails.vue";
import Category from "./pages/Category.vue";
import Pay from "./pages/Pay.vue";
import OrderCreate from "./pages/OrderCreate.vue";
import OrderPage from "./pages/OrderPage.vue";
const app = createApp(App);


const routes = [
  
  {path: "/orderPage", name:"OrderPage", component: OrderPage},
  {path: "/ordercreate", name:"ordercreate", component: OrderCreate},
  {path: "/payment", name: "Pay", component:Pay},
  { path: "/", name: "Home", component: Home },
  { path: "/favorites", name: "Favorites", component: Favorites }, 
  {path: '/products/:id',name: 'product', component: Product, props: true},
  {path : '/order', name: 'ordersSearch', component: ordersSearch},
  { path: '/order/:Code', name: 'OrderDetails',  component: OrderDetails, props: true },
  {path:'/cart', name:'Cart', component: Cart},
  {path: '/category/:id', name:'Category', component:Category}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

app.use(router);
app.use(autoAnimatePlugin);

app.mount("#app");
