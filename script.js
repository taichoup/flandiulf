var sources = [
    {
        name:"journaldesfemmes",   // same as 20 minutes.fr ?
        charset: "iso-8859-1",
        url:"http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/%s-jour/",
        amour:".//div[@class='layout_main']/table/tbody/tr[6]/",
        argent:".//div[@class='layout_main']/table/tbody/tr[9]/",
        sante:".//div[@class='layout_main']/table/tbody/tr[12]/",
        travail:".//div[@class='layout_main']/table/tbody/tr[15]/"
    }, {
        name:"horoscope.fr",
        charset:"utf-8",
        url:"http://www.horoscope.fr/horoscopes/horoscope_%s.html",
        amour:".//div[@id='horo-jour-amour']/div/p[2]",
        argent:".//div[@id='horo-jour-travail']/div[2]/div[2]/p",
        sante:".//div[@id='horo-jour-bienetre']/div[1]/div[2]/p",
        travail:".//div[@id='horo-jour-travail']/div[1]/div[2]/p"
    }, {
        name:"le parisien",
        charset:"utf-8",
        url:"http://astrologie.leparisien.fr/astrologie/zodiaque/%s.html",
        amour:".//article[@class='np-article-predictionvipsign']/section/div/article/p[1]",
        argent:"",
        sante:".//article[@class='np-article-predictionvipsign']/section/div/article/p[3]",
        travail:".//article[@class='np-article-predictionvipsign']/section/div/article/p[2]"
    }, {
        name:"elle.fr",
        charset:"utf-8",
        url:"http://www.elle.fr/Astro/Horoscope/Quotidien/%s",
        amour:".//article[@id='text']/p[1]",
        argent:".//article[@id='text']/p[2]",
        sante:".//article[@id='text']/p[3]",
        travail:".//article[@id='text']/p[4]"
    }
]

function sendForm(form) {
    var sign = document.getElementById("select_sign").value;
    var category = document.getElementById("select_cat").value;
    // document.getElementById("select_sign").submit();
    alert("Sign is " + sign + " and category is " + category);
    var request = {
        s: sign,
        c: category
    };
    console.log(request);
    return request;
}

var out = ""; // container for fetched values
 
function parse() {
 $('a').each( // go through each anchor on page and make ajax request to fetch html
  function(idx, item) { 
   var url = $(item).attr('href'); // get url
   console.log('Fetching: '+ url); // debug note
    
   // make ajax request (http://api.jquery.com/jQuery.ajax/)
   $.ajax({
    url: url, 
    async: false, // do it synchronously
   }).done(function(data) { // data variable contains fetched html
    var dataRetrieved = $('div',$(data)).html(); // get value we're looking for
    console.log( 'Retrieved ' +  dataRetrieved); // debug note
     
    out += dataRetrieved + "\n"; // save retrieved value (+ separator)
   });
  } 
 );
 console.log("-----------------\nParsing done, output:\n"+out); // print out parsed values
}