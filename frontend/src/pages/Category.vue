<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import { onMounted } from 'vue';
import CardList from '../components/CardList.vue';
const route = useRoute();
const id = ref()
const categoryItems = ref([])
const items = ref([])
const localItems = localStorage.getItem("items");
const filteredItems = ref([])
import { computed } from 'vue';
items.value = localItems ? JSON.parse(localItems) : [];
console.log('Items in category')
console.log( items.value)  
const categories = {
  5: 'Формовые свечи',
  1: 'Гипсовые изделия',
  3: 'Интерьерные наборы',
  2: 'Подарочные наборы',
  4: 'Контейнерные свечи'
}
const categoryName = computed(() => {
  return categories[id.value] || 'Категория не найдена'; // Возвращает имя категории или сообщение об ошибке
});
// function filterItemsById(items, targetId) {
//   return items.filter(item => item.Category === targetId);
// }
function findItemsByCategory(itemss, targetCategory) {
  return itemss.filter(item => item.Category === Number(targetCategory));
}
onMounted(() => {
  id.value = route.params.id; // Присваиваем значение к реактивной переменной id
  console.log("Полученный id:", id.value);

  filteredItems.value = findItemsByCategory(items.value, id.value)

});
</script>
<template>
    <h2 class="px-4 lg:px-16 text-3xl font-bold mb-8">{{ categoryName }}</h2>
    <ul
      class="nav__menu"
      id="menu"
      tabindex="-1"
      aria-label="main navigation"
      hidden
    >
      <li class="nav__item"><a href="#" class="nav__link">Home</a></li>
      <li class="nav__item"><a href="#" class="nav__link">Shop</a></li>
      <li class="nav__item"><a href="#" class="nav__link">Blog</a></li>
      <li class="nav__item"><a href="#" class="nav__link">About</a></li>
      <li class="nav__item"><a href="#" class="nav__link">Contact</a></li>
    </ul>
    <div class="lg:mx-16 mx-4">
        <CardList :items="filteredItems" is-favorites /></div>
  </template>
  