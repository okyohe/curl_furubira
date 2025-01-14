<template>
  <div id="app">
    <Header />
    <Fv />
    <Impression />
    <Facility />
    <ExperiencePlan />
    <DuringStay />
    <Access />
    <AccommodationFee />
    <LastPhoto />
    <Footer />
  </div>
</template>

<script>
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

export default {
  components: {
    Header,
    Fv,
    Impression,
    Facility,
    ExperiencePlan,
    DuringStay,
    Access,
    AccommodationFee,
    LastPhoto,
    Footer,
  },
};
</script>

<style>
/* Add global styles here */
:root {
  --font-size-text: 16px;
  --font-size-heading: 24px;
}

p,
a {
  font-size: var(--font-size-text);
  font-family: "Noto Sans JP", serif;
}

h1,
h2,
h3,
h4,
h5,
h6,
button,
div {
  font-size: var(--font-size-heading);
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
  font-style: normal;
}
section {
  padding: 2rem 0;
}
</style>
