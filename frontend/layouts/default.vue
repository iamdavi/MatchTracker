<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      expand-on-hover
      style="height: 100% !important;"
      fixed
      app
    >
      <v-list>
        <v-list-item link>
          <v-list-item-content>
            <v-list-item-title class="text-h6">
              Sandra Adams
            </v-list-item-title>
            <v-list-item-subtitle>sandra_a88@gmail.com</v-list-item-subtitle>
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
      <span>By: <b>David Otero</b></span>
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
          to: '/'
        },
        {
          icon: 'mdi-sword-cross',
          title: 'Rivales',
          to: '/'
        },
        {
          icon: 'mdi-soccer',
          title: 'Partidos',
          to: '/'
        },
        {
          icon: 'mdi-strategy',
          title: 'Jugadas',
          to: '/'
        },
        {
          icon: 'mdi-logout',
          title: 'Logout',
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
