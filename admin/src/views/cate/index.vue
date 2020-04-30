<template>
  <div class="cate-page">
    <div class="boder1 pb10 pt10 pl10">分类列表 <el-button class="ml15" type="primary" size="small" @click="dialogVisible=true">新增分类</el-button></div>
    <div class="mt15">
      <el-form class="mt30" label-position="left" ref="form" :model="form" status-icon label-width="60px">
        <el-row :gutter="10">
          <el-col :span="5">
            <el-form-item label="分类id">
              <el-input-number v-model="form.cate_id" :controls="false" :step='1' step-strictly></el-input-number>
            </el-form-item>
          </el-col>
          <el-col :span="5">
            <el-form-item label="分类名" prop="cate_name">
              <el-input v-model="form.cate_name" placeholder="分类名"></el-input>
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
          prop="cate_id"
          label="分类id"
          width="100">
        </el-table-column>
        <el-table-column
          prop="cate_name"
          label="分类名">
        </el-table-column>
        <el-table-column
          prop="cate_order"
          label="排序">
        </el-table-column>
        <el-table-column
          prop="cate_show"
          label="默认菜单">
          <template slot-scope="scope">
            <el-switch
              v-model="scope.row.cate_show"
              @change="cateShowHandle(scope.row)"
              >
            </el-switch>
          </template>
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
      title="新增分类"
      :visible.sync="dialogVisible"
      width="30%">
      <div>
        <el-form ref="form2" :model="form2" :rules="rules" label-width="80px">
          <el-row :gutter="10">
            <el-form-item label="分类名" prop="cate_name">
              <el-input v-model="form2.cate_name" :maxlength="25" show-word-limit placeholder="请输入分类名"></el-input>
            </el-form-item>
            <el-form-item label="父级">
              <!-- <el-select v-model="form2.cate_parent_id" placeholder="请选择">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select> -->
              <el-cascader :options="options" :props="optionProps" v-model="form2.cate_parent_id" :show-all-levels="false"></el-cascader>
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
      title="分类编辑"
      :visible.sync="updatemodal"
      width="60%">
      <div>
        <el-form ref="form3" :model="form3" :rules="rules" label-width="80px">
          <el-row :gutter="10">
            <el-form-item label="分类名" prop="cate_name">
              <el-input v-model="form3.cate_name" :maxlength="25" show-word-limit placeholder="请输入分类名"></el-input>
            </el-form-item>
            <el-form-item label="分类logo">
              <el-input v-model="form3.cate_img" placeholder="请输入标题"></el-input>
            </el-form-item>
            <el-form-item label="排序">
              <el-input-number v-model="form3.cate_order" :max="99" :controls="false" :step='1' step-strictly></el-input-number>
            </el-form-item>
            <el-form-item label="默认菜单">
              <el-switch v-model="form3.cate_show"></el-switch>
            </el-form-item>
            <el-form-item label="标题">
              <el-input v-model="form3.cate_title" :maxlength="100" show-word-limit  placeholder="请输入标题"></el-input>
            </el-form-item>
            <el-form-item label="关键词">
              <el-input v-model="form3.cate_keywords" :maxlength="125" show-word-limit  placeholder="请输入关键词"></el-input>
            </el-form-item>
            <el-form-item label="描述">
              <el-input v-model="form3.cate_description" type="textarea" :row="2" :maxlength="500" show-word-limit  placeholder="请输入描述"></el-input>
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
import { getCateList,addCate,cateDelete,cateUpdate,catelevels,cateUpdateShow } from '@/api/cate'
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
        cate_id: '', // cate_id
        cate_name: '', // cate_name
      },
      form2: {
        cate_name: null, // cate_name
        cate_parent_id: [0], // 父级id
      },
      form3: {
        cate_id: null,
        cate_name: null,
        cate_title: null,
        cate_keywords: null,
        cate_description: null,
        cate_img: null,
        cate_order: null,
        cate_show: null
      },
      tableData: [],
      options: [
        { cate_id: 0,cate_name: '顶级栏目' }
      ],
      optionProps: {
        checkStrictly: true,
        value: 'cate_id',
        label: 'cate_name',
        children: 'children'
      },
      rules: {
        cate_name: [
          { required: true,message: '请输入分类名称',trigger: 'blur' }
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
        this.queryDelete(row.cate_id)
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
          cate_id: this.form.cate_id,
          cate_name: this.form.cate_name,
          pageIndex: this.pageIndex,
          pageSize: this.pageSize
        }
      }
      getCateList(param).then(res => {
        this.tableData = res.data.data.map(item => {
          item.cate_show = item.cate_show===1
          return item
        });
        this.total = res.data.total;
      },err => {
        this.$message.error(err.msg);
        console.log(err)
      })
    },
    addCateQuery() {
      const param = {
        data: {
          cate_name: this.form2.cate_name,
          cate_parent_id: this.form2.cate_parent_id[this.form2.cate_parent_id.length-1]
        }
      }
      // console.log(param)
      // return false;
      this.loading = true
      addCate(param).then(res => {
        this.dialogVisible=false
        this.loading = false
        this.form2.cate_name = ''
        this.form2.cate_parent_id = 0
        this.queryList()
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
          this.addCateQuery();
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
      param.data.cate_show = param.data.cate_show ? 1 : 2
      this.loading = true
      cateUpdate(param).then(res => {
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
    queryDelete(cate_id) {
      const param = {
        data: {
          cate_id
        }
      }
      this.loading = true
      cateDelete(param).then(res => {
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
          const data = res.data
          this.options = this.options.concat(data)
        }
      },err => {
        this.$message.error(err.msg);
        console.log(err)
      })
    },
    cateShowHandle(val) {
      console.log(val)
      const param = {
        data: {
          cate_id: val.cate_id,
          cate_show: val.cate_show ? 1 : 2
        }
      }
      this.loading = true
      cateUpdateShow(param).then(res => {
        this.loading = false
        this.$message(
          {
            message: '修改成功!',
            type: 'success',
          }
        )
        this.queryList()
      },err => {
        this.loading = false
        this.$message.error(err.msg);
        console.log(err)
      })
    }
  },
  mounted () {
    this.queryList()
    this.qeuryOneList()
  }
}
</script>
