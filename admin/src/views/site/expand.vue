<template>
  <div class="site-expand">
    <div class="boder1 pb10 pt10 pl10">拓展设置</div>
    <div class="mt15">
      <el-form class="mt30" ref="form" :model="form" label-width="40px">
        <el-row :gutter="20">
          <el-col :span="6">
            <el-form-item label="键">
              <el-input v-model="form.key" placeholder="如：site_uploadMax"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="描述">
              <el-input v-model="form.des" placeholder="如：最大上传"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="值">
              <el-input v-model="form.key" placeholder="对应值"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="6"><el-button type="primary" @click="onSubmit">新增</el-button></el-col>
        </el-row>
      </el-form>
    </div>
    <div class="mt15">
      <el-table
        :data="tableData"
        border
        style="width: 100%">
        <el-table-column
          label="序号"
          type="index"
          width="50">
        </el-table-column>
        <el-table-column
          prop="key"
          label="键"
          width="150">
        </el-table-column>
        <el-table-column
          prop="des"
          label="描述"
          width="400">
        </el-table-column>
        <el-table-column
          prop="val"
          label="值">
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
  </div>
</template>
<script>
import { getSiteExpandList } from '@/api/site'
export default {
  name: 'siteExpand',
  data () {
    return {
      pageIndex: 1,
      pageSize: 10,
      total: 0,
      form: {
        key: '', // 键
        des: '', // 描述
        val: '', // 值
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
          pageSize: this.pageSize,
        }
      }
      getSiteExpandList(param).then((res) => {
        console.log(res)
        this.tableData = res.data.data;
        this.total = res.data.total;
      })
    }
  },
  mounted () {
    this.queryList()
  }
}
</script>
<style lang="scss" scoped>

</style>
