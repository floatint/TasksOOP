function convert() {
        var valsList = document.getElementById("fromValutes");
        var val1_name = valsList.options[valsList.selectedIndex].value;
        valsList = document.getElementById("toValutes");
        var val2_name = valsList.options[valsList.selectedIndex].value;
        var inputArea = document.getElementById("fromVal");
        var count = inputArea.value;
    $.ajax({
        type: "POST",
        url: '/convert',
        data: {'val1_name': val1_name, 'val2_name': val2_name, 'count': count},
        type: 'POST',
        success: function(response) {
            if (response["error"] == true){
                alert("Processing error. " + response["answer"]);
                document.getElementById("fromVal").value = null;
                document.getElementById("toVal").value = null;
                exit;
                }
            $('#toVal').val(response["answer"])
            console.log(response);
        },
        error: function(error) {
            alert('System error. See console.')
            console.log(error);
        }
    });
}

function change_val(){
    //document.getElementById("fromVal").value = null;
    document.getElementById("toVal").value = null;
}