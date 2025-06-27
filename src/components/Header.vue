<template>
  <header
    class="Header flex items-center justify-between bg-cover"
    @mouseleave="isOpen = false">
    <!-- ロゴ -->
    <div class="header-logo">
      <img :src="logoImage" alt="Logo" class="logo-image" />
    </div>
    <div class="action">
      <!-- ご予約ボタン -->
      <ReserveButton class="reserve" />
      <!-- ハンバーガーメニュー -->
      <div class="hamburger-menu cursor-pointer" @click="toggleMenu">
        <div :class="['line', isOpen ? 'open-line1' : '']"></div>
        <div :class="['line', isOpen ? 'open-line2' : '']"></div>
      </div>

      <!-- モバイルメニュー -->
      <div
        v-if="isOpen"
        class="mobile-menu bg-white text-black p-4"
        @mouseleave="isOpen = false">
        <!-- ×ボタン -->
        <div class="close-button" @click="isOpen = false">&times;</div>
        <ul>
          <li class="py-2 cursor-pointer" @click="scrollToSection('facility')">
            施設のご案内
          </li>

          <li
            class="py-2 cursor-pointer"
            @click="scrollToSection('duringStay')">
            滞在の楽しみ方
          </li>
          <li class="py-2 cursor-pointer" @click="scrollToSection('access')">
            アクセス
          </li>
          <li
            class="py-2 cursor-pointer"
            @click="scrollToSection('accommodationFee')">
            宿泊料金
          </li>
        </ul>
      </div>
    </div>
  </header>
</template>

<script>
import logoImage from "@/assets/images/logo/logo.png";
import ReserveButton from "./ui/ReserveButton.vue";
export default {
  name: "Header",
  components: {
    ReserveButton,
  },
  data() {
    return {
      logoImage,
      isOpen: false, // ハンバーガーメニューの開閉状態
    };
  },
  methods: {
    toggleMenu() {
      this.isOpen = !this.isOpen;
    },
    scrollToSection(sectionId) {
      const section = document.getElementById(sectionId);
      if (section) {
        section.scrollIntoView({ behavior: "smooth" });
      }
    },
  },
};
</script>

<style scoped>
/* 全体のヘッダー */
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
  background-image: url("@/assets/images/logo/background_navy.webp");
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
  background-image: url("@/assets/images/logo/background_beige.webp");
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
    background-image: url("@/assets/images/logo/background_navy-mobile.webp");
  }

  .logo-image {
    height: 60px;
  }
  .mobile-menu {
    background-image: url("@/assets/images/logo/background_beige-mobile.webp");
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

/* 360px以下の画面幅でheaderのボタンを非表示にする */
@media (max-width: 450px) {
  .reserve {
    display: none;
  }
}
</style>
