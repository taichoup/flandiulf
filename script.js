
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
        var jqxhr = $.getJSON("astrodump.json", function(responseTxt, statusTxt, xhr) {
            //blop
        })
            .done(function(data) {
                alert("External content loaded successfully!");
                var items = [];
                $.each(data, function(key, val) {
                    items.push( "<li id='" + key + "'>" + val + "</li>" );
                });
                console.log(items);
                $( "<ul/>", {
                    "class": "my-new-list",
                    html: items.join( "" )
                }).appendTo( "body" );
            })
            .fail(function() {
                alert("Error: " + xhr.status + ": " + xhr.statusText);
            });
    });
});