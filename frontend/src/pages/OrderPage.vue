
    <style scoped>
    body {
        font-family: 'Poppins', sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f8f9fa;
        color: #333;
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
    .success-animation {
        text-align: center;
        padding: 30px 0;
        background-color: #f8fff8;
    }
    .checkmark {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        display: inline-block;
        stroke-width: 3;
        stroke: #4CAF50;
        stroke-miterlimit: 10;
        animation: fill .4s ease-in-out .4s forwards, scale .3s ease-in-out .9s both;
    }
    .checkmark-circle {
        stroke-dasharray: 166;
        stroke-dashoffset: 166;
        stroke-width: 3;
        stroke-miterlimit: 10;
        stroke: #4CAF50;
        fill: none;
        animation: stroke 0.6s cubic-bezier(0.65, 0, 0.45, 1) forwards;
    }
    .checkmark-check {
        transform-origin: 50% 50%;
        stroke-dasharray: 48;
        stroke-dashoffset: 48;
        animation: stroke 0.3s cubic-bezier(0.65, 0, 0.45, 1) 0.8s forwards;
    }
    @keyframes stroke {
        100% { stroke-dashoffset: 0; }
    }
    @keyframes scale {
        0%, 100% { transform: none; }
        50% { transform: scale3d(1.1, 1.1, 1); }
    }
    @keyframes fill {
        100% { box-shadow: inset 0 0 0 100px #4CAF50; }
    }
    .confirmation-details {
        padding: 25px;
    }
    .thank-you {
        text-align: center;
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 20px;
        color: #4CAF50;
    }
    .order-info {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 25px;
    }
    .info-row {
        display: flex;
        justify-content: space-between;
        margin-bottom: 15px;
        font-size: 15px;
    }
    .info-label {
        color: #666;
    }
    .info-value {
        font-weight: 500;
    }
    .delivery-time {
        text-align: center;
        margin: 25px 0;
        padding: 15px;
        background-color: #fff3e0;
        border-radius: 15px;
    }
    .delivery-title {
        font-weight: 600;
        color: #ff8f00;
        margin-bottom: 10px;
    }
    .delivery-estimate {
        font-size: 20px;
        color: #ff6f00;
    }
    .track-order-btn {
        display: block;
        width: 100%;
        padding: 15px;
        background-color: #FF6B6B;
        color: white;
        border: none;
        border-radius: 50px;
        font-size: 16px;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.3s ease;
        margin-bottom: 15px;
    }
    .track-order-btn:hover {
        background-color: #FF5252;
    }
    .return-home-btn {
        display: block;
        width: 100%;
        padding: 15px;
        background-color: transparent;
        color: #FF6B6B;
        border: 2px solid #FF6B6B;
        border-radius: 50px;
        font-size: 16px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .return-home-btn:hover {
        background-color: #fff0f0;
    }
    </style>
<template>

    <div class="">
      
        
        <div class="success-animation">
            <svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52">
                <circle class="checkmark-circle" cx="26" cy="26" r="25" fill="none"/>
                <path class="checkmark-check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8"/>
            </svg>
        </div>
        
        <div class="confirmation-details">
            <div class="thank-you">Спасибо за заказ!</div>
            
            <div class="order-info">
                <div class="info-row">
                    <span class="info-label">Номер заказа:</span>
                    <span class="info-value">#{{ orderData.Code }}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">Имя клиента:</span>
                    <span class="info-value">{{ orderData.name}}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">Эл. почта:</span>
                    <span class="info-value">{{ orderData.email}}</span>
                </div>
          
                <div class="info-row">
                    <span class="info-label">Адрес доставки:</span>
                    <span class="info-value">{{ orderData.address }}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">Общая стоимость:</span>
                    <span class="info-value">{{ orderData.price }} руб.</span>
                </div>
                <div class="info-row">
                    <span class="info-label">Метод оплаты:</span>
                    <span class="info-value">{{ orderData.Payment_method }}</span>
                </div>
            </div>
            
            <div class="delivery-time">
                <div class="delivery-title">Приблизительное время доставки</div>
                <div class="delivery-estimate">10-15 дней</div>
            </div>
            
            <button @click="addOrders" class="track-order-btn">Отследить заказ</button>
            <router-link to="/"><button class="return-home-btn">Вернуться на главную</button></router-link>
        </div>
    </div>
</template>
  <script>
  import { computed,ref } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import axios from 'axios';
  export default {
    setup() {
        const orders = ref(JSON.parse(localStorage.getItem('orders')) || []);
      const route = useRoute();
      const router = useRouter();
      const orderData = computed(() => {
        return JSON.parse(route.query.orderData || '{}');

      });
      
      console.log(orderData.value)
  
      const addOrders = async () => {
  if (orderData.value.Code) {
    console.log('kfs boss')


  try {
    const response = await axios.get(`http://192.168.0.32:8000/orders/${orderData.value.Code}`);
    console.log('mcboss')
    if (response.status === 200) {
      const order = response.data.data[0]; 
      console.log('wowo')// Предполагаем, что ответ содержит объект заказа
    
      // Проверяем, содержит ли заказ поле id
      if (order.id) {
        console.log(order.id)
        // Проверяем, не добавлен ли уже заказ
        if (!orders.value.find(o => o.id === order.id)) {
          orders.value.push(order); // Добавляем новый заказ
          console.log('orderp[oj]')

          localStorage.setItem('orders', JSON.stringify(orders.value));
          
          console.log(orders.value) // Сохраняем массив в localStorage
        } else {
          console.log("Заказ уже добавлен ранее.");
        }
        

        router.push({ name: 'OrderDetails', params: { Code: orderData.value.Code } });


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
      };
      // Получаем данные из параметров запроса и парсим их
   
      return {

        addOrders,
        orderData,
      };
      
    },
  };
  

  </script>
  
  <style scoped>
  .order-page {
    padding: 20px;
    max-width: 600px;
    margin: auto;
  }
  
  .order-summary h2,
  .order-items h2 {
    margin-top: 20px;
  }
  
  .order-items img {
    width: 100px; /* Задайте нужный размер */
    height: auto; /* Сохраните пропорции изображения */
  }
  
  .order-items ul {
    list-style-type: none;
    padding: 0;
  }
  </style>
  