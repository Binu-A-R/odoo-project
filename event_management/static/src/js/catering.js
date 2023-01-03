$(document).ready(function () {
    $('.advanced-select').select2();
            console.log('start_date-->')

    $(function() {
            $("#start_date").datepicker();
            var date1 = $("#start_date")
            console.log('start_date-mcf->',date1)

    });
     $(function() {
                $("#end_date").datepicker();
                var date2 = $("#date2")
                            console.log('end_date-mcf->',date2)

            });
             function func() {
                date1 = new Date(date1.value);
                date2 = new Date(date2.value);
                var milli_secs = date1.getTime() - date2.getTime();
                var days = milli_secs / (1000 * 3600 * 24);
                console.log('days',days)
                document.getElementById("duration").innerHTML =
                Math.round(Math.abs(days));
}
});