<template>
  <div class="col-sm-2">
    <div class="card mb-3" v-bind:class="borderClass(apartment)">
      <div class="card-header" v-bind:class="borderClass(apartment)">
        Квартира №{{ apartment.number }}
      </div>
      <div class="card-body">
        <ul class="list-group list-group-flush">
          <li class="list-group-item" v-bind:class="borderClass(apartment)">
            Площадь: {{ apartment.area }}
          </li>
          <li class="list-group-item" v-bind:class="borderClass(apartment)">
            Комнат: {{ apartment.rooms }}
          </li>
          <li class="list-group-item" v-bind:class="borderClass(apartment)">
            Балкон: {{ translateClasses(apartment.balcony) }}
          </li>
          <li class="list-group-item" v-bind:class="borderClass(apartment)">
            Отделка: {{ translateClasses(apartment.finishing) }}
          </li>
          <li class="list-group-item" v-bind:class="borderClass(apartment)">
            Стартовая цена: {{ apartment.start_price }}
          </li>
        </ul>
      </div>
      <div class="card-footer" v-bind:class="borderClass(apartment)">
        <div v-if="isNotSold(apartment)">
          <PlaceBid />
        </div>
        <div v-else>Продано</div>
      </div>
    </div>
  </div>
</template>

<script>
import PlaceBid from "@/components/PlaceBid";

export default {
  props: {
    apartment: {
      type: Object,
      required: true,
    },
  },
  methods: {
    borderClass(apartment) {
      return {
        "border-info": apartment.status === "for sale",
        "border-warning": apartment.status === "trading",
        "border-secondary": apartment.status === "sold out",
      };
    },
    isNotSold(apartment) {
      return apartment.status !== "sold out" ? true : false;
    },
    translateClasses(classForTranslate) {
      return classForTranslate !== true ? "Есть" : "Нет";
    },
  },
  components: {
    PlaceBid,
  },
};
</script>
