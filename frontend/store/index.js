export const state = () => ({
  baseUrl: 'http://127.0.0.1:8000/api',
  equipos: [],
  jugadores: [],
  jugador: {
    numero: '',
    nombre: ''
  },
  equipo: {
    nombre: '',
    descripcion: '',
    color: ''
  },
  equipoYaExiste: false
})

export const mutations = {
  // EQUIPO
  setEquipo(state, payload) {
    state.equipo = payload
  },
  updateEquipo(state, payload) {
    Object.entries(payload).forEach(campo => {
      state.equipo[campo[0]] = campo[1]
    });
  },
  setEquipoYaExiste(state, payload) {
    state.equipoYaExiste = payload
  },
  // JUGADORES
  setJugadores(state, payload) {
    state.jugadores = payload
  },
  removeJugador(state, jugadorId) {
    const index = state.jugadores.findIndex(item => item.id === jugadorId)
    state.jugadores.splice(index, 1)
  },
  addJugador(state, payload) {
    state.jugadores.push(payload)
  },
  // JUGADOR
  setJugador(state, payload) {
    state.jugador = payload
  },
  updateJugador(state, payload) {
    Object.entries(payload).forEach(campo => {
      state.jugador[campo[0]] = campo[1]
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
  // EQUIPO ACTUAL
  async editEquipo({ commit }, equipo) {
    try {
      await this.$axios.put('/equipo/', equipo).then(res => {
        commit('setEquipo', res.data)
			  this.$router.push('/')
      })
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se ha podido editar el equipo'
      })
    }
  },
  async getEquipo({ commit }) {
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
  // JUGADORES
  async getJugadores({ commit }) {
    try {
      await this.$axios.get('/jugadores/').then(res =>  commit('setJugadores', res.data) )
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se ha podido obtener los jugadores'
      })
    }
  },
  async editJugador({ commit }, jugador) {
    try {
      await this.$axios.put(`/jugadores/${jugador.id}/`, jugador).then(res => commit('setJugador', res.data) )
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se ha podido editar el jugador'
      })
    }
  },
  async removeJugador({ commit, state }) {
    try {
      await this.$axios.delete(`/jugadores/${state.jugador.id}/`).then(() => {
        commit('removeJugador', state.jugador.id)
        commit('setJugador', {numero: "", nombre: ""})
      })
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se ha podido eliminar el equipo'
      })
    }
  },
  async newJugador({ commit, state }) {
    try {
      await this.$axios.post('/jugadores/', state.jugador).then(res => {
        commit('addJugador', res.data)
        commit('setJugador', {numero: "", nombre: ""})
      })
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se ha podido eliminar el equipo'
      })
    }
  }
}