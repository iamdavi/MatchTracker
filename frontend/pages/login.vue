<template>
  <div>
    <form @submit.prevent="login">
      <input v-model="user.username" type="text" placeholder="Username">
      <input v-model="user.password" type="text" placeholder="Password">
      <button type="submit">Enviar</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      user: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    async login() {
      try {
        await this.$auth.loginWith('local', {
          data: this.user
        })
        this.$toasted.global.defaultSuccess({
          msg: 'Usuario autenticado correctamente'
        })
      } catch (err) {
        this.$toasted.global.defaultError({
          msg: 'Credenciales inválidas'
        })
      }
    }
  }
}
</script>
