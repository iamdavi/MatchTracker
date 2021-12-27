<template>
  <v-card class="login-card mx-auto">
    <v-card-title class="text-h4">
      Inicio de sesión
    </v-card-title>
    <v-card-text>
      <v-form 
        v-model="valid"
        @submit.prevent="login"
      >
        <v-container>
          <v-row>
            <v-col cols="12" >
              <v-text-field
                v-model="user.username"
                :counter="25"
                label="Usuario"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12" >
              <v-text-field
                v-model="user.password"
                label="Contraseña"
                required
                :rules="[rules.required, rules.min]"
                :counter="10"
                :type="show1 ? 'text' : 'password'"
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="show1 = !show1"
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-container fluid>
                <v-row justify="space-between">
                  <v-col>
                    <v-btn text color="primary" @click="login">Registrarse</v-btn>
                  </v-col>
                  <v-col class="text-right">
                    <v-btn color="primary" @click="login">Entrar</v-btn>
                  </v-col>
                </v-row>
              </v-container>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Login',
  layout: 'empty',
  data() {
    return {
      user: {
        username: 'admin',
        password: 'admin'
      },
      valid: false,
      show1: false,
      rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
        },
      }
    },
  methods: {
    ...mapActions(['setLoggedInUser']),
    async login() {
      try {
        await this.$auth.loginWith('local', { data: this.user })
          .then(() => {
            this.setLoggedInUser()
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

<style scoped>
  .login-card {
    max-width: 500px;
  }
</style>