<template>
  <Button
    @click="navigateToAirbnb"
    class="reserve-button text-black py-2 px-4 rounded zen-old-mincho-semibold">
    ご予約はこちら
  </Button>
</template>

<script>
import { Button } from "@/components/ui/button";

export default {
  name: "ReserveButton",
  components: {
    Button,
  },
  methods: {
    navigateToAirbnb() {
      window.location.href = "https://www.airbnb.com/";
    },
  },
};
</script>

<style scoped>
.reserve-button {
  font-size: var(--font-size-heading);
  background-color: rgb(227 218 194 / var(--tw-bg-opacity, 1));
}
</style>
