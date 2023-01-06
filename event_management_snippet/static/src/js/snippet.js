odoo.define('event_management_snippet.dynamic', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   console.log('sndkmc')
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.js_dynamic_snippet',
       start:  function () {
           var self = this;
             rpc.query({
               route: '/latest_events',
               params: {},
           }).then(function (result) {
               self.$('#total_booking').html(result);
               console.log('result--->', result)
           });
       },
   });
             console.log('result--->')

   PublicWidget.registry.js_dynamic_snippet = Dynamic;
   return Dynamic;
});