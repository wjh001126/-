<template>
  <div class="container">
    <header>
      <!-- 顶部部分 -->
    </header>
    <div class="home-intro">
      <h1>吃西瓜不吐籽</h1>
      <h1>斯人若彩虹，遇上方知有</h1>
      <p v-if="isLoading">Loading...</p>
      <p v-else>{{ hitokoto }}</p>
    </div>

    <div class="image-row">
      <!-- 第一个部分，三张图片 -->
      <div class="image-overlay">
        <img
          src="../assets/picture/11.jpg"
          alt="Image 111"
          loading="lazy"
          width="600"
          height="444"
        />
        <div class="overlay-text">在我心里</div>
      </div>
      <div class="image-overlay">
        <img
          src="../assets/picture/2.jpg"
          alt="Image 2"
          loading="lazy"
          width="600"
          height="444"
        />
        <div class="overlay-text">你真的</div>
      </div>
      <div class="image-overlay">
        <img
          src="../assets/picture/8.jpg"
          alt="Image 3"
          loading="lazy"
          width="600"
          height="444"
        />
        <div class="overlay-text">很特别</div>
      </div>
    </div>
    <div class="image-row">
      <!-- 第二个部分，四张图片 -->
      <div class="image-overlay">
        <img
          src="../assets/picture/4.jpg"
          alt="Image 4"
          loading="lazy"
          width="600"
          height="444"
        />
        <div class="overlay-text">要是</div>
      </div>
      <div class="image-overlay">
        <img
          src="../assets/picture/5.jpg"
          alt="Image 5"
          loading="lazy"
          width="600"
          height="444"
        />
        <div class="overlay-text">能和你</div>
      </div>
      <div class="image-overlay">
        <img
          src="../assets/picture/6.jpg"
          alt="Image 6"
          loading="lazy"
          width="600"
          height="444"
        />
        <div class="overlay-text">在一起</div>
      </div>
      <div class="image-overlay">
        <img
          src="../assets/picture/7.jpg"
          alt="Image 7"
          loading="lazy"
          width="600"
          height="444"
        />
        <div class="overlay-text">就好了</div>
      </div>
    </div>
    <!-- 随便写点内容 -->
    <!-- 文字介绍盒子 -->
    <div class="intro-box">
      <p>《唐多令·芦叶满汀洲》</p>
      <p>宋代 刘过</p>
      <p>芦叶满汀洲，寒沙带浅流。</p>
      <p>二十年重过南楼。</p>
      <p>柳下系船犹未稳，能几日，又中秋。</p>
      <p>黄鹤断矶头，故人今在否？</p>
      <p>旧江山浑是新愁。</p>
      <p>欲买桂花同载酒，终不似，少年游。</p>
    </div>
    <!-- 登录按钮 -->
    <div class="login-button">
      <router-link to="/login">登录</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "MyHome",
  data() {
    return {
      hitokoto: "",
      isLoading: true,
      loadingMessage: "加载中...",
    };
  },
  created() {
    this.fetchHitokoto();
  },
  methods: {
    fetchHitokoto() {
      // 请确保网络环境允许访问该 API，如果无法访问，请检查链接的合法性，并在网络稳定的情况下重试。
      fetch("https://v1.hitokoto.cn")
        .then((res) => res.json())
        .then((data) => {
          this.hitokoto = data.hitokoto;
          this.isLoading = false;
        })
        .catch((err) => {
          console.error(err);
          this.isLoading = false;
        });
    },
  },
};
</script>

<style scoped>
/* 全局容器样式 */
.container {
  margin: 0; /* 移除默认外边距 */
  padding: 0; /* 移除默认内边距 */
  font-family: Arial, sans-serif; /* 设置字体为Arial，无Arial时使用系统默认无衬线字体 */
  background-color: #2c2c2c; /* 设置背景颜色为深沉黑灰色 */
  color: #f5f5f5; /* 设置字体颜色为浅灰色 */
  width: 100vw; /* 设置宽度为视口宽度的100% */
  min-height: 100vh; /* 设置最小高度为视口高度的100% */
  padding: 20px; /* 设置内边距为20px */
}

/* 容器样式，确保最大宽度为100%并居中 */
.container {
  max-width: 100%;
  margin: 0 auto; /* 垂直方向0，水平方向自动，实现居中 */
  padding: 20px;
}

/* 头部样式 */
header {
  border-bottom: 1px solid #6b6b6b; /* 设置底部边框为1px的深灰色 */
  padding-top: 120px; /* 设置顶部内边距为120px */
  height: 100px; /* 设置header的高度为100px */
  margin-top: 300px; /* 添加20px的顶部外边距 */
}

/* 首页介绍区域样式 */
.home-intro {
  text-align: center; /* 文本居中 */
  padding: 20px 0; /* 设置顶部和底部内边距为20px */
}

/* 首页介绍区域标题样式 */
.home-intro h1 {
  color: #eae8f1; /* 设置标题颜色为高贵的紫色 */
}

