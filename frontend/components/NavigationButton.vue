<template>
    <div>
        <a v-if="back" @click="$router.go(-1)">
          <c-icon  class="nav-button" name="chevron-left" size="40px" color="white" />
        </a>
        <a v-if="forward" @click="$router.go(1)">
          <c-icon class="nav-button" name="chevron-right" size="40px" color="white" />
        </a>
    </div>
</template>

<script>
export default {
    props:['back','forward']
}
</script>

<style scoped>
.nav-button {
  background: rgb(0, 0, 0);
  border: none;
  box-shadow: rgba(255, 255, 255, 0.15) 0 10px 30px 0;
  transition: 0.2s cubic-bezier(0.445, 0.05, 0.55, 0.95);
  border-radius: 1rem 1rem 1rem 1rem;
  cursor: pointer;
}
.nav-button:hover {
  border: none;
  box-shadow: rgba(255, 255, 255, 0.36) 0 10px 30px 0;
}

</style>
