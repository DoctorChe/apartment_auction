<template>
  <form @submit.prevent="setBidDuration">
    Задайте время для проведения аукциона в минутах
    <input type="number" v-model="bidDuration" />
    <button class="btn btn-outline-primary btn-sm mx-2">Старт</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      bidDuration: Number,
    };
  },
  methods: {
    setBidDuration() {
      if (this.bidDuration > 0 && this.bidDuration <= 10) {
        this.$emit("create-auction", this.bidDuration);
      } else {
        alert("Время должно лежать в диапазоне от 1 до 10 минут.");
      }
    },
  },
};
</script>

<style scoped>
input {
  width: 50px;
}
</style>
