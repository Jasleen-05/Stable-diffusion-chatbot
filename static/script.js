window.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector("form");
  const spinner = document.getElementById("spinner");
  const image = document.getElementById("generated-image");

  if (form && spinner) {
    form.addEventListener("submit", () => {
      spinner.classList.remove("hidden");
    });
  }

  if (image && spinner) {
    image.onload = () => {
      spinner.classList.add("hidden");
    };
  }
});