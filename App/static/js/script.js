// const checkbox = document.querySelector("#mostrar-textarea");
// const textarea = document.querySelector("#textarea");

// checkbox.addEventListener("change", () => {
//   textarea.hidden = !checkbox.checked;
// });
const checks = document.querySelectorAll(".change")
checks.forEach(check => {
    const checkbox = check.childNodes[1].childNodes[1]
    const textarea = check.childNodes[3]
    checkbox.addEventListener("change", () => {
        textarea.hidden = !checkbox.checked
    });
});
