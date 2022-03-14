$(document).ready(function() {
    function validate() {

        console.log("validating");

        var day = parseInt($("#days").val());
        var month = parseInt($("#months").val());

        console.log("day: " + day);
        console.log("month: " + month);

        var daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

        if(month == 2) {
            if(day > 29) {
                $("#dayAlert").text("February only has 29 days");
                $('#sub').prop('disabled', true);
                return false;
            }
            else{
                $("#dayAlert").text("");
                $('#sub').prop('disabled', false);
                return true;
            }
        }
        else if(day > daysInMonth[month-1]){
            $("#dayAlert").text("That month only has " + daysInMonth[month-1] + " days");
            $('#sub').prop('disabled', true);
            return false;
        }
        else{
            $("#dayAlert").text("");
            $('#sub').prop('disabled', false);
            return true;
        }
    };

    $("#days").change(function(){
        $("#dayAlert").text("");
        var currentText = parseInt($(this).val());
        validate();
        if(currentText > 31 || currentText < 1){
            $("#dayAlert").text("Days should be a valid number between 1 and 31");
        }
    });
    $("#months").change(function(){
        $("#monthAlert").text("");
        validate();
        var currentText = parseInt($(this).val());
        if(currentText > 12 || currentText < 1){
            $("#monthAlert").text("Months should be a valid number between 1 and 12");
        }
    });

});

function clicked(e) {
    if(!confirm('This action cannot be undone.\n Are you sure you hate this person?')) {
        e.preventDefault();
    }
}