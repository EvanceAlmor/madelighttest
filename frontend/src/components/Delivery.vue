
<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap');

  body {
    font-family: 'Roboto', sans-serif;
    background-color: #f7f7f7;
    margin: 0;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
  }
  .container {
    background-color: #ffffff;
    border-radius: 20px;
    padding: 40px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    max-width: 450px;
    width: 100%;
  }
  h1 {
    text-align: center;
    color: #333;
    margin-bottom: 40px;
    font-weight: 500;
    font-size: 28px;
  }
  .delivery-option {
    display: flex;
    align-items: flex-start;
    margin-bottom: 30px;
    transition: all 0.3s ease;
    padding: 15px;
    border-radius: 15px;
  }
  .delivery-option:hover {
    background-color: #f9f9f9;
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
  }
  .icon {
    width: 60px;
    height: 60px;
    background-color: #ffeae3;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 20px;
    flex-shrink: 0;
    transition: all 0.3s ease;
  }
  .delivery-option:hover .icon {
    background-color: #ffd1c1;
  }
  .icon svg {
    width: 30px;
    height: 30px;
    fill: #ff6b35;
  }
  .details {
    flex-grow: 1;
  }
  h2 {
    margin: 0 0 8px 0;
    font-size: 20px;
    color: #333;
    font-weight: 500;
  }
  p {
    margin: 0;
    font-size: 15px;
    color: #666;
    line-height: 1.5;
  }
  .price {
    font-weight: 500;
    color: #ff6b35;
    margin-bottom: 5px;
  }
</style><script></script>
<template>
  <!-- <h2>Варианты доставки</h2>
  <div class="grid grid-cols-3 text-center">
    <div class="lg:p-40">
      <p class="text-xl">Самовывоз</p>
      <h5>БесплатноВы можете забрать заказ самостоятельно г. Омск, Кировский район, ул. Крупской 38</h5>
    </div>
  </div> -->
  <html><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Варианты доставки</title>

</head>
<body>
    <h1>Варианты доставки</h1>
    
    <div class="delivery-option">
      <div class="icon">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M19 7h-1V6a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v1H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2zm-9 0V6h4v1h-4z"/>
        </svg>
      </div>
      <div class="details">
        <h2>Самовывоз</h2>
        <p class="price">Бесплатно</p>
        <p>Вы можете забрать товар самостоятельно из магазина, Советский район (АМЗ)</p>
      </div>
    </div>

    <div class="delivery-option">
      <div class="icon">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M19.15 8a2 2 0 0 0-1.72-1H15V5a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h1a3 3 0 0 0 6 0h2a3 3 0 0 0 6 0h1a1 1 0 0 0 1-1v-3.15l-1.85-2.85zM8 16a1 1 0 1 1 0-2 1 1 0 0 1 0 2zm9 0a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"/>
        </svg>
      </div>
      <div class="details">
        <h2>Доставка курьером</h2>
        <p class="price">300 руб.</p>
        <p>Доставка курьером осуществляется по городу. Стоимость доставки фиксированная - 300 руб.</p>
      </div>
    </div>

    <div class="delivery-option">
      <div class="icon">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M20 4H4C2.9 4 2 4.9 2 6v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
        </svg>
      </div>
      <div class="details">
        <h2>Доставка почтой и СДЭК</h2>
        <p class="price">От 300 р.</p>
        <p>Доставка осуществляется с учетом вашей дальности от магазина</p>
      </div>
    </div>
</body>
</html>
</template>
