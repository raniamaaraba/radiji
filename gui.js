const {characterCheck} = require("./ja_en.js");
const pgAdmin = require("postgres");
const {app, BrowserWindow, ipcMain} = require("electron");
const sql = pgAdmin({})
const path = require('node:path')

let win = null;

const createWindow = () => {
    win = new BrowserWindow({
        width: 800,
        height: 600,
        resizeable: false,
        webPreferences: {
            nodeIntegration: true,
            preload: path.join(__dirname, 'front_end.js')
        }
        
    })
    ipcMain.handle('ping', () => 'pong')

    win.loadFile("index.html");
    win.webContents.openDevTools();

};

app.whenReady().then(createWindow);
