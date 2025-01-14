<template>
  <section class="section-container">
    <!-- Background Image -->
    <div class="background-image"></div>

    <!-- Content Overlay -->
    <div class="content-overlay">
      <!-- Title -->
      <SmallHeading :title-en="'Access'" :title-ja="'アクセス'" />

      <!-- Google Map -->
      <div class="map-container">
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2904.5588589451468!2d140.6424101!3d43.281616899999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5f0af914a103b813%3A0x6f4271aeb03ae3e8!2z44Kr44O844Or44G144KL44Gz44KJ!5e0!3m2!1sja!2sjp!4v1736841370355!5m2!1sja!2sjp"
          width="600"
          height="600"
          style="border: 0; width: 100%; height: 100%"
          allowfullscreen=""
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>

      <!-- Access Information -->
      <div class="info-container">
        <div>
          <h3 class="info-title">バスでお越しのお客様</h3>
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
.section-container {
  position: relative;
  min-height: 100vh;
  overflow: hidden;
}

.background-image {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 0;
  background-image: url("@/assets/images/background_kamui.png");
  background-size: cover;
  background-position: center;
}
.content-overlay {
  position: relative;
  z-index: 10;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 4rem 1rem;
  text-align: center;
  width: 100vw;
}
.title-container {
  margin-bottom: 4rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.title {
  margin-bottom: 0.5rem;
  font-size: 1.5rem;
  font-weight: 500;
  letter-spacing: 0.05em;
}
.subtitle {
  font-size: 0.875rem;
}
.map-container {
  margin-bottom: 4rem;
  height: 400px;
  width: 100%;
  max-width: 64rem;
}
.info-container {
  margin: 0 auto;
  max-width: 48rem;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 2rem;
  display: grid;
  gap: 3rem;
}
.info-title {
  margin-bottom: 1.5rem;
  font-size: 1.125rem;
}
.info-text {
  margin-bottom: 1rem;
  line-height: 1.75;
}
</style>
