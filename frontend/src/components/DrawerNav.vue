<script setup>
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
} from "@headlessui/vue";
import { Bars3Icon, BellIcon, XMarkIcon } from "@heroicons/vue/24/outline";
const emit = defineEmits(["openDrawer"]);
defineProps({
  totalPrice: Number,
});
</script>
<template>
  <Disclosure as="nav" class="bg-white-800" v-slot="{ open }">
    <div class="py-6 px-2 lg:px-40 w-full">
      <div class="relative flex h-16 items-center justify-between w-full">
        <div class="absolute inset-y-0 left-0 flex items-center md:hidden">
          <!-- Mobile menu button-->
          <DisclosureButton
            class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-white-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
          >
            <span class="absolute -inset-0.5" />
            <span class="sr-only">Open main menu</span>
            <img
              v-if="!open"
              src="/menu.svg"
              class="transition opacity-50 hover:opacity-80 block h-6 w-6"
              aria-hidden="true"
            />
            <img
              v-else
              src="/close2.svg"
              class="transition opacity-50 hover:opacity-80 block h-6 w-6"
              aria-hidden="true"
            />
          </DisclosureButton>
        </div>
        <div
          class="flex flex-1 h-16 py-2 items-center justify-center md:items-stretch md:justify-start w-full"
        >
          <router-link to="/">
            <li class="flex items-center gap-2 sm:gap-4">
              <img class="w-10" src="/logo2.png" alt="Your Company" />
              <div>
                <h2 class="text-xl font-bold uppercase">Madelight</h2>
                <p class="text-slate-400">Магазин для вашего дома</p>
              </div>
            </li></router-link
          >
          <div
            class="absolute inset-y-0 right-0 hidden md:ml-6 md:block right-0 py-4"
          >
            <ul class="flex items-center gap-10 mr-4">
              <router-link to="/cart">
              <li
                
                class="flex items-center cursor-pointer gap-3 text-gray-500 hover:text-black"
              >
                <img class="fill-gray-800" src="/cart.svg" alt="Cart" />
                <b>{{ totalPrice }} руб.</b>
              </li>
            </router-link>
              <router-link to="/favorites">
                <li
                  class="flex items-center cursor-pointer gap-3 text-gray-500 hover:text-black"
                >
                  <img src="/heart.svg" alt="Cart" />
                  <span>Закладки</span>
                </li>
              </router-link>
              <router-link to="/order">
              <li 
                class="flex items-center cursor-pointer gap-3 text-gray-500 hover:text-black"
              >
                <img src="/profile.svg" alt="Cart" />
                <span>Заказы</span>
              </li></router-link>
            </ul>
          </div>
        </div>
        <div
          class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0"
        ></div>
      </div>
    </div>

    <DisclosurePanel class="md:hidden"
      ><ul class="flex items-center gap-10">
        <div class="space-y-1 px-2 pb-3 pt-2">
          <router-link to="/cart">
              <li
                
                class="flex items-center cursor-pointer gap-3 text-gray-500 hover:text-black"
              >
                <img class="fill-gray-800" src="/cart.svg" alt="Cart" />
                <b>{{ totalPrice }} руб.</b>
              </li>
            </router-link>
          <router-link to="/favorites">
            <li
              class="flex items-center cursor-pointer gap-3 text-gray-500 hover:text-black"
            >
              <img src="/heart.svg" alt="Cart" />
              <span>Закладки</span>
            </li>
          </router-link>
          <router-link to="/order">
              <li 
                class="flex items-center cursor-pointer gap-3 text-gray-500 hover:text-black"
              >
                <img src="/profile.svg" alt="Cart" />
                <span>Заказы</span>
              </li></router-link>
        </div>
      </ul>
    </DisclosurePanel>
  </Disclosure>
</template>
