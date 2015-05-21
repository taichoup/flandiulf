var sources = [
    {
        name:"journaldesfemmes",   // same as 20 minutes.fr ?
        url:"http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/%s-jour/".replace('%s', "belier"),
        amour:".//div[@class='layout_main']/table/tbody/tr[6]/",
        argent:".//div[@class='layout_main']/table/tbody/tr[9]/",
        sante:".//div[@class='layout_main']/table/tbody/tr[12]/",
        travail:".//div[@class='layout_main']/table/tbody/tr[15]/"
    }, {
        name:"horoscope.fr",
        url:"http://www.horoscope.fr/horoscopes/horoscope_%s.html".replace('%s', "belier"),
        amour:".//div[@id='horo-jour-amour']/div/p[2]",
        argent:".//div[@id='horo-jour-travail']/div[2]/div[2]/p",
        sante:".//div[@id='horo-jour-bienetre']/div[1]/div[2]/p",
        travail:".//div[@id='horo-jour-travail']/div[1]/div[2]/p"
    }, {
        name:"le parisien",
        url:"http://astrologie.leparisien.fr/astrologie/zodiaque/%s.html".replace('%s', "belier"),
        amour:".//article[@class='np-article-predictionvipsign']/section/div/article/p[1]",
        argent:"",
        sante:".//article[@class='np-article-predictionvipsign']/section/div/article/p[3]",
        travail:".//article[@class='np-article-predictionvipsign']/section/div/article/p[2]"
    }, {
        name:"elle.fr",
        url:"http://www.elle.fr/Astro/Horoscope/Quotidien/%s".replace('%s', "belier"),
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

request = {s:"belier", c:"sante"} // this will later be set differently

var out = ""; // container for fetched values

