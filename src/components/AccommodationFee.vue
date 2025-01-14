<template>
  <section>
    <div class="wrapper">
      <SmallHeading :title-ja="'料金'" :title-en="'Accommodation Fee'" />
      <div class="table-wrapper">
        <table class="table">
          <thead>
            <tr>
              <th>宿泊料金</th>
              <th>価格</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>宿泊料金</td>
              <td>5,987円/1人1泊</td>
            </tr>
            <tr>
              <td>鹿の灯制作体験</td>
              <td>7,987円/1人1個</td>
            </tr>
            <tr>
              <td>宿泊料金 + 鹿の灯制作体験</td>
              <td>13,974円/1人1泊</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>

<script>
import SmallHeading from "./ui/SmallHeading.vue";
export default {
  name: "AccommodationFee",
  components: {
    SmallHeading,
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

.table-wrapper {
  margin-top: 2rem;
}

.table {
  width: 100%;
  text-align: left;
}

.table th,
.table td {
  padding: 0.5rem 1rem;
}

.table th {
  background-color: #f2f2f2;
  font-weight: bold;
}

.table td {
  background-color: #fff;
}
</style>
