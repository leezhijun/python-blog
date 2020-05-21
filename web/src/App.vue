<template>
  <div id="app">
    <div class="page-index clearfix">
      <Topbar />
      <section class="content blog-content clearfix">
        <Header />
        <section class="mt10 clearfix">
          <Aside />
          <router-view/>
        </section>
      </section>
    </div>
  </div>
</template>

<style lang="scss">
#app{
  width: 100%;
  min-height: 100%;
  padding-bottom: 80px;
  color: #857E6D;
  background-image: url('../src/assets/img/bg.png');
  background-position: top center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  // background-size: cover;
  background-color: #2b2b37;
}

</style>
