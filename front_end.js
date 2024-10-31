const { contextBridge, ipcRenderer } = require('electron');
const {characterCheck} = require("./ja_en.js");

contextBridge.exposeInMainWorld('versions', {
    node: () => process.versions.node,
    chrome: () => process.versions.chrome,
    electron: () => process.versions.electron,
    ping: () => ipcRenderer.invoke('ping')
})



window.addEventListener('keydown', (e) => {
    console.log(e.key)
    if (e.key === 'Enter') {
        characterCheck(document.getElementById("Search").value)
    }
})