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
    position: relative;
}
.back-btn {
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    color: white;
    font-size: 24px;
    cursor: pointer;
}
.order-summary {
    padding: 25px;
    border-bottom: 1px solid #eee;
}
.order-id {
    font-size: 16px;
    color: #888;
    margin-bottom: 10px;
}
.order-status {
    display: inline-block;
    padding: 6px 12px;
    background-color: #4CAF50;
    color: white;
    border-radius: 20px;
    font-size: 14px;
    margin-bottom: 15px;
}
.price-details {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 15px;
    margin-top: 15px;
}
.price-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
    font-size: 15px;
    color: #666;
}
.price-row.total {
    font-weight: 600;
    color: #333;
    font-size: 18px;
    border-top: 1px solid #eee;
    padding-top: 10px;
    margin-top: 10px;
}
.delivery-info {
    padding: 25px;
    border-bottom: 1px solid #eee;
}
.section-title {
    font-weight: 600;
    font-size: 18px;
    margin-bottom: 15px;
}
.info-row {
    margin-bottom: 15px;
}
.info-label {
    color: #888;
    font-size: 14px;
    margin-bottom: 5px;
}
.info-value {
    font-size: 16px;
    color: #333;
}
.items-list {
    padding: 25px;
}
.item {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}
.item-image {
    width: 60px;
    height: 60px;
    border-radius: 10px;
    object-fit: cover;
    margin-right: 15px;
}
.item-details {
    flex-grow: 1;
}
.item-name {
    font-weight: 500;
    margin-bottom: 5px;
}
.item-price {
    color: #FF6B6B;
    font-weight: 600;
}
.item-quantity {
    color: #888;
    font-size: 14px;
}
.support-btn {
    display: block;
    width: calc(100% - 50px);
    margin: 0 25px 25px;
    padding: 15px;
    background-color: #FF6B6B;
    color: white;
    border: none;
    border-radius: 50px;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
.support-btn:hover {
    background-color: #FF5252;
}
</style>
<template>
<div class="container">
    
    <div v-if="loading">
        <p class="text-gray-500">Загрузка...</p> <!-- Сообщение о загрузке -->
      </div>
    <div v-if="order !== null" class="order-summary">
        <div class="order-id">Заказ #{{ order.Code }}</div>
        <div class="order-status">Доставлено</div>
        <div class="price-details">
            <div class="price-row">
                <span>Стоимость заказа</span>
                <span>{{order.price}}</span>
            </div>
            <div class="price-row">
                <span>Доставка</span>
                <span>200</span>
            </div>
            <div class="price-row total">
                <span>Общая стоимость</span>
                <span>{{order.price + 200}}</span>
            </div>
        </div>
    </div>

    <div v-if="order !== null" class="delivery-info">
        <div class="section-title">Информация о доставке</div>
        <div class="info-row">
            <div class="info-label">Адрес</div>
            <div class="info-value">{{ order.address }}</div>
        </div>
        <div class="info-row">
            <div class="info-label">Дата создания заказа</div>
            <div class="info-value">{{ order.date.slice(0,10) }}</div>
        </div>
        <div class="info-row">
            <div class="info-label">Номер телефона</div>
            <div class="info-value">+{{ order.phoneNumber }}</div>
        </div>
    </div>

    <div v-if="order !== null" class="items-list">
        <div class="section-title">Товары заказа</div>
        <div v-for="item in order.items" class="item">
            <img :src="item.image_url" :alt="item.title" class="item-image">
            <div class="item-details">
                <div class="item-name">{{ item.title }}</div>
                <div class="item-quantity">Количество: {{ item.quantity }}</div>
                <div class="item-price">{{ item.price }}</div>
            </div>
        </div>
    </div>

    <button class="support-btn">Написать в поддержку</button>
</div>
</template>
 
<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const order = ref(null); // Инициализация переменной order
const loading = ref(true); // Переменная для отслеживания состояния загрузки

const fetchOrderDetails = () => {
  const orders = JSON.parse(localStorage.getItem('orders')) || [];
  const foundOrder = orders.find(o => o.Code === route.params.Code);

  if (foundOrder) {
    order.value = foundOrder;
  } else {
    console.error("Order not found");
    order.value = null; // Установите null, если заказ не найден
  }
  loading.value = false; // Завершите загрузку
};

onMounted(fetchOrderDetails); // Вызов функции, когда компонент монтируется
</script>