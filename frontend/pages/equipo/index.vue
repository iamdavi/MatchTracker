<template>
	<v-container fill-height>
		<v-row justify="center">
			<v-col md="5" sm="12">
				<v-card v-on:keyup.enter="editEquipo()" class="text-center pa-3">
					<equipo-form /> <!-- Formulario de equipo -->
          <div class="d-flex justify-space-between mt-5">
            <v-btn text to="/">
              Cancelar
            </v-btn>
            <v-btn
              color="primary"
						  @click="editEquipo()"
            >
              Continuar
            </v-btn>
          </div>
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
import { mapActions } from 'vuex'
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
	methods: {
    ...mapActions({
      editEquipo: 'equipo/editEquipo'
    }),
    prueba() {
      console.log('algo');
    }
  }
}
</script>