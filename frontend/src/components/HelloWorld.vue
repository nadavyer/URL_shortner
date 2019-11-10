<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <!-- <p>
      SMALL TITLE
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>-->
    <form @submit.prevent="handleUrl">
      <label>
        <input type="longUrl" v-model="longUrl" placeholder="pase your long URL here..." />
      </label>

      <button>Make it shorter!</button>
    </form>
    <h3>Essential Links</h3>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },
  data() {
    return {
      longUrl: '',
    };
  },
  methods: {
    handleUrl() {
      console.log(this.longUrl);
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
