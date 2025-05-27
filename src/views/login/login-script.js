import { ref } from 'vue'
import axios from 'axios'

export const email = ref('')
export const password = ref('')
export const isButtonVisible = ref(false) // Controla a visibilidade do botão
export const token = ref('') // Armazena o token JWT
export const userRole = ref('') // Armazena o papel do usuário

export const handleLogin = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/auth/login', {
      email: email.value,
      password: password.value,
    })

    console.log('Response data:', response.data);

    token.value = response.data.access_token
    userRole.value = response.data.role // Supondo que o backend retorna o papel do usuário

    console.log('Login bem-sucedido:', response.data)
    isButtonVisible.value = true // Torna o botão visível após o login bem-sucedido
    // Redirecionar ou armazenar informações adicionais, se necessário

    // Redirecionar para a página inicial após o login bem-sucedido
    window.location.href = '/home';
  } catch (error) {
    console.error('Erro no login:', error.response?.data || error.message)
    alert('Credenciais inválidas. Tente novamente.')
  }
}