<template>
  <div>
    <a @mouseenter.prevent="setLightBox" :href="image.full_size" class="glightbox">
        <figure>
        <img :src="image.medium_square_crop" class="image" />
        </figure>
    </a>
  </div>
</template>

<script>
import GLightbox from 'glightbox'
export default {
    props:['image'],
    data(){
        return{
            lightbox: ''
        }
    },
    methods: {
        setLightBox(){
            this.lightbox = GLightbox({
                touchNavigation: true,
                loop: false,
                openEffect: 'fade',
                closeEffect: 'fade',
                slideEffect: 'slide'
            })
        },
        toggleLightBox(){
            this.lightbox.open()
        }
  }
}
</script>

<style>
.image {
    padding: 1rem;
    width: 300px;
    height: 300px;
    object-fit: cover;
}
@media only screen and (max-width: 750px) {
 .image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
}

/* overwriting the initial overflow */
/* .glightbox-open {
    overflow:hidden
} */
</style>