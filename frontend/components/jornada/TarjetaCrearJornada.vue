<template>
	<v-card>
		<v-container>
			<v-row justify="space-between">
				<v-col md="12" sm="12" xs="12">
					<v-toolbar-title class="pl-0">
						Crear jornada
					</v-toolbar-title>
				</v-col>
			</v-row>
			<v-row justify="space-between">
				<v-col md="12" sm="12" xs="12">
					<v-row>
						<v-col sm="auto">
							<v-icon>mdi-order-numeric-ascending</v-icon>
						</v-col>
						<v-col>
							<v-text-field
								v-model="numero"
								label="Número"
								class="d-inline"
								hide-details
							/>
						</v-col>
						<v-col sm="auto">
							<v-icon>mdi-calendar</v-icon>
						</v-col>
						<v-col>
							<v-menu
								v-model="menu1"
								:close-on-content-click="false"
								max-width="290"
							>
								<template #activator="{ on, attrs }">
									<v-text-field
										:value="computedDateFormatted"
										class="pa-0 ma-0"
										clearable
										hide-details
										label="Fecha"
										readonly
										v-bind="attrs"
										v-on="on"
										@click:clear="fecha= null"
									></v-text-field>
								</template>
								<v-date-picker
									v-model="fecha"
									@change="menu1 = false"
								></v-date-picker>
							</v-menu>
						</v-col>
					</v-row>
				</v-col>
			</v-row>
			<v-row justify="space-between">
				<v-col md="12" sm="12" xs="12">
					<v-btn 
						color="primary" 
						block
						@click="newJornada()"
					>
						Crear
						<v-icon>mdi-plus</v-icon>
					</v-btn>
				</v-col>
			</v-row>
		</v-container>
	</v-card>
</template>

<script>
import { mapActions } from 'vuex'
import { mapFields } from '@/helpers'

export default {
	data() {
		return {
			menu1: false
		}
	},
	computed: {
		jornada() {
			return this.$store.state.jornada.jornada
		},
		computedDateFormatted() {
			return this.formatDate(this.fecha)
		},
		...mapFields({
			fields: ["numero", "fecha"],
			base: "jornada",
			mutation: "jornada/updateJornada"
		}),
	},
	methods: {
		formatDate (date) {
			if (!date) return null
			const [year, month, day] = date.split('-')
			return `${day}/${month}/${year}`
		},
		...mapActions({
      newJornada: 'jornada/newJornada'
    }),
  },
}
</script>

<style>
	
</style>