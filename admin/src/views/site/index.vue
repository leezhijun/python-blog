<template>
  <div class="site-page">
    <div class="boder1 pb10 pt10 pl10">基础设置</div>
    <el-form class="mt30" ref="form" :model="form" label-width="120px">
      <el-form-item label="网站名称">
        <el-input v-model="form.site_name"></el-input>
      </el-form-item>
      <el-form-item label="网址">
        <el-input v-model="form.site_url"></el-input>
      </el-form-item>
      <el-form-item label="网站标题">
        <el-input v-model="form.site_title"></el-input>
      </el-form-item>
      <el-form-item label="关键词">
        <el-input v-model="form.site_keywords"></el-input>
      </el-form-item>
      <el-form-item label="站点描述">
        <el-input v-model="form.site_descript" type="textarea" :row="2"></el-input>
      </el-form-item>
      <el-form-item label="站点邮箱">
        <el-input v-model="form.site_email"></el-input>
      </el-form-item>
      <el-form-item label="备案信息">
        <el-input v-model="form.site_copy"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交保存</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  name: 'sitePage',
  data () {
    return {
      form: {
        site_name: '', // 站点名称
        site_url: '', // 网址
        site_title: '', // 站点名称
        site_keywords: '', // 关键词
        site_descript: '', // 描述
        site_email: '', // 站点邮箱
        site_copy: '' // 备案信息
      }
    }
  }
}
</script>
<style lang="scss" scoped>

</style>
