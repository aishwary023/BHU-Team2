<template>
  <div>
    <br />
    <h1 v-if="company.companyName">{{ company.companyName }}</h1>
    <p v-if="!company.companyName">Company Name</p>
    <h4 v-if="company.companyName">{{ company.symbol }}</h4>
    <br />
    <hr />
    <div>
      <b-card
        title="Description"
        style="max-width: 20rem;"
        class="mb-2"
        v-if="company.description"
      >
        <b-card-text >
          {{ company.description | truncate(300, '...') }}
        </b-card-text>
      </b-card>
    </div>

    <div>
      <b-card
        title="Other Info"
        style="max-width: 20rem;"
        class="mb-2"
        v-if="company.description"
      >
      <label><b>CEO:</b> </label> {{ company.CEO }} <br>
      <label><b>Country:</b> </label> {{ company.country }} <br>
      <label><b>Website:</b> </label> <a :href="company.website">{{ company.website }}</a>
      </b-card>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      company: {}
    };
  },
  props: ['info'],
  name: 'CompanyInfo',
  watch: {
    info: function(newVal) {
      let url =
        'https://cloud.iexapis.com/stable/stock/' +
        newVal +
        '/company?token=' +
        process.env.VUE_APP_API_KEY;
      axios
        .get(url)
        .then((response) => {
          this.company = response.data;
          console.log(this.company)
        })
        .catch((error) => {
          this.company = {}
          console.log(error);
        });
    }
  }
};
</script>
