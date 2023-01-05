$(document).ready(function () {
    $('.advanced-select').select2();
    $('#btn').on('click', function(){
             var start_date = $('#start_date').val();
             console.log("start date",start_date)


             var end_date = $('#end_date').val();
             console.log("end_date",end_date)

             if (end_date < start_date){
                 alert('End date should be greater than Start date.');
                $('#end_date').val('');
             }
             console.log("Success: end date  changes")
    });



   $(document).ready(function() {
  $('#start_date').on('change', function(){
    var startDate = new Date($('#start_date').val());
                                  console.log("start date",startDate)

    var endDate = new Date($('#end_date').val());
                                  console.log("end date",endDate)

    var timeDiff = Math.abs(endDate.getTime() - startDate.getTime());
    var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));
                                      console.log("diffDays",diffDays)

        $('#duration').val(diffDays);
         });
    $('#end_date').on('change', function(){
        var startDate = new Date($('#start_date').val());
        console.log("start date",startDate)

        var endDate = new Date($('#end_date').val());
         console.log("end date",endDate)

        var timeDiff = Math.abs(endDate.getTime() - startDate.getTime());
        var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));
        console.log("diffDays",diffDays)
//        $('#duration').val(diffDays);

                $('#duration').val(diffDays);




    })
  });
});



