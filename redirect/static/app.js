$("button").click(function() {
    var params = {"url": $("#url").val()};

    function success_function(data) {
        if (data['error']) {
            $("#url").tooltip('destroy');
            $("#url").tooltip('hide')
                .attr('data-original-title', data['error'])
                .tooltip('show');
        } else {
            $("#new_url_input").val(data['new_url']);

            $("#orig_url").addClass("hidden");
            $("#new_url").removeClass("hidden");

            setTimeout(
                function() { $("#new_url_input").select(); },
                100
            );
        }
    }

    $.post("/get_new_url/", params, success_function);
});