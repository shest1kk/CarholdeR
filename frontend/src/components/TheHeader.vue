<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light shadow mh-72">
    <div class="container justify-content-center">
      <a id="navbar-brand" class="navbar-brand" href="#">
        <span class="text-danger fw-medium">CAR</span>holde<span
          class="text-danger fw-medium">RRR</span>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="navbar" id="navbarSupportedContent">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link fw-normal ps-3" aria-current="page" href="#">Машины</a>
          </li>
          <li class="nav-item">
            <a class="nav-link fw-normal ps-3" href="#">Зоны поездок</a>
          </li>
          <li class="nav-item">
            <a class="nav-link fw-normal ps-3" href="#">Безопасность</a>
          </li>
          <li class="nav-item">
            <a class="nav-link fw-normal ps-3" href="#">Вопросы</a>
          </li>
          <li class="nav-item">
            <a class="nav-link fw-medium ps-3" href="#">Регистрация</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-danger fw-medium ps-3" href="#">Авторизация</a>
          </li>
        </ul>

      </div>
    </div>
  </nav>
</template>

<script>
document.title = 'CarholdeR';

export default {
  name: "TheHeader"
}

</script>

<style scoped>
.nav-link {
  font-size: 18px;
}

.nav-link:hover {
  text-decoration: underline 2px;
  text-underline-position: under;
}
</style>