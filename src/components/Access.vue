<template>
  <section class="section-container">
    <div class="content">
      <!-- Title -->
      <SmallHeading :title-en="'Access'" :title-ja="'アクセス'" />
      <!-- Google Map -->
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2904.5588589451468!2d140.6424101!3d43.281616899999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5f0af914a103b813%3A0x6f4271aeb03ae3e8!2z44Kr44O844Or44G144KL44Gz44KJ!5e0!3m2!1sja!2sjp!4v1736841370355!5m2!1sja!2sjp"
        allowfullscreen=""
        width="100%"
        height="100%"
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"></iframe>

      <div class="logo-container">
        <img
          class="logo"
          src="../assets/images/logo/boxlogo_navy.png"
          alt="Curl Furubira logo" />
        <p>駐車場完備（2台）</p>
        <p>〒046-0102 北海道古平郡古平町丸山町103</p>
      </div>
      <!-- Access Information -->
      <div class="info-container">
        <div>
          <h3 class="info-title">バスでお越しのお客様</h3>
          <hr class="tiny-heading-line" />
          <p class="info-text">
            札幌駅、小樽駅、または余市駅からバスに乗車し、丸山町停留所で下車してください。
          </p>
          <p class="info-text">
            バス停から徒歩約7分の位置に「カールふるびら」があります。
          </p>
          <p class="info-text">
            バスでのアクセスは地元の景色をゆっくりと楽しむことができます。
          </p>
        </div>

        <div>
          <h3 class="info-title">車でお越しのお客様</h3>
          <hr class="tiny-heading-line" />
          <p class="info-text">
            札幌駅から車で約1時間20分、高速道路を利用してアクセスすることができます。
          </p>
          <p class="info-text">
            途中の小樽や余市を経由するルートも選択可能です。
          </p>
          <p class="info-text">
            ドライブ中は、北海道の広大な自然と美しい景色を存分にお楽しみいただけます。
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import SmallHeading from "./ui/SmallHeading.vue";
export default {
  name: "AccessSection",
  components: {
    SmallHeading,
  },
};
</script>

<style scoped>
section {
  background-image: url("@/assets/images/logo/background_kamui.png");
  background-size: cover;
  background-position: center;
}

.info-container {
  background-color: rgba(255, 255, 255, 0.8);
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 3rem;
  text-align: center;
  align-items: center;
  width: 100%;
  gap: 2rem;
}

.logo-container {
  padding: 2rem;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
}
.logo-container p {
  text-decoration: underline;
}
.logo {
  max-width: 200px;
}

iframe {
  min-height: 400px;
}
@media (max-width: 360px) {
  .info-container {
    padding: 2rem 0.5rem;
  }
}
</style>
