<template>
  <el-container>
    <el-header> 管理员 </el-header>
    <el-container>
      <el-aside width="200px">
        <el-menu
          default-active="2"
          class="el-menu-vertical-demo"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
        >
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>导航一</span>
            </template>
            <el-menu-item-group>
              <template slot="title">分组一</template>
              <el-menu-item index="1-1">选项1</el-menu-item>
              <el-menu-item index="1-2">选项2</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="分组2">
              <el-menu-item index="1-3">选项3</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="1-4">
              <template slot="title">选项4</template>
              <el-menu-item index="1-4-1">选项1</el-menu-item>
            </el-submenu>
          </el-submenu>
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
  name: "MyAdmin",
  methods: {
    goToClass() {
      this.$router.push("/MyAdmin/MyClass");
    },
    goToScore() {
      this.$router.push("/MyAdmin/MyScore");
    },
    goToStudent() {
      this.$router.push("/MyAdmin/MyStudents");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
  height: 75vh;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
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
