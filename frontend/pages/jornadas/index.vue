<template>
	<v-row justify="center">
		<v-col md="8" sm="12" >
			<v-row>
				<v-col cols="12">
					<h1>Jornadas</h1>
				</v-col>
				<v-col cols="12">
					<tarjeta-crear-jornada></tarjeta-crear-jornada>
				</v-col>
				<v-col cols="12">
					<listado-jornadas></listado-jornadas>
				</v-col>
			</v-row>
		</v-col>
	</v-row>
</template>

<script>
import TarjetaCrearJornada from '@/components/jornada/TarjetaCrearJornada'
import ListadoJornadas from '@/components/jornada/ListadoJornadas'

export default {
  name: 'Jornadas',
	components: {
		TarjetaCrearJornada,
		ListadoJornadas
	},
  data() {
    return {
    }
  }
}
</script>