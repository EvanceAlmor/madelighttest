<script setup>
  import axios from 'axios';
  import { onMounted, ref, watch, defineEmits, computed, Transition } from 'vue';
  import { useRoute } from 'vue-router';
  import { TransitionRoot, TransitionChild } from '@headlessui/vue';
  const currentSlide = ref(0);
  const images = ref([]);
  const items = ref(JSON.parse(localStorage.getItem('items')) || []);
  const cart = ref(JSON.parse(localStorage.getItem('cart')) || []);
  console.log(cart.value)
  const route = useRoute();
  const id = ref(route.params.id);
  console.log(id.value)
  const product = ref({});
  const cartItem = computed(() => {
  return cart.value.find((item) => item.id === Number(id.value)) || { id: Number(id.value), quantity: 0 };
});// Вернет найденный товар или объект с дефолтными значениями
const nutrition = ref({ Color: product.value.Color, size: product.value.size, Carbs: '90g', Fat: '28g' });
console.log(nutrition)
console.log(cartItem.value)
const increaseQuantity = () => {
  if (cartItem.value.quantity < 10) {
    addToCart(); // Увеличивает количество в корзине
  }
};

const decreaseQuantity = () => {
  if (cartItem.value.quantity > 1) {
    cartItem.value.quantity--;
  }
};

  const rating = 4.8;
  const reviewsCount = 124;
  const cookTime = '20-25 min';
  const cookingMethod = 'Wood-fired';
  const productDescription = 'Our signature Margherita pizza...';
  const ingredients = ['Кожа', 'Резина', 'Подошва'];
 

  const additionalInfo = '• Gluten-free crust available (+$3)...';

  const fetchProduct = () => {
    if (id.value) {
      const foundProduct = items.value.find(item => item.id === Number(id.value));
      product.value = foundProduct || { title: "Product Not Found", price: 0, image_url: "" };
    }
    
  images.value = [
 product.value.image_url,
 product.value.Image_urls
  ];

  };

  const getCartItem = (productId) => cart.value.find(item => item.id === productId);

  const validateQuantity = () => {
  const item = cartItem.value;
  if (item.quantity < 1) item.quantity = 1;
  if (item.quantity > 10) item.quantity = 10;
};

const addToCart = () => {
  const existingItem = cart.value.find((item) => item.id === product.value.id);
  if (existingItem) {
    existingItem.quantity++;
  } else {
    cart.value.push({ ...product.value, quantity: 1 });
  }
  location.reload()
};
const res = cartItem.value.quantity === 0

const Sendlist = () => {
  try {
    console.log('sendlist')
    localStorage.removeItem('Orderdata');
    const orderItems = [cartItem.value]
    localStorage.setItem('Orderdata', JSON.stringify(orderItems));
  } catch (error) {
    console.error('Error saving data:', error);
  }
};

onMounted(() => {
  fetchProduct(); // Загрузить продукт
nutrition.value = { Color: product.value.Color, Size: product.value.size, Category: product.value.Category};
  console.log(nutrition)
  // Обновлять продукт при смене маршрута
  watch(() => route.params.id, () => {
    id.value = route.params.id;
    fetchProduct();
  });
});
  watch(cart, () => {
  localStorage.setItem('cart', JSON.stringify(cart.value));
}, { deep: true });

// Сохранить список товаров
watch(items, () => {
  localStorage.setItem('items', JSON.stringify(items.value));
});


  const nextSlide = () => {
    currentSlide.value = (currentSlide.value + 1) % images.value.length;
  };

  const prevSlide = () => {
    currentSlide.value = (currentSlide.value - 1 + images.value.length) % images.value.length;
  };
  console.log(cartItem.value)
