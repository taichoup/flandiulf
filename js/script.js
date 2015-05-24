
var request = {};

function sendForm(form) {
    var sign = document.getElementById("select_sign").value;
    var category = document.getElementById("select_cat").value;
    // alert("Sign is " + sign + " and category is " + category);
    request.s = sign;
    request.c = category;
    // console.log(request);
    return request;
}

function resetTable() {
    $("#results-table").remove();
}


$(document).ready(function() {
    $("button").click(function() {
        sendForm();
        var jqxhr = $.getJSON("../astrodump2.json", function() {
            //blop
        })
            .done(function(data) {
                alert("External content loaded successfully!");
                var items = [];
                // resetTable();
                $.each(data, function(i) {
                    var sign = data[i].sign;
                    var cat = data[i].category;
                    if (sign === request.s && cat === request.c) {
                        items.push( "<tr><td>" + data[i].source + "</td><td>" + data[i].content + "</td></tr>" );
                    }
                });
                $( "<table/>", {
                    "class": "table",
                    "id": "results-table",
                    html: items.join( "" )
                }).appendTo( "body" );
            })
            .fail(function() {
                alert("JQXHR ERROR.");
            });
    });
});