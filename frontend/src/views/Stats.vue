<template>
  <div class="stats">
    <h3>Total redirects: {{ redirectedUrls }}</h3>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'Stats',
  data() {
    return {
      redirectedUrls: '',
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
