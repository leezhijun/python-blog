<template>
  <div class="article-page">
    <div class="boder1 pb10 pt10 pl10">发布文章</div>
    <div class="mt15">
      <el-form class="mt30" ref="form" label-position="left" :model="form" label-width="80px">
        <el-form-item label="文章标题">
          <el-input v-model="form.article_title" placeholder="文章标题"></el-input>
        </el-form-item>
        <el-form-item label="关键词">
          <el-input v-model="form.article_keywords" placeholder="关键词逗号隔开"></el-input>
        </el-form-item>
        <el-form-item label="网页描述">
          <el-input v-model="form.article_description" type="textarea" :row="2" placeholder="网页描述"></el-input>
        </el-form-item>
        <el-row :gutter="10">
          <el-col :span="8">
            <el-form-item label="类型">
              <el-radio v-model="form.article_type" :label="1">文章</el-radio>
              <el-radio v-model="form.article_type" :label="2">单页</el-radio>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="推荐">
              <el-switch v-model="form.article_is_push"></el-switch>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="热门">
              <el-switch v-model="form.article_is_hot"></el-switch>
            </el-form-item>
          </el-col>
        </el-row>

        <el-form-item label="权重排序">
          <el-input-number v-model="form.article_order" :max="99" :controls="false" :step='1' step-strictly></el-input-number>
        </el-form-item>
        <el-form-item label="类目选择" v-if="form.article_type===1">
          <!-- <el-select v-model="form.cate_id" placeholder="请选择">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select> -->
          <el-cascader :options="options" :props="optionProps" v-model="cateArr" :show-all-levels="false"></el-cascader>
        </el-form-item>
        <el-form-item label="文章标签">
          <el-input v-model="tag" style="width:220px"></el-input><el-button class="ml20" :disabled='tags.length>2' type="primary" @click="addTagToList">添加</el-button>
        </el-form-item>
        <el-form-item label="">
          <el-tag
            class="mr10"
            v-for="tag in tags"
            :key="tag.name"
            closable
            @close='delTag(tag.tag_id)'
            :type="tag.type">
            {{tag.tag_name}}
          </el-tag>
        </el-form-item>
      </el-form>
      <div class="editor">
        <!-- <textarea id="simplemde"></textarea> -->
        <MyEditor v-model="form.article_content" placeholder="请输入文章类容" />
      </div>
      <div class="mt30 tc pb30">
        <el-button @click="submitClick(0)" type="default">保存</el-button>
        <el-button @click="submitClick(1)" v-if="!article_id" type="primary">发布</el-button>
        <el-button @click="submitClick(2)" v-else type="primary">修改</el-button>
      </div>
    </div>
  </div>
</template>
<script>
import MyEditor from '@/components/MyEditor'
import { catelevels } from '@/api/cate'
import { addArticle,articleSelectId,articleUpdate } from '@/api/article'
import { searchTag,delTagArticle } from '@/api/tag'
export default {
  name: 'AddPage',
  components: {
    MyEditor
  },
  data () {
    return {
      article_id: null,
      form: {
        cate_id: null,
        article_title: '',
        article_keywords: '',
        article_description: '',
        article_order: 10,
        article_content: '',
        article_type: 1,
        article_is_hot: false,
        article_is_push: false,
      },
      options: [],
      cateArr: [],
      optionProps: {
        checkStrictly: true,
        value: 'cate_id',
        label: 'cate_name',
        children: 'children'
      },
      tag: '', // 标签
      tags: [], // 标签列表
    }
  },
  methods: {
    handleClick() {},
    submitClick(type) {
      // console.log(this.simplemde.value())
      // console.log(this.cateArr); return false;
      if (!this.form.article_title) {
        this.$message({
          message: '标题不能为空',
          type: 'warning'
        });
        return false
      }
      if (!this.form.article_content&&type!==0) {
        this.$message({
          message: '文章内容不能为空',
          type: 'warning'
        });
        return false
      }
      if (this.cateArr.length>0&&this.form.article_type===1) {
        this.form.cate_id = this.cateArr[this.cateArr.length-1]
      } else {
        this.form.cate_id = null
      }
      const param = {
        data: this.form
      }
      param.data.article_is_hot = param.data.article_is_hot ? 1 : 0
      param.data.article_is_push = param.data.article_is_push ? 1 : 0
      param.data.article_status = type>0 ? 1 : 0
      param.data.tags = this.tags
      this.loading = true
      // console.log(param); return false;
      if (this.article_id) {
        param.data.article_id = this.article_id
        articleUpdate(param).then(res => {
          this.loading = false
          this.$message(
            {
              message: type ? '修改成功!': '保存成功!',
              type: 'success',
            }
          )
          this.$router.push({ name: 'articlePage' })
        },err => {
          this.loading = false
          this.$message.error(err.msg);
          console.log(err)
        })
      } else {
        addArticle(param).then(res => {
          this.loading = false
          this.$message(
            {
              message: type ? '发布成功!': '保存成功!',
              type: 'success',
            }
          )
          this.$router.push({ name: 'articlePage' })
        },err => {
          this.loading = false
          this.$message.error(err.msg);
          console.log(err)
        })
      }
    },
    qeuryOneList() {
      catelevels().then(res => {
        if (res.data.length>0) {
          this.options = res.data
        }
      },err => {
        this.$message.error(err.msg);
        console.log(err)
      })
    },
    queryId() {
      const param = {
        data: {
          article_id: this.article_id
        }
      }
      articleSelectId(param).then(res => {
        console.log(res)
        this.form = Object.assign(this.form,res.data,
        { article_is_hot: res.data.article_is_hot===1 ,article_is_push: res.data.article_is_push===1 }
        )
        if (res.data.cateArr) {
          this.cateArr = res.data.cateArr
        }
        if (res.data.tags) {
          this.tags = res.data.tags
        }
      },err => {
        this.$message.error(err.msg);
        console.log(err)
      })
    },
    addTagToList() {
      if (!this.tag) {
        this.$message(
            {
              message: '添加标签不能为空',
              type: 'warning',
            }
          )
      }
      // this.tags.push({ tag_name: this.tag })
      this.searchTagQuery()
    },
    searchTagQuery() {
      const param = {
        data: {
          tag_name: this.tag
        }
      }
      searchTag(param).then(res => {
        if (this.tags.filter(item => item.tag_id===res.data.tag_id).length>0) {
          this.$message(
            {
              message: '不要重复添加!',
              type: 'warning',
            }
          )
        }else {
          this.tags.push(res.data);
          this.tag = ''
          this.$message(
            {
              message: '添加成功!',
              type: 'success',
            }
          )
        }
      },err => {
        this.$message.error(err.msg);
        console.log(err)
      })
    },
    delTag(tag_id) {
      if (this.article_id) {
        const param = {
          data: {
            article_id: this.article_id,
            tag_id
          }
        }
        delTagArticle(param).then(res => {
          // console.log(res)
          this.tags = this.tags.filter(item => item.tag_id!==tag_id)
          this.$message(
            {
              message: '删除成功!',
              type: 'success',
            }
          )
        },err => {
          this.$message.error(err.msg);
          console.log(err)
        })
      } else {
        this.tags = this.tags.filter(item => item.tag_id!==tag_id)
      }
    }
  },
  beforeMount () {
    console.log(this.$route)
    if (this.$route.query.article_id) {
      console.log(this.$route.query.article_id)
      this.article_id = this.$route.query.article_id
      this.queryId()
    }
  },
  mounted () {
    this.qeuryOneList();
  }
}
</script>
