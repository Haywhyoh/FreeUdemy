// Sign up imports
const signupEmail = document.getElementById("signup-email");
const signupEmailError = document.querySelector("#signup-email + span");
const signupUsername = document.getElementById("signup-username");
const signupUsernameError = document.querySelector("#signup-username + span");
const signupPassword = document.getElementById("signup-password");
const signupPasswordError = document.querySelector("#signup-password + span");
const signupRepeatPassword = document.getElementById("signup-repeat-password");
const signupRepeatPasswordError = document.querySelector(
  "#signup-repeat-password + span"
);

// Sign up validation

signupEmail.addEventListener("input", function () {
  const re = /\S+@\S+\.\S+/;
  const validateUserEmail = re.test(signupEmail.value);
  if (!signupEmail) {
    signupEmailError.textContent = "Email cannot be empty";
    signupEmailError.style.display = "block";
  } else {
    signupEmailError.textContent = null;
    signupEmailError.style.display = "none";
  }
  if (!validateUserEmail) {
    console.log(validateUserEmail);
    signupEmailError.textContent = "Email is not valid";
    signupEmailError.style.display = "block";
  } else {
    signupEmailError.textContent = null;
    signupEmailError.style.display = "none";
  }
});

signupUsername.addEventListener("input", function () {
  if (!signupUsername.value) {
    signupUsernameError.textContent = "Username cannot be empty";
    signupUsernameError.style.display = "block";
  } else {
    signupUsernameError.textContent = null;
    signupUsernameError.style.display = "none";
  }
});

signupPassword.addEventListener("input", function () {
  if (!signupPassword.value) {
    signupPasswordError.textContent = "Password cannot be empty";
    signupPasswordError.style.display = "block";
  } else {
    signupPasswordError.textContent = null;
    signupPasswordError.style.display = "none";
  }
});

signupRepeatPassword.addEventListener("input", function () {
  if (!signupRepeatPassword.value) {
    signupRepeatPasswordError.textContent = "Repeat Password cannot be empty";
    signupRepeatPasswordError.style.display = "block";
  } else {
    signupRepeatPasswordError.textContent = null;
    signupRepeatPasswordError.style.display = "none";
  }
  if (signupPassword.value !== signupRepeatPassword.value) {
    signupRepeatPasswordError.textContent =
      "Password is not equal to repeat password";
    signupRepeatPasswordError.style.display = "block";
  } else {
    signupRepeatPasswordError.textContent = null;
    signupRepeatPasswordError.style.display = "none";
  }
});