</script>

    
 
    
    
    <template>
      <div class="">
       
    
        <div class="product-card">
            <div class="carousel overflow-hidden w-full ">
              <div class="relative flex transition-transform duration-700 ease-in-out"
           :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
        <div 
          v-for="(image, index) in images" 
          :key="index" 
          class="w-full flex-shrink-0"
        >
          <img 
            :src="image" 
            :alt="`Image ${index + 1}`" 
            class="w-full h-full object-cover"
          />
        </div>

          
                </div>
                <button class="carousel-btn prev" @click="prevSlide">←</button>
                <button class="carousel-btn next" @click="nextSlide">→</button>
              </div>
       
    
          <div class="product-details">
            <div class="product-name">{{ product.title }}</div>
            <!-- <div class="product-meta">
              <span class="meta-item">⭐ {{ rating }} ({{ reviewsCount }} reviews)</span>
              <span class="meta-item">🕒 {{ cookTime }}</span>
              <span class="meta-item">🔥 {{ cookingMethod }}</span>
            </div> -->
            <div class="product-price">{{ product.price }} руб.</div>
    
            <div class="description">{{ productDescription }}</div>
    
            <div class="section-title">Состав</div>
            <div class="ingredients">
              <span class="ingredient-tag" v-for="ingredient in ingredients" :key="ingredient">{{ ingredient }}</span>
            </div>
    
            <div class="section-title">Характеристики</div>
            <div class="nutrition-info">
              <div class="nutrition-item" v-for="(value, label) in nutrition" :key="label">
                <div class="nutrition-value">{{ value }}</div>
                <div class="nutrition-label">{{ label }}</div>
              </div>
            </div>
            <div class="flex flex-wrap gap-4 mt-4">
  <!-- Кнопка "Добавить в корзину" или "Товар в корзине" -->
   <div v-if="res" class="flex-1">
  <button 
   
    @click="addToCart" 
    class="w-full transition  py-3 bg-green-500 text-white rounded-lg cursor-not-allowed"
  >
    Добавить в корзину
  </button>
</div>
 <router-link v-else to="/cart" class="flex-1">
  <button class="w-full py-3 transition bg-gray-500 text-white rounded-lg cursor-not-allowed"
     >
    Товар в корзине
  </button>
</router-link>
  <!-- Кнопка "Купить сейчас" -->
  <router-link 
    to="/ordercreate" 
    class="flex-1"
  >
    <button 
      @click="Sendlist" 
      class="w-full py-3 bg-orange-500 text-white rounded-lg hover:bg-orange-600 transition"
    >
      Купить сейчас
    </button>
  </router-link>
