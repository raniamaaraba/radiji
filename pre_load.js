//pre-load file : intermedian

const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('versions', {
    loadNewPage: (fileName) => ipcRenderer.invoke('search-feature',fileName),
    languageDefine: (L) => ipcRenderer.invoke('lang-query', L),
    load: (searching) => ipcRenderer.invoke('search-feature', searching),
    load: (define) => ipcRenderer.invoke('define-feature', define)
})




