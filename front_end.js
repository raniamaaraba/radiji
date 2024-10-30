const {characterCheck} = require("./ja_en.js");
window.addEventListener('keydown', (e) => {
    console.log(e.key)
    if (e.key === 'Enter') {
        characterCheck(document.getElementById("Search"))
    }
})