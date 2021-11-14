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
            <v-list-item-title>
              <v-icon color="error" class="mr-2">
                mdi-delete
              </v-icon> 
              <span>Eliminar</span>
            </v-list-item-title>
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
}
</script>