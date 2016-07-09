$("button").click(function() {
    var url = $("#url").val();

    $.post(
      "/get_new_url/",
      {"url": url},
      function(data) {
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
            function() {$("#new_url_input").select();},
            100
          );
         }
      }
    );
});