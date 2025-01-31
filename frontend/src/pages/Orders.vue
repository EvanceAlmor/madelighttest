<template>
<html>
<head>
  <base href="https://websim.creativeengine.ai/">
</head>
<body class="font-sans flex justify-center items-center ">
  <div class="w-fulls rounded-3xl overflow-hidden flex flex-col">
    <div class="p-5 text-center relative bg-gradient-to-r from-violet-200 to-pink-200">
      <div
        class="absolute left-5 top-1/2 -translate-y-1/2 text-2xl cursor-pointer">
        ←</div>
      <h1 class="p-5 text-lg font-semibold text-center relative-title">Delivery Details</h1>
    </div>
    <div class=" overflow-y-auto p-5">
      <form id="deliveryForm">
        <div class="mb-5">
          <label for="recipientName"
            class="block font-medium mb-1">Recipient's
            Name</label>
          <input type="text" id="recipientName"
            class="w-full p-3 rounded-lg text-base border-[#ffe0e0] hover: border-[#ffc6c6]" required>
        </div>
        <div class="mb-5">
          <label for="deliveryAddress"
            class="block font-medium mb-1">Delivery
            Address</label>
          <input type="text" id="deliveryAddress"
            class="w-full p-3 rounded-lg text-base border-[#ffe0e0]" required>
        </div>
        <div class="mb-5">
          <label for="city"
            class="block font-medium mb-1">City</label>
          <input type="text" id="city"
            class="w-full p-3 rounded-lg text-base border-[#ffe0e0]" required>
        </div>
        <div class="mb-5">
          <label for="postalCode"
            class="block font-medium mb-1">Postal
            Code</label>
          <input type="text" id="postalCode"
            class="w-full p-3 rounded-lg text-base border-[#ffe0e0]" required>
        </div>
        <div class="mb-5">
          <label for="country"
            class="block font-medium mb-1">Country</label>
          <select id="country"
            class="w-full p-3 rounded-lg text-base appearance-none bg-no-repeat  border-[#ffe0e0]"
            required>
            <option value="">Select a country</option>
            <option value="US">United States</option>
            <option value="CA">Canada</option>
            <option value="UK">United Kingdom</option>
            <option value="AU">Australia</option>
            <!-- Add more countries as needed -->
          </select>
        </div>
        <div class="mb-5">
          <label for="phoneNumber"
            class="block font-medium mb-1">Phone
            Number</label>
          <input type="tel" id="phoneNumber"
            class="w-full p-3 rounded-lg text-base  border-[#ffe0e0]" required>
        </div>
        <div class="mb-5">
          <label for="email" class="block font-medium mb-1">Email
            Address</label>
          <input type="email" id="email"
            class="w-full p-3 rounded-lg text-base  border-[#ffe0e0]" required>
        </div>
        <div class="mb-5">
          <label for="deliveryInstructions"
            class="block font-medium mb-1">Delivery Instructions
            (Optional)</label>
          <textarea id="deliveryInstructions"
            class="w-full p-3 rounded-lg text-base  border-[#ffe0e0]"
            rows="3"></textarea>
        </div>
        <button type="submit"
          class="w-full p-15 rounded-3xl text-lg font-semibold cursor-pointer bg-red-300 py-4 text-white transition">Confirm
          Delivery
          Details</button>
      </form>
    </div>
  </div>
  
</body>
</html>
</template>
  <script setup></script>