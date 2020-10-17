

function add_option(nazwa_opcji, nazwa_formularza){
    var option = document.createElement("option");
    option.text = nazwa_opcji;
    option.value = nazwa_opcji;
    nazwa_formularza.add(option);
};




var form_pochodzenie = document.getElementById("form_pochodzenie");
var form_rowery = document.getElementById("form_rowery");

function get_pochodzenie_options(){
    const Http = new XMLHttpRequest();
    const url='/pochodzenie';
    Http.open("POST", url);
    Http.send();

    Http.onreadystatechange = (e) => {
         if(Http.readyState === 4){
           var pochodzenie_lista = Http.responseText.split(';'); //responseTEXT = odpowiedz (return) z formularza Flask
           //console.log(pochodzenie_lista); //console log pokazuje tylko w konsoli przegladarki
           pochodzenie_lista.forEach(element => add_option(element, form_pochodzenie));
         };

    };
};


function get_rowery_options(){

    var form_pochodzenie = document.getElementById("form_pochodzenie");
    var pochodzenie_value = form_pochodzenie.value;

    //console.log(pochodzenie_value);
    const Http = new XMLHttpRequest();
    const url=`/rowery?pochodzenie=${pochodzenie_value}`;
    Http.open("POST", url);
    Http.send();

    Http.onreadystatechange = (e) => {
         if(Http.readyState === 4){
           var rowery_lista = Http.responseText.split(';');
           //console.log(rowery_lista);
           rowery_lista.forEach(element => add_option(element, form_rowery));
         };

    };
};


get_pochodzenie_options();

form_pochodzenie.addEventListener("change", get_rowery_options); // jak sie zmienia formularz pochodzenie to wywoluje funkcje get_rowery_options

//
//if(jezeli cos){
//
//wykonaj
//}
//



