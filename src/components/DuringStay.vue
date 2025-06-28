<template>
  <section>
    <SmallHeading
      :title-ja="'滞在の楽しみ方'"
      :title-en="'During Stay'"
      :isWhite="true" />
    <div class="content-wrapper content">
      <!-- Day marker -->
      <h3 class="day-title">
        <div class="day-marker">
          <h4 class="day-number">DAY1</h4>
        </div>
        <span class="day-description"> 秘境ふるびらを味わう </span>
      </h3>

      <!-- Timeline -->
      <div class="timeline">
        <!-- Left side - Timeline -->
        <div class="timeline-left">
          <div class="timeline-line"></div>

          <!-- Timeline items -->
          <div class="timeline-items">
            <div
              v-for="item in timelineItems"
              :key="item.number"
              class="timeline-item">
              <div class="timeline-marker">
                <div class="marker-circle">{{ item.number }}</div>
              </div>
              <div class="timeline-text">{{ item.text }}</div>
              <img
                :src="rowImages[item.number - 1].src"
                :alt="rowImages[item.number - 1].alt"
                class="image-item mobile-image" />
            </div>
          </div>
        </div>

        <!-- Right side - Images -->
        <div class="image-grid">
          <img
            v-for="(img, index) in rowImages"
            :key="index"
            :src="img.src"
            :alt="img.alt"
            class="image-item desktop-image" />
        </div>
      </div>
    </div>
    <div class="content-wrapper day2 content">
      <!-- Day marker -->
      <h3 class="day-title">
        <div class="day-marker">
          <h4 class="day-number">DAY2</h4>
        </div>
        <span class="day-description"> ふるびら周辺をドライブ </span>
      </h3>

      <!-- Timeline -->
      <div class="timeline">
        <!-- Left side - Images -->
        <div class="image-grid">
          <img
            v-for="(img, index) in rowImagesDay2"
            :key="index"
            :src="img.src"
            :alt="img.alt"
            class="image-item desktop-image" />
        </div>
        <!-- Right side - Timeline -->
        <div class="timeline-left">
          <div class="timeline-line"></div>

          <!-- Timeline items -->
          <div class="timeline-items">
            <div
              v-for="item in timelineItemsDay2"
              :key="item.number"
              class="timeline-item">
              <div class="timeline-marker">
                <div class="marker-circle">{{ item.number }}</div>
              </div>
              <div class="timeline-text">{{ item.text }}</div>
              <img
                :src="rowImagesDay2[item.number - 1].src"
                :alt="rowImagesDay2[item.number - 1].alt"
                class="image-item mobile-image" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";
import SmallHeading from "./ui/SmallHeading.vue";
import unidon from "@/assets/images/generated/unidon.webp";
import sado from "@/assets/images/generated/sado.webp";
import onsen from "@/assets/images/generated/onsen.webp";
import cheers from "@/assets/images/generated/cheers.webp";
import drive from "@/assets/images/generated/drive.webp";
import bannya from "@/assets/images/generated/bannya.webp";
import fruitpark from "@/assets/images/generated/fruitpark.webp";
import whiskey from "@/assets/images/generated/whiskey.webp";

const timelineItems = ref([
  {
    number: 1,
    text: "採れたてうに丼とたらこを\nいただきます(6-8月)",
  },
  {
    number: 2,
    text: "ふるびら地元の方と\n「茶道」を体験",
  },
  {
    number: 3,
    text: "鉄分たっぷりで心も体も温まる\nふるびら温泉へ",
  },
  {
    number: 4,
    text: "カールふるびらに帰宅して\nみんなで乾杯!",
  },
]);

const rowImages = ref([
  {
    src: unidon,
    alt: "海鮮丼",
  },
  {
    src: sado,
    alt: "茶道",
  },
  {
    src: onsen,
    alt: "Traditional onsen",
  },
  {
    src: cheers,
    alt: "Group gathering",
  },
]);

const timelineItemsDay2 = ref([
  {
    number: 1,
    text: "積丹ブルーを横目に\n黄金岬・神威岬までドライブ",
  },
  {
    number: 2,
    text: "かつてのニシン番屋でタイムスリップ\n「鰊伝習館 ヤマシメ番屋」（積丹町）",
  },
  {
    number: 3,
    text: "名産の果物をテーマにした農村公園\n「農村公園フルーツパークにき」（仁木町）",
  },
  {
    number: 4,
    text: "見学の後にはウイスキーの無料試飲も！\n「ニッカウヰスキー余市蒸溜所」（余市町）",
  },
]);

