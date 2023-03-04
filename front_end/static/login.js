// Login form imports
const loginEmail = document.getElementById("login-email");
const loginEmailError = document.querySelector("#login-email + span");
const loginPassword = document.getElementById("login-password");
const loginPasswordError = document.querySelector("#login-password + span");
const loginBtn = document.getElementById("login-btn");

// Login form validation

loginEmail.addEventListener("input", function () {
  const re = /\S+@\S+\.\S+/;
  const validateEmail = re.test(loginEmail.value);
  if (!validateEmail) {
    loginEmailError.textContent = "Email is not valid";
    loginEmailError.style.display = "block";
  } else {
    loginEmailError.textContent = null;
    loginEmailError.style.display = "none";
  }
});

loginPassword.addEventListener("input", function () {
  const password = loginPassword.value;
  if (password.length < 5) {
    loginPasswordError.style.display = "block";
    loginPasswordError.textContent = "Password cannot be less 5 characters";
  } else {
    loginPasswordError.style.display = "none";
    loginPasswordError.textContent = null;
  }
});
