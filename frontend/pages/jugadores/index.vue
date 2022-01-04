<template>
	<v-row justify="center">
		<v-col md="8" sm="12" >
			<div class="d-flex align-center justify-space-between">
				<h1>Jugadores</h1>
				<v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              v-bind="attrs"
              v-on="on"
            >
              Crear
							<v-icon
								right
								dark
							>
								mdi-plus
							</v-icon>
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">Crear jugador</span>
            </v-card-title>

            <v-form @submit.prevent="newJugador()">
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                      md="2"
                      cols="12"
                    >
                      <v-text-field
                        v-model="numero"
                        label="Número"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      md="10"
                      cols="12"
                    >
                      <v-text-field
                        v-model="nombre"
                        label="Nombre"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions class="d-flex justify-space-between">
                <v-btn
                  color="blue darken-1"
                  text
                  @click="dialog = false"
                >
                  Cancelar
                </v-btn>
                <v-btn
                  color="primary"
                  type="submit"
                >
                  Crear
                </v-btn>
              </v-card-actions>
            </v-form>
          </v-card>
        </v-dialog>
			</div>
      <v-card>
			  <tabla-jugadores />
      </v-card>
		</v-col>
	</v-row>
</template>
<script>
import { mapState, mapActions } from 'vuex'
import TablaJugadores from '@/components/TablaJugadores'
import { mapFields } from '@/helpers'

export default {
	name: 'Jugadores',
	data() {
		return {
			dialog: false		
		}
	},
	component: {
		TablaJugadores
	},
  computed: {
    ...mapState({
      equipo: 'equipo/equipo', 
      jugador: 'jugador/jugador'
    }),
		...mapFields({
			fields: ["numero", "nombre"],
			base: "jugador",
			mutation: "jugador/updateJugador"
		}),
  },
	methods: {
		...mapActions({
      newJugador: 'jugador/newJugador'
    }),
		close() {
      this.dialog = false
		}
	},
}
</script>