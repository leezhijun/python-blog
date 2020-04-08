<template>
  <div class="site-page">
    <div class="boder1 pb10 pt10 pl10">邮件服务</div>
    <el-form class="mt30" ref="form" :model="form" label-width="120px">
      <el-form-item label="SMTP服务器">
        <el-input v-model="form.smtp_url" placeholder="如：smtp.163.com"></el-input>
      </el-form-item>
      <el-form-item label="SMTP端口号">
        <el-input v-model="form.smtp_port" placeholder="一般为 25 或 465"></el-input>
      </el-form-item>
      <el-form-item label="发件人邮箱">
        <el-input v-model="form.smtp_emial"></el-input>
      </el-form-item>
      <el-form-item label="发件人昵称">
        <el-input v-model="form.smtp_nickname"></el-input>
      </el-form-item>
      <el-form-item label="邮箱登入密码">
        <el-input v-model="form.smtp_password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交保存</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  name: 'sitePageEmail',
  data () {
    return {
      form: {
        smtp_url: '', // SMTP服务器
        smtp_port: '', // SMTP端口号
        smtp_emial: '', // 发件人邮箱
        smtp_nickname: '', // 发件人昵称
        smtp_password: '', // 邮箱登入密码
      }
    }
  }
}
</script>
<style lang="scss" scoped>

</style>
