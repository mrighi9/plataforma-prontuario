import { ref } from 'vue'

export const email = ref('')
export const password = ref('')

export const handleLogin = () => {
  console.log('Email:', email.value)
  console.log('Senha:', password.value)
  // Adicione lógica de autenticação aqui
}