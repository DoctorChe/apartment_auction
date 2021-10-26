<template>
  <div>
    <Floor
      v-for="floor in apartmentsByFloors"
      :key="floor"
      v-bind:floor="floor"
    />
  </div>
</template>

<script>
import Floor from "@/components/Floor";
export default {
  props: ["apartments"],
  components: {
    Floor,
  },
  computed: {
    apartmentsByFloors() {
      var apartmentsByFloor = {};
      this.apartments.forEach((apartment) => {
        if (typeof apartmentsByFloor[apartment.floor] !== "undefined") {
          apartmentsByFloor[apartment.floor].push(apartment);
        } else {
          apartmentsByFloor[apartment.floor] = [apartment];
        }
      });
      return apartmentsByFloor;
    },
    apartmentsByFloorsLength() {
      return Object.keys(this.apartmentsByFloors).length;
    },
  },
};
</script>
