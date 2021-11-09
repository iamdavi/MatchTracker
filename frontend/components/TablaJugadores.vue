<template>
  <v-card>
    <v-data-table
      :headers="cabeceraTabla"
      :items="equipoActual.jugadores"
      :items-per-page="-1"
      hide-default-footer
      class="elevation-1"
    >
    </v-data-table>
  </v-card>
</template>
<script>
// import { mapState } from 'vuex'

export default {
  // components: { 
  //   FormularioEquipo 
  // },
  name: 'TablaJugadores',
  // eslint-disable-next-line vue/require-prop-types
  props: ['equipoActual'],
  data() {
    return {
      cabeceraTabla: [
        { text: 'Id', align: 'left', value: 'id' },
        { text: 'Numero', align: 'left', value: 'numero' },
        { text: 'Nombre', align: 'center', value: 'nombre' },
      ]
    }
  },
  // computed: {
  //   ...mapState(['equipoActual'])
  // }
}
</script>