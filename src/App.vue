<template>
  <!-- <div> -->
  <!-- </div> -->
  <div class="chart">
    <h1 class="big-text">BuyHighSellLow.com</h1>
    <Line :data="data" :options="options" />
  </div>
  <div class="myclass">
    <button class="button" @click="openBuyPopup">
      <h2>buy</h2>
    </button>
    <button class="button" @click="openSellPopup">
      <h2>sell</h2>
    </button>
  </div>
  <div>
  </div>
  <div v-if="isBuyPopupVisible" class="popup-overlay">
      <div class="popup-content">
        <img src="@/assets/egg.webp" alt="Easter egg">
        <h2>Congratulations!</h2>
        <p>You have sold the stock for less than you bought it for!</p>
        <button @click="closeBuyPopup">Close</button>
      </div>
  </div>
  <div v-if="isSellPopupVisible" class="popup-overlay">
      <div class="popup-content">
        <h2>Ah...</h2>
        <p>You seem to have sold the stock for more than you bought it for...</p>
        <button @click="closeSellPopup">Close</button>
      </div>
  </div>
</template>

<script lang="ts">
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import { Line } from 'vue-chartjs'
import { data, options } from './chartConfig.ts'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

export default {
  name: 'App',
  components: {
    Line
  },
  data() {
    return {
      data: data, // Assign imported chart data
      options: options, // Assign imported chart options
      isBuyPopupVisible: false, // State to track popup visibility
      isSellPopupVisible: false, // State to track popup visibility
    };
  },
  methods: {
    openBuyPopup() {
      this.isBuyPopupVisible = true; // Show the popup
    },
    closeBuyPopup() {
      this.isBuyPopupVisible = false; // Hide the popup
    },
    openSellPopup() {
      this.isSellPopupVisible = true; // Show the popup
    },
    closeSellPopup() {
      this.isSellPopupVisible = false; // Hide the popup
    },
  }
}
</script>

<style scoped>
  .chart {
    position: relative;
    height: 500px;
    width: 600px;
  }
  .button {
    position: relative;
    height: 40px;
    width: 60px;
    margin-left: 10px;
  }
  .myclass {
    margin-top: auto;
  }
  .big-text{
    font-size: 50px;
  }
  .popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; /* Ensure it's on top */
}
.popup-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  width: 300px;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
</style>