</div>
          </div>
        </div>
      </div>
    </template>
       <style scoped>
       body {
           font-family: 'Poppins', sans-serif;
           margin: 0;
           padding: 0;
           background-color: #f8f9fa;
           color: #333;
       }
       .container {
         width: 100%;
         padding: 0;
         margin:0;
       }
       .product-card {
           background-color: white;
           border-radius: 20px;
           overflow: hidden;
           display: grid;
           grid-template-columns: 1fr;
       }
       @media (min-width: 692px) {
           .product-card {
               grid-template-columns: 1fr 1fr;
           }
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
       .carousel {
           position: relative;
           width: 100%;
           height: 400px;
           overflow: hidden;
       }
       @media (min-width: 1000px) {
        .carousel {
          height: 600px;
        }
      }
       .carousel-inner {
           display: flex;
           transition: transform 0.5s ease;
           height: 100%;
       }
       .carousel-item {
           min-width: 100%;
           height: 100%;
       }
       .carousel-item img {
        width: 100%;
    height: 600px; /* Выберите нужную высоту */
    object-fit: contain; /* Обеспечивает полное отображение изображения */
       }
       .carousel-btn {
           position: absolute;
           top: 50%;
           transform: translateY(-50%);
           background: rgba(255,255,255,0.8);
           border: none;
           width: 40px;
           height: 40px;
           border-radius: 50%;
           font-size: 20px;
           cursor: pointer;
           display: flex;
           align-items: center;
           justify-content: center;
           z-index: 2;
       }
       .carousel-btn.prev { left: 10px; }
       .carousel-btn.next { right: 10px; }
       .carousel-dots {
           position: absolute;
           bottom: 15px;
           left: 50%;
           transform: translateX(-50%);
           display: flex;
           gap: 8px;
           z-index: 2;
       }
       .dot {
           width: 8px;
           height: 8px;
           border-radius: 50%;
           background: rgba(255,255,255,0.5);
           cursor: pointer;
       }
       .dot.active { background: white; }
       .product-details {
           padding: 25px;
       }
       .product-name {
           font-size: 32px;
           font-weight: 600;
           margin-bottom: 10px;
       }
       .product-meta {
           display: flex;
           gap: 20px;
           margin-bottom: 20px;
       }
       .meta-item {
           display: flex;
           align-items: center;
           gap: 5px;
           color: #666;
       }
       .product-price {
           color: #FF6B6B;
           font-size: 28px;
           font-weight: 600;
           margin-bottom: 20px;
       }
       .description {
           color: #666;
           line-height: 1.8;
           margin-bottom: 25px;
           font-size: 16px;
       }
       .section-title {
           font-weight: 600;
           margin-bottom: 15px;
           font-size: 20px;
       }
       .ingredients {
           display: flex;
           flex-wrap: wrap;
           gap: 10px;
           margin-bottom: 25px;
       }
       .ingredient-tag {
           background-color: #f8f9fa;
           padding: 10px 20px;
           border-radius: 50px;
           font-size: 14px;
           color: #666;
       }
       .add-to-cart-btn {
           width: 100%;
           padding: 20px;
           background-color: #FF6B6B;
          border: none;
           border-radius: 50px;
       
           cursor: pointer;
       
           display: flex;
           align-items: center;
           justify-content: center;
   
       }
      .add-to-order-btn{
        width: 100%;
     
           background-color: #22ff20;
          border: none;
           border-radius: 50px;
           width: 50%;
           cursor: pointer;
          height: 16vw;
           display: flex;
           align-items: center;
           justify-content: center;
          border-radius: 0px 50px 50px 0px;
      }
       .cart-btn {
          
          
           background-color: #22ff20;
          border: none;
           border-radius: 50px;
           height: 16vw;
           cursor: pointer;
        width: 50%;
           display: flex;
           align-items: center;
           justify-content: center;
          border-radius: 50px 0% 0% 50px;
       }
       .add-to-cart-btn:hover {
           background-color: #FF5252;
           transform: translateY(-2px);
       }
       .nutrition-info {
           display: grid;
           grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
           gap: 15px;
           margin-bottom: 25px;
       }
       .nutrition-item {
           background: #f8f9fa;
           padding: 15px;
           border-radius: 10px;
           text-align: center;
       }
       .nutrition-value {
           font-size: 20px;
           font-weight: 600;
           color: #FF6B6B;
       }
       .nutrition-label {
           font-size: 14px;
           color: #666;
       }
       .quantity-controls {
           display: flex;
           align-items: center;
           margin-bottom: 25px;
       }
       .quantity-btn {
           width: 40px;
           height: 40px;
           border-radius: 50%;
           border: 1px solid #ddd;
           background: white;
           font-size: 20px;
           display: flex;
           align-items: center;
           justify-content: center;
           cursor: pointer;
           color: #666;
       }
       .button-container {
    display: flex; /* Используем Flexbox для кнопок */
    gap: 10px; /* Пробел между кнопками */
    width: 100%; /* Задаем ширину контейнера */
}

.add-to-order-btn, .cart-btn {
    flex: 1; /* Обе кнопки будут занимать равное пространство */
    min-width: 120px; /* Минимальная ширина кнопок */
    height: 50px; /* Установите одинаковую высоту */
    border: none; /* Убираем стандартные бордюры */
    border-radius: 30px; /* Округлые углы */
    background-color: #FF6B6B; /* Цвет фона */
    color: white; /* Цвет текста */
    cursor: pointer; /* Курсор при наведении */
    transition: background-color 0.3s ease; /* Плавный переход при наведении */
}

.add-to-cart-btn:hover, .add-to-order-btn:hover {
    background-color: #FF5252; /* Цвет при наведении */
}
       .quantity {
          border: none;
          background-color: #FF6B6B;
           margin: 0 20px;
           font-weight: 500;
           font-size: 18px;
       }
       
       .additional-info {
           margin-top: 25px;
           padding-top: 25px;
           border-top: 1px solid #eee;
       }

       </style>
  <!-- <div class="flex mt-10">
    <img
      src="/sneakers/sneakers-4.jpg"
      alt="sneaker"
      class="w-2/4 h-auto border border-4 border-black"
    />
    <div class="items-center px-20">
      <p class="text-2xl w-full">Мужские Кроссовки Nike Blazer Mid Suede</p>
      <div class="px-10">
        <h2>13000 руб.</h2>
        <h2>
          Nike Blazer - это кроссовки, которые сочетают функциональность и
          стиль. Они выполнены из прочного материала, который обеспечивает
          комфортную ходьбу и поддержку для ног. Высокое качество материалов и
          технологии производства делает кроссовки долговечными и устойчивыми к
          износу.
        </h2>
      </div>
    </div>
  </div>  -->
<!--   
  <div class="relative z-10" role="dialog" aria-modal="true"> -->
  <!--
      Background backdrop, show/hide based on modal state.
  
      Entering: "ease-out duration-300"
        From: "opacity-0"
        To: "opacity-100"
      Leaving: "ease-in duration-200"
        From: "opacity-100"
      
        To: "opacity-0"
    -->
   <!-- <div
    class="fixed inset-0 hidden bg-gray-500 bg-opacity-75 transition-opacity md:block"
    aria-hidden="true"
  ></div> -->


  <!--
          Modal panel, show/hide based on modal state.
  
          Entering: "ease-out duration-300"
            From: "opacity-0 translate-y-4 md:translate-y-0 md:scale-95"
            To: "opacity-100 translate-y-0 md:scale-100"
          Leaving: "ease-in duration-200"
            From: "opacity-100 translate-y-0 md:scale-100"
            To: "opacity-0 translate-y-4 md:translate-y-0 md:scale-95"
        -->
<!--  
  <div
    class="relative flex w-full items-center overflow-hidden bg-white px-4 pb-8 pt-14 sm:px-6 sm:pt-8 md:p-6 lg:p-8"
  > -->
    <!-- <router-link to="/"
      ><button
        type="button"
        class="absolute right-4 top-4 text-gray-400 hover:text-gray-500 sm:right-6 sm:top-8 md:right-6 md:top-6 lg:right-8 lg:top-8"
      >
        <span class="sr-only">Close</span>
        <svg
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          aria-hidden="true"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>
    </router-link> -->
    <!-- <style scoped>
body {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f8f9fa;
    color: #333;
}
.container {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr ;
    gap: 40px;
    background-color: white;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    overflow: hidden;
    padding: 40px;
}
.header {
    grid-column: 1 / -1;
    background: linear-gradient(135deg, #FF6B6B, #FF8E53);
    color: white;
    padding: 25px 40px;
    text-align: left;
    font-size: 32px;
    font-weight: 600;
    letter-spacing: 0.5px;
    border-radius: 15px;
    display: flex;
    align-items: center;
}




.product-image-section {
    position: relative;
}
@media (max-width: 768px) {
    .product-image-section {
        position: grid;
    }
}
.product-image {
    width: 100%;
    height: 500px;
    object-fit: cover;
    border-radius: 15px;
}
.product-details {
    padding: 20px 0;
}
.product-name {
    font-size: 36px;
    font-weight: 600;
    margin-bottom: 15px;
}
.product-price {
    color: #FF6B6B;
    font-size: 32px;
    font-weight: 600;
    margin-bottom: 25px;
}
.description {
    color: #666;
    line-height: 1.8;
    font-size: 18px;
    margin-bottom: 30px;
}
.section-title {
    font-weight: 600;
    margin-bottom: 15px;
    font-size: 24px;
}
.ingredients {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 30px;
}
.ingredient-tag {
    background-color: #f8f9fa;
    padding: 12px 20px;
    border-radius: 50px;
    font-size: 16px;
    color: #666;
    transition: all 0.3s ease;
}
.ingredient-tag:hover {
    background-color: #FF6B6B;
    color: white;
}
.quantity-controls {
    display: flex;
    align-items: center;
    margin-bottom: 30px;
}
.quantity-btn {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: 2px solid #ddd;
    background: white;
    font-size: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    color: #666;
    transition: all 0.3s ease;
}
.quantity-btn:hover {
    border-color: #FF6B6B;
    color: #FF6B6B;
}
.quantity {
    margin: 0 30px;
    font-weight: 500;
    font-size: 24px;
}
.add-to-cart-btn {
    width: 100%;
    padding: 20px;
    background-color: #FF6B6B;
    color: white;
    border: none;
    border-radius: 50px;
    font-size: 20px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
}
.add-to-cart-btn:hover {
    background-color: #FF5252;
    transform: translateY(-2px);
}
.cart-icon {
    width: 24px;
    height: 24px;
}
</style>
<template>
<div class="container">
   
    

        <img :src="product.image_url" alt="Delicious Margherita Pizza with fresh ingredients" class="product-image">

    
    <div class="product-details">
        <div class="product-name">{{ product.title }}</div>
        <div class="product-price">{{ product.price }}</div>
        
        <div class="description">
            Our signature Margherita pizza features a thin, crispy crust topped with fresh San Marzano tomatoes, 
            premium buffalo mozzarella, fresh basil leaves, and a drizzle of extra virgin olive oil. 
            Baked to perfection in our wood-fired oven for that authentic Italian taste.
            Each pizza is crafted with care using traditional techniques and the finest ingredients.
        </div>
        
        <div class="section-title">Ingredients</div>
        <div class="ingredients">
            <span class="ingredient-tag">Fresh Mozzarella</span>
            <span class="ingredient-tag">San Marzano Tomatoes</span>
            <span class="ingredient-tag">Fresh Basil</span>
            <span class="ingredient-tag">Olive Oil</span>
            <span class="ingredient-tag">Sea Salt</span>
            <span class="ingredient-tag">Italian Flour</span>
        </div>
        
       <div class="quantity-controls">
            <button class="quantity-btn decrease">-</button>
            <span class="quantity">{{  }}</span>
            <button class="quantity-btn increase">+</button>
        </div>
        
        <button class="add-to-cart-btn">
            <svg class="cart-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="9" cy="21" r="1"></circle>
                <circle cx="20" cy="21" r="1"></circle>
                <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
            </svg>
            Add to Cart
        </button> -->
        <!-- </div>
<div class="flex  gap-1" v-if="cartItem">
  <button  v-if="cartItem.quantity > 0" @click="addToCart" type="submit" class="add-to-cart-btn rounded-l-3xl">Добавить в корзину</button>
  <button  v-else @click="addToCart" type="submit" class="add-to-cart-btn rounded-l-3xl"><div class="quantity-controls">
    <button @click="decreaseQuantity" class="quantity-btn decrease mr-4">-</button>

    <input type="number" v-if="cartItem" v-model="cartItem.quantity" @input="validateQuantity" min="1" max="4" placeholder="" required class="quantity w-11">
    <button @click="increaseQuantity" class="quantity-btn increase">+</button>
</div></button>        
  <button   @click="addToCart" type="submit" class="add-to-order-btn rounded-r-3xl">Купить сейчас {{ cartItem.quantity }}</button>

</div>
    </div>

</template>
    -->
