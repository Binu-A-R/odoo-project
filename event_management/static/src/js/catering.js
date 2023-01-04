$(document).ready(function () {
    $('.advanced-select').select2();
    $('#end_date').on('change', function(){
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

    $('#start_date').on('change', function(){
                 var start_date = $('#start_date').val();
                  console.log("start date",start_date)

                 var end_date = $('#end_date').val();
                 console.log("end_date",end_date)
if(end_date == true){
                 if (end_date < start_date){
                     alert('End date should be greater than Start date.');
                    $('#start_date').val('');
                 }
                 console.log("Success: start date  changes")
   } });

   $(document).ready(function() {
  $('#start_date').on('change', function(){
    var startDate = new Date($('#start_date').val());
                                  console.log("start date",startDate)

    var endDate = new Date($('#end_date').val());
                                  console.log("end date",endDate)

    var timeDiff = Math.abs(endDate.getTime() - startDate.getTime());
    var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));
                                      console.log("diffDays",diffDays)
if((startDate == true) && (endDate== true)){
        $('#duration').val(diffDays);
        }  });
    $('#end_date').on('change', function(){
        var startDate = new Date($('#start_date').val());
        console.log("start date",startDate)

        var endDate = new Date($('#end_date').val());
         console.log("end date",endDate)

        var timeDiff = Math.abs(endDate.getTime() - startDate.getTime());
        var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));
        console.log("diffDays",diffDays)
        if((startDate == true) && (endDate== true)){
        $('#duration').val(diffDays);
        }
    })
  });
});



