<template>
  <div class="stats">
    <h3>Total redirects: {{ redirectedUrls['all_count'] }}</h3>
    <h3>Successful redirects from today: {{ redirectedUrls['all_good_today'] }}</h3>
    <h3>Bad redirects from today: {{ redirectedUrls['all_bad_today'] }}</h3>
    <h3>Good redirects from last hour: {{ redirectedUrls['all_good_hour'] }}</h3>
    <h3>Bad redirects from last hour: {{ redirectedUrls['all_bad_hour'] }}</h3>
    <h3>Good redirects from last minute: {{ redirectedUrls['all_good_minute'] }}</h3>
    <h3>Bad redirects from last minute: {{ redirectedUrls['all_bad_minute'] }}</h3>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'Stats',
  data() {
    return {
      redirectedUrls: {
        all_count: -1,
        all_good_today: -1,
        all_bad_today: -1,
        all_good_hour: -1,
        all_bad_hour: -1,
        all_good_minute: -1,
        all_bad_minute: -1,
      },
    };
  },
  methods: {
    showData() {
      const path = 'http://localhost:5000/api/stats';
      axios({
        method: 'get',
        url: path,
      })
        .then((response) => {
          this.redirectedUrls = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.showData();
  },
};
</script>
