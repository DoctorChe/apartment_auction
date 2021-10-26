<template>
  <div class="login position-absolute top-50 start-50 translate-middle">
    <main class="form-signin">
      <form>
        <h1 class="h3 mb-3 fw-normal">Войдите в систему</h1>

        <div class="form-floating">
          <input
            type="name"
            class="form-control"
            id="floatingInput"
            placeholder="Имя"
          />
          <label for="floatingInput">Введите имя</label>
        </div>

        <button class="w-100 btn btn-lg btn-primary" type="submit">
          Войти
        </button>
      </form>
    </main>
  </div>
</template>

<style>
body {
  background-color: #f5f5f5;
}

.form-signin {
  max-width: 330px;
}
</style>
