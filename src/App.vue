<template>
  <div class="App">
    <div id="login">
      <header>Login to get started</header>
      <p>Username: <input type="text" v-model="username" /></p>

      <p>Password: <input type="password" v-model="password" /></p>

      <div id="btn-container">
        <button id="login-btn" @click="authenticate">Login</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    authenticate: function () {
      const { username, password } = this;
      const reqBody = { username, password };

      fetch(`http://localhost:5000/authenticate`, {
        method: 'POST',
        body: JSON.stringify(reqBody),
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.validated) {
            console.log('success');
          } else {
            console.log('failed');
          }
        });
    },
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');

* {
  font-family: 'Open Sans', sans-serif;
}

html,
body,
#app,
.App {
  height: 100%;
  margin: 0;
}

.App {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  background-color: #f6f6f6;
}

header {
  text-align: center;
  font-size: 18px;
}

#login {
  background-color: #fff;

  border: 1px solid black;
  border-radius: 15px;

  padding: 10px;
}

input {
  border: 1px solid rgb(48, 117, 245);
  border-style: none none solid none;

  color: rgb(48, 117, 245);
}

#btn-container {
  display: flex;
  justify-content: center;
}

#login-btn {
  border-radius: 3px;
  border: 1px solid #000;

  background-image: linear-gradient(
    to bottom right,
    rgb(48, 48, 245),
    rgb(52, 194, 250)
  );
  color: #fff;
}
</style>
