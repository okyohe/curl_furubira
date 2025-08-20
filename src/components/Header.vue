<template>
  <header class="Header flex items-center justify-between bg-cover" :style="{ backgroundImage: `url(${backgroundNavyImg})` }">
    <div class="header-logo">
      <img :src="logoImg" alt="Logo" class="logo-image" />
    </div>
    <div class="action">
      <ReserveButton class="reserve" />
      <!-- <div class="hamburger-menu cursor-pointer" @click="toggleMenu">
        <div class="line" :class="{ 'open-line1': isMenuOpen }"></div>
        <div class="line" :class="{ 'open-line2': isMenuOpen }"></div>
      </div> -->
    </div>
    <!-- <div v-if="isMenuOpen" class="mobile-menu" :style="{ backgroundImage: `url(${backgroundBeigeImg})` }"> -->
      <!-- <div class="close-button" @click="toggleMenu">×</div>
      <nav>
        <ul>
          <li><a href="#fv">ホーム</a></li>
          <li><a href="#impression">印象</a></li>
          <li><a href="#facility">施設</a></li>
          <li><a href="#experiencePlan">体験プラン</a></li>
          <li><a href="#duringStay">滞在の楽しみ方</a></li>
          <li><a href="#access">アクセス</a></li>
          <li><a href="#accommodationFee">料金</a></li>
        </ul>
      </nav>
    </div> -->
  </header>
</template>

<script setup>
import { ref } from 'vue';
import ReserveButton from "./ui/ReserveButton.vue";
import logoImg from "@/assets/images/logo/logo.webp";
import backgroundNavyImg from "@/assets/images/logo/background_navy.webp";
import backgroundBeigeImg from "@/assets/images/logo/background_beige.webp";
import backgroundNavyMobileImg from "@/assets/images/logo/background_navy-mobile.webp";
import backgroundBeigeMobileImg from "@/assets/images/logo/background_beige-mobile.webp";

const isMenuOpen = ref(false);

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};
</script>

<style scoped>
.Header {
  position: fixed; /* ヘッダーを固定 */
  top: 0; /* 上部に配置 */
  left: 0; /* 左端に配置 */
  width: 100%;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  font-size: var(--font-size-heading);
  z-index: 1000; /* 他の要素の上に表示 */
}

/* ロゴ */
.logo-image {
  height: 80px;
}

.action {
  display: flex;
  gap: 3rem;
}
/* ハンバーガーメニュー */
.hamburger-menu {
  height: 45px;
  display: flex;
  flex-direction: column;
  gap: 11px;
  justify-content: center;
  cursor: pointer; /* カーソルをポインターに変更 */
}

.hamburger-menu .line {
  width: 35px;
  height: 3px;
  background-color: rgb(255, 255, 255);
  transition: all 0.3s ease;
}

/* ハンバーガーメニュー開閉時のアニメーション */
.open-line1 {
  transform: rotate(45deg) translate(5px, 5px);
}
.open-line2 {
  transform: rotate(-45deg) translate(5px, -5px);
}

/* モバイルメニュー */
.mobile-menu {
  position: absolute;
  top: 80px;
  right: 0;
  width: 200px;
  border-radius: 4px;
  z-index: 10;
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
  font-style: normal;
  color: #000333;
  box-shadow: 0.1rem 0.1rem 1rem #00033399;
  padding-top: 40px; /* ×ボタンのスペースを確保 */
}

/* メディアクエリ */
@media (max-width: 768px) {
  .Header {
    height: 68px;
  }

  .logo-image {
    height: 60px;
  }

  .hamburger-menu .line {
    width: 25px;
    height: 2px;
  }
}

.hamburger-menu:hover .line {
  /* ホバー時のスタイルを追加 */
  background-color: rgb(255, 255, 255); /* 必要に応じて色を変更 */
}

/* ×ボタンのスタイル */
.close-button {
  font-size: 1.5rem;
  font-weight: bold;
  position: absolute;
  top: 10px;
  right: 15px;
  cursor: pointer;
}
</style>
