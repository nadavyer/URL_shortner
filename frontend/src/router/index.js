import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/routes/stats',
    name: 'Stats',
    component: () => import('../views/Stats.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
