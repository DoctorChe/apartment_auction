<template>
  <div>
    <h1 class="text-center">Аукцион</h1>
    <div class="row m-2">
      <div class="col-sm-6 text-center">
        <SetBidDuration @create-auction="createAuction" />
      </div>
      <div class="col-sm-1 text-center">
        <button class="btn btn-outline-primary btn-sm mx-2" @click="signIn">
          Коннект
        </button>
      </div>
      <div class="col-sm-4 text-center">
        Время до конца аукциона: {{ finish }}
      </div>
    </div>
    <Loader v-if="loading" />
    <ApartmentList v-else v-bind:apartments="apartments" />
  </div>
</template>

<script>
import axios from "axios";
import ApartmentList from "@/components/ApartmentList";
import Loader from "@/components/Loader";
import SetBidDuration from "@/components/SetBidDuration";

let sseClient;

export default {
  data() {
    return {
      apartments: [],
      countdown: "...",
      loading: true,
    };
  },
  mounted() {
    const url = "http://localhost:8082/apartments";
    // fetch(url)
    //   .then((response) => response.json())
    //   //   .then((json) => (this.apartments = json));
    //   .then((json) => (this.apartments = json));
    axios
      .get(url)
      .then((response) => {
        // JSON responses are automatically parsed.
        this.apartments = response.data;
      })
      .catch((e) => {
        this.errors.push(e);
      });
    this.loading = false;
  },
  methods: {
    // async fetchApartments() {
    //   console.log("fetchApartments");
    //   try {
    //     // this.isApartmentsLoading = true;
    //     const url = "http://localhost:8082/apartments";
    //     const response = await axios.get(url, {
    //       //   params: {
    //       //     _page: this.page,
    //       //     _limit: this.limit,
    //       //   },
    //     });
    //     // this.totalPages = Math.ceil(
    //     //   response.headers["x-total-count"] / this.limit
    //     // );
    //     console.log(response.data);
    //     this.apartments = response.data;
    //   } catch (e) {
    //     alert("Ошибка");
    //   } finally {
    //     // this.isApartmentsLoading = false;
    //   }
    // },
    // setCountdown(data) {
    //   this.countdown = data;
    // },
    startAuction(bidDuration) {
      const url = `http://localhost:8082/auctions/stream?bid_duration=${bidDuration}`;

      sseClient = this.$sse.create(url);

      // Catch any errors (ie. lost connections, etc.)
      sseClient.on("error", (e) => {
        console.error("lost connection or failed to parse!", e);

        // If this error is due to an unexpected disconnection, EventSource will
        // automatically attempt to reconnect indefinitely. You will _not_ need to
        // re-add your handlers.
      });

      // Handle messages without a specific event
      sseClient.on("update", this.handleUpdate);

      //   // Handle 'chat' messages
      //   sseClient.on("end", this.handleEnd);

      // Handle once for a ban message
      sseClient.once("end", this.handleEnd);

      sseClient
        .connect()
        // .then((sse) => {
        //   console.log("We're connected!");

        //   // Unsubscribes from event-less messages after 7 seconds
        //   setTimeout(() => {
        //     sseClient.off("update", this.handleUpdate);
        //     console.log("Stopped listening to event-less messages!");
        //   }, 7000);

        //   // Unsubscribes from chat messages after 14 seconds
        //   setTimeout(() => {
        //     sse.off("end", this.handleEnd);
        //     console.log("Stopped listening to chat messages!");
        //   }, 14000);
        // })
        .catch((err) => {
          // When this error is caught, it means the initial connection to the
          // events server failed.  No automatic attempts to reconnect will be made.
          console.error("Failed to connect to server", err);
        });

      //   const evtSource = new EventSource(url);
      //   evtSource.addEventListener("update", function(event) {
      //     // Logic to handle status updates
      //     // console.log("Пришло сообщение...");
      //     // console.log(event);
      //     // console.log(event.data);
      //     this.countdown = event.data;
      //     // this.setCountdown(event.data);
      //     console.log(this.countdown);
      //   });
      //   evtSource.addEventListener("end", function(event) {
      //     console.log(event.data);
      //     this.countdown = "Аукцион окончен";
      //     evtSource.close();
      //   });
      //   //   this.countdown = "Аукцион окончен совсем";
    },
    handleEnd(banMessage) {
      // Note that we can access properties of message, since our parser is set to JSON
      // and the hypothetical object has a `reason` property.
      //   this.messages.push(`You've been banned! Reason: ${banMessage.reason}`);
      console.warn(banMessage);
      //   sseClient.disconnect();
      //   sseClient.sourse.close();
      //   console.warn(typeof sseClient.sourse);
    },
    handleUpdate(message) {
      // Note that we can access properties of message, since our parser is set to JSON
      // and the hypothetical object has these properties.
      //   this.messages.push(`${message.user} said: ${message.text}`);
      console.warn(message);
      this.countdown = message;
    },
    createAuction(bidDuration) {
      //   const url = `http://localhost:8082/auctions/`;
      const url = `http://localhost:8082/auctions?bid_duration=${bidDuration}`;
      console.log(bidDuration);
      // const response = await axios.get(url, {
      //       params: {
      //         bid_duration: bidDuration,
      //       },
      //   });
      axios
        // .post(url, { bid_duration: bidDuration })
        .post(url)
        .then((response) => {
          //   this.apartments = response.data;
          console.log(response.data);
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
    getAuction() {
      const url = `http://localhost:8082/auctions/1/`;
      axios
        .get(url)
        .then((response) => {
          console.log(response.data);
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
    connectAuction() {
      const url = `http://localhost:8082/auctions/connect/`;
      axios
        .get(url)
        .then((response) => {
          console.log(response.data);
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
    createBid() {
      const apartmentId = 1;
      const amount = 5000000;
      const url = `http://localhost:8082/bids?apartment_id=${apartmentId}&amount=${amount}`;
      axios
        .post(url)
        .then((response) => {
          console.log(response.data);
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
    signIn() {
      const name = "Duncan";
      const url = `http://localhost:8082/users/sign-in?name=${name}`;
      axios
        .post(url)
        .then((response) => {
          console.log(response.data);
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
  },
  components: {
    ApartmentList,
    Loader,
    SetBidDuration,
  },
  computed: {
    finish() {
      return this.countdown;
    },
  },
  sse: {
    cleanup: true,
  },
};
</script>
