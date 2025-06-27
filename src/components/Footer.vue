<template>
  <footer class="Footer">
    <div class="info-container">
      <div class="reserve-container">
        <ReserveButton />
        <div class="social-icons">
          <!-- <a href="#" class="icon">
          <img
            src="@/assets/images/facebook_logo.png"
            alt="Facebook"
            class="social-logo" />
        </a> -->
          <a
            href="https://www.instagram.com/curl_furubira/"
            target="_blank"
            class="icon">
            <img
              src="@/assets/images/logo/Instagram_logo.png"
              alt="Instagram"
              class="social-logo" />
          </a>
        </div>
      </div>
      <div class="description">
        <img
          src="@/assets/images/logo/boxlogo_white.png"
          alt="カールふるびら"
          class="logo" />
        <div class="text">
          <p class="address">〒046-0102 北海道古平郡古平町丸山町103</p>
          <p class="email">yohey.watanave@gmail.com</p>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
import ReserveButton from "./ui/ReserveButton.vue";
export default {
  name: "Footer",
  components: {
    ReserveButton,
  },
};
</script>

<style scoped>
.Footer {
  background-image: url("../assets/images/logo/background_navy.webp");
  color: #fff;
  padding: 2rem;
  padding-bottom: 4rem;
  text-align: center;
}

@media (max-width: 768px) {
  .Footer {
    background-image: url("../assets/images/logo/background_navy-mobile.webp");
  }
}

.info-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 1rem;
}

.address,
.email {
  margin: 0.5rem 0;
}

.social-icons {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-top: 1rem;
}

.icon {
  color: #fff;
  text-decoration: none;
  font-size: 1rem;
}

.social-logo {
  width: 24px;
  height: 24px;
}

.icon:hover {
  text-decoration: underline;
}
.description {
  display: flex;
  flex-direction: row;
  align-items: center;
  flex-wrap: wrap;
  justify-content: center;
}
.description .logo {
  width: 200px;
}
.description p {
  color: #fff;
}
</style>
