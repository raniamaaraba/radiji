//render - client side file


function characterDetermine(string){
    let kanji = false;
    let hiragana = false;
    let english = false;
    let katakana = false;
    if ((/^[A-Z a-z]+$/.test(string)) === true){
        // tests for english characters
        english = true;
        return ["English", string];
    }
    else if ((/[\u2f00-\u2fdf\u4e00-\u9fff]+/.test(string)) === true){
        //tests if the given string contains any kanji characters
        kanji = true;
        return ["Japanese" , string];
    }
    else if ((/[\u3040-\u309f]+/.test(string)) === true ){
        //tests if there any hiragana characters present in the string
        hiragana = true;
        return ["Kun-Yomi", string];
    } else {
        //defaults to hiragana otherwise
        katakana = true;
        return ["On-Yomi",string]
    }    
}

window.addEventListener('keydown', (e) => {
    console.log(e.key)
    if (e.key === 'Enter') {
        const language = characterDetermine(document.getElementById("Search").value);
        const result =  window.versions.languageDefine(language);
        localStorage.setItem('db_res', JSON.stringify(result));
        const storedJSONData = localStorage.getItem('db_res');
        if (language === 'Japanese') {
            window.versions.loadNewPage('search.html');
        } else {
            window.versions.loadNewPage('definition.html');
        }
        
    }
})




