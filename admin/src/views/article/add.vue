<template>
  <div class="article-page">
    <div class="boder1 pb10 pt10 pl10">发布文章</div>
    <div class="mt15">
      <el-form class="mt30" ref="form" :model="form" label-width="120px">
        <el-form-item label="标题">
          <el-input v-model="form.article_title" placeholder="文章标题"></el-input>
        </el-form-item>
        <el-form-item label="关键词">
          <el-input v-model="form.article_keywords" placeholder="关键词逗号隔开"></el-input>
        </el-form-item>
        <el-form-item label="网页描述">
          <el-input v-model="form.article_description" type="textarea" :row="2" placeholder="网页描述"></el-input>
        </el-form-item>
        <el-form-item label="文章类型">
          <el-radio v-model="form.article_type" :label="1">文章</el-radio>
          <el-radio v-model="form.article_type" :label="2">单页</el-radio>
        </el-form-item>
        <el-form-item label="权重">
          <el-input-number  size="mini" v-model="form.article_order" :min="1" :max="100"></el-input-number>
        </el-form-item>
        <el-form-item label="类目选择" v-if="form.article_type===1">
          <el-select v-model="value" placeholder="请选择">
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
        <el-button @click="saveClick" type="default">保存</el-button>
        <el-button @click="pushClick" type="primary">发布</el-button>
      </div>
    </div>
  </div>
</template>
<script>
import 'simplemde/dist/simplemde.min.css'
import 'github-markdown-css'
import SimpleMDE from 'simplemde'
export default {
  name: 'AddPage',
  data () {
    return {
      simplemde: null,
      form: {
        article_title: '',
        article_keywords: '',
        article_description: '',
        article_order: 10,
        article_content: '',
        article_type: 1
      },
      options: [{
          value: '选项1',
          label: '黄金糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }],
        value: ''
    }
  },
  methods: {
    handleClick() {},
    saveClick() {
      console.log(this.simplemde.value())
    },
    pushClick() {}
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
  }
}
</script>
