<template>
    <div class=" flex h-full pb-2 mt-4 w-full">
      <button
        type="button"
        @click="openModal"
        class="rounded-md mb-4 object-bottom h-10 w-full bg-red-400 px-4 py-2 text-md font-bold text-white hover:bg-black/30 focus:outline-none focus-visible:ring-2 focus-visible:ring-white/75"
      >
        {{ title }}
      </button>
    </div>
    <TransitionRoot appear :show="isOpen" as="template">
      <Dialog as="div" @close="closeModal" class="absolute z-20">
        <TransitionChild
          as="template"
          enter="duration-300 ease-out"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="duration-200 ease-in"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div class="fixed inset-0 bg-black/25" />
        </TransitionChild>
  
        <div class="fixed inset-0 overflow-y-auto">
          <div
            class="flex min-h-full items-center justify-center p-4 text-center"
          >
            <TransitionChild
              as="template"
              enter="duration-300 ease-out"
              enter-from="opacity-0 scale-95"
              enter-to="opacity-100 scale-100"
              leave="duration-200 ease-in"
              leave-from="opacity-100 scale-100"
              leave-to="opacity-0 scale-95"
            >
              <DialogPanel
                class="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all"
              >
                <DialogTitle
                  as="h3"
                  class="text-2xl w-full h-16 gap-10 flex font-medium leading-6 text-gray-900"
                >
                  Введите данные о доставке
                  
                <div class="mt-4 ml-10 ">
                  <button
                    type="button"
                    class="w-10 h-10   inline-flex "
                    @click="closeModal"
                  >
                  <img
          class="opacity-40 hover:opacity-100 cursor-pointer transition"
          src="/close2.svg"
        />
                  </button>
                </div>
                </DialogTitle>
                <form id='deliveryForm'>
                <div class="mb-5">
          <label for="User"
            class="block font-medium mb-1">ФИО</label>
          <input v-model="data.name" type="text" id="User"
            class="w-full p-3 rounded-lg text-base border-[#ffe0e0]" required>
        </div><div class="mb-5">
          <label for="deliveryAddress"
            class="block font-medium mb-1">Адрес доставки</label>
          <input v-model="data.address" type="text" id="deliveryAddress"
            class="w-full p-3 rounded-lg text-base border-[#ffe0e0]" required>
        </div><div class="mb-5">
          <label for="phoneNumber"
            class="block font-medium mb-1">Номер телефона</label>
          <input v-model="data.phoneNumber"  type="text" id="phoneNumber"
            class="w-full p-3 rounded-lg text-base border-[#ffe0e0]" required>
        </div>     <div class="mb-5">
          <label for="emailAddress"
            class="block font-medium mb-1">Электронная почта</label>
          <input v-model="data.email" type="email" id="emailAddress"
            class="w-full p-3 rounded-lg text-base border-[#ffe0e0]" required>
        </div>     <div class="mb-5">
          <label for="deliveryDescription"
            class="block font-medium mb-1">Дополнительные замечания о доставке</label>
          <input v-model="data.description" name="deliveryDescription" type="text" id="deliveryDescription"
            class="w-full p-3 rounded-lg text-base border-[#ffe0e0]" required>
        </div>
                <div class="mt-2">
                  <p class="text-sm text-gray-500">
                    Your payment has been successfully submitted. We’ve sent you
                    an email with all of the details of your order.
                  </p>
                </div>
  
                <div class="mt-4">
                  <button
                    type="submit"
                    class="w-full  inline-flex justify-center rounded-md border border-transparent bg-orange-300 px-4 py-2 text-sm font-medium text-white hover:bg-orange-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-orange-500 focus-visible:ring-offset-2"
                    @click="sendData"
                  >Оформить заказ
                  </button>
                </div></form>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
  </template>
  
  <script setup>
  import { onMounted, reactive, ref } from 'vue'
  import axios from 'axios';
  import {
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogPanel,
    DialogTitle,
  } from '@headlessui/vue'
  const cart = localStorage.getItem("cart")
  const data = reactive({
  name: '',
  phoneNumber: '',
  email: '',
  description: '',
  address: '',
  items: JSON.parse(cart),
  Order_status: 1,

  })

defineProps({
  title: String
})

function sendData(event) {
console.log(cart)
console.log(data)
axios.post(
  'http://localhost:8000/orders/',
  
data,
  {
    headers: {
      'accept': 'application/json',
      'Content-Type': 'application/json'
    }
  }
);
}
const isOpen = ref(false)
  function closeModal() {
    isOpen.value = false
  }
  function openModal() {
    isOpen.value = true
  }
  </script>