const rowImagesDay2 = ref([
  {
    src: drive,
    alt: "ドライブ",
  },
  {
    src: bannya,
    alt: "ヤマシメ番屋",
  },
  {
    src: fruitpark,
    alt: "Fruit Park",
  },
  {
    src: whiskey,
    alt: "Nikka Whisky Distillery",
  },
]);
</script>

<style scoped>
section {
  background-image: url("../assets/images/logo/background_navy.webp");
  color: #e3dac2;
  min-height: 100vh;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

@media (max-width: 768px) {
  section {
    background-image: url("../assets/images/logo/background_navy-mobile.webp");
  }
}

.content-wrapper {
  margin: 0 auto;
  position: relative;
  padding: 2rem;
  border: 1px solid #ffffff;
  margin: 2rem 0;
}

.day-title {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  margin: 1rem 0;
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
}

.day-marker {
  background-color: #e3dac2;
  color: #1a2332;
  border-radius: 50%;
  width: 5rem;
  height: 5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 0;
  overflow: hidden;
}

.day2 .day-marker {
  background-color: #b2c8ac;
}

.day-number {
  font-size: 1.5rem;
  font-weight: 600;
  font-size: var(--font-size-heading);
}

.day-description {
  color: #e3dac2;
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
  font-style: normal;
  font-size: var(--font-size-heading);
}

.timeline {
  margin-top: 4rem;
  display: flex;
  gap: 2rem;
}

.timeline-left {
  position: relative;
  flex: 1;
}

.timeline-line {
  position: absolute;
  left: 1.4rem;
  top: 5rem;
  bottom: 5rem;
  width: 1px;
  background-color: rgba(227, 218, 194, 0.5);
}

.timeline-items {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
  font-style: normal;
}

.timeline-item {
  position: relative;
  height: 12.5rem;
  display: flex;
  align-items: center;
}

.timeline-marker {
  position: absolute;
  left: 1.5rem;
  transform: translateX(-50%);
}

.marker-circle {
  background-color: #e3dac2;
  color: #1a2332;
  border-radius: 50%;
  width: 3rem;
  height: 3rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  font-weight: 600;
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
  font-style: normal;
}

.day2 .marker-circle {
  background-color: #b2c8ac;
}

.timeline-text {
  margin-left: 4rem;
  color: #e3dac2;
  font-size: 1.125rem;
  white-space: pre-line;
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
  font-style: normal;
}

.image-grid {
  flex: 2;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.image-item {
  object-fit: cover;
  object-position: center;
  width: 100%;
  height: 12.5rem;
  transition: transform 0.3s ease;
  margin: 0.5rem 0;
}

.image-grid,
.timeline-item {
  overflow: hidden;
}

.mobile-image {
  display: none;
}

@media (max-width: 1000px) {
  .timeline {
    flex-direction: column;
  }
  .timeline-line {
    left: 1.4rem;
    top: 3rem;
    bottom: 18rem;
    width: 1px;
    background-color: rgba(227, 218, 194, 0.5);
  }

  .image-grid {
    display: none;
  }

  .timeline-item {
    flex-direction: column;
    align-items: flex-start;
    height: auto;
    margin-bottom: 2rem;
  }

  .timeline-text {
    margin-left: 4rem;
    margin-bottom: 1.5rem;
  }

  .mobile-image {
    display: block;
    width: 100%;
    height: auto;
  }

  .desktop-image {
    display: none;
  }

  .day2 .timeline {
    flex-direction: column;
  }

  .day2 .image-grid {
    order: 2;
  }
}

@media (min-width: 1001px) {
  .desktop-image {
    width: 100%;
    height: 12.5rem;
  }
}

/* 360px以下のスタイルを追加 */
@media (max-width: 360px) {
  .content-wrapper {
    border: none;
  }
  .content {
    width: 100vw;
    padding: 0.5rem;
  }
}

@media (max-width: 425px) {
  .day-marker {
    width: auto;
    height: auto;
    padding: 0.5rem 1rem;
    border-radius: 0;
    display: inline-flex;
    justify-content: center;
    align-items: center;
  }
}
</style>
