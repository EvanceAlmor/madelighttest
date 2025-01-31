<template>
    <div v-html="htmlContent"></div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  
  export default {
    setup() {
      const htmlContent = ref('');
  
      onMounted(async () => {
        try {
          const response = await fetch('/hff.html'); // Убедитесь, что путь корректный
          htmlContent.value = await response.text();
        } catch (error) {
          console.error('Ошибка при загрузке файла:', error);
        }
      });
  
      return {
        htmlContent
      };
    }
  };
  </script>
  
<style scoped>
.payform-tbank {
    display: flex;
    margin: 2px auto;
    flex-direction: column;
    max-width: 250px;
}

.payform-tbank-row {
    margin: 2px;
    border-radius: 4px;
    flex: 1;
    transition: 0.3s;
    border: 1px solid #DFE3F3;
    padding: 15px;
    outline: none;
    background-color: #DFE3F3;
    font-size: 15px;
}

.payform-tbank-row:focus {
    background-color: #FFFFFF;
    border: 1px solid #616871;
    border-radius: 4px;
}

.payform-tbank-btn {
    background-color: #FBC520;
    border: 1px solid #FBC520;
    color: #3C2C0B;
}

.payform-tbank-btn:hover {
    background-color: #FAB619;
    border: 1px solid #FAB619;
}
</style>
