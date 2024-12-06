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
        班级信息
      </span>
    </el-header>
    <!-- 数据表格 -->
    <el-table
      v-if="tableData.length > 0"
      :data="tableData"
      style="width: 100%"
      @selection-change="handleSelectionChange"
      row-key="class_id"
    >
      <el-table-column
        v-if="showBatchDelete"
        type="selection"
        width="55"
      ></el-table-column>
      <el-table-column prop="class_id" label="班级班号" width="140">
      </el-table-column>
      <el-table-column prop="cls_rank" label="班级排名" width="120">
      </el-table-column>
      <el-table-column prop="head_teacher" label="班主任"> </el-table-column>
      <el-table-column prop="student_count" label="学生总数"> </el-table-column>
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

    <!-- 删除确认对话框 -->
  </el-main>
</template>

<script>
export default {
  name: "OrdinaryClass",
  data() {
    return {
      tableData: [],
      message: "",
      error: null,
      addFormData: {
        class_id: "",
        cls_rank: "",
        head_teacher: "",
        student_count: 0,
      },
    };
  },
  created() {
    this.fetchClasses();
  },
  methods: {
    async fetchClasses() {
      try {
        // 注意：确保这里的URL与后端接口匹配
        const response = await fetch("http://127.0.0.1:8000/WJH/classes");
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
    handleClose(done) {
      this.$confirm("确认关闭？")
        .then(() => {
          done();
        })
        .catch(() => {});
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
