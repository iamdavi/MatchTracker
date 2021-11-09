<template>
    <v-container fill-height>
      <v-row justify="center">
        <v-col md="5" sm="12">
			<v-card class="create-form-card mx-auto text-center">
				<v-stepper v-model="e1">
					<v-stepper-header>
						<v-stepper-step
							:complete="e1 > 1"
							editable
							step="1"
						>
						</v-stepper-step>

						<v-divider></v-divider>

						<v-stepper-step
							:complete="e1 > 2"
							editable
							step="2"
						>
						</v-stepper-step>

					</v-stepper-header>

					<v-stepper-items>
						<v-stepper-content step="1" class="stepper-create-form-content">
								<v-form 
									v-model="valid"
									@submit.prevent="formEquipo"
								>
									<v-container>
										<v-row>
											<v-col class="text-center">
												<h2>Información del equipo</h2>
											</v-col>
											<v-col cols="12">
												<v-text-field
													v-model="equipo.nombre"
													:rules="nameRules"
													:counter="50"
													label="Nombre"
													required
												></v-text-field>
											</v-col>
											<v-col cols="12">
												<v-text-field
													v-model="equipo.descripcion"
													:rules="nameRules"
													:counter="250"
													label="Descripcion"
												></v-text-field>
											</v-col>
											<v-col cols="12">
												<v-text-field
													v-model="equipo.color"
													:rules="nameRules"
													:counter="7"
													label="Color del equipo"
												></v-text-field>
											</v-col>
										</v-row>
									</v-container>
									<v-btn
										type="submit"
										color="primary"
										@click="e1 = 2"
									>
										Continue
									</v-btn>

									<v-btn text>
										Cancel
									</v-btn>
								</v-form>
						</v-stepper-content>

						<v-stepper-content step="2">
							<v-card
							class="mb-12"
							color="grey lighten-1"
							height="200px"
							></v-card>

							<v-btn
							color="primary"
							@click="e1 = 3"
							>
								Continue
							</v-btn>

							<v-btn text>
								Cancel
							</v-btn>
						</v-stepper-content>

					</v-stepper-items>
				</v-stepper>
			</v-card>
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'EquipoNew',
  data() {
    return {
			e1: 1,
			yaExiste: false
    }
  },
  computed: {
    ...mapState(['equipo'])
  },
  created() {
	  this.getEquipo()
		if (this.equipo.nombre !== '') {
			this.yaExiste = true
		}
  },
  methods: {
	  ...mapActions(['getEquipo', 'newEquipo', 'editEquipo']),
	  formEquipo() {
		  if (this.yaExiste) {
				this.editEquipo();
			} else {
				this.newEquipo();
			}
	  }
  },
}
</script>

<style scoped>
  /* .create-form-card {
  } */
	.stepper-create-form-content {
		padding: 4px 16px 16px 16px; 
	} 
</style>