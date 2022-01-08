<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      :clipped="clipped"
      style="height: 100% !important;"
      fixed
      app
    >
      <v-list>
        <v-list-item link class="text-center user-data-navbar">
          <v-list-item-content>
            <v-list-item-title class="text-h6">
              {{ $auth.user.username }}
            </v-list-item-title>
            <v-list-item-subtitle>
              {{ $auth.user.email }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
        <!-- Logged in menu items -->
      </v-list>
      <template #append>
        <color-mode-picker />
      </template>
    </v-navigation-drawer>
    <v-app-bar
      :clipped-left="clipped"
      fixed
      app
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title v-text="title" />
      <v-spacer />
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer app>
      <span>By: <b>David Otero</b> &amp; <b>Txema Otero</b></span>
    </v-footer>
  </v-app>
</template>

<script>
import { mapState } from 'vuex'
import ColorModePicker from "@/components/ColorModePicker";

export default {
  components: {
    ColorModePicker
  },
  middleware: 'necesitaEquipo',
  data () {
    return {
      clipped: true,
      drawer: false,
      items: [
        {
          icon: 'mdi-home',
          title: 'Inicio',
          to: '/'
        },
        {
          icon: 'mdi-handball',
          title: 'Jugadores',
          to: '/jugadores'
        },
        {
          icon: 'mdi-sword-cross',
          title: 'Rivales',
          to: '/rivales'
        },
        {
          icon: 'mdi-soccer',
          title: 'Partidos',
          to: '/#'
        },
        {
          icon: 'mdi-strategy',
          title: 'Jugadas',
          to: '/#'
        },
        {
          icon: 'mdi-logout',
          title: 'Cerrar sesion',
          to: '/logout'
        }
      ],
      miniVariant: true,
      right: true,
      rightDrawer: false,
      title: 'Match Tracker'
    }
  },
  computed: {
    ...mapState('auth', ['loggedIn'])
  }
}
</script>

<style scoped>
.user-data-navbar {
  min-height: 125px;
}
</style>