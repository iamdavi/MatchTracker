<template>
	<div>
		<v-select
			v-model="ligaSeleccionada"
			label="Liga en la que juegas"
			class="pt-0"
			:items="ligas"
			@change="getEquiposDb()"
		></v-select>

		<v-select
			v-model="nombre"
			label="Equipo"
			:items="equipos"
		></v-select>
	</div>
</template>
<script>
import equiposDb from '@/data/equipos.json'
import { mapFields } from '@/helpers'

export default {
	name: 'StepOne',
	data() {
		return {
			ligas: [],
			equipos: [],
			ligaSeleccionada: null
		}
	},
	computed: {
		...mapFields({
			fields: ["nombre"],
			base: "equipo",
			mutation: "updateEquipo"
		}),
	},
	created() {
		this.ligas = equiposDb.ligas.map(liga => liga.nombre);
	},
	methods: {
		getEquiposDb() {
			this.equipos = Object.keys(equiposDb.ligas.find(liga => liga.nombre === this.ligaSeleccionada).equipos);
		}
	},
}
</script>