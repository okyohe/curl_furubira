<template>
  <button
    @click="navigateToAirbnb"
    class="reserve-button text-black py-2 px-4 rounded flex items-center gap-2">
    <img
      src="@/assets/images/logo/airbnb_logo_navy.png"
      alt="Airbnb Logo"
      class="w-6 h-6" />
    ご予約はAirbnbから
  </button>
</template>

<script>
export default {
  name: "ReserveButton",

  methods: {
    navigateToAirbnb() {
      window.open("https://www.airbnb.jp/rooms/1186456384717300245", "_blank");
    },
  },
};
</script>

<style scoped>
.reserve-button {
  position: relative;
  overflow: hidden;
  font-size: var(--font-size-heading);
  background-color: rgb(227 218 194 / var(--tw-bg-opacity, 1));
  color: #000333;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
  font-family: "Zen Old Mincho", serif;
}

.reserve-button::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.5),
    transparent
  );
  transition: left 0.3s ease;
}

.reserve-button:hover::before {
  left: 100%;
}

.reserve-button:hover {
  background-color: rgb(247 238 214);
}
</style>
