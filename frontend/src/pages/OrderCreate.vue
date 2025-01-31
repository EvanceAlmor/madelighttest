<template>
    <div class="container">
      <div class="progress-bar"></div>
  
      <form id="orderForm" class="form-container" @submit="sendData">
        <div class="form-group">
          <label class="form-label">ФИО {{receivedData}}</label>
          <input
            v-model="data.name"
            type="text"
            class="form-input"
            id="name"
            placeholder="Введите ваше полное имя"
            required
            @blur="validateName"
          />
          <div class="error" v-if="errors.name">{{ errors.name }}</div>
        </div>
  
        <div class="form-group">
          <label class="form-label">Номер телефона</label>
          <input
            v-model="data.phoneNumber"
            type="text"
            class="form-input"
            id="phoneNumber"
            placeholder="Введите ваш номер телефона"
            required
            @blur="validatePhoneNumber"
          />
          <span v-if="errors.phoneNumber" class="error">{{ errors.phoneNumber }}</span>
        </div>
  
        <div class="form-group">
          <label class="form-label">Почта</label>
          <input
            v-model="data.email"
            type="email"
            class="form-input"
            id="emailAddress"
            placeholder="Введите ваш адрес эл. почты"
            required
            @blur="validateEmail"
          />
          <div class="error" v-if="errors.email">{{ errors.email }}</div>
        </div>
  
        <div class="form-group">
          <label class="form-label">Замечание к доставке</label>
          <input
            v-model="data.description"
            type="text"
            class="form-input"
            id="deliveryDescription"
            placeholder="Введите замечания к доставке"
            required
            @blur="validateDescription"
          />
          <div class="error" v-if="errors.description">{{ errors.description }}</div>
        </div>
  
        <div class="address-section">
          <div class="section-title">Адрес доставки</div>
  
          <div class="form-group">
            <label class="form-label">Улица</label>
            <input
              v-model="data.address"
              type="text"
              class="form-input"
              id="address"
              placeholder="Введите улицу доставки"
              required
              @blur="validateAddress"
            />
            <div class="error" v-if="errors.address">{{ errors.address }}</div>
          </div>
  
          <div class="form-group">
            <label class="form-label">Город</label>
            <input
              v-model="data.city"
              type="text"
              class="form-input"
              placeholder="Введите город или район доставки"
              required
              @blur="validateCity"
            />
            <div class="error" v-if="errors.city">{{ errors.city }}</div>
          </div>
        </div>
  
        <div class="section-title">Метод оплаты</div>
        <div class="payment-options">
          <div
            class="payment-option"
            v-for="method in paymentMethods"
            :key="method.value"
            :class="{ selected: selectedPaymentMethod === method.value }"
            @click="selectPaymentMethod(method.value)"
          >
            {{ method.label }}
          </div>
        </div>
  
        <button type="submit" class="place-order-btn">
          <span class="btn-text">Создать заказ</span>
          <span class="loader"></span>
        </button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { reactive, ref } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  const cart = localStorage.getItem("cart");
  const orderItems = localStorage.getItem('Orderdata')
  console.log(orderItems)
  const router = useRouter();
  
  const data = reactive({
    name: '',
    phoneNumber: '',
    email: '',
    description: '',
    address: '',
    items: JSON.parse([orderItems]),
    Order_status: 1,
  });
  
  const errors = reactive({
    name: '',
    phoneNumber: '',
    email: '',
    description: '',
    address: '',

  });
  
  const selectedPaymentMethod = ref('card');
  const paymentMethods = [
    { label: 'Картой', value: 'card' },
    { label: 'Оплата в telegram', value: 'cash' },
  ];
  
  const validateName = () => {
    errors.name = data.name ? '' : 'Please enter your full name';
  };
  
  const validatePhoneNumber = () => {
    const phoneRegex = /^\+?[0-9]{10,15}$/; // простой regex для проверки номера телефона
    errors.phoneNumber = phoneRegex.test(data.phoneNumber) ? '' : 'Please enter a valid phone number';
  };
  
  const validateEmail = () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // простой regex для проверки адреса электронной почты
    errors.email = emailRegex.test(data.email) ? '' : 'Please enter a valid email address';
  };
  
  const validateDescription = () => {
    errors.description = data.description ? '' : 'Please enter a description';
  };
  
  const validateAddress = () => {
    errors.address = data.address ? '' : 'Please enter your street address';
  };
  
  const validateCity = () => {
    errors.city = data.city ? '' : 'Please enter your city';
  };
  
  async function sendData(event) {
    event.preventDefault();
    
    // Валидация всех полей перед отправкой
    validateName();
    validatePhoneNumber();
    validateEmail();
    validateDescription();
    validateAddress();
    validateCity();
    console.log(errors.phoneNumber)
    // Если есть ошибки, не отправлять данные
    if (Object.values(errors).some(error => error)) {
      console.log('Validation errors:', errors);
      return;
    }
    data.Payment_method = selectedPaymentMethod.value;
    // Если валидация прошла, отправляем данные
    try {
      const response = await axios.post('http://192.168.0.32:8000/orders/', data, {
        headers: {
          'accept': 'application/json',
          'Content-Type': 'application/json',
        },
      });
      handleResponse(response.data);
    } catch (error) {
      console.error('Ошибка при отправке данных:', error);
    }
  }
  
  const handleResponse = (responseData) => {
    router.push({ name: 'OrderPage', query: { orderData: JSON.stringify(responseData) } });
  };
  
  const selectPaymentMethod = (method) => {
    selectedPaymentMethod.value = method;
    console.log(selectedPaymentMethod.value);
  };
  
  const props = defineProps(['receivedData']);
  </script>

