<template>
  <div
    class="Header flex items-center justify-between bg-cover"
    :style="{ backgroundImage: `url(${backgroundImage})` }">
    <!-- ロゴ -->
    <div class="header-logo">
      <img :src="logoImage" alt="Logo" class="logo-image" />
    </div>
    <div class="action">
      <!-- ご予約ボタン -->
      <button
        class="reservation-button bg-[#E3DAC2] text-black py-2 px-4 rounded zen-old-mincho-semibold">
        ご予約はこちら
      </button>

      <!-- ハンバーガーメニュー -->
      <div class="hamburger-menu cursor-pointer" @click="toggleMenu">
        <div :class="['line', isOpen ? 'open-line1' : '']"></div>
        <div :class="['line', isOpen ? 'open-line2' : '']"></div>
      </div>

      <!-- モバイルメニュー -->
      <div v-if="isOpen" class="mobile-menu bg-white text-black p-4">
        <ul>
          <li class="py-2">メニュー1</li>
          <li class="py-2">メニュー2</li>
          <li class="py-2">メニュー3</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import backgroundImage from "@/assets/images/background_navy.png";
import logoImage from "@/assets/images/logo.png";

export default {
  name: "Header",
  data() {
    return {
      backgroundImage,
      logoImage,
      isOpen: false, // ハンバーガーメニューの開閉状態
    };
  },
  methods: {
    toggleMenu() {
      this.isOpen = !this.isOpen;
    },
  },
};
</script>

<style scoped>
/* 全体のヘッダー */
.Header {
  width: 100%;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  font-size: var(--font-size-heading);
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

/* ご予約ボタン */
.reservation-button {
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
  font-style: normal;
}

/* モバイルメニュー */
.mobile-menu {
  position: absolute;
  top: 100px;
  right: 0;
  width: 200px;
  border: 1px solid #ccc;
  border-radius: 4px;
  z-index: 10;
}

/* メディアクエリ */
@media (max-width: 768px) {
  .Header {
    height: 68px;
  }

  .logo-image {
    height: 60px;
  }

  .hamburger-menu {
    height: 30px;
  }

  .hamburger-menu .line {
    width: 25px;
    height: 2px;
  }
}
</style>
