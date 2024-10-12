const form = document.querySelector("#login-form");
const message = document.querySelector("#message");

const dbUsername = "Username";
const dbPassword = "Password";

form.addEventListener("submit", (event) => {
  event.preventDefault();

  // get user inputs

  const username = event.target.username.value;
  const password = event.target.password.value;

  if (username === dbUsername && password === dbPassword) {
    message.textContent = "Login successful";
  } else {
    message.textContent = "Incorrect username or password";
  }

  // Clear form input

  event.target.reset();
});
