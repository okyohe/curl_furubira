<template>
  <section>
    <SmallHeading
      :title-ja="'滞在の楽しみ方'"
      :title-en="'During Stay'"
      :isWhite="true" />
    <div class="content-wrapper">
      <!-- Day marker -->
      <h3 class="day-title">
        <div class="day-marker">
          <span class="day-number">DAY1</span>
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
            class="image-item" />
        </div>
      </div>
    </div>
    <div class="content-wrapper day2">
      <!-- Day marker -->
      <h3 class="day-title">
        <div class="day-marker">
          <span class="day-number">DAY2</span>
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
            class="image-item" />
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

const timelineItems = ref([
  {
    number: 1,
    text: "採れたてうに丼とたらこを\nいただきます(6-8月)",
  },
  {
    number: 2,
    text: "「鹿の灯」を手作り",
  },
  {
    number: 3,
    text: "ふるびら温泉へ",
  },
  {
    number: 4,
    text: "カールふるびらに帰宅して\nみんなで乾杯!",
  },
]);

const rowImages = ref([
  {
    src: new URL("@/assets/images/background_kamui.png", import.meta.url).href,
    alt: "Writing workshop",
  },
  {
    src: new URL("@/assets/images/background_kamui.png", import.meta.url).href,
    alt: "Writing workshop",
  },
  {
    src: new URL("@/assets/images/background_kamui.png", import.meta.url).href,
    alt: "Traditional onsen",
  },
  {
    src: new URL("@/assets/images/background_kamui.png", import.meta.url).href,
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
    src: new URL("@/assets/images/background_kamui.png", import.meta.url).href,
    alt: "Kamui Cape",
  },
  {
    src: new URL("@/assets/images/background_kamui.png", import.meta.url).href,
    alt: "Yamashime Ban’ya",
  },
  {
    src: new URL("@/assets/images/background_kamui.png", import.meta.url).href,
    alt: "Fruit Park",
  },
  {
    src: new URL("@/assets/images/background_kamui.png", import.meta.url).href,
    alt: "Nikka Whisky Distillery",
  },
]);
</script>

<style scoped>
section {
  background-image: url("../assets/images/background_navy.png");
  color: #e3dac2;
  min-height: 100vh;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.content-wrapper {
  max-width: 80%;
  width: 800px;
  margin: 0 auto;
  position: relative;
  padding: 2rem;
  border: 1px solid #ffffff;
  margin: 2rem 0;
}

.day-title {
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  width: 100%;
  flex-wrap: wrap;
  margin: 1rem 0 0 0;
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
}

.day-description {
  color: #e3dac2;
}

.timeline {
  margin-top: 4rem;
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 2rem;
}
.day2 .timeline {
  display: grid;
  grid-template-columns: 2fr 1fr;
}

.timeline-left {
  position: relative;
  height: 12.5rem;
}

.timeline-line {
  position: absolute;
  left: 2rem;
  top: 2rem;
  bottom: 2rem;
  width: 1px;
  background-color: #3a4352;
}

.timeline-items {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.timeline-item {
  position: relative;
  width: 100%;
  height: 12.5rem;
  justify-content: center;
  align-content: center;
  justify-content: center;
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
}

.day2 .marker-circle {
  background-color: #b2c8ac;
}

.timeline-text {
  margin-left: 4rem;
  color: #e3dac2;
  font-size: 1.125rem;
  white-space: pre-line;
}

.image-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

.image-item {
  object-fit: cover;
  width: 100%;
  height: 12.5rem;
}
</style>
