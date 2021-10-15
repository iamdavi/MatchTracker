<template>
  <div></div>
</template>

<script>
export default {
  data() {
    return {
      refresh: this.$auth.strategy.refreshToken.get()
    }
  },
  created() {
    this.logoutUser()
  },
  methods: {
    async logoutUser() {
      await this.$auth.logout({
        data: {
          refresh: this.refresh
        }
      })
    }
  },
}
</script>