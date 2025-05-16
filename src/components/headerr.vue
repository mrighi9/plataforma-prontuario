<template>
  <div class="headerr">
    <div class="userInfo">
      <!-- Lupa -->
      <div class="icon search">
        <img src="@/assets/search.svg" alt="Search" />
      </div>

      <!-- Sino de notificações -->
      <div class="icon notification">
        <img src="@/assets/bell.svg" alt="Notifications" />
        <span class="notification-badge"></span>
      </div>

      <!-- Foto do usuário e nome -->
      <div class="user">
        <span class="user-name">Juliana</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.headerr {
  width: 95vw;
  top: 0;
  right: 0;
  height: 10vh;
  background-color: white;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding: 0 1rem;
  position: fixed;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.userInfo {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}


.icon {
  position: relative;
  cursor: pointer;
}

.icon img {
  width: 24px;
  height: 24px;
}

.notification-badge {
  position: absolute;
  top: -5px;
  right: -5px;
  background-color: #ff3366;
  color: white;
  font-size: 0.75rem;
  font-weight: bold;
  border-radius: 50%;
  width: 16px;
  height: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.user {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.user-photo {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  object-fit: cover;
}

.user-name {
  font-size: 1rem;
  font-weight: 500;
  color: #333;
}
</style>