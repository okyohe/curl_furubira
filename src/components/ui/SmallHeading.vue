<template>
  <div class="small-heading content">
    <div
      class="title-container"
      :style="isWhite ? { color: '#fff' } : { color: 'inherit' }">
      <hr class="divider" :style="isWhite ? { backgroundColor: '#fff' } : {}" />
      <h2 class="heading">{{ titleJa }}</h2>
      <hr class="divider" :style="isWhite ? { backgroundColor: '#fff' } : {}" />
    </div>
    <p
      class="subheading"
      :style="isWhite ? { color: '#fff' } : { color: 'inherit' }">
      {{ titleEn }}
    </p>
  </div>
</template>

<script>
export default {
  name: "SmallHeading",
  props: {
    titleJa: {
      type: String,
      required: true,
    },
    titleEn: {
      type: String,
      required: true,
    },
    isWhite: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style scoped>
.small-heading {
  text-align: center;
  display: block;
  margin-bottom: 2rem;
}
.subheading {
  font-family: "Zen Old Mincho", serif;
  font-weight: 600;
  font-style: normal;
}

.title-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.heading {
  font-size: var(--font-size-heading);
  font-weight: bold;
  margin: 0 1rem;
}

.subheading {
  font-size: 14px;
  margin: 0;
}

.divider {
  border: 0;
  height: 2px;
  background-color: #000;
  width: 30%;
}
</style>
