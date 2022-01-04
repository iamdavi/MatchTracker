<template>
	<div>
		<v-select
			v-model="liga"
			label="Liga en la que juegas"
			class="pt-0"
			:items="ligas"
			@change="getEquiposFromLiga()"
		></v-select>

		<v-select
			v-model="nombre"
			label="Equipo"
			:items="equipos"
		></v-select>
	</div>
</template>
<script>
import { mapActions } from 'vuex'
import { mapFields } from '@/helpers'

export default {
	name: 'StepOne',
	data() {
		return {
			equipos: [],
			ligaSeleccionada: '',
		}
	},
	computed: {
		ligas() {
			if (this.$store.state.equipo.ligas.ligas) {
				return this.$store.state.equipo.ligas.ligas.map(liga => liga.nombre);
			}
			return []
		},
		...mapFields({
			fields: ["nombre", "liga"],
			base: "equipo",
			mutation: "equipo/updateEquipo"
		}),
	},
	created() {
		this.getEquiposDisponibles();
	},
	methods: {
		...mapActions({
			getEquiposDisponibles: 'equipo/getLigasEquiposDisponibles'
		}),
		getEquiposFromLiga() {
			this.equipos = Object.keys(this.$store.state.equipo.ligas.ligas.find(liga => liga.nombre === this.$store.state.equipo.equipo.liga).equipos);
		}
	},
}
</script>