<template>
  <div class="row justify-content-center">
    <hr />
    Этаж №{{ floor[0].floor }}
    <ApartmentItem
      v-for="apartment in floor"
      :key="apartment"
      v-bind:apartment="apartment"
    />
  </div>
</template>

<script>
import ApartmentItem from "@/components/ApartmentItem";
export default {
  props: ["floor"],
  components: {
    ApartmentItem,
  },
};
</script>
