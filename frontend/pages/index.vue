<template>
  <div>
    <v-row v-if="equipoActual">
      <v-col cols="12" sm="12" md="6">
        <h1>Información</h1>
        <v-card>
          <v-card-title>
            {{ equipoActual.nombre }}
          </v-card-title>
          <v-card-text>
            {{ equipoActual.descripcion }}
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="6">
        <h1>Jugadores</h1>
        <tabla-jugadores :equipo-actual="equipoActual" />
      </v-col>
    </v-row>
    <v-row v-else>
      <v-col cols="12" class="text-center mt-5">
        <h1>Vaya! Parece que no has creado ningún equipo</h1>
        <h3 class="mt-3">Prueba a crear uno <a href="#">aquí.</a></h3>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import TablaJugadores from '@/components/TablaJugadores'

export default {
  name: 'Index',
  component: {
    TablaJugadores
  },
  data() {
    return {
    }
  },
  computed: {
    ...mapState(['equipoActual'])
  },
  created() {
    this.getEquipoActual()
  },
  methods: {
    ...mapActions(['getEquipoActual'])
  },
}
</script>

<style scoped>
  .login-card {
    max-width: 500px;
  }
</style>