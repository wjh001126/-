<template>
  <div class="container">
    <div class="header">注册</div>
    <div class="form-wrapper">
      <input
        type="text"
        v-model="username"
        placeholder="Username"
        class="input-item"
        @input="checkInputLength"
      />
      <input
        type="password"
        v-model="password"
        placeholder="Password"
        class="input-item"
        @input="checkInputLength"
      />
      <button type="button" class="btn" @click="register">马上注册</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserEnroll",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async register() {
      if (this.username.length > 16 || this.password.length > 16) {
        alert("用户名和密码均不得超过16个字符");
        return;
      }
      if (!this.username || !this.password) {
        alert("用户名和密码不能为空");
        return;
      }
      try {
        const response = await fetch("http://127.0.0.1:8000/WJH/register", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
          }),
        });
        if (!response.ok) {
          throw new Error("连接失败");
        }
        const result = await response.json();
        if (result.success) {
          alert("注册成功");
          // 可以在这里添加跳转到登录页面的逻辑
          this.$router.push("/login");
        } else {
          alert(result.message || "注册失败");
        }
      } catch (error) {
        alert(`注册失败: ${error.message}`);
      }
    },
    checkInputLength(event) {
      const maxLength = 16;
      if (event.target.value.length > maxLength) {
        alert(`输入内容不得超过${maxLength}个字符`);
        event.target.value = event.target.value.substring(0, maxLength);
      }
    },
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
html,
body {
  height: 100%;
  font-family: Arial, sans-serif;
}
body {
  background-color: #f7f7f7;
  display: flex;
  justify-content: center;
  align-items: center;
}
.container {
  background-color: white;
  width: 100%;
  max-width: 400px;
  padding: 40px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.header {
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 20px;
}
.input-item {
  width: 100%;
  margin-bottom: 15px;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}
.input-item::placeholder {
  color: #aaa;
}
.btn {
  display: block;
  width: 100%;
  padding: 15px;
  margin-top: 20px;
  background-color: #5c67f2;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.btn:hover {
  background-color: #4a54e1;
}
.msg {
  text-align: center;
  margin-top: 15px;
  font-size: 14px;
}
a {
  color: #5c67f2;
  text-decoration: none;
}
</style>
