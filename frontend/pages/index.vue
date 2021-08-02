<template>
  <div>
  <div class="cards-container">

    <card v-for="category in categories" :key="category.id" :link="`${category.slug}`" data-image="">
      <h1 slot="header">{{ category.header }}</h1>
      <p slot="content">{{ category.content }}</p>
    </card>

  </div>
  
  <h1 class="title" style="padding-top: 50px;">Im@payam.space</h1>
  </div>
</template>

<script>
export default {
   head() {
    return {
      script: [{ src: 'https://identity.netlify.com/v1/netlify-identity-widget.js' }],
    };
  },
  // transition: 'slide-fade',
  data(){
    return {
      categories: [
        { 'header': 'Art', 'content': 'learn about my most recent Art projects, Installations, Photography, Design and Music...' ,'slug':'art'},
        { 'header':'Web', 'content':'Full-Stack Web development is probably something that Im most passionate about, here you can find my most recent works + codes ', 'slug':'web'},
        { 'header': 'NFT', 'content': 'Do you love Blockchain? how about computer generated Arts? well here you can Buy, Mint and Sell Arts as NFTs, Click to get started!', 'slug':'nft' },
        { 'header': 'Experiance', 'content': 'Do you love Blockchain? how about computer generated Arts? well here you can Buy, Mint and Sell Arts as NFTs, Click to get started!', 'slug':'experiance' },
        { 'header': 'Installation', 'content': 'Do you love Blockchain? how about computer generated Arts? well here you can Buy, Mint and Sell Arts as NFTs, Click to get started!', 'slug':'installation' },
        { 'header': 'Whoami', 'content': 'Thanks for visiting my Page! Im Payam Saremi, I have created this website to get to know people who are interested in my work, want to know more about me? Y/n', 'slug':'whoami' },
      ]
    }
  }

}
</script>

<style>

</style>