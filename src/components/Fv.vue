<template>
  <div class="Fv" @click="nextImage">
    <div class="white-overlay" :class="{ 'fade-active': isFading }"></div>
    <picture>
      <source :srcset="currentImage.mobile" media="(max-width: 768px)" />
      <img
        :src="currentImage.desktop"
        class="background"
        alt="背景画像"
        fetchpriority="high"
        decoding="async" />
    </picture>
    <div class="overlay">
      <img :src="boxlogo_white" class="logo" alt="ロゴ" />
      <div class="vertical-text">
        <h1>
          <span class="highlight">カールふるびら</span>
          <span class="highlight">北海道古平町の田舎体験宿</span>
        </h1>
      </div>
    </div>
    <div
      v-show="showScrollIndicator"
      class="scroll-indicator"
      @click="scrollDown">
      <span class="arrow">▼</span>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted } from "vue";

import boxlogo_white from "../assets/images/logo/boxlogo_white.webp";
import pillow_desktop from "../assets/images/photos/0_100_white_pillow.webp";
import pillow_mobile from "../assets/images/photos/0_100_white_pillow-mobile.webp";
import dining_desktop from "../assets/images/photos/0_101_dining.webp";
import dining_mobile from "../assets/images/photos/0_101_dining-mobile.webp";
import navypillow_desktop from "../assets/images/photos/0_103_navypillow.webp";
import navypillow_mobile from "../assets/images/photos/0_103_navypillow-mobile.webp";

// アーティスティック画像のリスト
const images = [
  {
    desktop: pillow_desktop,
    mobile: pillow_mobile,
  },
  {
    desktop: dining_desktop,
    mobile: dining_mobile,
  },
  {
    desktop: navypillow_desktop,
    mobile: navypillow_mobile,
  },
];

const currentIndex = ref(0);
const currentImage = ref(images[currentIndex.value]);
const isFading = ref(false);

let intervalId;

const showScrollIndicator = ref(true);

function startImageTransition() {
  intervalId = setInterval(nextImage, 10000); // 10秒ごとに画像を切り替え
}

function resetImageTransition() {
  clearInterval(intervalId);
  startImageTransition();
}

function nextImage() {
  isFading.value = true;
  setTimeout(() => {
    currentIndex.value = (currentIndex.value + 1) % images.length;
    currentImage.value = images[currentIndex.value];
    setTimeout(() => {
      isFading.value = false;
    }, 500); // フェードインの時間
  }, 500); // フェードアウトの時間
  resetImageTransition(); // タップによるトランジションが行われた場合に時間をリセット
}

function handleScroll() {
  showScrollIndicator.value = false;
}

function scrollDown() {
  window.scrollBy({
    top: window.innerHeight / 2, // 画面の半分だけスクロール
    behavior: "smooth",
  });
}

onMounted(() => {
  startImageTransition();
  window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
  clearInterval(intervalId);
  window.removeEventListener("scroll", handleScroll);
});

watch(currentIndex, () => {
  // 画像が切り替わった後にフェードインを開始
  isFading.value = false;
});
</script>

<style scoped>
.Fv {
  position: relative;
  height: 100vh;
  overflow: hidden;
}

.background {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.6;
  transition: opacity 1s ease-in-out;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.445);
  z-index: 2; /* オーバーレイの下に来るように */
}

.logo {
  width: 50%;
  max-width: 400px;
  height: auto;
  margin-bottom: 20px;
}

.vertical-text {
  position: absolute;
  right: 10%;
  top: 40%;
  transform: translateY(-30%);
  writing-mode: vertical-rl;
  text-align: left;
}

.vertical-text h1 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.vertical-text span {
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
  font-style: normal;
  display: inline-block;
}

.vertical-text .highlight {
  background-color: #000333;
  color: white;
  padding: 10px 5px;
  margin: 5px;
  font-size: var(--font-size-heading, 1.5rem);
  white-space: nowrap;
  letter-spacing: 6px;
}

.highlight:nth-child(2) {
  margin-top: 36px; /* 2つ目の文章を下げる */
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease-in-out;
}

.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
}

@media (max-width: 768px) {
  .overlay {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .logo {
    width: 70%;
  }
  .vertical-text {
    position: static; /* Override absolute positioning */
    right: auto; /* Reset */
    top: auto; /* Reset */
    transform: none; /* Override transform */
    writing-mode: horizontal-tb; /* Override writing mode */
    text-align: center; /* Override text align */
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px; /* Space from logo */
  }
  .vertical-text h1 {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .vertical-text .highlight {
    background-color: rgba(255, 255, 255, 0); /* Transparent BG */
    writing-mode: horizontal-tb; /* Ensure horizontal */
    margin: 5px 0; /* Vertical margin between highlights */
    text-align: center;
    padding: 5px 10px;
    color: white;
    letter-spacing: normal; /* Reset from PC style */
    white-space: normal; /* Allow text wrapping, reset from PC style */
  }

  .scroll-indicator {
    transform: translateX(-50%) translateY(0);
    bottom: 40px;
  }
}

.white-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.7);
  opacity: 0;
  pointer-events: none;
  z-index: 1; /* オーバーレイが他の要素の上に来るように */
  transition: opacity 1s ease-in-out;
}

.fade-active {
  opacity: 1;
}

.scroll-indicator {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 3;
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/* アニメーション用の疑似要素を追加 */
.scroll-indicator::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  animation: bounce 2s infinite;
}

.arrow,
.scroll-text {
  position: relative;
  z-index: 1;
}

.arrow {
  font-size: 1.5rem;
  color: white;
}

.scroll-text {
  font-size: 0.75rem;
  color: white;
  margin-top: 5px; /* 矢印との間隔 */
}

@keyframes bounce {
  0%,
  20%,
  50%,
  80%,
  100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
}
</style>
