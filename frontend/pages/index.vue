<template>
  <div>
    <v-row v-if="equipo">
      <v-col cols="12" sm="12" md="6">
		    <h1>Información</h1>
        <informacion-tarjeta :equipo="equipo" />
      </v-col>
      <v-col cols="12" sm="12" md="6">
        <div class="d-flex align-center justify-space-between">
          <h1>Jugadores</h1>
          <v-btn color="primary" to="/jugadores">Ver todo</v-btn>
        </div>
        <tabla-jugadores />
      </v-col>
    </v-row>

    <v-row v-else>
      <v-col cols="12" class="text-center mt-5">
        <h1>Vaya! Parece que no has creado ningún equipo</h1>
        <h3 class="mt-3">Prueba a crear uno <a to="/equipo/new">aquí.</a></h3>
      </v-col>
    </v-row>

  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import TablaJugadores from '@/components/TablaJugadores'
import InformacionTarjeta from '@/components/InformacionTarjeta'

export default {
  name: 'Index',
  component: {
    TablaJugadores,
    InformacionTarjeta
  },
  data() { return { } },
  computed: {
    ...mapState(['equipo'])
  },
  created() {
    this.getEquipo()
  },
  methods: {
    ...mapActions(['getEquipo'])
  },
}
</script>

<style scoped>
  .v-list--dense > i {
    font-size: 21px;
  }
</style>