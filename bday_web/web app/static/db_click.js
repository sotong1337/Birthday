$('tr').click( function() {
    var new_window = $(this).find('a').attr('href');
    if (new_window != undefined) {
        window.location = new_window
    }
});