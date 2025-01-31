<script setup>
import axios from 'axios'

var data = {
username: '',
password: '',
}

const headers = {
"Content-Type": "application/x-www-form-urlencoded",
"accept": "application/x-www-form-urlencoded"
}

const config = {withCredentials: true,
headers: headers
}

function sendData(event) {
axios.post("http://localhost:8000/auth/login", data, config)
.then(response => {
console.log(response);
})
.catch(error => {
if (error.response.statusText){
  
}
});

} 
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";

axios.get('http://localhost:8000/orders/authenticated-route')
const name = 'bonds'

axios.get('http://localhost/users/me', {
  headers: {
    'accept': 'application/json'
  },
  withCredentials: true // Включаем передачу куки
})

function getEmail(event) {console.log(axios.get('http://localhost:8000/users/me', {
  headers: {
    'accept': 'application/json'
  },
  withCredentials: true // Включаем передачу куки
}))
} 
</script>
<template>
    <!--
      This example requires updating your template:
  
      ```
      <html class="h-full bg-white">
      <body class="h-full">
      ```
    -->
    <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
       
        <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Войдите в учетную запись</h2>
    
      </div>
      
      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <div class="space-y-6">
          <div>
            <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email адрес</label>
            <div class="mt-2">
              <input v-model="data.username" id="email" name="email" type="email" autocomplete="email" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>
  
          <div>
            <div class="flex items-center justify-between">
              <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Пароль</label>
              <div class="text-sm">
                <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Забыли пароль?</a>
              </div>
            </div>
            <div class="mt-2">
              <input v-model="data.password" id="password" name="password" type="password" autocomplete="current-password" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>
  
          <div>
            <button @click='sendData' class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Войти</button>
            <button @click='getEmail' class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">getemali</button>
      
          </div>

  
        <p class="mt-10 text-center text-sm text-gray-500">
          Нет учетной записи?
          {{ ' ' }}
          <router-link to="/register">
          <a href="#" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Создайте ее!</a></router-link>
        </p>
      </div>
    </div>
    </div>
  </template>