<template>
	<v-container fill-height>
		<v-row justify="center">
			<v-col md="5" sm="12">
				<v-card class="create-form-card text-center">
					<v-form 
						v-model="valid"
						@submit.prevent="formEquipo"
					>
						<v-container>
							<v-row>
								<v-col class="text-center pb-0">
									<h2>Información del equipo</h2>
								</v-col>
							</v-row>

							<equipo-form /> <!-- Formulario de equipo -->

							<div class="d-flex justify-space-between mt-5">
								<v-btn text to="/">
									Cancelar
								</v-btn>
								<v-btn
									type="submit"
									color="primary"
									@click="e1 = 2"
								>
									Continuar
								</v-btn>
							</div>
						</v-container>
					</v-form>
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import EquipoForm from '@/components/equipo/EquipoForm'

export default {
  name: 'Equipo',
	components: {
		EquipoForm
	},
  data() {
    return {
			e1: 1,
			valid: false,
			menu: false,
    }
  },
  computed: {
    ...mapState(['equipo']),
		yaExiste() {
			return this.equipo.nombre !== ''
		},
		equipoForm() {
			return { ...this.equipo }
		},
  },
  created() {
	  this.getEquipo()
  },
  methods: {
	  ...mapActions(['getEquipo', 'newEquipo', 'editEquipo']),
	  formEquipo() {
		  if (this.yaExiste) {
				this.editEquipo(this.equipo);
			} else {
				this.newEquipo(this.equipo);
			}
			this.$router.push('/')
	  }
  }
}
</script>