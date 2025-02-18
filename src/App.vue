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
:root {
  --font-size-text: 16px;
  --font-size-cta: 18px;
  --font-size-heading: 20px;
}
h1,
h2,
h3,
h4,
h5,
h6 {
  font-size: var(--font-size-heading);
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
  font-style: normal;
}
button,
div,
a {
  font-size: var(--font-size-cta);
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
  font-style: normal;
  color: #000333;
}
div,
p,
span {
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
  background-image: url(import.meta.env.VITE_BACKGROUND_IMAGE_BEIGE);
  background-repeat: repeat;
  background-size: auto;
}

section.navy {
  background-image: url(import.meta.env.VITE_BACKGROUND_IMAGE_NAVY);
  background-repeat: repeat;
  background-size: auto;
}

section.kamui {
  background-image: url(import.meta.env.VITE_BACKGROUND_IMAGE_KAMUI);
  background-repeat: repeat;
  background-size: auto;
}
.tiny-heading-line {
  border: 0;
  height: 1px;
  background-color: #000;
  margin: 1rem 0;
}

@media (max-width: 768px) {
  .content {
    width: 100%;
  }
}
</style>
