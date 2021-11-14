<template>
	<v-row justify="center">
		<v-col md="8" sm="12" >
			<h1>Jugadores</h1>
			<tabla-jugadores />
		</v-col>
	</v-row>
</template>
<script>
import { mapState } from 'vuex'
import TablaJugadores from '@/components/TablaJugadores'

export default {
	name: 'Jugadores',
	data() {
		return {
			
		}
	},
	component: {
		TablaJugadores
	},
  computed: {
    ...mapState(['equipo'])
  },
}
</script>