export const state = () => ({
  jornadas: [],
  jornada: {
    numero: '',
    fecha: ''
  }
})

export const mutations = {
  setJornada(state, payload) {
    state.jornada = payload
  },
  setJornadas(state, payload) {
    state.jornadas = payload
	},
  updateJornada(state, payload) {
    Object.entries(payload).forEach(campo => {
      state.jornada[campo[0]] = campo[1]
    });
  },
	addJornada(state, payload) {
		state.jornadas.push(payload)
	}
}

export const actions = {
  async getJornadas({ commit }) {
    try {
      await this.$axios.get('/jornadas/').then(res => commit('setJornadas', res.data))
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se han podido cargar las jornadas'
      })
    }
  },
	async newJornada({ commit, state }) {
		try {
			await this.$axios.post('/jornadas/', state.jornada).then(res => {
				commit('addJornada', res.data)
				commit('setJornada', {
					numero: '',
					fecha: ''
				})
			})
		} catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se ha podido crear la jornada'
      })
		}
	},
  async getJornada({ commit }, id) {
    try {
      await this.$axios.get(`/jornadas/${id}/`).then(res => {
        commit('setJornada', res.data)
      })
    } catch (error) {
      this.$toast.global.defaultError({
        msg: 'No se han podido obtener la informaciond de la jornada'
      })
    }
  }
}