/* 图片容器样式 */
.image-row {
  display: flex; /* 使用弹性盒子布局 */
  justify-content: center; /* 水平居中 */
  margin: 30px auto; /* 垂直方向30px外边距，水平方向自动外边距实现居中 */
  gap: 40px; /* 保持图片间隔为40px */
  width: 60%; /* 设置宽度为屏幕宽度的三分之二 */
}

/* 计算最大图片宽度 */
.max-image-width {
  max-width: calc(60vw / 3 - 70px); /* 基于图片盒子宽度的三分之一减去70px */
}

/* 图片样式 */
.image-row img {
  width: 100%; /* 图片宽度填满容器 */
  height: 56.25%; /* 图片高度设置为宽度的56.25%，以实现3:4的宽高比 */
  object-fit: cover; /* 保持图片宽高比，裁剪超出部分 */
  transition: filter 0.3s ease; /* 平滑过渡效果 */
}

/* 第二行图片样式，与第一行图片宽度一致 */
.image-row:nth-child(2) img {
  width: 100%; /* 图片宽度填满容器 */
  height: 56.25%; /* 图片高度设置为宽度的56.25% */
}

/* 图片覆盖层样式 */
.image-overlay {
  position: relative; /* 相对定位 */
  display: inline-block; /* 内联块级元素 */
}

/* 图片覆盖层中的图片样式 */
.image-overlay img {
  display: block; /* 块级元素 */
  width: 100%; /* 图片宽度填满容器 */
  height: auto; /* 高度自动 */

  transition: filter 0.3s ease; /* 平滑过渡效果 */
}

/* 鼠标悬停在图片覆盖层上的图片样式 */
.image-overlay:hover img {
  filter: blur(11px); /* 模糊效果 */
}

/* 图片覆盖层上的文字样式 */
.overlay-text {
  position: absolute; /* 绝对定位 */
  top: 50%; /* 顶部距离为父元素高度的50% */
  left: 50%; /* 左侧距离为父元素宽度的50% */
  transform: translate(-50%, -50%); /* 居中定位 */
  color: #ffffff; /* 字体颜色 */
  font-size: 24px; /* 字体大小 */
  opacity: 0; /* 初始透明度 */
  transition: opacity 0.3s ease; /* 透明度过渡效果 */
  text-align: center; /* 文本居中 */
}

/* 鼠标悬停在图片覆盖层上的文字样式 */
.image-overlay:hover .overlay-text {
  opacity: 1; /* 透明度为1，显示文字 */
}

@media (max-width: 768px) {
  .image-row img {
    width: calc(50% - 20px); /* 小屏幕下图片宽度 */
  }
}

/* 媒体查询，适用于较小屏幕（例如平板和部分大手机） */
@media (max-width: 768px) {
  .image-row {
    gap: 20px; /* 在较小屏幕上，间隔减少为20px */
    width: 100%; /* 图片盒子宽度占满屏幕宽度 */
  }
  .image-row img {
    width: calc(50% - 20px); /* 小屏幕下图片宽度 */
    height: auto; /* 高度自动调节 */
    object-fit: cover; /* 保持图片比例，裁剪超出部分 */
  }
}

/* 媒体查询，适用于较小屏幕（例如手机） */
@media (max-width: 480px) {
  .image-row {
    gap: 10px; /* 在非常小的屏幕上，间隔减少为10px */
    width: 100%; /* 图片盒子宽度占满屏幕宽度 */
  }
  .image-row img {
    width: 100%; /* 超小屏幕下图片占满宽度 */
    height: auto; /* 高度自动调节 */
    object-fit: cover; /* 保持图片比例，裁剪超出部分 */
  }
  header {
    border-bottom: 1px solid #6b6b6b; /* 设置底部边框为1px的深灰色 */
    padding-top: 120px; /* 设置顶部内边距为120px */
    height: 100px; /* 设置header的高度为100px */
    margin-top: 30px; /* 添加20px的顶部外边距 */
  }
}

/* 文字介绍盒子样式 */
.intro-box {
  width: 66.666%; /* 与图片容器相同的宽度 */
  margin: 30px auto; /* 垂直方向30px外边距，水平方向自动外边距实现居中 */
  padding: 20px;
  background-color: #333; /* 深色背景 */
  color: #f5f5f5; /* 字体颜色与页面一致 */
  text-align: center; /* 文本居中 */
}

.intro-box p {
  font-size: 16px;
  line-height: 1.6;
  color: #d8dade;
  margin-bottom: 8px;
}

.intro-box p:not(:last-child) {
  margin-bottom: 8px;
}

/* 登录按钮样式 */
.login-button {
  margin: 30px auto; /* 垂直方向30px外边距，水平方向自动外边距实现居中 */
  text-align: center; /* 文本居中 */
}

/* 路由链接样式 */
.login-button router-link {
  display: inline-block;
  padding: 10px 20px;
  background-color: #b388ff; /* 高贵紫作为按钮颜色 */
  color: #ffffff; /* 白色字体 */
  text-decoration: none; /* 移除下划线 */
  border-radius: 5px; /* 圆角边框 */
  transition: background-color 0.3s ease; /* 平滑背景颜色变化 */
}

/* 登录按钮悬停效果 */
.login-button router-link:hover {
  background-color: #9a67e6; /* 悬停时的背景颜色 */
}
</style>
