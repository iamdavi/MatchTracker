<template>
  <v-card class="d-flex justify-space-between px-4 rounded-0">
    <v-icon>mdi-brightness-6</v-icon>
    <v-switch
      v-model="darkTheme"
      class="mx-5 "
      @click="switchTheme()"
    ></v-switch>
    <v-icon>mdi-brightness-4</v-icon>
  </v-card>
</template>

<script>
  export default {
    name: 'ColorModePicker',
    data() {
      return {
        darkTheme: false
      }
    },
    mounted() {
      if (localStorage.darkTheme) {
        this.darkTheme = true
        this.switchTheme()
      }
    },
    methods: {
      switchTheme () {
        if (this.darkTheme) {
          this.$vuetify.theme.dark = true;
          localStorage.darkTheme = true
        } else {
          localStorage.removeItem('darkTheme')
          this.$vuetify.theme.dark = false;
        }
      }
    }
  }
</script>