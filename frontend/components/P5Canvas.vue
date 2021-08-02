<template>
<div>
    <div id="p5Canvas"></div>
</div>
</template>

<script>
// import P5 from 'p5'
export default {
    name:'P5Canvas',
    data () {
    return {
        width: 0,
        height: 0,
        xoff:0
    }
    },
    async mounted () {
        const { default: P5 } = await import('p5')

        const sketch = (s) => {
            s.setup = () => {
                this.width = window.innerWidth
                this.height = window.innerHeight
                s.createCanvas(this.width, this.height)
                
            }
            s.draw = () => {
                s.noLoop()
                let randomW = s.map(s.noise(this.xoff), 0, 1, 0, this.width)
                this.xoff += 0.01
                s.background(33, 33, 33)
                // s.ellipse(randomW, this.height / 2, 50, 50);
                for(let i = 0; i < 5; i += 0.01){
                    let peril = s.map(s.noise(i), 0, 1, 0, this.width)
                    i += 0.01
                    s.ellipse(peril, this.height / 2, 50, 50);
                }
            }
        }
        // eslint-disable-next-line no-unused-vars
        const P5Canvas = new P5(sketch, 'p5Canvas')
  }
}
</script>

<style>

</style>