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
						@click="paso = 2"
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
						@click="newEquipo(); paso = 3"
					>
						Continue
					</v-btn>
				</v-stepper-content>

				<v-stepper-content step="3">
					<h3 class="inner-stepper-title">Datos de los jugadores</h3>
					<equipo-form />
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
import EquipoForm from '@/components/equipo/EquipoForm'

export default {
	name: 'Start',
	layout: 'empty',
	component: {
		EquipoForm,
		StepOne
	},
	data() {
		return {
			paso: 1
		}
	},
	methods: {
		...mapActions(['newEquipo'])
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