<template>
  <div>
    <h1>{{ rival.nombre }}</h1>
    <v-card>
      <tabla-jugadores />
    </v-card>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import TablaJugadores from '@/components/TablaJugadores'

export default {
  name: "DetalleRival",
	component: {
		TablaJugadores
	},
  computed: {
    rival() {
      return this.$store.state.rival.rival
    }
  },
  created() {
    const id = this.$route.params.id
    this.getRival(id)
  },
	methods: {
		...mapActions({
      getRival: 'rival/getRival'
    }),
	},
}
</script>

<style>

</style>