<template>
  <el-main>
    <!-- 顶部Header -->
    <el-header>
      <!-- 使用 el-row 和 el-col 来布局按钮，并添加自定义样式 -->
      <span
        style="
          flex-grow: 1;
          margin-right: 20px;
          text-align: center;
          display: block;
        "
      >
        学生成绩信息
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
      <el-table-column prop="total_score" label="总成绩"> </el-table-column>
      <el-table-column prop="score_rank" label="分数排名"> </el-table-column>
      <el-table-column prop="class_" label="班级"> </el-table-column>
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
  name: "OrdinaryScore",
  data() {
    return {
      tableData: [],
      message: "",
      error: null,
      addFormData: {
        // 用户输入的数据
        student_id: "",
        stu_name: "",
        total_score: "",
        score_rank: "",
        class_: "",
      },
    };
  },
  created() {
    this.fetchStudentScores();
  },
  methods: {
    async fetchStudentScores() {
      try {
        const response = await fetch("http://127.0.0.1:8000/WJH/studentscores");
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
        this.error = error.message;
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
