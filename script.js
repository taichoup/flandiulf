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