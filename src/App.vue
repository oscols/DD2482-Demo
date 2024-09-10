<template>
  <h2>{{ msg }}</h2>
  <input v-model="msg">
  <div id="app">
    <line-chart v-if="chartData" :chart-data="chartData" :options="chartOptions"></line-chart>
  </div>
</template>

<style scoped>
.chart-container {
  position: relative;
  height: 400px; /* Adjust this to your needs */
  width: 600px;  /* Adjust this to your needs */
}
</style>

<script>
import LineChart from './components/LineChart.vue'


export default {
  data() {
    return {
      msg: 'Hello World!',
      chartData: null, // Initialize as null
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    }
  },
  components: {
    LineChart
  },
  // mounted() {
  //   this.chartData = {
  //     labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
  //     datasets: [
  //       {
  //         label: 'Data One',
  //         backgroundColor: 'rgba(75, 192, 192, 0.2)',
  //         borderColor: 'rgba(75, 192, 192, 1)',
  //         pointBackgroundColor: 'rgba(75, 192, 192, 1)',
  //         pointBorderColor: '#fff',
  //         data: [40, 39, 10, 40, 39, 80, 40],
  //         fill: true
  //       }
  //     ]
  //   };
  // console.log(this.chartData);
  // }
}

</script>