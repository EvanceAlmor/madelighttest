<script setup>
import { ref,reactive, provide, watch, computed, onMounted } from "vue";
import Drawer from "./components/Drawer.vue";
import DrawerNav from "./components/DrawerNav.vue";
import axios from "axios";
const cart = ref([]);
const favorites = ref([]);
const drawerOpen = ref(false);
const items = ref([])
const dataitems = ref([])
const totalPrice = computed(() => {return cart.value.reduce((total, item) => total + (item.price * item.quantity), 0);});
const vatPrice = computed(() => Math.round((totalPrice.value * 5) / 100));
const filterProducts = (products) => {
  return products
    .filter((product) => {
    const matchesQuery = filters.searchQuery
      ? product.title.toLowerCase().includes(filters.searchQuery.toLowerCase())
      : true;
    console.log("Matches search query:", matchesQuery, product.title);
    return matchesQuery;
  })
  .filter((product) => {
    const matchesColor = filters.colors.length
      ? filters.colors.includes(product.Color.toLowerCase())
      : true;
    console.log("Matches color:", matchesColor, product.Color);
    return matchesColor;
  })
  .filter((product) => {
      return filters.categories.length
        ? filters.categories.includes(product.Category.toString())
        : true;
    })
  .filter((product) => {
      return filters.sizes.length
        ? filters.sizes.some(size => size.toLowerCase() === product.size.toLowerCase())
        : true;
    })
    .sort((a, b) => {
      if (filters.sortBy === "title") {
        return a.title.localeCompare(b.title);
      } else if (filters.sortBy === "price") {
        return a.price - b.price;
      } else if (filters.sortBy === "unPrice") {
        return b.price - a.price;
      }
      return 0;
    });
};
const filters = reactive({
  sortBy: "title",
  searchQuery: "",
  colors: ['white','beige','blue','brown','green', 'purple'],
  categories: ['1','2','3', '4','5'],
  sizes: ['2L','6L','12L','18L','20L','40L'],
});
const fetchItems = async () => {
  try {
    const params = {
      sortBy: filters.sortBy,
    };
    const { data } = await axios.get(
      `http://192.168.0.32:8000/products`,
    );
      console.log(data)
      
    items.value = data.map((obj) => ({
      ...obj,
      isFavorite: false,
      isAdded: false,
    }));

  } catch (err) {
    console.log(err);
  }
};
const closeDrawer = () => {
  drawerOpen.value = false;
};

const openDrawer = () => {
  drawerOpen.value = true;
};

const addToCart = (item) => {
  const cartitem = {
    ...item,
    quantity: 1
  }
  cart.value.push(cartitem);
  item.isAdded = true;
  
};
const addToFavorite = (item) => {
  // Проверяем, что favorites существует и инициализировано
  if (!favorites.value) {
    favorites.value = []; // Инициализация как пустого массива
  }

  // Проверяем, есть ли элемент уже в избранном
  const isAlreadyFavorite = favorites.value.some((favItem) => favItem.id === item.id);

  if (!isAlreadyFavorite) {
    // Если элемента нет в избранном, добавляем его
    favorites.value.push(item);
    item.isFavorite = true; // Устанавливаем флаг
  } else {
    console.log('Item is already in favorites');
  }
};

const removeFromFavorites = (item) => {
  favorites.value.splice(favorites.value.indexOf(item), 1);
  item.isFavorite = false;
};
const removeFromCart = (item) => {
  cart.value.splice(cart.value.indexOf(item), 1);
  item.isAdded = false;
};

onMounted(async () => {
  const localCart = localStorage.getItem("cart");
  cart.value = localCart ? JSON.parse(localCart) : [];
  const localFavorites = localStorage.getItem("favorites");
  favorites.value = localCart ? JSON.parse(localFavorites) : [];
  const localItems = localStorage.getItem('items');
  items.value = localItems ? JSON.parse(localItems) : [];
  await fetchItems()
  
  console.log(items.value)
  items.value = items.value.map((item) => ({
    ...item,
    isAdded: cart.value.some((cartItem) => cartItem.id === item.id),
  }));
  items.value = items.value.map((item) => ({
    ...item,
    isFavorite: Array.isArray(favorites.value) && favorites.value.some((FavItem) => FavItem.id === item.id),

}));
dataitems.value = items.value
provide('items', items)
provide('dataitems', dataitems)
});
watch(
  items,
  () => {
    localStorage.setItem('items', JSON.stringify(items.value));
  }
)
watch(
  () => [filters.colors, filters.sortBy,filters.searchQuery, filters.categories, filters.sizes],
  () => {
    console.log("Filters updated:", filters);
    dataitems.value = filterProducts(items.value);
    console.log('filtered items', dataitems.value)
  },
  { deep: true }
);

watch(
  cart,
  () => {
    localStorage.setItem("cart", JSON.stringify(cart.value));
  },
  { deep: true }
);
watch(
  favorites,
  () => {
        localStorage.setItem("favorites", JSON.stringify(favorites.value));
    },
  { deep: true }
  
)
provide('filters', filters)
provide('favorites', {
  favorites,
  addToFavorite,
  removeFromFavorites,
})
provide('dataitems', dataitems)
provide("items", items)
provide("cart", {
  cart,
  closeDrawer,
  openDrawer,
  addToCart,
  removeFromCart,
});


/* Корзина (END) */
</script>

<template>
  <Drawer v-if="drawerOpen" :total-price="totalPrice" :vat-price="vatPrice" />

  <DrawerNav :total-price="totalPrice" @open-drawer="openDrawer" />
  <div><router-view></router-view></div>
  
</template>
