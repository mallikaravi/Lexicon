function attachEvents() {
    $("#showTownsButton ").on("click ", show);
    $("#items li").on("click", select);

    function select() {
        let li = $(this);

        if (li.attr("data-selected")) {
            li.removeAttr("data-selected");

            li.css("background", "");
        } else {
            li.attr("data-selected", true)
            li.css("background", "#ddd")
        }
    }

    function show() {
        let selectedList = $("#items li[data-selected=true]");
        let towns = selectedList.toArray()
            .map(li => li.textContent)
            .join(",");
        $("#selectedTowns").text("selected towns:" + towns)

    }



}