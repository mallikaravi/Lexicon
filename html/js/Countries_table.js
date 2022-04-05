function initializeTable() {
    $("#createLink").click(createCountry);
    addCountryToTable("Sweden", "Stockholm");
    addCountryToTable("Germany", "Berlin");
    addCountryToTable("France", "Paris");
    fixRowLinks();
}

function createCountry() {
    let country = $('#newCountryText').val();
    let capital = $('#newCapitalText').val();
    addCountryToTable(country, capital, true);
    $('#newCountryText').val('');
    $('#newCapitalText').val('');
    fixRowLinks();
}
//we are creating row with given data and appending same to the table
function addCountryToTable(country, capital) {
    let row = $('<tr>')
        .append($("<td>").text(country))
        .append($("<td>").text(capital))
        .append($("<td>")
            .append($("<a href='#'>[Up]</a>").click(moveRowUp))
            .append(" ")
            .append($("<a href='#'>[Down]</a>").click(moveRowDown))
            .append(" ")
            .append($("<a href='#'>[Delete]</a>").click(deleteRow)));
    row.css('display', 'none');
    $("#countriesTable").append(row);
    row.fadeIn();
}
//will be called when we press the "up" button and the current row will be moved up
function moveRowUp() {
    let row = $(this).parent().parent();
    row.fadeOut(function() {
        row.insertBefore(row.prev());
        row.fadeIn();
        fixRowLinks();
    });
}

function moveRowDown() {
    let row = $(this).parent().parent();
    row.fadeOut(function() {
        row.insertAfter(row.next());
        row.fadeIn();
        fixRowLinks();
    });
}

function deleteRow() {
    let row = $(this).parent().parent();
    row.fadeOut(function() {
        row.remove();
        fixRowLinks();
    });
}



function fixRowLinks() {

    $('#countriesTable a').css('display', 'inline');
    let tableRows = $('#countriesTable tr');

    //second row doesnt need "up" action

    $(tableRows[2]).find("a:contains('Up')")
        .css('display', 'none');

    //last row that doesnt need "down" action
    $(tableRows[tableRows.length - 1]).find("a:contains('Down')")
        .css('display', 'none');
}