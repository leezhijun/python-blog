<template>
  <li class="post-item" :class="{mt60:item.article_img,mt10:!item.article_img}">
    <div class="post-content clearfix">
      <div class="asset_img" v-if="item.article_img">
        <div class="img"><img :src="item.article_img" /></div>
        <div class="counts f12">
          <span><i class="iconfont icon-liulan f12"></i>{{item.article_browse_count}}</span>
          <span class="ml10"><i class="iconfont icon-comments f12"></i> 0</span>
        </div>
      </div>
      <h3 class="title ell cursor" @click="jumpArticle(item.article_id)">{{item.article_title}}</h3>
      <div class="des ell2">{{item.article_description}}</div>
    </div>
    <div class="post-others">
      <span class="tiem mr20"><i class="iconfont icon-time f12"></i>{{item.article_publish_time}}</span>
      <span class="cate mr20" v-if="item.cate_name"><i class="iconfont icon-category f12"></i>{{item.cate_name}}</span>
      <span class="tag" v-if="item.tags"><i class="iconfont icon-tags f12"></i><span v-for="i in item.tags" :key="i.tag_id">{{i.tag_name}}</span> </span>
      <span class="fr"><i class="iconfont icon-like f12"></i>{{item.article_like_count}}</span>
    </div>
  </li>
</template>
<script>
export default {
  name: 'PostItem',
  props: ['item'],
  data () {
    return {}
  },
  methods: {
    jumpArticle(id) {
      this.$router.push({ name: 'Article', query: { id } })
    }
  }
};
</script>
<style lang="scss" scoped>
.post-item {
  padding: 10px;
  // margin-bottom: 10px;
  border-radius: 4px;
  border: 1px solid #fff;
  box-shadow: 0px 1px 2px 1px #e0dfdb;
  background-color: #f7f6f1;
}
.mt60{
  margin-top: 60px;
}
.title {
  padding: 10px 0;
  font-size: 18px;
  color: #817e74;
  border-bottom: 1px solid #eeeee6;
}
.des {
  height: 2.8em;
  overflow: hidden;
  margin-top: 15px;
  margin-bottom: 15px;
  font-size: 14px;
  color: #b4b0a4;
  line-height: 1.4;
}
.post-others {
  border-top: 1px solid #eeeee6;
  padding-top: 10px;
  font-size: 12px;
  color: #9f9d92;
  i {
    margin-right: 2px;
  }
}
.asset_img{
  width: 180px;
  height: 140px;
  padding: 5px;
  margin-top: -40px;
  margin-right: 10px;
  float: left;
  border: 1px solid #f9f8f3;
  border-radius: 2px;
  box-shadow: 0 -1px 4px 2px #e8e8e8;
  background-color: #f7f6f1;
  img{
    width: 100%;
    height: 108px;
    border-radius: 2px;
  }
  .counts{
    padding-top: 5px;
    color: #9F9D92;
    i{
      margin-right: 2px;
    }
  }
}
</style>
