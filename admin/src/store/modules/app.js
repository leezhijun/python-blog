const app = {
  state: {
    isCollapse: false, // navbar折叠/展开
  },
  mutations: {
    toggleCollapse(state) {
      state.isCollapse = !state.isCollapse
    }
  },
  actions: {},
  getters: {}
}

export default app
