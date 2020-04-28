<template>
  <div class="login-page">
    <div class="login-form">
      <h3 class="tc f24 c333">blogAdmin</h3>
      <el-form class="mt20" :model="ruleForm" status-icon :rules="rules" ref="ruleForm">
        <el-form-item prop="username">
          <el-input v-model.trim="ruleForm.username" placeholder="请输入用户名">
            <i slot="prefix" class="el-input__icon el-icon-user"></i>
          </el-input>
        </el-form-item>
        <el-form-item prop="pass">
          <el-input type="password" v-model="ruleForm.pass" placeholder="请输入密码" autocomplete="off">
            <i slot="prefix" class="el-input__icon el-icon-lock"></i>
          </el-input>
        </el-form-item>
        <el-form-item prop="checkPass">
          <el-input type="password" v-model="ruleForm.checkPass" placeholder="请输入重复密码" autocomplete="off">
            <i slot="prefix" class="el-input__icon el-icon-lock"></i>
          </el-input>
        </el-form-item>
        <el-form-item class="tc">
          <el-button type="primary" @click="submitForm('ruleForm')" style="width:100%">登陆</el-button>
          <!-- <el-button @click="resetForm('ruleForm')">重置</el-button> -->
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script>
import { login } from '@/api/login'
import { getToken } from '@/utils/auth.js'
export default {
  name: 'LoginPage',
  data () {
    var checkUserName = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入用户名'));
      } else {
        callback();
      }
    };
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
      if (this.ruleForm.checkPass !== '') {
        this.$refs.ruleForm.validateField('checkPass');
      }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.ruleForm.pass) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };

    return {
      ruleForm: {
        username: '',
        pass: '',
        checkPass: ''
      },
      rules: {
        username: [
          { validator: checkUserName, trigger: 'blur' }
        ],
        pass: [
          { validator: validatePass, trigger: 'blur' }
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur' }
        ],
      }
    }
  },
  methods: {
    queryLogin() {
      const param = {
        data: {
          username: this.ruleForm.username,
          password: this.ruleForm.pass,
        }
      }
      login(param).then(res => {
        console.log(res)
        this.$router.push({ path: '/' })
      }, err => {
        this.$message.error(err.msg);
        console.log(err)
      })
    },
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.queryLogin();
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  },
  mounted () {
    const token = getToken() // 获取token
    if (token) { // 有值表示已经登陆
      this.$router.push({ name: 'HomePage' })
    }
  }
}
</script>
<style lang="scss" scoped>
.login-page{
  width: 100%;
  height: 100%;
  background-color: #f2f2f2;
  color: #666;
}
.login-form{
  width: 300px;
  margin: 0 auto;
  position: relative;
  top: 50%;
  transform:translateY(-50%);
}
</style>
