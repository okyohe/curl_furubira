<template>
  <div class="Fv">
    <img
      src="@/assets/images/background_kamui.png"
      class="background"
      alt="背景画像" />
    <div class="overlay">
      <img src="@/assets/images/boxlogo_white.png" class="logo" alt="ロゴ" />
      <div class="vertical-text">
        <h2>
          <span class="highlight">自然に囲まれた</span>
          <span class="highlight">あなたの充電スポット</span>
        </h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Fv",
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Zen+Old+Mincho:wght@600&display=swap");

.Fv {
  position: relative;
  height: calc(100vh - 100px); /* ヘッダーの高さを指定してください */
  overflow: hidden;
}

.background {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.6;
  background-color: rgba(0, 0, 0, 0.2);
  mix-blend-mode: multiply;
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
}

.logo {
  width: 50%;
  max-width: 600px;
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

.vertical-text h2 {
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

@media (max-width: 768px) {
  .Fv {
    height: calc(100vh - 68px);
  }
}
</style>
