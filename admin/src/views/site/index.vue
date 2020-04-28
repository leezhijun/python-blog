<template>
  <div class="site-page">
    <div class="boder1 pb10 pt10 pl10">基础设置</div>
    <el-form class="mt30" ref="form" :model="form" :rules="rules" label-width="120px">
      <el-form-item label="网站名称">
        <el-input v-model="form.site_name"></el-input>
      </el-form-item>
      <el-form-item label="网址" prop="site_url">
        <el-input v-model="form.site_url" placeholder="https://xxx.com/"></el-input>
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
      <el-form-item label="站点邮箱" prop="site_email">
        <el-input v-model="form.site_email"></el-input>
      </el-form-item>
      <el-form-item label="备案信息">
        <el-input v-model="form.site_copy"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('form')">提交保存</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import { getSiteExpandList,updateSiteIndex } from '@/api/site'
export default {
  name: 'sitePage',
  data () {
    const checkEmail = (rule, value, callback) => {
      const reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"); // 正则表达式
      if (value&&!reg.test(value)) {
        callback(new Error('请输入正确的邮箱'));
      } else {
        callback();
      }
    };
    const checkUrl = (rule, value, callback) => {
      const reg = new RegExp("[a-zA-z]+://[^\s]*"); // 正则表达式
      if (value&&!reg.test(value)) {
        callback(new Error('请输入正确的网址'));
      } else {
        callback();
      }
    };
    return {
      form: {
        site_name: '', // 站点名称
        site_url: '', // 网址
        site_title: '', // 站点名称
        site_keywords: '', // 关键词
        site_descript: '', // 描述
        site_email: '', // 站点邮箱
        site_copy: '' // 备案信息
      },
      rules: {
        site_email: [
          { validator: checkEmail, trigger: 'blur' }
        ],
        site_url: [
          { validator: checkUrl, trigger: 'blur' }
        ],
      }
    }
  },
  methods: {
    queryInfo() {
      getSiteExpandList().then(res => {
        console.log(res)
        const data = res.data
        this.form = Object.assign(this.form,data)
        console.log(this.form)
      }, err => {
        this.$message.error(err.msg);
        console.log(err)
      })
    },
    queryForm() {
      const param = {
        data: {
          site_name: this.form.site_name, // 站点名称
          site_url: this.form.site_url, // 网址
          site_title: this.form.site_title, // 站点名称
          site_keywords: this.form.site_keywords, // 关键词
          site_descript: this.form.site_descript, // 描述
          site_email: this.form.site_email, // 站点邮箱
          site_copy: this.form.site_copy // 备案信息
        }
      }
      updateSiteIndex(param).then(res => {
        this.$message({
          message: '保存成功',
          type: 'success'
        })
        this.queryInfo()
      }, err => {
        this.$message.error(err.msg);
        console.log(err)
      })
    },
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.queryForm();
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
  },
  mounted () {
    this.queryInfo()
  }
}
</script>
<style lang="scss" scoped>

</style>
