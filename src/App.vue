<template>
  <div id="app">
    <Header />
    <main>
      <Fv id="fv" />
      <Impression id="impression" />
      <Facility id="facility" />
      <ExperiencePlan id="experiencePlan" />
      <DuringStay id="duringStay" />
      <Access id="access" />
      <AccommodationFee id="accommodationFee" />
      <LastPhoto id="lastPhoto" />
    </main>
    <Footer />
  </div>
</template>

<script setup>
import Header from "./components/Header.vue";
import Fv from "./components/Fv.vue";
import Impression from "./components/Impression.vue";
import Facility from "./components/Facility.vue";
import ExperiencePlan from "./components/ExperiencePlan.vue";
import DuringStay from "./components/DuringStay.vue";
import Access from "./components/Access.vue";
import AccommodationFee from "./components/AccommodationFee.vue";
import LastPhoto from "./components/LastPhoto.vue";
import Footer from "./components/Footer.vue";

import backgroundBeigeUrl from "@/assets/images/logo/background_beige.webp";
import backgroundNavyUrl from "@/assets/images/logo/background_navy.webp";
import backgroundKamuiUrl from "@/assets/images/logo/background_kamui.webp";

// CSSを明示的に読み込み
import "./assets/index.css";

const backgroundBeige = `url(${backgroundBeigeUrl})`;
const backgroundNavy = `url(${backgroundNavyUrl})`;
const backgroundKamui = `url(${backgroundKamuiUrl})`;
</script>

<style>
/* 基本的なスタイルを直接埋め込み */
:root {
  --font-size-text: 16px;
  --font-size-cta: 18px;
  --font-size-heading: 20px;
}

h1, h2, h3, h4, h5, h6 {
  font-size: var(--font-size-heading);
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
  font-style: normal;
}

button, div, a {
  font-size: var(--font-size-cta);
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
  font-style: normal;
  color: #000333;
}

div, p, span {
  font-size: var(--font-size-text);
  font-family: "Noto Sans JP", serif;
  font-optical-sizing: auto;
  color: #000333;
}

section {
  padding: 2rem 0;
}

.content {
  width: 67%;
  max-width: 990px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.social-links img {
  width: 30px;
  height: 30px;
}

section {
  display: flex;
  justify-content: center;
  align-items: center;
}

section.beige {
  background-image: v-bind(backgroundBeige);
  background-repeat: repeat;
  background-size: auto;
}

section.navy {
  background-image: v-bind(backgroundNavy);
  background-repeat: repeat;
  background-size: auto;
}

section.kamui {
  background-image: v-bind(backgroundKamui);
  background-repeat: repeat;
  background-size: auto;
}
</style>
