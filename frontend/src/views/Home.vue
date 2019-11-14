<template>
  <div class="home">
    <img alt="Vue logo" width="200" height="200" src="../assets/logo2.jpg">
    <h1 class="cover-heading"> URL Shortner</h1>
    <form @submit.prevent="handleUrl">
      <label>
        <input class="form-control" id="placeholder"
        v-model="longUrl" placeholder="paste your URL here.." />
      </label>
      <button id="short-button" class="btn btn-primary">Make it shorter!</button>
    </form>
    <p>Shortened URL: <a :href="res">{{ res }}</a></p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      longUrl: '',
      res: '',
    };
  },
  methods: {
    handleUrl() {
      const path = 'http://localhost:5000/api/shorten';
      axios({
        method: 'post',
        url: path,
        data: {
          longUrl: this.longUrl,
        },
      })
        .then((response) => {
          this.res = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#short-button {
  margin-left: 3px;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #007bff;
}
</style>
