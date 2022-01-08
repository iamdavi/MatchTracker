<template>
	<div>
		<v-stepper v-model="paso" class="mb-3" alt-labels non-linear>
			<v-stepper-header>
				<v-stepper-step :completed="paso > 1" step="1" class="stepper-title" :editable="paso > 1">Selecciona equipo</v-stepper-step>
				<v-divider></v-divider>
				<v-stepper-step :completed="paso > 2" step="2" class="stepper-title" :editable="paso > 2">Datos del equipo</v-stepper-step>
				<v-divider></v-divider>
				<v-stepper-step :completed="paso > 3" step="3" class="stepper-title">Datos de los jugadores</v-stepper-step>
			</v-stepper-header>
			<v-stepper-items>
				<v-stepper-content step="1">
					<h2 class="inner-stepper-title">Selecciona equipo</h2>
					<step-one class="my-5" />
					<v-btn
						color="primary"
						block
						@click="setJugadoresOfEquipo(); paso = 2"
					>
						Continue
					</v-btn>
				</v-stepper-content>

				<v-stepper-content step="2">
					<h2 class="inner-stepper-title">Datos del equipo</h2>
					<equipo-form class="my-5" titulo="" />
					<v-btn
						color="primary"
						block
						@click="paso = 3"
					>
						Continue
					</v-btn>
				</v-stepper-content>

				<v-stepper-content step="3">
					<h2 class="inner-stepper-title">Datos de los jugadores</h2>
					<tabla-jugadores class="my-5" />
					<v-btn
						color="primary"
						block
						@click="newEquipoJugadores()"
					>
						Guardar equipo
					</v-btn>
				</v-stepper-content>

			</v-stepper-items>
		</v-stepper>

		<v-card class="create-form-card text-center">
		</v-card>
	</div>
</template>

<script>
import { mapActions } from 'vuex'
import StepOne from '@/components/StepOne'
import TablaJugadores from '@/components/TablaJugadores'
import EquipoForm from '@/components/equipo/EquipoForm'

export default {
	name: 'Start',
  components: { 
    StepOne,
    TablaJugadores,
    EquipoForm
  },
	layout: 'empty',
	data() {
		return {
			paso: 1
		}
	},
	methods: {
		...mapActions({
      newEquipoJugadores: 'equipo/newEquipoJugadores'
    }),
    setJugadoresOfEquipo() {
      const jugadores = []
      const equipo = this.$store.state.equipo.equipo
      const liga = this.$store.state.equipo.ligas.ligas.filter(liga => liga.nombre === equipo.liga)[0]
      const jugadoresEquipo = liga.equipos[equipo.nombre]
      jugadoresEquipo.forEach(jugador => {
        jugadores.push({
          numero: jugador[0],
          nombre: jugador[1]
        })
      });
      this.$store.commit('jugador/setJugadores', jugadores)
    }
	},
}
</script>

<style>
.v-application--is-ltr .v-stepper__label {
	text-align: center !important;
}

.inner-stepper-title {
	display: none;
}

@media (max-width: 959px) {
	.inner-stepper-title {
		display: block;
	}
}
</style>