<template>
    <div>
      <line-chart :chart-data="chartData" :options="chartOptions"></line-chart>
    </div>
</template>
  
<script>
  import { Line } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale } from 'chart.js'
  
  ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale)
  
  export default {
    components: {
      LineChart: Line
    },
    data() {
      return {
        chartData: {
          labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
          datasets: [
            {
              label: 'Data One',
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              pointBackgroundColor: 'rgba(75, 192, 192, 1)',
              pointBorderColor: '#fff',
              data: [40, 39, 10, 40, 39, 80, 40],
              fill: true, // Enable to fill the area under the line
            }
          ]
        },
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
    }
  }
</script>
  
<style scoped>
  .chart-container {
    position: relative;
    height: 400px;
    width: 600px;
  }
</style>
  