export const state = () => ({
  baseUrl: 'http://127.0.0.1:8000/api',
  equipos: [],
  jugadores: [],
  equipo: {
    nombre: '',
    descripcion: '',
    color: ''
  }
})

export const mutations = {
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
  // EQUIPO ACTUAL
  async editEquipo({ commit, state }) {
    try {
      const res = await this.$axios.put('/equipo/', state.equipo)
      commit('setEquipo', res.data)
    } catch (error) {
      this.$toasted.global.defaultError({
        msg: 'No se ha podido editar el equipo'
      })
    }
  },
  async getEquipo({ commit }) {
    try {
      const res = await this.$axios.get('/equipo/')
      console.log(typeof res.data[0])
      commit('setEquipo', res.data[0])
    } catch (error) {
      this.$toasted.global.defaultError({
        msg: 'No se ha podido obtener el equipo'
      })
    }
  },
  async removeEquipo({ commit }) {
    try {
      await this.$axios.delete('/equipo/')
      commit('setEquipo', {})
    } catch (error) {
    }
  },
  async newEquipo({ commit }, equipo) {
    try {
      const res = await this.$axios.post('/equipo/', equipo)
      commit('setEquipo', res.data)
    } catch (error) {
    }
  },
  // async newEquipo({ commit }, equipo) {
  //   try {
  //     const res = await this.$axios.post('/equipo/', equipo)
  //     commit('updateEquipos', res.data)
  //   } catch (error) {
  //   }
  // },
  // async getEquipos({ commit }) {
  //   const equipos = []
  //   try {
  //     const res = await this.$axios.get('/equipos')
  //     res.data.forEach(equipo => { equipos.push(equipo) });
  //     commit('setEquipos', equipos)
  //   } catch (error) {
  //   }
  // },
  // EQUIPO CONCRETO
  // async getEquipo({ commit, state }, idEquipo) {
  //   try {
  //     const res = await this.$axios.get(`/equipos/${idEquipo}`)
  //     commit('setEquipo', res.data)
  //   } catch (error) {
  //     this.$toasted.global.defaultError({
  //       msg: 'No se pudo obtener el equipo'
  //     })
  //   }
  // },
  // async editEquipo({ commit, state }, idEquipo) {
  //   try {
  //     const res = await this.$axios.put(`/equipos/${idEquipo}`, state.equipo)
  //     commit('setEquipo', res.data)
  //   } catch (error) {
  //   }
  // },
}