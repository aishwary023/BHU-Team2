<template>
  <div id="app">
    <b-container>
      <b-row>
        <b-col cols="8" class="left mr-2">
          <div>
            <b-input-group prepend="Search" class="mt-3">
              <b-form-input v-model="searchInput" placeholder="e.g. AAPL">
              </b-form-input>
              <b-input-group-append>
                <b-button @click="fetchData()" variant="success">
                  Search
                </b-button>
              </b-input-group-append>
            </b-input-group>
          </div>
          <br />
          <b-row>
            <b-col>
              <label for="datepicker-sm"><b>Start Date</b></label>
              <b-form-datepicker
                id="start-datepicker"
                v-model="startDate"
                class="mb-2"
              ></b-form-datepicker>
            </b-col>
            <b-col>
              <label for="datepicker-sm"><b>End Date</b></label>
              <b-form-datepicker
                id="end-datepicker"
                v-model="endDate"
                class="mb-2"
              ></b-form-datepicker>
            </b-col>
          </b-row>
          <hr />
          <div>
            Chart
            <hr />
            <div id="chart">
              <apexchart
                type="candlestick"
                height="350"
                :options="chartOptions"
                :series="series"
              ></apexchart>
            </div>
          </div>
        </b-col>

        <b-col class="right">
          <company-info :info="queryParams"></company-info>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios';
import CompanyInfo from './components/CompanyInfo.vue';

export default {
  name: 'App',
  components: {
    CompanyInfo
  },
  data() {
    return {
      searchInput: '',
      startDate: '',
      endDate: '',
      queryParams: {},
      data: [],
      series: [],
      chartOptions: {
        chart: {
          type: 'candlestick',
          height: 350
        },
        title: {
          text: 'CandleStick Chart',
          align: 'left'
        },
        xaxis: {
          type: 'datetime'
        },
        yaxis: {
          tooltip: {
            enabled: true
          }
        }
      }
    };
  },
  methods: {
    fetchData() {
      this.data = []
      this.series = []
      // Add GET Request
      this.queryParams = {
        symbol: this.searchInput,
        start: this.startDate,
        end: this.endDate
      };

      let baseUrl = 'http://127.0.0.1:8000/stock/list/';
      let url =
        baseUrl +
        '?symbol=' +
        this.queryParams.symbol +
        '&start=' +
        this.queryParams.start +
        '&end=' +
        this.queryParams.end;

      axios
        .get(url)
        .then((response) => {
          this.data = response.data;
          this.showDefaultGraph();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    showDefaultGraph() {
      // process data
      let data = []
      console.log('SHOW');
      for (let i = 0; i < this.data.length; i++) {
        let dateArray = this.data[i].date.split('-');
        let obj = {
          x: new Date(dateArray[0], dateArray[1], dateArray[2]),
          y: [
            this.data[i].open,
            this.data[i].high,
            this.data[i].low,
            this.data[i].close
          ]
        };
        data.push(obj);
      }


      this.series.push({data: data})
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.left {
  border: 1px solid black;
}
.right {
  border: 1px solid black;
}
</style>
