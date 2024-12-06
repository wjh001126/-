<template>
  <el-main>
    <!-- 顶部Header -->
    <el-header>
      <span
        style="
          flex-grow: 1;
          margin-right: 20px;
          text-align: center;
          display: block;
        "
      >
        学生学籍信息
      </span>
    </el-header>
    <!-- 数据表格 -->
    <el-table
      v-if="tableData.length > 0"
      :data="tableData"
      style="width: 100%"
      @selection-change="handleSelectionChange"
      row-key="student_id"
    >
      <el-table-column
        v-if="showBatchDelete"
        type="selection"
        width="55"
      ></el-table-column>
      <el-table-column prop="student_id" label="学号" width="140">
      </el-table-column>
      <el-table-column prop="stu_name" label="姓名" width="120">
      </el-table-column>
      <el-table-column prop="gender" label="性别"> </el-table-column>
      <el-table-column prop="class_" label="班级"> </el-table-column>
      <el-table-column prop="birth_date" label="出生日期"> </el-table-column>
      <el-table-column prop="school" label="学校"> </el-table-column>
    </el-table>

    <!-- 无数据提示 -->
    <el-alert
      v-if="message === 'No data available'"
      title="暂无数据"
      type="info"
    >
    </el-alert>

    <!-- 错误提示 -->
    <el-alert v-if="error" :title="error" type="error" show-icon> </el-alert>
  </el-main>
</template>

<script>
export default {
  name: "OrdinaryStudent",
  data() {
    return {
      tableData: [],
      message: "",
      error: null,
      addFormData: {
        student_id: "",
        stu_name: "",
        gender: "", // 新增性别字段
        class_: "", // 班级
        birth_date: "", // 新增出生日期字段
        school: "", // 新增学校字段
      },
    };
  },
  created() {
    this.fetchStudentScores();
  },
  methods: {
    async fetchStudentScores() {
      try {
        // 注意：确保这里的URL与后端接口匹配
        const response = await fetch("http://127.0.0.1:8000/WJH/enrollments");
        if (!response.ok) {
          throw new Error("连接到服务器失败");
        }
        const data = await response.json();
        if (data.success) {
          this.tableData = data.data;
          this.message = data.message || "";
          if (this.tableData.length === 0 && !this.error) {
            this.message = "No data available"; // 设置无数据消息
          }
        } else {
          this.error = data.message || "未知错误";
        }
      } catch (error) {
        this.error = error.message || "请求数据时发生错误";
      }
    },
  },
};
</script>

<style>
.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}

.row-style {
  padding-top: 10px; /* 自定义上边距 */
  padding-bottom: 10px; /* 自定义下边距 */
}

.row-style {
  align-items: center; /* 垂直居中 */
  height: 100%; /* 确保占满整个header的高度 */
}
.el-aside {
  color: #333;
}
</style>
