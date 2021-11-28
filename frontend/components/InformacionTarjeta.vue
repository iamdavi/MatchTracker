<template>
  <v-card>
    <v-card-title>
      <span :style="{ 'color': equipo.color }">{{ equipo.nombre }}</span>
      <v-spacer></v-spacer>
      <v-menu offset-y left>
        <template #activator="{ on, attrs }">
          <v-btn
            icon
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
        <v-list dense>
          <v-list-item link to="/equipo">
            <v-list-item-title>
              <v-icon color="primary" class="mr-2">
                mdi-pencil
              </v-icon> 
              <span>Editar</span>
            </v-list-item-title>
          </v-list-item>
          <v-list-item link>
      <v-dialog
        transition="dialog-bottom-transition"
        max-width="600"
      >
        <template #activator="{ on, attrs }">
          <v-list-item-title 
            v-bind="attrs"
            v-on="on"
          >
            <v-icon color="error" class="mr-2">
              mdi-delete
            </v-icon> 
            <span>Eliminar</span>
          </v-list-item-title>
        </template>
        <template #default="dialog">
          <v-card>
            <v-card-title>
              Estás seguro de que quieres eliminar el equipo? Perderás todos los 
              datos registrados, las jugadas, los jugadores las estadísticas...
            </v-card-title>
            <v-card-actions class="d-flex justify-space-between mt-5">
              <v-btn
                text
                @click="dialog.value = false"
              >Cancelar</v-btn>
              <v-btn
                text
                @click="removeEquipo(); dialog.value = false"
              >Aceptar</v-btn>
            </v-card-actions>
          </v-card>
        </template>
      </v-dialog>

            <!-- <v-list-item-title @click="eliminarEquipo()">
              <v-icon color="error" class="mr-2">
                mdi-delete
              </v-icon> 
              <span>Eliminar</span>
            </v-list-item-title> -->
          </v-list-item>
        </v-list>
      </v-menu>
    </v-card-title>
    <v-card-text>
      {{ equipo.descripcion }}
    </v-card-text>
  </v-card>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'InformacionTarjeta',
  props: {
    equipo: {
			type: Object,
			default: Object
    }
  },
  data() {
    return {
    }
  },
  computed: {
    ...mapState(['equipo'])
  },
  methods: {
    ...mapActions(['removeEquipo'])
  },
}
</script>