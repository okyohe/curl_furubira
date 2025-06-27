<template>
  <section>
    <div class="facility">
      <!-- 画像セクション（縦画像用） -->
      <div class="image-section">
        <img
          v-for="(image, index) in facilityImages"
          :key="index"
          :src="image.src"
          :alt="image.alt"
          class="vertical-image" />
      </div>
      <SmallHeading :title-ja="'施設'" :title-en="'facility'" />

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

      <!-- サブルーム画像セクション -->
      <div class="image-section">
        <img
          v-for="(image, index) in subroomImages"
          :key="index"
          :src="image.src"
          :alt="image.alt"
          class="vertical-image" />
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

      <!-- アメニティ画像セクション -->
      <div class="image-section">
        <img
          v-for="(image, index) in amenityImages"
          :key="index"
          :src="image.src"
          :alt="image.alt"
          class="vertical-image" />
      </div>
    </div>
  </section>
</template>

<script>
import SmallHeading from "./ui/SmallHeading.vue";
import { Card } from "@/components/ui/card";
import ReserveButton from "@/components/ui/ReserveButton.vue";

// 画像のインポート
import diningImg from "@/assets/images/photos/10_room_dining_stove_side.webp";
import kitchenImg from "@/assets/images/photos/16_room_kitchen_close.webp";
import tokonomaImg from "@/assets/images/photos/30_room_tokonoma_withdesk_fusumaside.webp";
import bedroomImg from "@/assets/images/photos/25_room_bedroom_view.webp";
import boxLogoNavy from "@/assets/images/logo/boxlogo_navy.png";
// amenity images
import roomDiningStove from "../assets/images/photos/11_room_dining_stove.webp";
import roomEntranceFireExtinguisher from "../assets/images/photos/5_room_entrance_fire_extinguisher.webp";
import roomBedroomKey from "../assets/images/photos/27_room_bedroom_key.webp";
import roomBathroomBath from "../assets/images/photos/40_room_bathroom_bath.webp";
import roomBathroomSink from "../assets/images/photos/40_room_bathroom_sink.webp";
import roomBathroomTowel from "../assets/images/photos/41_room_bathroom_towel.webp";
import roomBathroomWasherDryer from "../assets/images/photos/41_room_bathroom_washerdryer.webp";
import roomToiletPull from "../assets/images/photos/50_room_toilet_pull.webp";
import entranceImg from "@/assets/images/photos/5_room_entrance.webp";
import diningWifiPanelImg from "@/assets/images/photos/12_room_dining_wifipanel.webp";
import diningFrameImg from "@/assets/images/photos/12_room_dining_frame.webp";
import entranceSlippersImg from "@/assets/images/photos/5_room_entrance_slippers.webp";

export default {
  name: "Facility",
  components: {
    SmallHeading,
    Card,
    ReserveButton,
  },
  data() {
    return {
      // ロゴ画像の定義
      logo: boxLogoNavy,
      // 縦画像として表示するための画像リスト
      facilityImages: [
        {
          src: roomDiningStove,
          alt: "ダイニングストーブ",
        },
        {
          src: diningWifiPanelImg,
          alt: "ダイニングのWiFiパネル",
        },
        {
          src: diningFrameImg,
          alt: "ダイニングのフレーム",
        },
        {
          src: roomBathroomBath,
          alt: "バスルームのバス",
        },
      ],
      subroomImages: [
        {
          src: entranceImg,
          alt: "入口",
        },
        {
          src: roomEntranceFireExtinguisher,
          alt: "入口の消火器",
        },
        {
          src: roomBedroomKey,
          alt: "寝室の鍵",
        },
        {
          src: entranceSlippersImg,
          alt: "入口のスリッパ",
        },
      ],
      amenityImages: [
        {
          src: roomBathroomSink,
          alt: "バスルームのシンク",
        },
        {
          src: roomBathroomTowel,
          alt: "バスルームのタオル",
        },
        {
          src: roomBathroomWasherDryer,
          alt: "バスルームの洗濯乾燥機",
        },
        {
          src: roomToiletPull,
          alt: "トイレのプル",
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
          description: "くつろぎの和室でボードゲームや団らんのひとときを",
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
  computed: {
    logo() {
      if (document.documentElement.classList.contains("webp")) {
        return boxLogoNavyWebp;
      } else {
        return boxLogoNavy;
      }
    },
  },
};
</script>

<style scoped>
section {
  background-image: url("../assets/images/logo/background_beige.webp");
  padding: 0;
}
.facility {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

/* 画像セクション：縦画像用グリッドレイアウト */
.image-section {
  display: grid;
  width: 100%;
  grid-template-columns: repeat(4, 1fr);
  margin: 5rem 0;
}
.image-section:nth-of-type(1) {
  margin: 0 0 5rem 0;
}
div:nth-of-type(8) {
  margin: 5rem 0 0 0;
}

.vertical-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.room-section {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

@media (max-width: 768px) {
  /* スマホ・タブレットでは2列×2段のグリッド表示 */
  .image-section {
    grid-template-columns: repeat(2, 1fr);
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
