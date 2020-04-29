<template>
  <div class="article-page">
    <div class="boder1 pb10 pt10 pl10">文章列表</div>
    <div class="mt15">
      <el-form class="mt30" ref="form"  label-position="left" :model="form" status-icon label-width="60px">
        <el-row :gutter="10">
          <el-col :span="5">
            <el-form-item label="文章id">
              <el-input-number v-model="form.article_id" :max="99" :controls="false" :step='1' step-strictly></el-input-number>
            </el-form-item>
          </el-col>
          <el-col :span="5">
            <el-form-item label="文章名" prop="article_title">
              <el-input v-model="form.article_title" placeholder="文章名"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="2"><el-button type="primary" @click="onSubmit('form')">搜索</el-button></el-col>
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
          prop="article_id"
          label="文章id"
          width="100">
        </el-table-column>
        <el-table-column
          prop="article_title"
          label="文章名">
        </el-table-column>
        <el-table-column
          prop="article_alias"
          label="文章别名">
        </el-table-column>
        <el-table-column
          prop="article_order"
          label="排序">
        </el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="300">
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
    <!-- 新增 -->
    <el-dialog
      title="新增文章"
      :visible.sync="dialogVisible"
      width="30%">
      <div>
        <el-form ref="form2" :model="form2" :rules="rules" label-width="80px">
          <el-row :gutter="10">
            <el-form-item label="文章名" prop="article_title">
              <el-input v-model="form2.article_title" :maxlength="25" show-word-limit placeholder="请输入文章名"></el-input>
            </el-form-item>
            <el-form-item label="文章别名" prop="article_title">
              <el-input v-model="form2.article_alias" :maxlength="25" show-word-limit placeholder="请输入文章别名"></el-input>
            </el-form-item>
          </el-row>
        </el-form>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button size="small"  @click="dialogVisible = false">取 消</el-button>
        <el-button size="small" :disabled="loading"  type="primary" @click="addHandle('form2')">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 编辑 -->
    <el-dialog
      title="文章编辑"
      :visible.sync="updatemodal"
      width="60%">
      <div>
        <el-form ref="form3" :model="form3" :rules="rules" label-width="80px">
          <el-row :gutter="10">
            <el-form-item label="文章名" prop="article_title">
              <el-input v-model="form3.article_title" :maxlength="25" show-word-limit placeholder="请输入文章名"></el-input>
            </el-form-item>
            <el-form-item label="文章别名" prop="article_alias">
              <el-input v-model="form3.article_alias" :maxlength="25" show-word-limit placeholder="请输入文章别名"></el-input>
            </el-form-item>
            <el-form-item label="文章logo">
              <el-input v-model="form3.article_img" placeholder="请输入标题"></el-input>
            </el-form-item>
            <el-form-item label="排序">
              <el-input-number v-model="form3.article_order" :max="99" :controls="false" :step='1' step-strictly></el-input-number>
            </el-form-item>
            <el-form-item label="描述">
              <el-input v-model="form3.article_description" type="textarea" :row="2" :maxlength="500" show-word-limit  placeholder="请输入描述"></el-input>
            </el-form-item>
          </el-row>
        </el-form>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button size="small"  @click="updatemodal = false">取 消</el-button>
        <el-button size="small" :disabled="loading"  type="primary" @click="updateHandle('form3')">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
import { getArticleList,addArticle,articleDelete,articleUpdate } from '@/api/article'
export default {
  name: 'userPage',
  data () {
    return {
      pageIndex: 1,
      pageSize: 6,
      total: 0,
      dialogVisible: false, // 添加弹窗
      updatemodal: false, // 编辑弹窗
      loading: false,
      form: {
        article_id: '', // article_id
        article_title: '', // article_title
      },
      form2: {
        article_title: null, // article_title
        article_alias: null, // 别名
      },
      form3: {
        article_id: null,
        article_title: null,
        article_alias: null,
        article_description: null,
        article_img: null,
      },
      tableData: [],
      rules: {
        article_title: [
          { required: true,message: '请输入文章名称',trigger: 'blur' }
        ],
        article_alias: [
          { required: true,message: '请输入文章别名',trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    onSubmit(form) {
      this.$refs[form].validate((valid) => {
        if (valid) {
          this.queryList()
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      this.pageSize = val
      this.queryList()
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.pageIndex = val
      this.queryList()
    },
    handleClick(row) {
      console.log(row)
      this.form3 = Object.assign(this.form3,row)
      this.updatemodal = true
    },
    delClick(row) {
      console.log(row)
      this.$confirm('此操作将永久删除该类目, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.queryDelete(row.article_id)
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });
    },
    queryList() {
      const param = {
        data: {
          article_id: this.form.article_id,
          article_title: this.form.article_title,
          pageIndex: this.pageIndex,
          pageSize: this.pageSize
        }
      }
      getArticleList(param).then(res => {
        this.tableData = res.data.data
        this.total = res.data.total;
      },err => {
        this.$message.error(err.msg);
        console.log(err)
      })
    },
    addArticleQuery() {
      const param = {
        data: {
          article_title: this.form2.article_title,
          article_alias: this.form2.article_alias
        }
      }
      this.loading = true
      addArticle(param).then(res => {
        this.dialogVisible=false
        this.loading = false
        this.queryList()
        this.resetForm('form2')
        this.$message(
          {
            message: '添加成功!',
            type: 'success',
          }
        )
      },err => {
        this.loading = false
        this.$message.error(err.msg);
        console.log(err)
      })
    },
    addHandle(form) {
      this.$refs[form].validate((valid) => {
        console.log(valid)
        if (valid) {
          this.addArticleQuery();
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    updateQuery() {
      const param = {
        data: null
      }
      param.data = this.form3
      param.data.article_show = param.data.article_show ? 1 : 2
      this.loading = true
      articleUpdate(param).then(res => {
        this.updatemodal=false
        this.loading = false
        this.resetForm('form3')
        this.queryList()
        this.$message(
          {
            message: '修改成功!',
            type: 'success',
          }
        )
      },err => {
        this.loading = false
        this.$message.error(err.msg);
        console.log(err)
      })
    },
    updateHandle() {
      this.updateQuery()
    },
    queryDelete(article_id) {
      const param = {
        data: {
          article_id
        }
      }
      this.loading = true
      articleDelete(param).then(res => {
        this.loading = false
        this.queryList()
        this.$message(
          {
            message: '删除成功!',
            type: 'success',
          }
        )
      },err => {
        this.loading = false
        this.$message.error(err.msg);
        console.log(err)
      })
    },
  },
  mounted () {
    this.queryList()
  }
}
</script>
