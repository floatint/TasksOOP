function convert() {
        var valsList = $('#fromValutes')[0];
        var val1_name = valsList.options[valsList.selectedIndex].value;
        valsList = $("#toValutes")[0];
        var val2_name = valsList.options[valsList.selectedIndex].value;
        var inputArea = $('#fromVal')[0];
        var count = inputArea.value;
    $.ajax({
        type: "POST",
        url: '/convert',
        data: {'val1_name': val1_name, 'val2_name': val2_name, 'count': count},
        success: function(response) {
            if (response.error){
                alert("Processing error. " + response.message);
                $('#fromVal')[0].value = null;
                $('#toVal')[0].value = null;
                return;
            }
            $('#toVal')[0].text = response['answer'] + response['answer'];
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