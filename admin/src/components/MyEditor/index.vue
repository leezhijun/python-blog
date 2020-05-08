<template>
  <div class="editor" :style="{height:(height+70)+'px'}">
    <textarea id="simplemde"></textarea>
  </div>
</template>
<script>
import 'simplemde/dist/simplemde.min.css'
import 'github-markdown-css'
import SimpleMDE from 'simplemde'
export default {
  name: 'MyEditor',
  props: {
    value: String,
    placeholder: {
      type: String,
      default: ''
    },
    height: {
      type: Number,
      default: 500
    },
  },
  data () {
    return {
      simplemde: null,
      content: null,
      timer: null,
    }
  },
  watch: {
    content: function(newval,oldval) {
      this.$emit('input', newval)
    }
  },
  mounted () {
    const _this = this;
    SimpleMDE.prototype.createSideBySide = function() {
      var cm = this.codemirror;
      var wrapper = cm.getWrapperElement();
      var preview = wrapper.nextSibling;

      if(!preview || !/editor-preview-side/.test(preview.className)) {
        preview = document.createElement("div");
        preview.className = "editor-preview-side markdown-body";
        wrapper.parentNode.insertBefore(preview, wrapper.nextSibling);
      }

      // Syncs scroll  editor -> preview
      var cScroll = false;
      var pScroll = false;
      cm.on("scroll", function(v) {
        if(cScroll) {
          cScroll = false;
          return;
        }
        pScroll = true;
        var height = v.getScrollInfo().height - v.getScrollInfo().clientHeight;
        var ratio = parseFloat(v.getScrollInfo().top) / height;
        var move = (preview.scrollHeight - preview.clientHeight) * ratio;
        preview.scrollTop = move;
      });
    }
    this.simplemde = new SimpleMDE({
      element: document.getElementById('simplemde'),
      spellChecker: false,
      placeholder: this.placeholder,
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
    // document.querySelector('.editor-preview-side').classList.add('markdown-body');

    // console.log(document.querySelector('.CodeMirror-scroll'))
    document.querySelector('.CodeMirror-scroll').style.minHeight = this.height + 'px';
    // 初始值
    this.simplemde.value(this.value);

    this.simplemde.codemirror.on('change', () => {
      clearTimeout(this.timer)
      setTimeout(()=>{
        console.log(this.simplemde.value());
        this.content = this.simplemde.value()
      },500)
    })
  }
}
</script>
<style lang="scss" scoped>

</style>
