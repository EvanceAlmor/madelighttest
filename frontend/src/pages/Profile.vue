<template>
<html>
<head>
  <base href="https://websim.io/profile/">
  <title>Profile - Vishal Khadok</title>
</head>
<body class="font-sans bg-gray-100">
  <div class=" m-auto bg-white h-full">
    <header class="flex items-center px-10 pb-8 border-b-black">
      <a href="#" class="text-2xl no-underline mr-5">&#8249;</a>
      <h1>Profile</h1>
      <span class="ml-auto text-2xl">&#8942;</span>
    </header>
    
    <!-- <div class="flex items-center p-20 border border-b-2 border-b-gray-400">
      <img src="https://websim.io/profile/vishal_khadok.jpg" alt="Vishal Khadok" class="w-80 h-80 rounded-2xl object-cover mr-5">
      <div>
        <h2 class="text-xl font-bold m-0">Vishal Khadok</h2>
        <p class="text-md mt-5">I love fast food</p>
      </div>
    </div> -->
    <nav>
      <ul class="list-none px-10 flex gap-8 grid grid-cols-1 pb-8 h-full">
        <li>
          <a href="#personal-info"
            class="flex items-center  text-zinc-800">
            <svg class="w-6 h-6 mr-3.5" viewBox="0 0 24 24"
              fill="currentColor">
              <path
                d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
            </svg>
            <span class="grow">Personal Info</span>
            <span class="text-neutral-400">&#8250;</span>
          </a>
        </li>
        <li>
          <a href="#addresses"
            class="flex items-center text-zinc-800">
            <svg class="w-6 h-6 mr-3.5" viewBox="0 0 24 24"
              fill="currentColor">
              <path
                d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
            </svg>
            <span class="grow">Addresses</span>
            <span class="text-neutral-400">&#8250;</span>
          </a>
        </li>
        <li>
          <a href="#cart"
            class="flex items-center text-zinc-800">
            <svg class="w-6 h-6 mr-3.5" viewBox="0 0 24 24"
              fill="currentColor">
              <path
                d="M7 18c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2-.9-2-2-2zM1 2v2h2l3.6 7.59-1.35 2.45c-.16.28-.25.61-.25.96 0 1.1.9 2 2 2h12v-2H7.42c-.14 0-.25-.11-.25-.25l.03-.12.9-1.63h7.45c.75 0 1.41-.41 1.75-1.03l3.58-6.49c.08-.14.12-.31.12-.48 0-.55-.45-1-1-1H5.21l-.94-2H1zm16 16c-1.1 0-1.99.9-1.99 2s.89 2 1.99 2 2-.9 2-2-.9-2-2-2z" />
            </svg>
            <span class="grow">Cart</span>
            <span class="text-neutral-400">&#8250;</span>
          </a>
        </li>
        <li>
          <a href="#favourite"
            class="flex items-center text-zinc-800">
            <svg class="w-6 h-6 mr-3.5" viewBox="0 0 24 24"
              fill="currentColor">
              <path
                d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
            </svg>
            <span class="grow">Favourite</span>
            <span class="text-neutral-400">&#8250;</span>
          </a>
        </li>

        <li>
          <a href="#payment-method"
            class="flex items-center text-zinc-800">
            <svg class="w-6 h-6 mr-3.5" viewBox="0 0 24 24"
              fill="currentColor">
              <path
                d="M20 4H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z" />
            </svg>
            <span class="grow">Payment Method</span>
            <span class="text-neutral-400">&#8250;</span>
          </a>
        </li>
        <li>
          <a href="#faqs"
            class="flex items-center text-zinc-800">
            <svg class="w-6 h-6 mr-3.5" viewBox="0 0 24 24"
              fill="currentColor">
              <path
                d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z" />
            </svg>
            <span class="grow">FAQs</span>
            <span class="text-neutral-400">&#8250;</span>
          </a>
        </li>
        
        <li>
          <a href="#settings"
            class="flex items-center text-zinc-800">
            <svg class="w-6 h-6 mr-3.5" viewBox="0 0 24 24"
              fill="currentColor">
              <path
                d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z" />
            </svg>
            <span class="grow">Settings</span>
            <span class="text-neutral-400">&#8250;</span>
          </a>
        </li>
        <li>
          <a href="#log-out"
            class="flex items-center text-zinc-800">
            <svg class="w-6 h-6 mr-3.5" viewBox="0 0 24 24"
              fill="currentColor">
              <path
                d="M17 7l-1.41 1.41L18.17 11H8v2h10.17l-2.58 2.58L17 17l5-5zM4 5h8V3H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h8v-2H4V5z" />
            </svg>
            <span class="grow">Log Out</span>
            <span class="text-neutral-400">&#8250;</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>
  </body>
  </html>
</template>
<script >
</script>