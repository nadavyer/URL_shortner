<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="URL Shortner"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';

// console.log('Im running');

// const shortenLinkEndpoint = 'http://localhost:5000/api/shorten';
// const shortenLinkRequestOptions = {
//   method: 'post',
// };

// const handleShortenLinkResponse = (response) => {
//   console.log('response', response);
//   response.json().then((result) => {
//     console.log('result', result);
//   })
// };

// fetch(shortenLinkEndpoint, shortenLinkRequestOptions).then(handleShortenLinkResponse);

export default {
  name: 'home',
  components: {
    HelloWorld,
  },
};
</script>
