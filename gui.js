const {characterCheck} = require("./ja_en.js");
const pgAdmin = require("postgres");
const {app, BrowserWindow} = require("electron");
const sql = pgAdmin({})

let win = null;

const createWindow = () => {
    win = new BrowserWindow({
        width: 800,
        height: 600,
        resizeable: false,
        webPreferences: {
            nodeIntegration: true
        }
    })

    win.loadFile("index.html");
    win.webContents.openDevTools();

};

app.whenReady().then(createWindow);
