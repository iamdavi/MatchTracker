export const state = () => ({
  jugadores: [],
  jugador: {
    numero: '',
    nombre: ''
  }
})

export const mutations = {
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
  async editJugador({ commit, state }) {
    const jugador = state.jugador
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