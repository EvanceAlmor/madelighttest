<template>
  <div class="container mx-auto my-5 bg-white rounded-2xl  overflow-hidden">
    <div class="search-box px-5 pb-5 border-b">
      <input
        type="text"
        v-model="searchTerm"
        placeholder="Поиск заказов по коду"
        @keydown.enter="searchOrders"
        class="w-full pb-3 px-5 border-2 border-gray-300 rounded-full focus:outline-none focus:ring-2 focus:ring-red-400"
      />
    </div>
    
    <div class="order-list p-5">
      <div></div>
      <div v-if="orders.length === undefined || orders.length === 0 && searchTerm" class="no-orders text-center text-gray-500 py-10">
        Ничего не найдено.
      </div>
      <div v-for="order in orders" :key="order.id" class="order-item bg-white rounded-lg shadow hover:shadow-lg mb-5 transition transform hover:-translate-y-1">
        <div class="order-content">
                <img :src="order.items[0].image_url " :alt="order.items[0].image_url" class="order-image">
                <div class="order-details">
                    <div class="order-name">{{order.items[0].title}}...</div>
                    <div class="order-info">
                        <span class="order-code">{{order.Code}}</span>
                        <span>{{order.date.slice(0,10)}}</span>
                    </div>
                    <div class="order-price">{{order.price}}</div>
                </div>
            </div>
            <div class="order-actions">
                <button @click="removeOrder(order.id)" class="reorder-btn">Удалить</button>
                <router-link :to="'order/' + order.Code" class="details-btn">Детали</router-link> <!-- Кнопка для перехода -->
              
            </div>
          </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import axios from 'axios';

// Реактивные переменные
const orders = ref(JSON.parse(localStorage.getItem('orders')) || []);
const searchTerm = ref('');
console.log(orders.length)
// Фильтрация заказов для отображения
const filteredOrders = computed(() => {
  return orders.value.filter(order => {
    return order.name?.toLowerCase().includes(searchTerm.value.toLowerCase());
  });
});
const removeOrder = (orderId) => {
  orders.value = orders.value.filter(order => order.id !== orderId);
  localStorage.setItem('orders', JSON.stringify(orders.value));
};
// Функция поиска заказов
const searchOrders = async () => {
  if (!searchTerm.value) {
    return; // Выход, если строка поиска пуста
  }

  try {
    const response = await axios.get(`http://localhost:8000/orders/${searchTerm.value}`);
    
    if (response.status === 200) {
      const order = response.data.data[0]; // Предполагаем, что ответ содержит объект заказа
      console.log(order.name)
      // Проверяем, содержит ли заказ поле id
      if (order.id) {
        // Проверяем, не добавлен ли уже заказ
        if (!orders.value.find(o => o.id === order.id)) {
          orders.value.push(order); // Добавляем новый заказ
          localStorage.setItem('orders', JSON.stringify(orders.value));
          console.log(orders.value) // Сохраняем массив в localStorage
        } else {
          console.log("Заказ уже добавлен ранее.");
        }
      } else {
        console.error("Ответ от API не содержит валидного заказа:", order);
      }
    } else {
      console.error(`Ошибка сервера: ${response.status}`);
    }
  } catch (error) {
    console.error("Ошибка при поиске заказов:", error); // Обработка ошибок
  }
};
watch(
  orders,
  () => {
    localStorage.setItem("orders", JSON.stringify(orders.value));
  },
  { deep: true }
);
</script>

<style scoped>
body {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f8f9fa;
    color: #333;
}
.container {
    
    margin: 20px auto;
    background-color: white;
    
    overflow: hidden;
}
.header {
    background: linear-gradient(135deg, #FF6B6B, #FF8E53);
    color: white;
    padding: 25px 20px;
    text-align: center;
    font-size: 28px;
    font-weight: 600;
    letter-spacing: 0.5px;
}
.search-box {
    padding: 20px;
    background-color: #fff;
    border-bottom: 1px solid #eee;
}
input[type="text"] {
    width: 100%;
    padding: 15px 20px;
    border: 2px solid #e0e0e0;
    border-radius: 50px;
    font-size: 16px;
    transition: all 0.3s ease;
    outline: none;
}
input[type="text"]:focus {
    border-color: #FF6B6B;
    box-shadow: 0 0 0 3px rgba(255,107,107,0.2);
}
.order-list {
    padding: 10px 20px;
}
.order-item {
    background-color: #fff;
    border-radius: 15px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    margin-bottom: 20px;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.order-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.order-content {
    padding: 20px;
    display: flex;
    align-items: center;
}
.order-image {
    width: 80px;
    height: 80px;
    border-radius: 12px;
    object-fit: cover;
    margin-right: 20px;
}
.order-details {
    flex-grow: 1;
}
.order-name {
    font-weight: 600;
    font-size: 18px;
    margin-bottom: 5px;
    color: #333;
}
.order-info {
    color: #888;
    font-size: 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 8px;
}
.order-code {
    background-color: #f0f0f0;
    padding: 4px 8px;
    border-radius: 4px;
    font-weight: 500;
}
.order-price {
    font-weight: 600;
    color: #FF6B6B;
    font-size: 18px;
}
.order-actions {
    display: flex;
    justify-content: space-between;
    padding: 15px 20px;
    background-color: #f8f9fa;
    border-top: 1px solid #eee;
}
.reorder-btn, .details-btn {
    padding: 10px 20px;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.3s ease;
}
.reorder-btn {
    background-color: #FF6B6B;
    color: white;
}
.reorder-btn:hover {
    background-color: #FF5252;
}
.details-btn {
    background-color: #e0e0e0;
    color: #333;
}
.details-btn:hover {
    background-color: #d4d4d4;
}
.no-orders {
    text-align: center;
    padding: 40px 20px;
    color: #888;
    font-size: 16px;
}
</style>