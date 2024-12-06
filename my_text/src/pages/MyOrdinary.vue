<template>
  <el-container>
    <el-header> 普通用户 </el-header>
    <el-container>
      <el-aside width="200px">
        <el-menu
          default-active="2"
          class="el-menu-vertical-demo"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
        >
          <el-menu-item index="2" @click="goToClass">
            <i class="el-icon-menu"></i>
            <span slot="title">班级</span>
          </el-menu-item>
          <el-menu-item index="3" @click="goToScore">
            <i class="el-icon-document"></i>
            <span slot="title">成绩</span>
          </el-menu-item>
          <el-menu-item index="4" @click="goToStudent">
            <i class="el-icon-setting"></i>
            <span slot="title">学籍</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: "MyOrdinary",
  methods: {
    goToClass() {
      this.$router.push("/MyOrdinary/OrdinaryClass");
    },
    goToScore() {
      this.$router.push("/MyOrdinary/OrdinaryScore");
    },
    goToStudent() {
      this.$router.push("/MyOrdinary/OrdinaryStudent");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-header,
.el-footer {
  background-color: #48959ba9;
  color: #161515;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #48959ba9;
  color: #333333;
  text-align: center;
  line-height: 200px;
  height: 75vh;
}

.el-main {
  background-color: #e9eef3;
  color: #201c1c;
  text-align: center;
  height: 75vh;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>
