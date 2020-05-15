<template>
  <div class="pagination mt40">
    <ul>
      <li><i class="iconfont icon-prev"></i></li>
      <li>1</li>
      <li>2</li>
      <li>3</li>
      <li><i class="iconfont icon-next"></i></li>
    </ul>
  </div>
</template>
<script>
export default {
  name: 'Pagination' // 分页
}
</script>
<style lang="scss" scoped>
.pagination{
  display: flex;
  justify-content: center;
  li{
    float: left;
    padding: 6px 8px;
    margin-right: 10px;
    text-align: center;
    border-radius: 2px;
    background-color: #f7f6f1;
    border: 1px solid #fff;
    box-shadow: 0px 1px 6px 1px #d0d0d0;
  }
  i{font-size: 12px;font-weight: bold;}
}
</style>
