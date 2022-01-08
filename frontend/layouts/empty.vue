<template>
  <v-app>
    <v-app-bar app>
      <v-spacer />
      <v-toolbar-title v-text="'Match Tracker'" />
      <v-spacer />
    </v-app-bar>
    <v-container fill-height>
      <v-row justify="center">
        <v-col lg="8" md="10" sm="12">
          <Nuxt />
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: 'Empty',
  data () { return { } },
}
</script>