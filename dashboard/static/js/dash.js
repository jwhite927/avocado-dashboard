$(document).ready(function(){

    $("[name|='city']").change(function() {
        var serializedData = $("#selectCityForm").serialize();
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

