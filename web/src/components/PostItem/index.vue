<template>
  <li class="post-item">
    <div class="post-content clearfix">
      <div class="asset_img">
        <div class="img"><img src="@/assets/img/ar_logo.jpg" /></div>
        <div class="counts f12">
          <span><i class="iconfont icon-liulan f12"></i> 123</span>
          <span class="ml10"><i class="iconfont icon-comments f12"></i> 123</span>
        </div>
      </div>
      <h3 class="title ell">Hooks & Mobx 只需额外知道两个 Hook，便能体验到如此简单的开发方式</h3>
      <div class="des ell2">本文主要讲解了下我平时在工作开发中遇到的关于 Hooks 的一切缺点和问题，并尝试配合 Mobx 解决这些问题的经历。我觉得两者的配合可以极大的降低开发过程中有可能出现的问题以及极大的提高开发体验，而且学习成本也是非常的低。</div>
    </div>
    <div class="post-others">
      <span class="tiem mr20"><i class="iconfont icon-time f12"></i>2020-10-01 12:12:12</span>
      <span class="cate mr20"><i class="iconfont icon-category f12"></i>html</span>
      <span class="tag"><i class="iconfont icon-tags f12"></i>html,html5</span>
      <span class="fr"><i class="iconfont icon-like f12"></i>7</span>
    </div>
  </li>
</template>
<script>
export default {
  name: 'PostItem',
  data () {
    return {}
  }
};
</script>
<style lang="scss" scoped>
.post-item {
  padding: 10px;
  // margin-bottom: 10px;
  margin-top: 60px;
  border-radius: 4px;
  border: 1px solid #fff;
  box-shadow: 0px 1px 2px 1px #e0dfdb;
  background-color: #f7f6f1;
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
  height: auto;
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
    height: auto;
    border-radius: 2px;
  }
  .counts{
    padding-top: 5px;
    color: #9F9D92;
  }
}
</style>
