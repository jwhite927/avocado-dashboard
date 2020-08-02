$(document).ready(function(){

    $("#ChicagoButton").click(function() {
        var serializedData = $("#selectCityForm").serialize();

        $.ajax({
            url: $("selectCityForm").data('url'),
            data: serializedData,
            type: 'post',
            success: function(response) {
                $("#citySelected").append()
            }
        })
    });

});

