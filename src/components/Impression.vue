<template>
  <section>
    <div class="first-content content">
      <div class="left-content">
        <div class="text-content">
          <p>効率性から脱却し</p>
          <p>身体と心をリセットする</p>
          <p>田舎没入型民泊「カールふるびら」</p>
        </div>
        <div class="left-image">
          <img src="../assets/images/background_kamui.png" alt="kamui image" />
        </div>
      </div>
      <div class="vertical-divider">
        <h2 class="divider-text">非日常体験の秘密基地</h2>
      </div>
      <div class="right-content">
        <div class="text-content">
          <p>北海道の小さな町、</p>
          <p>ふるびら町の海近くに</p>
          <p>カールふるびらはあります。</p>
        </div>

        <div class="right-image">
          <img src="../assets/images/background_kamui.png" alt="kamui image" />
        </div>
      </div>
    </div>
    <div class="second-content content">
      <div class="description">
        <p>和風の古民家でもなく、現代風でもない、小さな町の</p>
        <p>住宅街の中にあるただの少し大きい古い家です。</p>
        <p>オーナーの「鹿くん」と地域の方々が手作業で</p>
        <p>整えた場所で、朝7時には地域の住民が集まります。</p>
        <p>喧騒から離れ、ゆったりとした時間が流れる空間で、</p>
        <p>心温まるひとときを過ごしてみませんか。</p>
      </div>

      <div class="logo">
        <img src="../assets/images/boxlogo_navy.png" alt="Curl Furubira logo" />
      </div>

      <div class="cta-button">
        <button>宿について詳しく知る</button>
      </div>

      <div class="social-links">
        <a href="https://www.instagram.com/curl_furubira/" target="_blank">
          <img src="../assets/images/Instagram_logo_navy.png" alt="Instagram" />
        </a>
      </div>
    </div>
  </section>
</template>

<style scoped>
section {
  background-image: url("../assets/images/background_beige.png");
  background-repeat: repeat;
  background-size: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.section-1,
.section-2 {
  background-color: transparent;
}

section {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.first-content {
  display: flex;
  flex-direction: row;
  margin: 0 auto;
  position: relative;
  padding: 20px 0;
}
.right-content {
  display: flex;
  flex-direction: column-reverse;
}

.second-content {
  display: flex;
  margin: 0 auto;
  position: relative;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  align-items: center;
  gap: 2rem;
}

.left-content,
.right-content {
  flex: 1;
}

.left-image,
.right-image {
  object-fit: cover;
  margin: 2rem 0;
  position: relative;
  width: 135%;
}

.left-image {
  left: -40%;
}

.right-image {
  right: 0%;
}

.vertical-divider {
  background-color: #1a1a3a;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px 10px;
  margin: 0 3rem;
  height: 75vh;
}

.divider-text {
  writing-mode: vertical-rl;
  color: white;
  letter-spacing: 0.2em;
  font-size: var(--font-size-heading);
}
.text-content {
  line-height: 3;
  margin: 5rem 0;
  padding: 0 2rem;
}

.description {
  line-height: 1.8;
  font-size: var(--font-size-text);
}

.cta-button button {
  padding: 12px 40px;
  border: 1px solid #1a1a3a;
  border-radius: 30px;
  background: transparent;
  cursor: pointer;
  font-size: var(--font-size-heading);
}

.intro-text {
  text-align: center;
  line-height: 1.8;
  margin: 20px 0;
  font-size: var(--font-size-text);
}

@media (max-width: 768px) {
  .first-content {
    flex-direction: column;
  }

  .vertical-divider {
    width: 100vw;
    margin: 0;
  }
  .divider-text {
    writing-mode: horizontal-tb;
  }
  .left-image,
  .right-image {
    position: static;
  }
  .right-content {
    flex-direction: column;
  }
}
</style>
