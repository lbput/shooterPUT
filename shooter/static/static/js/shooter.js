// enable ajax
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
     if (!(/^http:.*/.test(settings.url)
             || /^https:.*/.test(settings.url))) {
         // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken",
     $('input[name="csrfmiddlewaretoken"]').val());
     }
    }
});

$(document).on('ready', function() {

    $('#id_tour').on('change', function() {
       var tour = $(this).find(':selected').text();

        $.ajax({
           type: 'POST',
           url: '/tournament/get_comp_for_tour/',
           data: {
               tour: tour
           },
           success: function(data) {
               $('#id_comp').children().remove();
               $.each(data, function(key, val) {
                  $('#id_comp')
                      .append(
                          $('<option></option>')
                              .attr("value", key)
                              .text(val)
                      );
               });
           },
           error: function (request, status, error) {
               alert(request.responseText);
           }
        });
    });

    // $('#id_ammo').click(function() {
    //     $("#txtAge").toggle(this.checked);
    //     alert($('#id_ammo').prop('checked'))
    // });
    
    $('#tournament_signup').on('click', function() {
       if ($('#id_tour').val() == 0) {
           alert("You have to select a tournament");
           return false;
       }

       var tour = $('#id_tour').val();
       var comp = $('#id_comp').val();
       var ammo = $('#id_ammo').prop('checked');

       if (typeof tour == 'undefined' || tour == 0) {
           alert("You have to select a tournament");
           return false;
       }

       if (typeof comp == 'undefined' || comp == 0) {
           alert("You have to select a competition");
           return false;
       }
       var choice;
        if (ammo == true)
          choice = 'true';
        else 
          choice = 'false';

      $.ajax({
            type: 'POST',
            url: '/tournament/tournament_signup_ajax/',
            data: {
                tour: $('#id_tour').find(':selected').text(),
                comp: $('#id_comp').find(':selected').text(), 
                ammo: choice
            },
            success: function(data) {

                $('#bk').modal('show')  
                //alert("Ok, zostales zapisany.");
                top.location.href="/tournament";//redirection
                //$('#res_t').html(data.OK);
            },
            error: function (request, status, error) {
                alert(request.responseText);
            }
        });
    });

    $('#id_year').on('change', function() {
       var year = $(this).find(':selected').text();

        $.ajax({
           type: 'POST',
           url: '/tournament/get_tournaments/',
           data: {
               year: year
           },
           success: function(data) {
               $('#id_tournament').children().remove();
               $.each(data, function(key, val) {
                  $('#id_tournament')
                      .append(
                          $('<option></option>')
                              .attr("value", key)
                              .text(val)
                      );
               });
           },
           error: function (request, status, error) {
               alert(request.responseText);
           }
        });
    });

    $('#id_tournament').on('change', function() {
       var tour = $(this).find(':selected').text();
       var year = $('#id_year').find(':selected').text();

        $.ajax({
           type: 'POST',
           url: '/tournament/get_competitions/',
           data: {
               year:year,
               tour: tour
           },
           success: function(data) {
               $('#id_competition').children().remove();
               $.each(data, function(key, val) {
                  $('#id_competition')
                      .append(
                          $('<option></option>')
                              .attr("value", key)
                              .text(val)
                      );
               });
           },
           error: function (request, status, error) {
               alert(request.responseText);
           }
        });
    });

    $('#show_results').on('click', function() {
       if ($('#id_year').val() == 0) {
           alert("You have to select a year");
           return false;
       }

       var tour = $('#id_tournament').val();
       var comp = $('#id_competition').val();

       if (typeof tour == 'undefined' || tour == 0) {
           alert("You have to select a tournament");
           return false;
       }

       if (typeof comp == 'undefined' || comp == 0) {
           alert("You have to select a competition");
           return false;
       }

        $.ajax({
            type: 'POST',
            url: '/tournament/get_result_current_user/',
            data: {
                year: $('#id_year').find(':selected').text(),
                tour: $('#id_tournament').find(':selected').text(),
                comp: $('#id_competition').find(':selected').text()
            },
            success: function(data) {
                $('#results_table').html(data.table);
            },
            error: function (request, status, error) {
                alert(request.responseText);
            }
        });
    });


});
