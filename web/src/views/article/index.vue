<template>
  <div class="page-aricle">
    <Topbar />
    <section class="content blog-content clearfix">
      <Header />
      <section class="mt10 clearfix">
        <Aside />
        <section class="section fl">
          <article class="detail">
            <h1>大规格文件的上传优化</h1>
            <div class="article">
              第一步是结合项目背景，调研比较优化的解决方案。
文件上传失败是老生常谈的问题，常用方案是将一个大文件切片成多个小文件，并行请求接口进行上传，所有请求得到响应后，在服务器端合并所有的分片文件。当分片上传失败，可以在重新上传时进行判断，只上传上次失败的部分，减少用户的等待时间，缓解服务器压力。这就是分片上传文件。
            </div>
          </article>
        </section>
      </section>
    </section>
  </div>
</template>
<script>
export default {
  name: 'pageAricle'
}
</script>
<style lang="scss" scoped>
.section{
  .detail{
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 4px;
    border: 1px solid #fff;
    box-shadow: 0px 1px 2px 1px #e0dfdb;
    background-color: #f7f6f1;
  }
  h1{
    font-size: 18px;
    padding: 10px 0;
    border-bottom: 1px solid #e4e4e3;
  }
  .article{
    margin-top: 20px;
  }
}
</style>
