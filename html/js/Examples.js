/*$(document).ready(function() {
    $("#hide").click(function() {
        $("p").hide(1000);
    });
});
$(document).ready(function() {
    $("#show").click(function() {
        $("p").show(5000);
    });
});
$(document).ready(function() {
    $("button").click(function() {
        $("div.d1").toggle(1500);
    });
});*/
$(document).ready(function() {
    $("#button").click(function() {
        $("#div1").fadeToggle();
        $("#div2").fadeToggle("slow");
        $("#div3").fadeToggle(3000);
    });
});