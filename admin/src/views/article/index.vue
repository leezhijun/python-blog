<template>
  <div class="article-page">
    <div class="boder1 pb10 pt10 pl10">文章列表</div>
    <div class="mt15">
      <el-form class="mt30" ref="form" :model="form" label-width="80px">
        <el-row :gutter="10">
          <el-col :span="5">
            <el-form-item label="文章id">
              <el-input v-model="form.id" placeholder="标签id"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="5">
            <el-form-item label="文章标题">
              <el-input v-model="form.title" placeholder="文章标题"></el-input>
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
        <el-table-column
          label="序号"
          type="index"
          width="50">
        </el-table-column>
        <!-- <el-table-column
          prop="id"
          label="文章id"
          width="100">
        </el-table-column> -->
        <el-table-column
          prop="title"
          label="标题"
          width="200">
        </el-table-column>
        <el-table-column
          prop="keyword"
          label="关键词"
          width="200">
        </el-table-column>
        <el-table-column
          prop="time"
          label="发布时间"
          width="200">
        </el-table-column>
        <el-table-column
          prop="weight"
          label="权重"
          width="200">
        </el-table-column>
        <el-table-column
          prop="status"
          label="状态">
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
import { getArticleList } from '@/api/article'
export default {
  name: 'userPage',
  data () {
    return {
      pageIndex: 1,
      pageSize: 10,
      total: 0,
      dialogVisible: false,
      form: {
        name: '', // cate名称
        nickename: '' // cate昵称
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
      getArticleList(param).then(res => {
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
