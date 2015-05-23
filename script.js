
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



$(document).ready(function() {
    $("button").click(function() {
        var jqxhr = $.getJSON("astrodump2.json", function(responseTxt, statusTxt, xhr) {
            //blop
        })
            .done(function(data) {
                // alert("External content loaded successfully!");
                var items = [];
                $.each(data, function(i) {
                    if (data[i].sign === request.s && data[i].category === request.c) {
                        console.log("match");
                        items.push( "<tr><td>" + data[i].source + "</td><td>" + data[i].content + "</td></tr>" );
                    }
                    else {
                        continue
                    }
                });
                $( "<table/>", {
                    "class": "table",
                    html: items.join( "" )
                }).appendTo( "body" );
            })
            .fail(function() {
                alert("Error: " + xhr.status + ": " + xhr.statusText);
            });
    });
});