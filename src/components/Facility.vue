<template>
  <section>
    <div class="facility">
      <SmallHeading :title-ja="'施設'" :title-en="'facility'" />

      <!-- 画像セクション -->
      <div class="image-section">
        <div
          class="image-row"
          :class="{
            'first-row': row.index === 0,
            'second-row': row.index === 1,
          }"
          v-for="(row, rowIndex) in imageRows"
          :key="rowIndex">
          <img
            v-for="(image, imgIndex) in row.images"
            :key="imgIndex"
            :src="image.src"
            :alt="image.alt" />
        </div>
      </div>

      <!-- 部屋セクション -->
      <div class="room-section content">
        <Card v-for="(room, index) in rooms" :key="index">
          <div style="text-align: center">
            <img :src="room.image" :alt="room.alt" class="room-image" />
            <h3>{{ room.title }}</h3>
            <p>{{ room.description }}</p>
          </div>
        </Card>
      </div>

      <SmallHeading title-ja="備品" :title-en="'amenity'" />

      <!-- アメニティセクション -->
      <div class="amenity-section content">
        <p>
          持ち帰り不可（備え付け）:
          {{ amenities.join("、") }}
        </p>
      </div>

      <!-- CTAセクション -->
      <div class="cta-section content">
        <img :src="logo" alt="ロゴ" class="logo" />
        <ReserveButton />
      </div>
    </div>
  </section>
</template>

<script>
import SmallHeading from "./ui/SmallHeading.vue";
import { Card } from "@/components/ui/card";
import ReserveButton from "@/components/ui/ReserveButton.vue";

// 画像のインポート
import backgroundKamui1 from "@/assets/images/background_kamui.png";
import backgroundKamui2 from "@/assets/images/background_kamui.png";
import backgroundKamui3 from "@/assets/images/background_kamui.png";
import backgroundKamui4 from "@/assets/images/background_kamui.png";
import diningImg from "@/assets/images/room/dining.jpg";
import kitchenImg from "@/assets/images/room/kitchen.jpg";
import tokonomaImg from "@/assets/images/room/tokonoma.jpg";
import bedroomImg from "@/assets/images/room/bedroom.jpg";
import boxLogoNavy from "@/assets/images/boxlogo_navy.png";

export default {
  name: "Facility",
  components: {
    SmallHeading,
    Card,
    ReserveButton,
  },
  data() {
    return {
      // ロゴ画像のインポート
      logo: boxLogoNavy,

      imageRows: [
        {
          index: 0,
          images: [
            {
              src: backgroundKamui1,
              alt: "画像1",
            },
          ],
        },
        {
          index: 1,
          images: [
            {
              src: backgroundKamui2,
              alt: "画像2",
            },
            {
              src: backgroundKamui3,
              alt: "画像3",
            },
            {
              src: backgroundKamui4,
              alt: "画像4",
            },
          ],
        },
      ],
      rooms: [
        {
          image: diningImg,
          alt: "食卓画像",
          title: "食卓",
          description: "皆で集まれる広々スペース",
        },
        {
          image: kitchenImg,
          alt: "台所画像",
          title: "台所",
          description: "炊飯器、電子レンジ、オーブンを備えております",
        },
        {
          image: tokonomaImg,
          alt: "床の間画像",
          title: "床の間",
          description: "近郊のふるびら温泉で至福のひとときを",
        },
        {
          image: bedroomImg,
          alt: "寝室画像",
          title: "寝室",
          description: "静かで落ち着いた空間で、心地よい眠りを提供します",
        },
      ],
      amenities: [
        "枕カバー",
        "シーツ",
        "ハンドタオル",
        "バスタオル",
        "ドライヤー",
        "スリッパ",
        "ヘアアイロン",
        "トイレットペーパー",
        "シャンプー",
        "コンディショナー",
        "ボディーソープ",
        "ハンドソープ",
        "炊飯器",
        "電子レンジ",
        "電気ケトル",
        "Wi-Fi(約200Mbps)",
      ],
    };
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
  width: 99vw;
}

.image-row {
  display: flex;
  justify-content: space-around;
  gap: 0.3%;
  width: 100%;
}

.image-row.first-row img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.image-row.second-row img {
  width: 33%;
  height: 200px;
  object-fit: cover;
}

.room-section {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

@media (max-width: 768px) {
  .image-section {
    width: 100%;
  }
  .image-row.first-row {
    display: none;
  }
  .image-row.second-row {
    flex-direction: column;
    gap: 0;
  }
  .image-row.second-row img {
    width: 100%;
    height: 260px;
  }
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

@media (max-width: 360px) {
  .amenity-section {
    width: 100%;
    padding: 0.5rem;
  }
}
</style>
