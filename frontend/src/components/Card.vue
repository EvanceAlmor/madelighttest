<script setup>
import { stringify } from 'qs';

defineProps({
  id: Number,
  title: String,
  imageUrl: String,
  price: Number,
  isFavorite: Boolean,
  isAdded: Boolean,
  onClickFavorite: Function,
  onClickAdd: Function,
});

</script>

<template>
    <div
      class="bg-white aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md lg:aspect-none group-hover:opacity-95 relative border border-slate-100 rounded-3xl  cursor-pointer transition hover:-translate-y-2 hover:shadow-xl"
    >
      <div class="w-full bg-white">
        
        <img
          v-if="onClickFavorite"
          :src="!isFavorite ? '/like-1.svg' : '/like-2.svg'"
          alt="Like 1"
          class="absolute top-2 left-2"
          @click="onClickFavorite"
        />

        <router-link :to="{ name: 'product', params: { id } }">
        <img class="w-full h-auto items-stretch" :src="imageUrl" alt="Sneaker" />
        </router-link>
        <p class="mx-2 mt-2">{{ title }}</p>

        <div class="flex justify-between p-2 md:py-6">
          <router-link :to="{ name: 'product', params: { id } }">
          <div class="flex flex-col">
            <span class="text-slate-400">Цена:</span>
            <b>{{ price }} руб.</b>
          </div>
          </router-link>
          <img
            v-if="onClickAdd"
            @click="onClickAdd"
            :src="!isAdded ? '/plus.svg' : '/checked.svg'"
            alt="Plus"
          />
        </div>
      </div></div>
</template>
