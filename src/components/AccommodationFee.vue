<template>
  <section>
    <div class="wrapper">
      <SmallHeading :title-ja="'料金'" :title-en="'Accommodation Fee'" />
      <p>料金は季節と曜日によって変動します。</p>
      <p>Airbnbからご覧ください。</p>
    </div>
  </section>
</template>

<script>
import SmallHeading from "./ui/SmallHeading.vue";
import ReserveButton from "./ui/ReserveButton.vue";

export default {
  name: "AccommodationFee",
  components: {
    SmallHeading,
    ReserveButton,
  },
};
</script>

<style scoped>
section {
  background-image: url("../assets/images/background_beige.png");
}
.wrapper {
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
