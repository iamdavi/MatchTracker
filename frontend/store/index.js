export const state = () => ({
  baseUrl: 'http://127.0.0.1:8000/api',
  loggedInUser: {
    email: '',
    username: '',
  },
  equipos: [],
  equipo: {
    nombre: '',
    descripcion: ''
  }
})

export const mutations = {
  setLoggedInUser(state, payload) {
    state.loggedInUser = payload
  },
  setEquipo(state, payload) {
    state.equipo = payload
  },
  updateEquipoNombre(state, payload) {
    state.equipo.nombre = payload
  },
  updateEquipoDescripcion(state, payload) {
    state.equipo.descripcion = payload
  },
  setEquipos(state, payload) {
    state.equipos = payload
  },
  updateEquipos(state, payload) {
    state.equipos.push(payload)
  },
  setRemoveEquipo(state, payload) {
    state.equipos = state.equipos.filter(item => item.id !== payload)
  }
}

export const actions = {
  // Usuario logeado
  setLoggedInUser({ commit }) {
    // console.log('llega');
    commit('setLoggedInUser', {})
  },
  // Todos los equipos
  async getEquipos({ commit, state }) {
    const equipos = []
    // const path = state.baseUrl + '/equipos'
    try {
      const res = await this.$axios.get('/equipos')
      res.data.forEach(equipo => { equipos.push(equipo) });
      commit('setEquipos', equipos)
    } catch (error) {
    }
  },
  // Equipo concreto
  async getEquipo({ commit, state }, idEquipo) {
    try {
      const res = await this.$axios.get(`/equipos/${idEquipo}`)
      commit('setEquipo', res.data)
    } catch (error) {
    }
  },
  async editEquipo({ commit, state }, idEquipo) {
    try {
      const res = await this.$axios.put(`/equipos/${idEquipo}`, state.equipo)
      commit('setEquipo', res.data)
    } catch (error) {
    }
  },
  async removeEquipo({ commit, state }, idEquipo) {
    try {
      await this.$axios.delete(`/equipos/${idEquipo}`)
      commit('setRemoveEquipo', idEquipo)
    } catch (error) {
    }
  },
  async newEquipo({ commit, state }, equipo) {
    try {
      const res = await this.$axios.post('/equipos/', equipo)
      state.equipo.nombre = ''
      state.equipo.descripcion = ''
      commit('updateEquipos', res.data)
    } catch (error) {
    }
  }
}