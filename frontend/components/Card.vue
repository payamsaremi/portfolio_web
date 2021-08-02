<template>
  <div class="card-wrap"
      @mousemove="handleMouseMove"
      @mouseenter="handleMouseEnter"
      @mouseleave="handleMouseLeave"
      ref="card">
      <nuxt-link :to="link">
        <div class="card"
        :style="cardStyle">
        <div class="card-bg" :style="[cardBgTransform, cardBgImage]"></div>
        <div class="card-info">
          <slot name="category"></slot>
          <slot name="header"></slot>
          <slot name="content"></slot>
        </div>
      </div>
      </nuxt-link>
  </div>
</template>

<script scoped>
export default {
     mounted() {
    this.width = this.$refs.card.offsetWidth;
    this.height = this.$refs.card.offsetHeight;
  },
  props: ["dataImage","link"],
  data: () => ({
    width: 0,
    height: 0,
    mouseX: 0,
    mouseY: 0,
    mouseLeaveDelay: null
  }),

  computed: {
    mousePX() {
      return this.mouseX / this.width;
    },
    mousePY() {
      return this.mouseY / this.height;
    },
    cardStyle() {
      const rX = this.mousePX * 20;
      const rY = this.mousePY * -20;
      return {
        transform: `rotateY(${rX}deg) rotateX(${rY}deg)`
      };
    },
    cardBgTransform() {
      const tX = this.mousePX * -40;
      const tY = this.mousePY * -40;
      return {
        transform: `translateX(${tX}px) translateY(${tY}px)`
      };
    },
    cardBgImage() {
      return {
        backgroundImage: `url(${this.dataImage})`
      };
    }
  },

  methods: {
    handleMouseMove(e) {
      try {
        this.mouseX = e.pageX - this.$refs.card.offsetLeft - this.width / 2;
        this.mouseY = e.pageY - this.$refs.card.offsetTop - this.height / 2;
      } catch {
        console.log(e)
      }
    },
    handleMouseEnter() {
      clearTimeout(this.mouseLeaveDelay);
    },
    handleMouseLeave() {
      this.mouseLeaveDelay = setTimeout(() => {
        this.mouseX = 0;
        this.mouseY = 0;
      }, 1000);
    }
  }
}
</script>

<style>

p {
  line-height: 1.5em;
}

h1 + p, p + p {
  margin-top: 20px;
}

.card-wrap {
  margin: 10px;
  transform: perspective(1200px);
  transform-style: preserve-3d;
  cursor: pointer;
}
.card-wrap:hover .card-info {
  transform: translateY(0);
}
.card-wrap:hover .card-info p {
  opacity: 1;
}
.card-wrap:hover .card-info, .card-wrap:hover .card-info p {
  transition: 0.6s cubic-bezier(0.23, 1, 0.32, 1);
}
.card-wrap:hover .card-info:after {
  transition: 3s cubic-bezier(0.23, 1, 0.32, 1);
  opacity: 1;
  transform: translateY(0);
}
.card-wrap:hover .card-bg {
  transition: 0.5s cubic-bezier(0.23, 1, 0.32, 1), opacity 4s cubic-bezier(0.23, 1, 0.32, 1);
  opacity: 0.8;
}
.card-wrap:hover .card {
  transition: 0.5s cubic-bezier(0.23, 1, 0.32, 1);
  box-shadow: none;
}
.card-wrap:active .card {
  box-shadow: rgba(43, 43, 43, 0.66) 0 30px 60px 0, inset rgb(67, 67, 67) 0 0 0 5px, inset rgba(255, 255, 255, 0.4) 0 0 0 6px;
}

.card-bg {
  opacity: 0.5;
  position: absolute;
  top: -40px;
  left: -40px;
  width: 120%;
  height: 120%;
  padding: 0;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  transition: 0.8s cubic-bezier(0.445, 0.05, 0.55, 0.95), opacity 1s 0.8s cubic-bezier(0.445, 0.05, 0.55, 0.95);
  pointer-events: none;
}

.card-info {
  padding: 20px;
  position: absolute;
  bottom: 0;
  color: #fff;
  transform: translateY(40%);
  transition: 0.6s  cubic-bezier(0.215, 0.61, 0.355, 1);
}
.card-info p {
  opacity: 0;
  text-shadow: black 0 2px 3px;
  transition: 0.6s  cubic-bezier(0.215, 0.61, 0.355, 1);
}
.card-info * {
  position: relative;
  z-index: 1;
}
.card-info:after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  z-index: 0;
  width: 100%;
  height: 100%;
  background-image: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.6) 100%);
  background-blend-mode: overlay;
  opacity: 0;
  transform: translateY(100%);
  transition: 5s 1s cubic-bezier(0.445, 0.05, 0.55, 0.95);
}
.card-info h1 {
  font-family: "Raleway", sans-serif;
  font-size: 36px;
  font-weight: 700;
  text-shadow: rgba(0, 0, 0, 0.5) 0 10px 10px;
}

</style>