// src/entry.js
import { ViteSSG } from "vite-ssg";
import App from "./App.vue";
import "./assets/index.css";

// `export const createApp` は vite-ssg の設定で必要
export const createApp = ViteSSG(
  // ルートコンポーネント
  App,
  // ルート設定 (シンプルな設定)
  { routes: [{ path: "/", component: App }] }
);
