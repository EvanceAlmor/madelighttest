<!--
  This example requires some changes to your config:
  
  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  }
  ```
-->
<template>
  <Delivery/>
    <div class="bg-white w-full p-4">
      <div>
        <!-- Mobile filter dialog -->
        <TransitionRoot as="template" :show="mobileFiltersOpen">
          <Dialog class="relative z-40 lg:hidden" @close="mobileFiltersOpen = false">
            <TransitionChild as="template" enter="transition-opacity ease-linear duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="transition-opacity ease-linear duration-300" leave-from="opacity-100" leave-to="opacity-0">
              <div class="fixed inset-0 bg-black bg-opacity-25" />
            </TransitionChild>
  
            <div class="fixed inset-0 z-40 flex">
              <TransitionChild as="template" enter="transition ease-in-out duration-300 transform" enter-from="translate-x-full" enter-to="translate-x-0" leave="transition ease-in-out duration-300 transform" leave-from="translate-x-0" leave-to="translate-x-full">
                <DialogPanel class="relative ml-auto flex h-full w-full max-w-xs flex-col overflow-y-auto bg-white py-4 pb-12 shadow-xl">
                  <div class="flex items-center justify-between px-4">
                    <h2 class="text-lg font-medium text-gray-900">Filters</h2>
                    <button type="button" class="-mr-2 flex h-10 w-10 items-center justify-center rounded-md bg-white p-2 text-gray-400" @click="mobileFiltersOpen = false">
                      <span class="sr-only">Close menu</span>
                      <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                    </button>
                  </div>
  
                  <!-- Filters -->
                  <form class="mt-4 border-t border-gray-200">
                    <h3 class="sr-only">Categories</h3>
                    
                    <ul role="list" class="px-2 py-3 font-medium text-gray-900">
                      <li v-for="category in subCategories" :key="category.name">
                 
                        <a :href="category.href" class="block px-2 py-3">{{ category.name }}</a>
                      </li>
                    </ul>
                    <div>
      <div
        v-for="section in filtersColor"
        :key="section.id"
        class="border-t border-gray-200 px-4 py-6"
      >
        <h3 class="-mx-2 -my-3 flow-root">
          <button
            class="flex w-full items-center justify-between bg-white px-2 py-3 text-gray-400 hover:text-gray-500"
          >
            <span class="font-medium text-gray-900">{{ section.name }} </span>
          </button>
        </h3>
        <div class="pt-6">
          <div class="space-y-6">
            <div
              v-for="(option, optionIdx) in section.options"
              :key="option.value"
              class="flex items-center"
            >
              <input
                type="checkbox"
                :id="`filter-${section.id}-${optionIdx}`"
                v-model="option.checked"
                class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
              />
              <label
                :for="`filter-${section.id}-${optionIdx}`"
                class="ml-3 min-w-0 flex-1 text-gray-500"
              >
                {{ option.label }}
              </label>
            </div>
          </div>
        </div>
      </div>
                    </div>
                  </form>
                </DialogPanel>
              </TransitionChild>
            </div>
          </Dialog>
        </TransitionRoot>
       <input
         @input="onChangeSearchInput"
         class="border rounded-md w-full outline-none focus:border-gray-400"
         type="text"
         placeholder="Поиск..."
       />
        <main class=" w-full sm:px-6 ">
          <div class="flex items-baseline justify-between border-b border-gray-200 pb-6 pt-4">
            <h1 class="text-4xl font-bold tracking-tight text-gray-900">Товары</h1>
            <div class="bg-white flex justify-between items-center">
  

    
  </div>
  <!-- <div class="md:hidden w-full">
    <li class="flex list-none">
        <img class="w-8" src="/filter.svg" alt="" />
        <b class="pl-2 text-xl m-auto">Фильтры</b>
      </li>
    <div class="w-full relative">
      <img class="absolute left-4 top-7" src="/search.svg" />
      <input
        @input="onChangeSearchInput"
        class="w-full border mt-4 rounded-md py-2 pl-11 pr-4 outline-none focus:border-gray-400"
        type="text"
        placeholder="Поиск..."
      />
    </div>
  </div> -->
            <div class="flex items-center">
                      <select 
                          @change="onChangeSelect" class="rounded-xl w-12">
                          <option class="rounded-xl" value="title">По названию</option>
                          <option value="price">По цене (дешевые)</option>
                          <option value="unPrice">По цене (дорогие)</option>
                      </select>
                
  
              
              <button type="button" class="-m-2 ml-4 p-2 text-gray-400 hover:text-gray-500 sm:ml-6 lg:hidden" @click="mobileFiltersOpen = true">
                <span class="sr-only">Filters</span>
                <FunnelIcon class="h-5 w-5" aria-hidden="true" />
              </button>
            </div>
          </div>
  
          <section aria-labelledby="products-heading" class="pb-24 pt-6">
            <h2 id="products-heading" class="sr-only">Products</h2>
  
            <div class="grid grid-cols-1 gap-x-8 gap-y-10 lg:grid-cols-4">
              <!-- Filters -->
              <form class="hidden lg:block">
                <h3 class="sr-only">Категории</h3>
                <ul role="list" class="space-y-4 border-b border-gray-200 pb-6 text-sm font-medium text-gray-900">
                  <li v-for="category in subCategories" :key="category.name">
                    <a :href="category.href">{{ category.name }}</a>
                  </li>
                </ul>
  
                <Disclosure as="div" v-for="section in filtersColor" :key="section.id" class="border-b border-gray-200 py-6" >
                  <h3 class="-my-3 flow-root">
                    <DisclosureButton class="flex w-full items-center justify-between bg-white py-3 text-sm text-gray-400 hover:text-gray-500">
                      <span class="font-medium text-gray-900">{{ section.name }}</span>
                      <span class="ml-6 flex items-center">
                      </span>
                    </DisclosureButton>
                  </h3>
                  <DisclosurePanel class="pt-6">
                    <div class="space-y-4">
                      <div
              v-for="(option, optionIdx) in section.options"
              :key="option.value"
              class="flex items-center"
            >
              <input
                type="checkbox"
                :id="`filter-${section.id}-${optionIdx}`"
                v-model="option.checked"
                class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
              />
              <label
                :for="`filter-${section.id}-${optionIdx}`"
                class="ml-3 min-w-0 flex-1 text-gray-500"
              >
                {{ option.label }}
              </label>
            </div>
                    </div>
                  </DisclosurePanel>
                </Disclosure>
              </form>
  
              <!-- Product grid -->
              <div class="lg:col-span-3">
              <div class="mt-10">
    <CardList
      :items="dataitems"
      @add-to-favorite="onClickFavPlus"
      @add-to-cart="onClickAddPlus"
    />
  </div>
              </div>
            </div>
          </section>
        </main>
      </div>
    </div>
  </template>
  
  <script setup>
  import Multiselect from "@vueform/multiselect";
  import { watch, ref, onMounted } from "vue";
import debounce from "lodash.debounce";
import { inject } from "vue";
import CardList from "../components/CardList.vue";
import Delivery from "../components/Delivery.vue"
const { cart, addToCart, removeFromCart } = inject("cart");
const dataitems = inject('dataitems');

const items = inject('items'); 
console.log('iteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeem',items.value)// Убедитесь, что 'items' предоставляется родительским компонентом
const filters = inject('filters')
console.log(filters.sortBy)
const { favorites, addToFavorite, removeFromFavorites } = inject("favorites");
const onClickAddPlus = (item) => {
  if (!item.isAdded) {
    addToCart(item);
  } else {
    removeFromCart(item);
  }
};

const onClickFavPlus = (item) => {
  if (!item.isFavorite) {
    addToFavorite(item);
  } else {
    removeFromFavorites(item);
  }
};

const onChangeSelect = (event) => {
  
  filters.sortBy = event.target.value;
  console.log(filters.sortBy)

};

const onChangeSearchInput = (event) => {
  filters.searchQuery = event.target.value;
  console.log('Search query:', filters.searchQuery);
  filterProducts();
};


// Обработка изменений в корзине
watch(cart, () => {
  try {
    items.value = items.value.map((item) => ({
      ...item,
      isAdded: cart.value.some((cartItem) => cartItem.id === item.id), // Присваиваем isAdded в зависимости от наличия в cart
    }));
  } catch (err) {
    console.log(err);
  }
});
watch(favorites, () => {
  try {
  items.value = items.value.map((item) => ({
    ...item,
    isFavorite: favorites.value.some((favItem) => favItem.id === item.id), // Обновляем isFavorite в зависимости от favorites
  }));
  } catch (err) {
    console.log(err)
  }
});
  

// Первоначальная инициализация
onMounted(async () => {
  try {
    const localCart = localStorage.getItem("cart");
    cart.value = localCart ? JSON.parse(localCart) : [];


    items.value = items.value.map((item) => ({
      ...item,
      isAdded: cart.value.some((cartItem) => cartItem.id === item.id), // Задаем isAdded при инициализации
      isFavorite: favorites.value.some((favItem) => favItem.id === item.id), // Убедитесь, что есть isFavorite
    }));
  } catch (err) {
    console.log(err);
  }
});


  import {
    Dialog,
    DialogPanel,
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
    TransitionChild,
    TransitionRoot,
  } from '@headlessui/vue'
  import { XMarkIcon } from '@heroicons/vue/24/outline'
  import { FunnelIcon, MinusIcon, PlusIcon, Squares2X2Icon } from '@heroicons/vue/20/solid'
  
  const sortOptions = [
    { name: 'По названию', value: 'name' },
    { name: 'Сначала дешевые', value: 'price' },
    { name: 'Сначало дорогие', value: '-price' },
  ]
 
  const subCategories = [
    { name: 'Кросовки спортивные', href: '/category/5' },
    { name: 'Кросовки туристические', href: '/category/4' },
    { name: 'Повседневные кросовки', href: '/category/1' },
    { name: 'Универсальные кросовки', href: '/category/3' },
    { name: 'Акции', href: '/category/2' },
  ]

  const filteredProducts = ref([...items.value]);
  const filterProducts = () => {
    const selectedColors = filtersColor.value
  ?.find((filter) => filter.id === "Color")
  ?.options?.filter((option) => option.checked)
  ?.map((option) => option.value) || [];


  filteredProducts.value = items.value.filter((product) => {
    return (
      (selectedColors.length === 0 || selectedColors.includes(product.color))
    );
  });
};
const filtersColor = ref([
  {
    id: 'color',
    name: 'Цвета',
    options: [
      { value: 'white', label: 'White', checked: false },
      { value: 'beige', label: 'Beige', checked: false },
      { value: 'blue', label: 'Blue', checked: false },
      { value: 'brown', label: 'Brown', checked: false },
      { value: 'green', label: 'Green', checked: false },
      { value: 'purple', label: 'Purple', checked: false },
    ],
  },
  {
    id: 'category',
    name: 'Категории',
    options: [
      { value: '5', label: 'Свечи формовые', checked: false },
      { value: '4', label: 'Свечи контейнерные', checked: false },
      { value: '1', label: 'Гипсовые изделия', checked: false },
      { value: '3', label: 'Интерьерные наборы', checked: false },
      { value: '2', label: 'Подарочные наборы', checked: false },
    ],
  },
  {
    id: 'size',
    name: 'Размеры',
    options: [
      { value: '2l', label: '2L', checked: false },
      { value: '6l', label: '6L', checked: false },
      { value: '12l', label: '12L', checked: false },
      { value: '18l', label: '18L', checked: false },
      { value: '20l', label: '20L', checked: false },
      { value: '40l', label: '40L', checked: false },
    ],
  },
])
  console.log('Filters colors:', filters.colors);
console.log('Filters categories:', filters.categories);
console.log('Filters sizes:', filters.sizes);
console.log('filtersColor:', filtersColor.value);


const applyFiltersToCheckboxes = () => {
  filtersColor.value.forEach((filter) => {
    if (filter.id === 'color') {
      filter.options.forEach((option) => {
        // Приведение к нижнему регистру для `value` и сравнение с `filters.colors`
        option.checked = filters.colors.some(
          (color) => color.toLowerCase() === option.value.toLowerCase()
        );
      });
    } else if (filter.id === 'category') {
      filter.options.forEach((option) => {
        // Сравнение без преобразования
        option.checked = filters.categories.includes(option.value);
      });
    } else if (filter.id === 'size') {
      filter.options.forEach((option) => {
        // Приведение `label` к верхнему регистру для сравнения
        option.checked = filters.sizes.includes(option.label.toUpperCase());
      });
    }
  });
};


// Вызов функции
applyFiltersToCheckboxes();
  watch(filtersColor, filterProducts, { deep: true });
  watch(
  filtersColor,
  (newFiltersColor) => {
    newFiltersColor.forEach((filter) => {
      if (filter.id.toLowerCase() === 'color') {
        // Обновляем colors
        filters.colors = filter.options
          .filter((option) => option.checked)
          .map((option) => option.value);
      } else if (filter.id.toLowerCase() === 'category') {
        // Обновляем categories
        filters.categories = filter.options
          .filter((option) => option.checked)
          .map((option) => option.value);
      } else if (filter.id.toLowerCase() === 'size') {
        // Обновляем sizes
        filters.sizes = filter.options
          .filter((option) => option.checked)
          .map((option) => option.value);
      }
    });

    console.log('Updated filters:', filters);
  },
  { deep: true }
);
watch(() => filters.searchQuery, filterProducts);

  const mobileFiltersOpen = ref(false)
  </script>