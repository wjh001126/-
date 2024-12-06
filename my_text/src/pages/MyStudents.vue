<template>
  <el-main>
    <!-- 顶部Header -->
    <el-header>
      <!-- 使用 el-row 和 el-col 来布局按钮，并添加自定义样式 -->
      <el-row
        type="flex"
        justify="end"
        style="width: 100%; padding-right: 20px"
        class="row-style"
      >
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
        <el-button type="primary" @click="showAddDialog = true">添加</el-button>
        <el-button type="danger" @click="showBatchDelete = !showBatchDelete"
          >批量删除</el-button
        >
        <el-button
          v-if="showBatchDelete"
          type="danger"
          @click="confirmBatchDelete"
          >删除</el-button
        >
      </el-row>
    </el-header>

    <!-- 添加学生对话框 -->
    <el-dialog title="添加学生" :visible.sync="showAddDialog" width="30%">
      <el-form ref="addForm" :model="addFormData" label-width="100px">
        <el-form-item label="学号">
          <el-input v-model="addFormData.student_id"></el-input>
        </el-form-item>
        <el-form-item label="姓名">
          <el-input v-model="addFormData.stu_name"></el-input>
        </el-form-item>
        <el-form-item label="性别">
          <el-input v-model="addFormData.gender"></el-input>
        </el-form-item>
        <el-form-item label="班级">
          <el-input v-model="addFormData.class_"></el-input>
        </el-form-item>
        <el-form-item label="出生日期">
          <el-input v-model="addFormData.birth_date"></el-input>
        </el-form-item>
        <el-form-item label="学校">
          <el-input v-model="addFormData.school"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="showAddDialog = false">取消</el-button>
        <el-button type="primary" @click="addStudent">确定</el-button>
      </span>
    </el-dialog>

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
      <el-table-column label="操作" width="120">
        <template slot-scope="scope">
          <el-button
            type="danger"
            size="mini"
            @click="confirmDelete(scope.row.student_id)"
          >
            删除
          </el-button>
        </template>
      </el-table-column>
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
    <el-dialog
      title="删除确认"
      :visible.sync="deleteDialogVisible"
      width="30%"
      :before-close="handleClose"
    >
      <span>确定要删除选中的学号吗？</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="deleteDialogVisible = false">取消</el-button>
        <el-button type="danger" @click="deleteSelected">确定删除</el-button>
      </span>
    </el-dialog>
  </el-main>
</template>

<script>
export default {
  name: "MyStudents",
  data() {
    return {
      tableData: [],
      message: "",
      error: null,
      selectedRows: [],
      showBatchDelete: false, // 控制批量删除按钮的显示
      deleteDialogVisible: false, // 控制删除确认对话框的显示
      currentDeleteId: null, // 当前要删除的学号
      showAddDialog: false, // 控制添加对话框的显示
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
    confirmDelete(studentId) {
      this.currentDeleteId = studentId;
      this.deleteDialogVisible = true;
    },
    deleteSelected() {
      if (this.showBatchDelete) {
        this.sendDeleteRequest(this.selectedRows.map((row) => row.student_id));
      } else {
        this.sendDeleteRequest([this.currentDeleteId]);
      }
      this.deleteDialogVisible = false;
      this.selectedRows = [];
    },
    handleSelectionChange(val) {
      this.selectedRows = val;
    },
    confirmBatchDelete() {
      this.deleteDialogVisible = true;
    },
    // 发送删除请求到后端
    async sendDeleteRequest(studentIds) {
      try {
        const response = await fetch("http://127.0.0.1:8000/WJH/enrollments", {
          // 确保这里的URL与后端接口匹配
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ student_ids: studentIds }), // 将学号列表作为字典传递
        });
        if (!response.ok) {
          throw new Error("请求失败");
        }
        const data = await response.json();
        if (data.success) {
          this.$message({
            message: "删除成功",
            type: "success",
          });
          // 刷新表格数据
          this.fetchStudentScores();
        } else {
          this.$message.error(data.message || "删除操作失败");
        }
      } catch (error) {
        this.$message.error(error.message || "删除操作异常");
      }
    },
    handleClose(done) {
      this.$confirm("确认关闭？")
        .then(() => {
          done();
        })
        .catch(() => {});
    },

    addStudent() {
      // 调用添加函数，将 addFormData 发送给后端
      this.addStudentData(this.addFormData);
      this.showAddDialog = false; // 关闭对话框
    },
    // 添加学生数据的方法
    async addStudentData(studentData) {
      try {
        // 使用 fetch 发送 POST 请求到后端
        const response = await fetch("http://127.0.0.1:8000/WJH/enrollments", {
          // 确保这里的URL与后端接口匹配
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(studentData), // 将学生数据转换为 JSON 字符串
        });

        if (!response.ok) {
          throw new Error("添加请求失败");
        }

        const data = await response.json();
        if (data.success) {
          this.$message({
            message: "添加成功",
            type: "success",
          });
          // 刷新表格数据
          this.fetchStudentScores();
        } else {
          // 检查是否有特定的错误信息
          if (data.error === "学号已存在") {
            this.$message.error("学号已存在");
          } else {
            this.$message.error(data.message || "添加操作失败");
          }
        }
      } catch (error) {
        this.$message.error(error.message || "添加操作异常");
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
