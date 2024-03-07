<script setup>
import { VueFlip } from 'vue-flip';
import { ref, watch, computed, onMounted } from 'vue';
import { useCacheStore } from '@/stores/cache';

async function fetchDataFromAPI() {
    // Call your API to fetch 50 elements
    console.log("api request")
    const response = await fetch('/api/random?count=7');
    const data = await response.json();

    // Add fetched data to the cache
    const cacheStore = useCacheStore();
    cacheStore.addToCache(data);
}

function popFromCache() {
    const cacheStore = useCacheStore();
    return cacheStore.popFromCache();
}

function isNearEndOfList() {
    const cacheStore = useCacheStore();
    return cacheStore.data.length < 5; // Adjust the threshold as needed
}

const shouldFetchMore = computed(() => isNearEndOfList());

watch(shouldFetchMore, async () => {
    if (shouldFetchMore) {
        await fetchDataFromAPI();
    }
})

const currentData = ref({})
const currentImage = ref("")
const nextData = ref({})

function handleNext() {
    ;
    let nextImage = nextData.value.image_url;
    setTimeout(() => {
        currentData.value = nextData.value;
        nextData.value = popFromCache();
    }, 250)
}

onMounted(async () => {
    await fetchDataFromAPI();
    currentData.value = popFromCache();
    currentImage.value = currentData.value.image_url;
    nextData.value = popFromCache();
});

</script>

<template>
    <div class="center-screen" style="background-color: #f0f0f0">
        <VueFlip active-click="true" width="40%" height="80%" style="">
            <template v-slot:front>
                <div class="containerfront"
                    style="background-color: #ffffff; height: 100%;box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">

                    <div>
                    </div>

                    <div class="caption">
                        <h3>{{ currentData.id }}</h3>

                        <h3><i>{{ currentData.title }}</i></h3>
                    </div>

                    <div>
                        <h3 style="align-self: flex-end">
                            <a href="https://prout.tech/projects/xkcd-trainer" @click.stop="" target="_blank">
                                <i>?</i>
                            </a>
                        </h3>
                    </div>
                </div>
            </template>

            <template v-slot:back>
                <div class="container"
                    style="background-color: #ffffff; height: 100%; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
                    
                    <div class="caption">
                        <h3>{{ currentData.id }}</h3>
                        <br />
                        <h3><i>{{ currentData.title }}</i></h3>
                    </div>

                    <img class="image" v-bind:src="currentData.image_url" alt="Image">
                    
                    <button @click="handleNext">Next</button>
                </div>
            </template>

        </VueFlip>
    </div>
</template>

<style scoped>
.center-screen {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100%;
}

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 10px;
}

.containerfront {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 10px;
}

.image {
    min-width: 0;
    min-height: 0;
    max-width: 100%;
    padding: 10px;
}

.caption {
    text-align: center;
}
</style>
