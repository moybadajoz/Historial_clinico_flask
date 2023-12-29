const checks = document.querySelectorAll(".change")
checks.forEach(check => {
    const checkbox = check.childNodes[1].childNodes[1]
    const textarea = check.childNodes[3]
    checkbox.addEventListener("change", () => {
        textarea.hidden = !checkbox.checked
    });
});

let id_del = null
function delete_card(id) {
    const card = document.querySelector(".alert-box")    
    card.style.display = 'flex'
    id_del = id
}

function delete_() {
    fetch(`/eliminar?id=${id_del}`, {method: 'POST'})
    .then(Response => {
        location.reload()
    })
    .catch(error => {
        console.log('error')
    })
}

function close_card() {
    const card = document.querySelector(".alert-box")    
    card.style.display = 'none'
    id_del = null
}
