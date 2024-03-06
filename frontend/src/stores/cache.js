import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCacheStore = defineStore('cache', () => {
  const data = ref([])

  function addToCache(items) {
    data.value.push(...items)
  }
  function popFromCache() {
    return data.value.pop();
  }
  function clearCache() {
    data.value = [];
  }

  return {data, addToCache, popFromCache, clearCache}
});