<template>
  <div>
    <h1>Rivales</h1>
    <v-row>
      <v-col
        v-for="rival in rivales"
        :key="rival.id"
        lg="3"
        md="6"
        sm="6"
        xs="12"
      >
        <v-card>
          <v-app-bar
            flat
            color="rgba(0, 0, 0, 0)"
          >
            <v-toolbar-title class="text-h6 pl-0">
              {{ rival.nombre }}
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              :to="`/rivales/${rival.id}`"
              icon
            >
              <v-icon>mdi-eye</v-icon>
            </v-btn>
          </v-app-bar>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Rivales',
	data() {
		return {
		}
	},
  computed: {
    rivales() {
      return this.$store.state.rival.rivales
    }
  },
  created() {
    this.getRivales()
  },
	methods: {
		...mapActions({
      getRivales: 'rival/getRivales'
    }),
	},
}
</script>

<style>

</style>