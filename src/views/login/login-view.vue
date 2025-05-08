<template>
<div class="vetor">
  <img :src="vetor" class="vetor-" width="600" height="600px">

</div>
  <div class="login-container">
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <div class="feira">
        <img :src="feira" class="imagem" alt="Logo"/> 
      </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div class="form-group">
          <label for="password">Senha</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">Entrar</button>
      </form>
    </div>
  </template>
  
<script setup>
import { email, password, handleLogin } from './login-script.js'
import feira from '@/assets/feira.png'
import vetor from '@/assets/vetor.svg'
</script>  
<style src="./login-style.css"></style>