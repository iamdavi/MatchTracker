<template>
  <div>
    <v-row>
      <v-col cols="12" sm="12" md="6">
		    <h1>Información</h1>
        <informacion-tarjeta :equipo="equipo" />
      </v-col>
      <v-col cols="12" sm="12" md="6">
        <div class="d-flex align-center justify-space-between">
          <h1>Jugadores</h1>
          <v-btn color="primary" to="/jugadores">Ver todo</v-btn>
        </div>
        <v-card>
          <tabla-jugadores :items-per-page="7" />
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import TablaJugadores from '@/components/TablaJugadores'
import InformacionTarjeta from '@/components/InformacionTarjeta'

export default {
  name: 'Index',
  component: {
    TablaJugadores,
    InformacionTarjeta
  },
  data() { return { cargando: true } },
  computed: {
    equipo() {
      return this.$store.state.equipo.equipo
    }
    // ...mapState({
    //   equipo: 'equipo/equipo'
    // })
  },
  created() {
    this.getEquipo()
  },
  updated() {
    this.cargando = false
  },
  methods: {
    ...mapActions({
      getEquipo: 'equipo/getEquipo'
    })
  },
}
</script>

<style scoped>
  .v-list--dense > i {
    font-size: 21px;
  }
</style>