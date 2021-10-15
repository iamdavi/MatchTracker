<template>
  <v-card>
    <v-data-table
      :headers="cabeceraTabla"
      :items="equipos"
      :items-per-page="-1"
      hide-default-footer
      class="elevation-1"
    >
    </v-data-table>
  </v-card>
</template>
<script>
import { mapActions, mapState } from 'vuex'

export default {
  // components: { 
  //   FormularioEquipo 
  // },
  name: 'TablaJugadores',
  data() {
    return {
      cabeceraTabla: [
        { text: 'Id', align: 'left', value: 'id' },
        { text: 'Nombre', align: 'left', value: 'nombre' },
        { text: 'Descripcion', align: 'center', value: 'descripcion' },
      ]
    }
  },
  computed: {
    ...mapState(['equipos', 'equipo'])
  },
  created() {
    this.getEquipos()
  },
  methods: {
    ...mapActions(['getEquipos', 'newEquipo', 'removeEquipo'])
  },
}
</script>