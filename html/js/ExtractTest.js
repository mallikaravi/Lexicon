function extractTest() {
    $(document).ready(function() {
        let a = [];
        var listItems = $("#items li");
        for (let li of listItems) {
            let result = $(li).text();
            a.push(result);
        }
        $("button").css('background-color', "yellow");
        $('#result').text(a.join(','));

    });
}