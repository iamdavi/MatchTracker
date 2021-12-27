<template>
	<v-form 
		v-model="valid"
		@submit.prevent="formEquipo"
	>
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
			<v-text-field 
				v-model="color" 
				hide-details
				class="ma-0 pa-0" 
				solo
			>
				<template #append>
					<v-menu v-model="menu" top nudge-bottom="105" nudge-left="16" :close-on-content-click="false">
						<template #activator="{ on }">
							<div :style="swatchStyle" v-on="on" />
						</template>
						<v-card>
							<v-card-text class="pa-0">
								<v-color-picker v-model="color" hide-inputs flat />
							</v-card-text>
						</v-card>
					</v-menu>
				</template>
			</v-text-field>
			<p class="mb-0 text--secondary" style="font-size: 12px;">Color corporativo del equipo</p>
			<!-- <div class="d-flex justify-space-between mt-5">
				<v-btn text to="/">
					Cancelar
				</v-btn>
				<v-btn
					type="submit"
					color="primary"
				>
					Continuar
				</v-btn>
			</div> -->
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
    ...mapState(['equipo', 'equipoYaExiste']),
		...mapFields({
			fields: ["nombre", "descripcion", "color"],
			base: "equipo",
			mutation: "updateEquipo"
		}),
		swatchStyle() {
      return {
        backgroundColor: this.equipo.color,
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
	  ...mapActions(['getEquipo', 'newEquipo', 'editEquipo']),
	  formEquipo() {
		  if (this.equipoYaExiste) {
				this.editEquipo(this.equipo);
			} else {
				this.newEquipo(this.equipo);
			}
	  }
	},
}
</script>

<style scoped>

.shadow-0 {
	box-shadow: none !important;
}
</style>