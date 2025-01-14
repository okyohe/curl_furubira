<template>
  <div class="relative">
    <Circle size="48" bgColor="cream" textColor="primary">
      <span class="text-xl font-semibold">{{ number }}</span>
    </Circle>
    <div class="ml-16 text-cream text-lg">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import Circle from "./Circle.vue";

export default {
  name: "TimelineItem",
  components: {
    Circle,
  },
  props: {
    number: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
.ml-16 {
  margin-left: 4rem;
}

.text-lg {
  font-size: 1.125rem;
}

.text-cream {
  color: #e5ded3;
}
</style>
