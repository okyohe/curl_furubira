// src/entry.js
import { ViteSSG } from "vite-ssg";
import App from "./App.vue";
import "./assets/index.css";

const routes = [{ path: "/", component: App, name: "home" }];

export const createApp = ViteSSG(App, { routes });
