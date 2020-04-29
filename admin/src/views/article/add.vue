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
          <el-select v-model="form.cate_id" placeholder="请选择">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div class="editor">
        <textarea id="simplemde"></textarea>
      </div>
      <div class="mt15 tc pb30">
        <el-button @click="submitClick(0)" type="default">保存</el-button>
        <el-button @click="submitClick(1)" type="primary">发布</el-button>
      </div>
    </div>
  </div>
</template>
<script>
import { cateOneAll } from '@/api/cate'
import { addArticle } from '@/api/article'
import 'simplemde/dist/simplemde.min.css'
import 'github-markdown-css'
import SimpleMDE from 'simplemde'
export default {
  name: 'AddPage',
  data () {
    return {
      simplemde: null,
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
    }
  },
  methods: {
    handleClick() {},
    submitClick(type) {
      // console.log(this.simplemde.value())
      const param = {
        data: this.form
      }
      param.data.article_is_hot = param.data.article_is_hot ? 1 : 0
      param.data.article_is_push = param.data.article_is_push ? 1 : 0
      param.data.article_status = type
      param.data.article_content = this.simplemde.value()
      this.loading = true
      // console.log(param); return false;
      addArticle(param).then(res => {
        this.loading = false
        this.$message(
          {
            message: type ? '发布成功!': '保存成功!',
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
      cateOneAll().then(res => {
        if (res.data.length>0) {
          this.options = res.data.map(item => {
            return { value: item.cate_id, label: item.cate_name }
          })
        }
      },err => {
        this.$message.error(err.msg);
        console.log(err)
      })
    },
  },
  mounted () {
    const _this = this;
    this.simplemde = new SimpleMDE({
      element: document.getElementById('simplemde'),
      spellChecker: false,
      toolbar: ["bold", "italic", "heading", "|", "quote", "code", "unordered-list", "ordered-list", "table", "horizontal-rule", "clean-block", "|", "link", "image",
      {
        name: "preview",
        action: function togglePreview(editor) {
          var cm = editor.codemirror;
          var wrapper = cm.getWrapperElement();
          var toolbar_div = wrapper.previousSibling;
          var toolbar = editor.options.toolbar ? editor.toolbarElements.preview : false;
          var preview = wrapper.lastChild;
          if(!preview || !/editor-preview/.test(preview.className)) {
            preview = document.createElement("div");
            preview.className = "editor-preview markdown-body";
            wrapper.appendChild(preview);
          }
          if(/editor-preview-active/.test(preview.className)) {
            preview.className = preview.className.replace(
              /\s*editor-preview-active\s*/g, ""
            );
            if(toolbar) {
              toolbar.className = toolbar.className.replace(/\s*active\s*/g, "");
              toolbar_div.className = toolbar_div.className.replace(/\s*disabled-for-preview*/g, "");
            }
          } else {
            // When the preview button is clicked for the first time,
            // give some time for the transition from editor.css to fire and the view to slide from right to left,
            // instead of just appearing.
            setTimeout(function() {
              preview.className += " editor-preview-active";
            }, 1);
            if(toolbar) {
              toolbar.className += " active";
              toolbar_div.className += " disabled-for-preview";
            }
          }
          preview.innerHTML = editor.options.previewRender(editor.value(), preview);

          // Turn off side by side if needed
          var sidebyside = cm.getWrapperElement().nextSibling;
          if(/editor-preview-active-side/.test(sidebyside.className))
            SimpleMDE.toggleSideBySide(editor);
        },
        className: "fa fa-eye no-disable",
			  title: "Toggle Preview",
      }, "side-by-side", "fullscreen", "|", "guide"],
    });
    document.querySelector('.editor-preview-side').classList.add('markdown-body');
    this.qeuryOneList();
  }
}
</script>
