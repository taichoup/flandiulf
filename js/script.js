
var request = {};

stopwords = [
    "ai",
    "aie",
    "aient",
    "aies",
    "ait",
    "alors",
    "as",
    "au",
    "aucuns",
    "aura",
    "aurai",
    "auraient",
    "aurais",
    "aurait",
    "auras",
    "aurez",
    "auriez",
    "aurions",
    "aurons",
    "auront",
    "aussi",
    "autre",
    "aux",
    "avaient",
    "avais",
    "avait",
    "avant",
    "avec",
    "avez",
    "aviez",
    "avions",
    "avoir",
    "avons",
    "ayant",
    "ayante",
    "ayantes",
    "ayants",
    "ayez",
    "ayons",
    "c",
    "car",
    "ce",
    "cet",
    "cette",
    "cela",
    "ceci",
    "ces",
    "ceux",
    "chaque",
    "ci",
    "comme",
    "comment",
    "d",
    "dans",
    "de",
    "dedans",
    "dehors",
    "depuis",
    "des",
    "devrait",
    "doit",
    "donc",
    "dos",
    "du",
    "début",
    "elle",
    "elles",
    "en",
    "encore",
    "es",
    "essai",
    "est",
    "et",
    "eu",
    "eue",
    "eues",
    "eurent",
    "eus",
    "eusse",
    "eussent",
    "eusses",
    "eussiez",
    "eussions",
    "eut",
    "eux",
    "eûmes",
    "eût",
    "eûtes",
    "fait",
    "faites",
    "fois",
    "font",
    "furent",
    "fus",
    "fusse",
    "fussent",
    "fusses",
    "fussiez",
    "fussions",
    "fut",
    "fûmes",
    "fût",
    "fûtes",
    "hors",
    "ici",
    "il",
    "ils",
    "j",
    "je",
    "juste",
    "l",
    "la",
    "le",
    "les",
    "leur",
    "lui",
    "là",
    "m",
    "ma",
    "maintenant",
    "mais",
    "me",
    "mes",
    "mine",
    "moi",
    "moins",
    "mon",
    "mot",
    "même",
    "n",
    "ne",
    "ni",
    "nommés",
    "nos",
    "notre",
    "nous",
    "on",
    "ont",
    "ou",
    "où",
    "par",
    "parce",
    "pas",
    "peu",
    "peut",
    "plupart",
    "pour",
    "pourquoi",
    "qu",
    "quand",
    "que",
    "quel",
    "quelle",
    "quelles",
    "quels",
    "qui",
    "s",
    "sa",
    "sans",
    "se",
    "sera",
    "serai",
    "seraient",
    "serais",
    "serait",
    "seras",
    "serez",
    "seriez",
    "serions",
    "serons",
    "seront",
    "ses",
    "seulement",
    "si",
    "sien",
    "soient",
    "sois",
    "soit",
    "sommes",
    "son",
    "sont",
    "sous",
    "soyez",
    "soyons",
    "suis",
    "sur",
    "t",
    "ta",
    "tandis",
    "te",
    "tellement",
    "tels",
    "tes",
    "toi",
    "ton",
    "tous",
    "tout",
    "trop",
    "très",
    "tu",
    "un",
    "une",
    "voient",
    "vont",
    "vos",
    "votre",
    "vous",
    "y",
    "à",
    "ça",
    "étaient",
    "étais",
    "était",
    "étant",
    "étante",
    "étantes",
    "étants",
    "étiez",
    "étions",
    "été",
    "étée",
    "étées",
    "étés",
    "être"
]

function sendForm(form) {
    var sign = document.getElementById("select_sign").value;
    var category = document.getElementById("select_cat").value;
    request.s = sign;
    request.c = category;
    return request;
}

function resetTable() {
    $("#results-table").remove();
    $(".wordcloud").remove();
}


$(document).ready(function() {

    // SHIT THAT HAPPENS WHEN BUTTON IS CLICKED
    $("#formButton").click(function() {

        sendForm();

        var jqxhr = $.getJSON("../astrodump2.json",

function() {
        })
            .done(function(data) {
                var items = [];
                var listOfWords = [];
                resetTable();
                $.each(data,
function(i) {
                    var sign = data[i].sign;

                    var cat = data[i].category;

                    if (sign === request.s && cat === request.c) {
                        
                        items.push( "<tr><td>" + data[i].source + "</td><td>" + data[i].timestamp + "</td><td>" + data[i].content + "</td></tr>" );

                        var content = data[i].content.replace(/[\.,-\/#!$%\^&\*;:{}=\-_`~()]/g,"");
                        
                        var content = content.replace(/\s{2,}/g," ");
                        
                        listOfWords.push.apply(listOfWords, content.split(" "));
                    }
                });

                listOfWords = listOfWords.map(function(w) {
                    return w.toLowerCase();
                });

                function remove_stopwords(w) {
                    return stopwords.indexOf(w) === -1;
                }

                var filtered = listOfWords.filter(remove_stopwords);

                var filtered_with_weights = {};

                for (i=0;i<filtered.length;i++) {

                    if (filtered_with_weights[filtered[i]]) {

                        filtered_with_weights[filtered[i]] += 1;
                    }

                    else {filtered_with_weights[filtered[i]] = 1;}
                }

                // console.log(filtered_with_weights);

                LOW = filtered.map(function(w) {

                    return {text: w, size: 10 + filtered_with_weights[w] * 60}; // JNEED TO CHANGE THIS, MAKE IT AN INCREMENT LOOP OR FUNCTION !!!!
                
                })
                
                // [{text: "hello", size = 1}, {text: "world", size = 1}]


                $( "<table/>",
                    {
                        "class": "table",
                        "id": "results-table",
                        html: items.join( "" )
                    }
                ).appendTo( "#table-wrapper" );

                document.getElementById("cloud_button").disabled = false

            })
            .fail(function() {
                alert("JQXHR ERROR.");
            });
    });

});