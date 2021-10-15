<template>
  <v-row>
    <v-col cols="12" sm="12" md="6">
      <h1>Información</h1>
      <v-card>
        <v-card-title>
          Munttarpe
        </v-card-title>
        <v-card-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas ut purus vitae tellus commodo viverra. Quisque eu molestie lorem. Nam vitae posuere augue. Sed turpis tellus, ullamcorper eu aliquet id, bibendum in libero. Integer ultricies interdum ante, a tincidunt neque tristique eu. In hendrerit ipsum vitae semper varius. Praesent a turpis ac lectus facilisis faucibus. Suspendisse auctor velit sed massa finibus tincidunt. 
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" sm="12" md="6">
      <h1>Jugadores</h1>
      <tabla-jugadores />
    </v-col>
  </v-row>
</template>

<script>
import TablaJugadores from '@/components/TablaJugadores'

export default {
  name: 'Index',
  component: {
    TablaJugadores
  },
  data() {
    return {
    }
  }
}
</script>

<style scoped>
  .login-card {
    max-width: 500px;
  }
</style>