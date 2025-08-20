<template>
  <footer class="Footer" :style="{ backgroundImage: `url(${backgroundNavyImg})` }">
    <div class="info-container">
      <div class="reserve-container">
        <ReserveButton />
        <div class="social-icons">
          <a
            href="https://www.instagram.com/curl_furubira/"
            target="_blank"
            class="icon">
            <img
              :src="instagramLogo"
              alt="Instagram"
              class="social-logo" />
          </a>
        </div>
      </div>
      <div class="description">
        <img
          :src="logoImg"
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

<script setup>
import ReserveButton from "./ui/ReserveButton.vue";
import instagramLogo from "@/assets/images/logo/Instagram_logo.png";
import logoImg from "@/assets/images/logo/boxlogo_white.png";
import backgroundNavyImg from "@/assets/images/logo/background_navy.webp";
import backgroundNavyMobileImg from "@/assets/images/logo/background_navy-mobile.webp";
</script>

<style scoped>
.Footer {
  color: #fff;
  padding: 2rem;
  padding-bottom: 4rem;
  text-align: center;
}

@media (max-width: 768px) {
  .Footer {
    background-image: url("v-bind('backgroundNavyMobileImg')");
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
  gap: 1rem;
  margin-top: 2rem;
}

.logo {
  height: 60px;
}

.text {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.address,
.email {
  margin: 0.25rem 0;
  font-size: 0.9rem;
  color: #fff;
}

@media (max-width: 768px) {
  .description {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .logo {
    height: 50px;
  }
}
</style>
