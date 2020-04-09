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
          <el-radio v-model="form.article_type" label="1">文章</el-radio>
          <el-radio v-model="form.article_type" label="2">单页</el-radio>
        </el-form-item>
        <el-form-item label="权重">
          <el-input-number  size="mini" v-model="form.article_order" :min="1" :max="100"></el-input-number>
        </el-form-item>
        <el-form-item label="类目选择">
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
      <textarea id="simplemde"></textarea>
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
        article_description: ''
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
  computed: {
    isPreviewActive: function() {
      if (this.simplemde) {
        return this.simplemde.isPreviewActive()
      } else {
        return false
      }
    }
  },
  watch: {
    isPreviewActive: function (newValue,oldValue) {
      if (newValue) {
        document.querySelector('.editor-preview').classList.add('markdown-body');
      }
    },
  },
  mounted () {
    /* eslint-disable no-undef */
    this.simplemde = new SimpleMDE({
      element: document.getElementById('simplemde'),
    });
    const _this = this
    console.log(this.simplemde)
    this.simplemde.codemirror.on('change', function() {
      console.log(_this.simplemde.value());
    });
    this.simplemde.codemirror.on('optionChange', function() {
      console.log(1313131);
    });
    document.querySelector('.editor-preview-side').classList.add('markdown-body');

    // document.querySelector('.editor-preview').classList.add('markdown-body');
  }
}
</script>
