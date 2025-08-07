// src/entry.js
import { ViteSSG } from "vite-ssg";
import App from "./App.vue";
import "./assets/index.css";

export const createApp = ViteSSG(App, {
  routes: [{ path: "/", component: App, name: "home" }],
  base: "/",
  mode: "ssg",
});
