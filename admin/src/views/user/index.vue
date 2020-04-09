<template>
  <div class="user-page">
    <div class="boder1 pb10 pt10 pl10">用户列表 <el-button class="ml15" type="primary" size="small" @click="dialogVisible=true">新增用户</el-button></div>
    <div class="mt15">
      <el-form class="mt30" ref="form" :model="form" label-width="60px">
        <el-row :gutter="10">
          <el-col :span="5">
            <el-form-item label="ID">
              <el-input v-model="form.id" placeholder="用户id"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="5">
            <el-form-item label="用户名">
              <el-input v-model="form.name" placeholder="nickname"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="5">
            <el-form-item label="邮箱">
              <el-input v-model="form.emial" placeholder="xxxx@qq.com"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="5">
            <el-form-item label="手机">
              <el-input v-model="form.emial" placeholder="132****18"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="4"><el-button type="primary" @click="onSubmit">搜索</el-button></el-col>
        </el-row>
      </el-form>
    </div>
    <div class="mt15">
      <el-table
        :data="tableData"
        border
        style="width: 100%">
        <!-- <el-table-column
          label="序号"
          type="index"
          width="50">
        </el-table-column> -->
        <el-table-column
          prop="id"
          label="用户id"
          width="100">
        </el-table-column>
        <el-table-column
          prop="name"
          label="用户名"
          width="150">
        </el-table-column>
        <el-table-column
          prop="six"
          label="性别"
          width="100">
        </el-table-column>
        <el-table-column
          prop="email"
          label="用户邮箱"
          width="200">
        </el-table-column>
        <el-table-column
          prop="phone"
          label="用户手机"
          width="150">
        </el-table-column>
        <el-table-column
          prop="ip"
          label="用户ip"
          width="150">
        </el-table-column>
        <el-table-column
          prop="time"
          label="注册时间"
          width="150">
        </el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="200">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="primary" size="small">编辑</el-button>
            <el-button @click="delClick(scope.row)" type="danger" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="tr mt15">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page.sync="pageIndex"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total">
        </el-pagination>
      </div>
    </div>
    <el-dialog
      title="新增用户"
      :visible.sync="dialogVisible"
      width="30%">
      <div>
        <el-form ref="form2" :model="form" label-width="80px">
          <el-row :gutter="10">
            <el-form-item label="用户名">
              <el-input v-model="form.name" placeholder="nickname"></el-input>
            </el-form-item>
            <el-form-item label="邮箱">
              <el-input v-model="form.emial" placeholder="xxxx@qq.com"></el-input>
            </el-form-item>
            <el-form-item label="手机">
              <el-input v-model="form.emial" placeholder="132****18"></el-input>
            </el-form-item>
            <el-form-item label="密码">
              <el-input v-model="form.pass" placeholder="" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="确认密码">
              <el-input v-model="form.checkPass" placeholder="" autocomplete="off"></el-input>
            </el-form-item>
          </el-row>
        </el-form>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button size="small"  @click="dialogVisible = false">取 消</el-button>
        <el-button size="small"  type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
import { getUserList } from '@/api/user'
export default {
  name: 'userPage',
  data () {
    return {
      pageIndex: 1,
      pageSize: 10,
      total: 0,
      dialogVisible: false,
      form: {
        id: '', // 用户id
        name: '', // 用户名
        email: '', // 用户邮箱
        phone: '', // 用户手机
      },
      tableData: []
    }
  },
  methods: {
    onSubmit() {
      console.log(this.$refs.form)
    },
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
    },
    handleClick(row) {
      console.log(row)
    },
    delClick(row) {
      console.log(row)
    },
    queryList() {
      const param = {
        data: {
          pageIndex: this.pageIndex,
          pageSize: this.pageSize
        }
      }
      getUserList(param).then(res => {
        this.tableData = res.data.data;
        this.total = res.data.total;
      })
    },
  },
  mounted () {
    this.queryList()
  }
}
</script>
