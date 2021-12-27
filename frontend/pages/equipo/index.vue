<template>
	<v-container fill-height>
		<v-row justify="center">
			<v-col md="5" sm="12">
				<v-card class="create-form-card text-center">
					<equipo-form /> <!-- Formulario de equipo -->
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
import EquipoForm from '@/components/equipo/EquipoForm'

export default {
  name: 'Equipo',
	components: {
		EquipoForm
	},
  data() {
    return {
    }
  },
}
</script>