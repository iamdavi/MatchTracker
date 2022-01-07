export const state = () => ({
  ligas: [],
  equipos: [],
  equipo: {
    nombre: '',
    descripcion: '',
    color: '',
    liga: ''
  },
  equipoYaExiste: false
})

export const mutations = {
  setLigas(state, payload) {
    state.ligas = payload
  },
  setEquipo(state, payload) {
    state.equipo = payload
  },
  setEquipoYaExiste(state, payload) {
    state.equipoYaExiste = payload
  },
  updateEquipo(state, payload) {
    Object.entries(payload).forEach(campo => {
      state.equipo[campo[0]] = campo[1]
    });
  },
}

export const actions = {
  async nuxtServerInit({ commit }) {
    try {
      await this.$axios.get('/equipo/').then(res => {
        commit('setEquipo', res.data)
        commit('setEquipoYaExiste', true)
      })
    } catch (error) {
      commit('setEquipo', {
        nombre: '',
        descripcion: '',
        color: '#1976d2'
      })
    }
  },
  async getEquipo({ commit }) {
    try {
      await this.$axios.get('/equipo/').then(res => {
        commit('setEquipo', res.data)
        commit('setEquipoYaExiste', true)
        commit('jugador/setJugadores', res.data.jugadores, { root: true })
      })
    } catch (error) {
      commit('setEquipo', {
        nombre: '',
        descripcion: '',
        color: '#1976d2'
      })
    }
  },
  async getLigasEquiposDisponibles({ commit }) {
    try {
      await this.$axios.get('/equipos/disponibles/').then(res => {
        commit('setLigas', res.data)
      })
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se han podido obtener las ligas disponibles'
      })
    }
  },
  async editEquipo({ commit, state }) {
    try {
      await this.$axios.put('/equipo/', state.equipo).then(res => {
        commit('setEquipo', res.data)
			  this.$router.push('/')
      })
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se ha podido editar el equipo'
      })
    }
  },
  async removeEquipo({ commit }) {
    try {
      await this.$axios.delete('/equipo/').then(() => {
        commit('setEquipo', {})
        commit('setEquipoYaExiste', false)
        this.$router.push('/start')
      })
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se ha podido eliminar el equipo'
      })
    }
  },
  async newEquipo({ commit, state }) {
    try {
      await this.$axios.post('/equipo/', state.equipo).then(res => {
        commit('setEquipo', res.data)
        commit('setEquipoYaExiste', true)
      })
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se ha podido crear el equipo'
      })
    }
  },
  async newEquipoJugadores({ commit, state, rootState }) {
    try {
      const data = { ...state.equipo, jugadores: [...rootState.jugador.jugadores] }
      await this.$axios.post('/equipo/', data).then(res => {
        const equipoData = {
          nombre: res.data.nombre,
          descripcion: res.data.descripcion,
          color: res.data.color
        }
        commit('setEquipo', equipoData)
        commit('jugador/setJugadores', res.data.jugadores, { root: true })
        commit('setEquipoYaExiste', true)
			  this.$router.push('/')
      })
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se ha podido crear el equipo'
      })
    }
  }
}