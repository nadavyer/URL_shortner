<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <!-- <p>
      SMALL TITLE
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>-->
    <form @submit.prevent="handleUrl">
      <label>
        <input type="longUrl" v-model="longUrl" placeholder="paste your URL here.." />
      </label>
      <button>Make it shorter!</button>
    </form>
    <p>Shortened URL: <a :href="res">{{ res }}</a></p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },
  data() {
    return {
      longUrl: '',
      res: '',
    };
  },
  methods: {
    validURL(str) {
      const pattern = new RegExp('^(https?:\\/\\/)?'
      + '((\\d{1,3}\\.){3}\\d{1,3}))'// OR ip (v4) address
      + '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' // port and path
      + '(\\?[;&a-z\\d%_.~+=-]*)?'// query string
      + '(\\#[-a-z\\d_]*)?$', 'i'); // fragment locator
      return !!pattern.test(str);
    },
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
          // console.log(response.data);
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
  color: #42b983;
}
</style>
