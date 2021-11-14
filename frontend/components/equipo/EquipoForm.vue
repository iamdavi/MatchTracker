<template>
	<v-row>
		<v-col cols="12">
			<v-text-field
				v-model="nombre"
				:counter="50"
				label="Nombre"
				required
			></v-text-field>
		</v-col>
		<v-col cols="12">
			<v-text-field
				v-model="descripcion"
				:counter="250"
				label="Descripcion"
			></v-text-field>
		</v-col>
		<v-col cols="12">
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
		</v-col>
	</v-row>
</template>

<script>
import { mapState } from 'vuex'
import { mapFields } from '@/helpers'

export default {
  name: 'EquipoForm',
  data() {
    return {
			e1: 1,
			valid: false,
			menu: false,
    }
  },
  computed: {
    ...mapState(['equipo']),
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
  }
}
</script>