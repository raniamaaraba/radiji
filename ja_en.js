function characterDetermine(string){
    let kanji = false;
    let hiragana = false;
    let english = false;
    let katakana = false;
    if ((/^[A-Z a-z]+$/.test(string)) === true){
        // tests for english characters
        english = true;
        console.log("engrish");
    }
    else if ((/[\u2f00-\u2fdf\u4e00-\u9fff]+/.test(string)) === true){
        //tests if the given string contains any kanji characters
        kanji = true;
        console.log("kanji");
    }
    else if ((/[\u3040-\u309f]+/.test(string)) === true ){
        //tests if there any hiragana characters present in the string
        hiragana = true;
        console.log("hirabana");
    } else {
        //defaults to hiragana otherwise
        katakana = true;
        console.log("katakana");
    }    
}
module.exports.characterCheck = characterDetermine;