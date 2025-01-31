<script setup>
const emit = defineEmits(["onClickRemove", "increaseQuantity", "decreaseQuantity", "updateQuantity"]);

defineProps({
  id: Number,
  title: String,
  imageUrl: String,
  price: Number,
});
</script>
<style scoped>
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
    font-size: 600px;
    cursor: pointer;
}

</style>
<template>
   <div class="cart-item" v-auto-animate>
            <img :src="imageUrl" :alt="title"  class="item-image">
            <div class="item-details">
                <div class="item-name">{{ title }}</div>
                <div class="item-price">{{ price }}</div>
                <div class="quantity-controls">
                    <button class="quantity-btn decrease" @click="emit('decreaseQuantity')">-</button>
                    <input type="text" v-model="item.quantity" @input="emit('updateQuantity')" />
                    <button class="quantity-btn increase" @click="emit('increaseQuantity')">+</button>
                </div>
            </div>
            <button @click="emit('onClickRemove')" class="remove-btn ">×</button>
        </div>


 
</template>
