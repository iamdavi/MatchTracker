<template>
  <v-card>
    <v-data-table
      :headers="cabeceraTabla"
      :items="equipo.jugadores"
      :items-per-page="-1"
      hide-default-footer
      sort-by="numero"
      class="elevation-1"
    >
      <template #top>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <v-card>
            <v-card-title>
              <span class="text-h5">Editar jugador</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col md="2" sm="12" cols="12">
                    <v-text-field
                      v-model="numero"
                      label="Número"
                    ></v-text-field>
                  </v-col>
                  <v-col md="10" sm="12" cols="12">
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
                text
                @click="close"
              >
                Cancelar
              </v-btn>
              <v-btn
                color="primary"
                @click="editEquipo(equipo.id); dialog = false"
              >
                Guardar 
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title>Seguro que quieres eliminar el equipo {{ equipo.nombre }}?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="removeEquipo(equipo.id); dialogDelete = false">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
          </v-dialog>
        </template>
        <template #[`item.acciones`]="{ item }">
          <v-icon
            small
            class="mr-2"
            @click="setJugador(item); dialog = true"
          >
            mdi-pencil
          </v-icon>
          <v-icon
            small
            @click="deleteItem(item)"
          >
            mdi-delete
          </v-icon>
        </template>
    </v-data-table>
  </v-card>
</template>

<script>
import { mapState, mapActions, mapMutations } from 'vuex'
import { mapFields } from '@/helpers'

export default {
  name: 'TablaJugadores',
  components: {},
  data() {
    return {
      cabeceraTabla: [
        { text: 'Numero', align: 'left', value: 'numero' },
        { text: 'Nombre', align: 'center', value: 'nombre' },
        { text: 'Acciones',align:'right', value: 'acciones', sortable: false },
      ],
      dialog: false,
      dialogDelete: false,
      editedIndex: -1,
      editedItem: {
        name: '',
        calories: 0,
        fat: 0,
        carbs: 0,
        protein: 0,
      },
      defaultItem: {
        name: '',
        calories: 0,
        fat: 0,
        carbs: 0,
        protein: 0,
      },
    }
  },
  computed: {
    ...mapState(['equipo', 'jugador']),
		...mapFields({
			fields: ["numero", "nombre"],
			base: "jugador",
			mutation: "updateJugador"
		}),
  },
  watch: {
    dialog (val) {
      val || this.close()
    },
    dialogDelete (val) {
      val || this.closeDelete()
    },
  },
  created() {
    this.getEquipo()
  },
  methods: {
    ...mapActions(['getEquipo', 'editEquipo', 'newEquipo', 'removeEquipo']),
    ...mapMutations(['setJugador']),
    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    closeDelete () {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
  },
}
</script>
