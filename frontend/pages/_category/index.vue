<template>
  <div class="main">
  <div class="cards-container">
    <div v-for="category in filterByCategories" :key="category.id">
        <card :link="`${category.category.slug.toLowerCase()}/${category.id}`" :data-image="getThumbler(category.id)">
          <h3 slot="category">{{ category.category.name }}</h3>
          <h1 slot="header">{{ category.title }}</h1>
          <p slot="content">{{ category.description }}</p>
        </card>
    </div>
  </div>
  <div class="nav-buttons">
      <NavigationButton back="true"/>
  </div>
  </div>
</template>
       
<script>
export default {
  //transition: 'slide-fade',
  data(){
    return {}
  },
  async asyncData({ $axios,params }) {
    const slug = params.category
    const data = await $axios.$get('api/v1/projects/')
    console.log(slug)
    return { data, slug }
  },
  mounted(){
    this.getThumbler()
  },
  computed: {
    filterByCategories(){
      return this.data.filter( post => post.category.slug.toLowerCase() === this.slug.toLowerCase())
    }
  },
  methods: {
    getThumbler(id){
      for(let item in this.data){
        if(this.data[item].images.length && this.data[item].id === id){
          return this.data[item].images[0].image.medium_square_crop
        }
      }
    }
  }
}
</script>

<style scoped>
.nav-buttons {
  padding: 1rem 0 2rem 0;

  text-align: center;
}
</style>