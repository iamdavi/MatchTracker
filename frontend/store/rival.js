export const state = () => ({
  rivales: [],
  rival: {
    nombre: '',
    descripcion: ''
  }
})

export const mutations = {
  setRivales(state, payload) {
    state.rivales = payload
  },
  setRival(state, payload) {
    state.rival = payload
  }
}

export const actions = {
  async getRivales({ commit }) {
    try {
      await this.$axios.get('/rivales/').then(res => commit('setRivales', res.data))
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se han podido cargar los rivales'
      })
    }
  },
  async getRival({ commit }, id) {
    try {
      await this.$axios.get(`/rivales/${id}/`).then(res => {
        commit('setRival', res.data)
        commit('jugador/setJugadores', res.data.jugadores, { root: true })
      })
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se han podido obtener la informaciond el rival'
      })
    }
  }
}