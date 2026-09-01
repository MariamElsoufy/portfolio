document.getElementById("year").textContent = new Date().getFullYear();

function copyEmailWithFeedback(el, email, restoreText) {
  navigator.clipboard.writeText(email).then(() => {
    el.textContent = "Copied!";
    setTimeout(() => { el.textContent = restoreText; }, 1500);
  });
}

const emailCopy = document.getElementById("email-copy");
if (emailCopy) {
  emailCopy.style.cursor = "pointer";
  emailCopy.addEventListener("click", () => {
    copyEmailWithFeedback(emailCopy, emailCopy.dataset.email, emailCopy.dataset.email);
  });
}
