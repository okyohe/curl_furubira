<template>
  <section>
    <div class="facility">
      <SmallHeading :title-ja="'施設紹介'" :title-en="'facility'" />
      <!-- 画像セクション -->
      <div class="image-section">
        <div class="image-row first-row">
          <img src="@/assets/images/background_kamui.png" alt="画像1" />
        </div>
        <div class="image-row second-row">
          <img src="@/assets/images/background_kamui.png" alt="画像2" />
          <img src="@/assets/images/background_kamui.png" alt="画像3" />
          <img src="@/assets/images/background_kamui.png" alt="画像4" />
        </div>
      </div>

      <!-- 部屋セクション -->
      <div class="room-section content">
        <Card>
          <div style="text-align: center">
            <img
              src="@/assets/images/background_kamui.png"
              alt="リビング画像"
              class="room-image" />
            <h3>リビング</h3>
            <p>皆で集まれる広々スペース</p>
          </div>
        </Card>
        <Card>
          <div style="text-align: center">
            <img
              src="@/assets/images/background_kamui.png"
              alt="寝室画像"
              class="room-image" />
            <h3>寝室</h3>
            <p>和室でゆっくりとお休みいただけます</p>
          </div>
        </Card>
        <Card>
          <div style="text-align: center">
            <img
              src="@/assets/images/background_kamui.png"
              alt="キッチン画像"
              class="room-image" />
            <h3>キッチン</h3>
            <p>炊飯器、電子レンジ、オーブンを備えております</p>
          </div>
        </Card>
        <Card>
          <div style="text-align: center">
            <img
              src="@/assets/images/background_kamui.png"
              alt="温泉画像"
              class="room-image" />
            <h3>温泉</h3>
            <p>近郊のふるびら温泉で至福のひとときを</p>
          </div>
        </Card>
      </div>

      <!-- アメニティセクション -->
      <div class="amenity-section content">
        <SmallHeading title-ja="アメニティ・備品" />
        <p>持ち帰り可能（使い捨て）: 歯ブラシ、歯磨きセット、綿棒</p>
        <p>
          持ち帰り不可（備え付け）:
          枕カバー、シーツ、ハンドタオル、バスタオル、ドライヤー、スリッパ、ヘアアイロン、トイレットペーパー、シャンプー、コンディショナー、ボディーソープ、ハンドソープ、炊飯器、電子レンジ、オーブン、高速Wi-Fi(STARLINK)
        </p>
      </div>

      <!-- CTAセクション -->
      <div class="cta-section content">
        <img src="@/assets/images/boxlogo_navy.png" alt="ロゴ" class="logo" />
        <ReserveButton />
      </div>
    </div>
  </section>
</template>

<script>
import SmallHeading from "./ui/SmallHeading.vue";
import { Card, CardHeader } from "@/components/ui/card";
import ReserveButton from "@/components/ui/ReserveButton.vue";

export default {
  name: "Facility",
  components: {
    SmallHeading,
    Card,
    CardHeader,
    ReserveButton,
  },
};
</script>

<style scoped>
.facility {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

.image-section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  align-items: center;
  width: 100vw;
}

.image-row {
  display: flex;
  justify-content: center;
  gap: 1rem;
  width: 100%;
  justify-content: space-around;
}

.image-row:nth-child(1) img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}
.image-row:nth-child(2) img {
  height: 200px;
  object-fit: cover;
  width: 100%;
}

.room-section {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

@media (max-width: 768px) {
  .room-section {
    grid-template-columns: 1fr;
  }
}

.room-image {
  width: 100%;
  height: auto;
  margin-bottom: 1rem;
}

.card {
  width: 100%;
  border: 1px solid #ccc;
  padding: 1rem;
  border-radius: 8px;
  text-align: center;
}

.amenity-section {
  text-align: center;
  font-size: var(--font-size-text);
  width: 60%;
}

.cta-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.logo {
  max-width: 200px;
  margin-bottom: 1rem;
}

.custom-button {
  font-size: var(--font-size-heading);
}
</style>
