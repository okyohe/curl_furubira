<template>
  <section>
    <div class="facility">
      <SmallHeading :title-ja="'施設紹介'" :title-en="'facility'" />
      <!-- 画像セクション -->
      <div class="image-section">
        <div class="image-row">
          <img src="@/assets/images/background_kamui.png" alt="画像1" />
          <img src="@/assets/images/background_kamui.png" alt="画像2" />
          <img src="@/assets/images/background_kamui.png" alt="画像3" />
        </div>
        <div class="image-row">
          <img src="@/assets/images/background_kamui.png" alt="画像4" />
          <img src="@/assets/images/background_kamui.png" alt="画像5" />
        </div>
      </div>

      <!-- 部屋セクション -->
      <div class="room-section">
        <Card>
          <CardHeader>
            <CardTitle>リビング</CardTitle>
          </CardHeader>
          <CardContent>
            <img
              src="@/assets/images/background_kamui.png"
              alt="リビング画像"
              class="room-image" />
            <p>皆で集まれる広々スペース</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>寝室</CardTitle>
          </CardHeader>
          <CardContent>
            <img
              src="@/assets/images/background_kamui.png"
              alt="寝室画像"
              class="room-image" />
            <p>和室でゆっくりとお休みいただけます</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>キッチン</CardTitle>
          </CardHeader>
          <CardContent>
            <img
              src="@/assets/images/background_kamui.png"
              alt="キッチン画像"
              class="room-image" />
            <p>炊飯器、電子レンジ、オーブンを備えております</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>温泉</CardTitle>
          </CardHeader>
          <CardContent>
            <img
              src="@/assets/images/background_kamui.png"
              alt="温泉画像"
              class="room-image" />
            <p>近郊のふるびら温泉で至福のひとときを</p>
          </CardContent>
        </Card>
      </div>

      <!-- アメニティセクション -->
      <div class="amenity-section">
        <Heading title="アメニティ・備品" />
        <p>持ち帰り可能（使い捨て）: 歯ブラシ、歯磨きセット、綿棒</p>
        <p>
          持ち帰り不可（備え付け）:
          枕カバー、シーツ、ハンドタオル、バスタオル、ドライヤー、スリッパ、ヘアアイロン、トイレットペーパー、シャンプー、コンディショナー、ボディーソープ、ハンドソープ、炊飯器、電子レンジ、オーブン、高速Wi-Fi(STARLINK)
        </p>
      </div>

      <!-- CTAセクション -->
      <div class="cta-section">
        <img src="@/assets/images/boxlogo_navy.png" alt="ロゴ" class="logo" />
        <ReserveButton />
      </div>
    </div>
  </section>
</template>

<script>
import SmallHeading from "./ui/SmallHeading.vue";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import ReserveButton from "@/components/ui/ReserveButton.vue";

export default {
  name: "Facility",
  components: {
    SmallHeading,
    Card,
    CardContent,
    CardHeader,
    CardTitle,
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
  width: 100%;
  max-width: 1200px;
  align-items: center;
}

.image-row {
  display: flex;
  justify-content: center;
  gap: 1rem;
  width: 100%;
  max-width: 1200px;
  justify-content: space-around;
}

.image-row:nth-child(1) img {
  width: 33%;
  height: auto;
}
.image-row:nth-child(2) img {
  width: 50%;
  height: auto;
}

.room-section {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  width: 60%;
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
