<template>
	<v-form v-model="valid">
		<v-container v-if="titulo">
			<v-row>
				<v-col class="text-center pb-0">
					<h2>{{ titulo }}</h2>
				</v-col>
			</v-row>
		</v-container>
			<v-text-field
				v-model="nombre"
				:counter="50"
				label="Nombre"
				class="pt-0"
				required
			></v-text-field>
			<v-text-field
				v-model="descripcion"
				:counter="250"
				label="Descripcion"
			></v-text-field>
	</v-form>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { mapFields } from '@/helpers'

export default {
  name: 'EquipoForm',
	props: {
		titulo: {
			type: String,
			required: false,
			default: 'Información del equipo'
		}
	},
  data() {
    return {
			menu: false,
			valid: false,
    }
  },
  computed: {
    ...mapState({
			equipo: 'equipo/equipo', 
			equipoYaExiste: 'equipo/equipoYaExiste'
		}),
		...mapFields({
			fields: ["nombre", "descripcion", "color"],
			base: "equipo",
			mutation: "equipo/updateEquipo"
		}),
		swatchStyle() {
			const color = this.equipo ? this.equipo.color : '#1976d2'
      return {
        backgroundColor: color,
        cursor: 'pointer',
        height: '30px',
        width: '30px',
        borderRadius: this.menu ? '50%' : '4px',
        transition: 'border-radius 200ms ease-in-out'
      }
    }
  },
  created() {
	  this.getEquipo()
  },
	methods: {
	  ...mapActions({
		  getEquipo: 'equipo/getEquipo', 
		  newEquipo: 'equipo/newEquipo', 
		  editEquipo: 'equipo/editEquipo'
		}),
	},
}
</script>

<style scoped>

.shadow-0 {
	box-shadow: none !important;
}
</style>