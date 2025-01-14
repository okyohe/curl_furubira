<template>
  <div
    :class="[
      'flex items-center justify-center rounded-full',
      `bg-${bgColor} text-${textColor}`,
    ]"
    :style="{ width: `${size}px`, height: `${size}px` }">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "Circle",
  props: {
    size: {
      type: Number,
      default: 50,
    },
    bgColor: {
      type: String,
      default: "cream",
    },
    textColor: {
      type: String,
      default: "primary",
    },
  },
};
</script>

<style scoped>
.rounded-full {
  border-radius: 9999px;
}
</style>
