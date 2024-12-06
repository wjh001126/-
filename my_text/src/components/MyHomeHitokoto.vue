<template>
    <div class="home-intro">
        <h2>吃西瓜不吐籽</h2>
        <p  v-if="isLoading">{{ loadingMessage }}</p>
        <p  v-else>{{ hitokoto }}</p>
    </div>
</template>

<script>
export default {
    name: 'MyHomeHitokoto',
    data() {
        return {
            hitokoto: '',
            isLoading: true,
            loadingMessage: '加载中...'
        };
    },
    created() {
        this.fetchHitokoto();
    },
    methods: {
        fetchHitokoto() {
        fetch('https://v1.hitokoto.cn')
            .then(res => res.json())
            .then(data => {
            this.hitokoto = data.hitokoto;
            this.isLoading = false;
            })
            .catch(err => {
            console.error(err);
            this.isLoading = false;
            });
        }
    }
};
</script>

<style scoped>

</style>