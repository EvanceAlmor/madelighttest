<template>
  <div class="lg:px-32 md:px-8 ">
    <div class="cart-items">
      <div v-for="(item, index) in cartItems" :key="item.id" class="cart-item">
        <img :src="item.image_url" :alt="item.title" class="item-image lg:w-96" />
        <div class="item-details">
          <div class="item-name">{{ item.title }}</div>
          <div class="item-price">{{ item.price }} руб.</div>
          <div class="quantity-controls">
            <button class="quantity-btn decrease" @click="decreaseQuantity(index)">-</button>
            <input type="number" v-model="item.quantity" @input="updateQuantity(index)" min="1" class="quantity-input" />
            <button class="quantity-btn increase" @click="increaseQuantity(index)">+</button>
          </div>
        </div>
        <button class="remove-btn" @click="removeItem(index)">×</button>
      </div>
    </div>

    <div class="cart-summary" v-if="cartItems.length > 0">
      <div class="summary-row">
        <span>Цена товаров в корзине</span>
        <span>{{ subtotal.toFixed(2) }} руб</span>
      </div>
      <div class="summary-row">
        <span>Цена доставки</span>
        <span>250 руб.</span>
      </div>
      <div class="summary-row total">
        <span>Итоговая цена</span>
        <span>{{ total.toFixed(2) }} руб</span>
      </div>
    </div>

    <button v-if="cartItems.length > 0" @click="Sendlist" class="mb-40 w-full inline-flex justify-center rounded-md border border-transparent bg-orange-300 px-16 py-2 text-sm font-medium text-white hover:bg-orange-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-orange-500 focus-visible:ring-offset-2">Создать заказ</button>
    <img v-if="cartItems.length ===0" src="/package-icon.png" alt="Cart is empty" class="flex justify-center m-auto w-40 pt-40">
    <div class="empty-cart" v-if="cartItems.length === 0">
      Your cart is empty
    </div>
  </div>
</template>

<script>
import { ref, computed, watch } from 'vue';
import OrdersModal from '../components/OrdersModal.vue';
import { useRouter } from 'vue-router';

export default {
  components: { OrdersModal },
  setup() {
    const router = useRouter();
    const cartItems = ref([]);
    const localCart = localStorage.getItem("cart");
    cartItems.value = localCart ? JSON.parse(localCart) : [];

    const deliveryFee = 250;

    const subtotal = computed(() => {
      return cartItems.value.reduce((total, item) => total + (item.price * item.quantity), 0);
    });

    const total = computed(() => {
      return subtotal.value + deliveryFee;
    });

    const increaseQuantity = (index) => {
      cartItems.value[index].quantity++;
    };

    const decreaseQuantity = (index) => {
      if (cartItems.value[index].quantity > 1) {
        cartItems.value[index].quantity--;
      }
    };

    const updateQuantity = (index) => {
      const quantity = parseInt(cartItems.value[index].quantity);
      if (!isNaN(quantity) && quantity > 0) {
        cartItems.value[index].quantity = quantity;
      } else {
        cartItems.value[index].quantity = 1; // если невалидный ввод, устанавливаем в 1
      }
    };

    const removeItem = (index) => {
      cartItems.value.splice(index, 1);
    };

    // Функция для сохранения данных в localStorage
    const Sendlist = () => {
      const cartValue = cartItems.value;

      // Проверка на наличие элементов в cartValue
      if (cartValue.length === 0) {
        console.error('Cart is empty');
        return;
      }

      // Сохранение данных в localStorage
      try {
        localStorage.setItem('Orderdata', JSON.stringify(cartValue));
        console.log('Order data saved successfully:', cartValue);
        // Добавляем редирект используя useRouter из Composition API
   
        router.push('/ordercreate');
      } catch (error) {
        console.error('Error saving data to localStorage:', error);
      }
    };

    // Сохранение обновленных данных в localStorage
    watch(cartItems, () => {
      localStorage.setItem("cart", JSON.stringify(cartItems.value));
    }, { deep: true });

    return {
      cartItems,
      subtotal,
      total,
      increaseQuantity,
      decreaseQuantity,
      updateQuantity,
      removeItem,
      Sendlist, // Не забудьте вернуть функцию
    };
  }
};
</script>


  <style scoped>

body {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    
    background-color: #f8f9fa;
    color: #333;
}
.container {
    
  
    background-color: white;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
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
.cart-items {
    padding: 25px;
}
.cart-item {
    display: flex;
    align-items: center;
    padding: 15px;
    border-bottom: 1px solid #eee;
    position: relative;
}
.item-image {
    width: 80px;
    height: 80px;
    border-radius: 12px;
    object-fit: cover;
    margin-right: 15px;
}
.item-details {
    flex-grow: 1;
}
.item-name {
    font-weight: 500;
    font-size: 16px;
    margin-bottom: 5px;
}
.item-price {
    color: #FF6B6B;
    font-weight: 600;
    font-size: 16px;
}
.quantity-controls {
    display: flex;
    align-items: center;
    margin-top: 10px;
}
.quantity-btn {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    border: 1px solid #ddd;
    background: white;
    font-size: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    color: #666;
}
.quantity {
    margin: 0 15px;
    font-weight: 500;
}
.remove-btn {
    position: absolute;
    right: 15px;
    top: 15px;
    color: #ff4444;
    background: none;
    border: none;
    font-size: 20px;
    cursor: pointer;
}
.quantity-input {
  width: 50px;
  text-align: center;
  border: none;
}
.cart-summary {
    padding: 25px;
    background-color: #f8f9fa;
    margin: 20px 25px;
    border-radius: 15px;
}
.summary-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
    color: #666;
}
.summary-row.total {
    color: #333;
    font-weight: 600;
    font-size: 18px;
    padding-top: 10px;
    margin-top: 10px;
    border-top: 1px solid #ddd;
}
.checkout-btn {
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
.checkout-btn:hover {
    background-color: #FF5252;
}
.empty-cart {
    text-align: center;
    padding: 40px 25px;
    color: #888;
}
</style>