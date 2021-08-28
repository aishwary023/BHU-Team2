<template>
  <div id="app" class="mb-5" style="margin-top:10px">
    <h1>Team 2</h1>
    <b-container>
      <b-row>
        <b-col cols="8" class="left mr-2">
          <div>
            <b-input-group prepend="Search" class="mt-3">
              <b-form-input list="abcd" v-model="searchInput" placeholder="e.g. AAPL">
              </b-form-input>
              <datalist id="abcd">

                <option v-for="i in history" :key="i" :value="i"></option>
              </datalist>
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
          <b-row>
            <b-col>
              <b-form-select v-model="selected" :options="options"></b-form-select>
            </b-col>
            <b-col cols="3" class="text-right">
              <b-button @click="fetchData()" variant="success">
                Show Chart
              </b-button>
            </b-col>
          </b-row>

          <h5 class="mt-2" style="color: red" v-if="error">Please enter all details</h5>

          <hr />
          <div>
            Chart
            <hr />
            <div id="chart">
              <apexchart
                :type="chartType"
                height="350"
                :options="chartOptions"
                :series="series"
              ></apexchart>
            </div>
          </div>
        </b-col>

        <b-col class="right">
          <company-info :info="searchInput"></company-info>
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
      history: [],
      chartType: 'candlestick',
      error: false,
      selected: 1,
      options: [
        { value: 1, text: 'CandleStick' },
        { value: 3, text: 'Bar' }
      ],
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
      this.searchInput = this.searchInput.toUpperCase()
      if(!this.searchInput || !this.startDate || !this.endDate) {
        this.error = true;
        return;
      }
      if(!this.history.includes(this.searchInput))
        this.history.push(this.searchInput)
      this.error = false;

      this.data = [];
      this.series = [];

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
      console.log(url)
      axios
        .get(url)
        .then((response) => {
          console.log(response)
          this.data = response.data;
          switch(this.selected) {
            case 1:
              this.showCandleStick();
              return;
            case 3:
              this.bar()
              return;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    showCandleStick() {
      let data = [];
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
      this.chartType = 'candlestick'
      this.chartOptions = {
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
      this.series.push({ data: data });
    },
    bar() {
      this.chartType = 'bar'
      this.chartOptions = {
            chart: {
              type: 'bar',
              height: 500,
              stacked: true,
            },
            plotOptions: {
              bar: {
                horizontal: false,
              },
            },
            stroke: {
              width: 1,
              colors: ['#fff']
            },
            title: {
              text: '100% Stacked Bar'
            },
            xaxis: {
              categories: [],
            },
            tooltip: {
              y: {
                formatter: function (val) {
                  return val + "K"
                }
              }
            },
            fill: {
              opacity: 1
            },
            legend: {
              position: 'top',
              horizontalAlign: 'left',
              offsetX: 40
            }
          },
      this.series = [
        {
          name: 'Open',
          data: []
        },
        {
          name: 'High',
          data: []
        },
        {
          name: 'Low',
          data: []
        },
        {
          name: 'Close',
          data: []
        }
      ];
      for (let i = 0; i < this.data.length; i++) {
        let dateArray = this.data[i].date.split('-');

        this.chartOptions.xaxis.categories.push(dateArray[2] +"-"+ dateArray[1] +"-"+ dateArray[0])

        this.series[0].data.push(this.data[i].open);
        this.series[1].data.push(this.data[i].high);
        this.series[2].data.push(this.data[i].low);
        this.series[3].data.push(this.data[i].close);
      }
    },
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
