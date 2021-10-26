import { createApp } from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import VueSSE from "vue-sse";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

createApp(App)
  .use(store)
  .use(router)
  .use(VueSSE)
  .mount("#app");