<style scoped>
.error {
    color: #e53e3e;
    font-size: 13px;
    margin-top: 6px;
}

body {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 20px;
    background: linear-gradient(135deg, #f6f9fc, #eef2f7);
    color: #2d3748;
    min-height: 100vh;
}
.container {
 
    margin: 0 auto;
    background-color: white;
    border-radius: 24px;
    
    overflow: hidden;
}
.header {
    background: linear-gradient(135deg, #6366F1, #4F46E5);
    color: white;
    padding: 30px 25px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.header::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11 18c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm48 25c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm-43-7c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm63 31c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM34 90c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm56-76c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM12 86c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm28-65c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm23-11c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-6 60c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm29 22c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zM32 63c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm57-13c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-9-21c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM60 91c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM35 41c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM12 60c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2z' fill='rgba(255,255,255,0.05)' fill-rule='evenodd'/%3E%3C/svg%3E");
    opacity: 0.3;
}
.header h1 {
    margin: 0;
    font-size: 32px;
    font-weight: 600;
    letter-spacing: 0.5px;
}
.form-container {
    padding: 35px;
}
.form-group {
    margin-bottom: 25px;
}
.form-label {
    display: block;
    margin-bottom: 10px;
    color: #4a5568;
    font-weight: 500;
    font-size: 15px;
}
.form-input {
    width: 100%;
    padding: 14px 18px;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    font-size: 15px;
    transition: all 0.3s ease;
    box-sizing: border-box;
    background-color: #f8fafc;
}
.form-input:focus {
    border-color: #6366F1;
    background-color: #fff;
    outline: none;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.1);
}
.address-section {
    background-color: #f8fafc;
    padding: 25px;
    border-radius: 16px;
    margin-bottom: 30px;
    border: 1px solid #e2e8f0;
}
.section-title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 25px;
    color: #2d3748;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-title::before {
    content: '';
    display: block;
    width: 4px;
    height: 20px;
    background: #6366F1;
    border-radius: 2px;
}
.payment-options {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    margin-bottom: 30px;
}

.payment-option {
    padding: 20px;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    background-color: #f8fafc;
    font-weight: 500;
    display: flex;
    align-items: center;
    justify-content: center;
}
.payment-option.selected {
    border-color: #6366F1;
    background-color: #eef2ff;
    color: #6366F1;
}

.place-order-btn {
    width: 100%;
    padding: 16px;
    background: linear-gradient(135deg, #6366F1, #4F46E5);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.place-order-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(99, 102, 241, 0.2);
}

.place-order-btn:active {
    transform: translateY(0);
}
.loader {
    display: none;
    width: 24px;
    height: 24px;
    border: 3px solid rgba(255,255,255,0.3);
    border-top: 3px solid #fff;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin: 0 auto;
}
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
.progress-bar {
    height: 4px;
    background-color: rgba(255,255,255,0.2);
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
}
.progress-bar::after {
    content: '';
    position: absolute;
    height: 100%;
    width: 50%;
    background-color: rgba(255,255,255,0.5);
    animation: progress 2s ease infinite;
}
</style>