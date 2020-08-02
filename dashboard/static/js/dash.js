$(document).ready(function(){

    $("#ChicagoButton").click(function() {
        var serializedData = $("#selectCityForm").serialize();
        serializedData['city'] = "test"
        console.log(serializedData);
        $.ajax({
            url: $("selectCityForm").data('url'),
            data: serializedData,
            type: 'post',
            success: function(response) {
                $("#citySelectedList").append(
                '<h1>' + response.city_selected + ' Selected!</h1>'
                )
            }
        })
    });

});

