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
          <!-- <el-col :span="5">
              <el-cascader
                placeholder="请选择类目"
                v-model="cateArr"
                :options="options"
                :props="optionProps"
                collapse-tags
                clearable></el-cascader>
          </el-col> -->
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
          label="ID"
          width="100">
        </el-table-column>
        <el-table-column
          prop="article_title"
          label="标题">
        </el-table-column>
        <el-table-column
          prop="article_publish_time"
          label="发布时间">
        </el-table-column>
        <el-table-column
          prop="article_status"
          label="状态">
          <template slot-scope="scope">
            {{scope.row.article_status | statusfiler}}
          </template>
        </el-table-column>
        <el-table-column
          prop="article_alias"
          label="热门">
          <template slot-scope="scope">
            <el-switch
              v-model="scope.row.cate_show"
              @change="cateShowHandle(scope.row)"
              >
            </el-switch>
          </template>
        </el-table-column>
        <el-table-column
          prop="article_alias"
          label="推荐">
          <template slot-scope="scope">
            <el-switch
              v-model="scope.row.cate_show"
              @change="cateShowHandle(scope.row)"
              >
            </el-switch>
          </template>
        </el-table-column>
        <el-table-column
          prop="article_order"
          label="排序">
        </el-table-column>
        <el-table-column
          prop="article_like_count"
          label="点赞">
        </el-table-column>
        <el-table-column
          prop="article_browse_count"
          label="浏览">
        </el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="180">
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
    <!-- 编辑 -->
    <el-dialog
      title="文章编辑"
      :visible.sync="updatemodal"
      width="60%">
      <div>
        <el-form ref="form3" :model="form3" :rules="rules" label-width="80px">
          <el-row :gutter="10">
            <el-form-item label="标题" prop="article_title">
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
import { catelevels } from '@/api/cate'
export default {
  name: 'userPage',
  data () {
    return {
      pageIndex: 1,
      pageSize: 10,
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
      },
      options: [],
      cateArr: [],
      optionProps: {
        multiple: true,
        checkStrictly: true,
        value: 'cate_id',
        label: 'cate_name',
        children: 'children'
      },
    }
  },
  filters: {
    statusfiler: function(key) {
      switch (key) {
        case 0:
          return '草稿';
          break;
        case 1:
          return '公开';
          break;
        case 2:
          return '审核';
          break;
        case 3:
          return '回收站';
          break;
        default:
          break;
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
      this.$confirm('此操作将永久删除该文章, 是否继续?', '提示', {
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
      if (this.cateArr.length>0) {
        let a = []
        for (let index = 0; index < this.cateArr.length; index++) {
          const element = this.cateArr[index];
          a = [...a, ...element]
        }
        console.log(a)
        const cateTulp = new Set(a)
        // console.log(cateTulp)
        param.data.cateArr = [...cateTulp].join(',')
      }
      // console.log('queryList--',param); return false;
      getArticleList(param).then(res => {
        this.tableData = res.data.data
        this.total = res.data.total;
      },err => {
        this.$message.error(err.msg);
        console.log(err)
      })
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
    qeuryOneList() {
      catelevels().then(res => {
        if (res.data.length>0) {
          // const data = res.data.map(item => {
          //   return { value: item.cate_id, label: item.cate_name }
          // })
          const data = res.data

          console.log('-----------------------',this.options)
          this.$nextTick(() => {
            this.options = this.options.concat(data)
          })
        }
      },err => {
        this.$message.error(err.msg);
        console.log(err)
      })
    },
  },
  mounted () {
    this.queryList()
    this.qeuryOneList();
  }
}
</script>
