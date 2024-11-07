//main file with back end routine
const postgres = require("postgres");
const {app, BrowserWindow, ipcMain, protocol} = require("electron");
const path = require('node:path')

//file path for postgres
const sql = postgres( {
    host            : '127.0.0.1',
    port            : 5432,
    database         : 'radiji',
    username        : 'rankuluw',
    password        : 'password'
})

//'postgres://username:password@host:port/database'


let win = null;

const createWindow = () => {
    win = new BrowserWindow({
        width: 800,
        height: 700,
        resizeable: false,
        webPreferences: {
            nodeIntegration: true,
            preload: path.join(__dirname, 'pre_load.js')
        }
        
    })
    ipcMain.handle('lang-query', (_,arg) => languageColumn(arg))

    ipcMain.handle('search-feature', (_, searching) => { 
        win.loadFile(searching);
    })

    ipcMain.handle('define-feature', (_, defined) => {
        win.loadFile(defined);
    })

    win.loadFile("index.html");
    win.webContents.openDevTools();

};

async function languageColumn(lang) {
    console.log(lang);
    const language=lang[0];
    const stringVar=lang[1];
    let radiji = null
    if (language === "Japanese") {
        radiji = await sql`
            select
                "Japanese", "English", "Kun-Yomi","On-Yomi"
            from "Japanese-English"
            where "Japanese" = ${lang[1]}
        `
    }
    if (language === "English") {
        radiji = await sql`
            select
                "Japanese", "English", "Kun-Yomi","On-Yomi"
            from "Japanese-English"
            where "English" like ${'%'+lang[1]+'%'}
        `
    }
    if (language === "Kun-Yomi") {
        radiji = await sql`
            select
                "Japanese", "English", "Kun-Yomi","On-Yomi"
            from "Japanese-English"
            where "Kun-Yomi" like ${'%'+lang[1]+'%'}
        `
    }
    if (language === "On-Yomi") {
        radiji = await sql`
            select
                "Japanese", "English", "Kun-Yomi","On-Yomi"
            from "Japanese-English"
            where "On-Yomi" like ${'%'+lang[1]+'%'}
        `
    }
    console.log(radiji);
    return radiji
    //lang 0 " lang 1 '
    
}



app.whenReady().then(createWindow);
