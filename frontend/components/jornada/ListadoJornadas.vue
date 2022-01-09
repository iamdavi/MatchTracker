<template>
	<v-row>
		<v-col 
			v-for="jornada in jornadas" 
			:key="jornada.id"
			cols="12"
		>
			<h2 class="d-inline">Jornada número {{ jornada.numero }}</h2>
			<p class="d-inline ml-3 subtitle-1">{{ formatDate(jornada.fecha) }}</p>
			<v-btn
				color="primary"
 				class="mb-2"
				icon
			>
				<v-icon>mdi-pencil</v-icon>
      </v-btn>
		</v-col>
	</v-row>
</template>

<script>
import { mapActions } from 'vuex'

export default {
	data() {
		return {
			
		}
	},
	computed: {
		jornadas() {
			return this.$store.state.jornada.jornadas
		}
	},
	created() {
		this.getJornadas()
	},
	methods: {
		...mapActions({
      getJornadas: 'jornada/getJornadas'
    }),
		formatDate(date) {
			if (!date) return null
			const [year, month, day] = date.split('-')
			return `${day.slice(0,2)} / ${month} / ${year}`
		}
	},
}
</script>

<style>
	
</style>