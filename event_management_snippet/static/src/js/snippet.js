odoo.define('event_management_snippet.dynamic', function (require) {
    var core = require('web.core');
    var publicWidget = require('web.public.widget');
    var QWeb = core.qweb;
    var rpc = require('web.rpc');
    console.log('sndkmc')

    var EventCarousel = publicWidget.Widget.extend({
        selector: '.js_dynamic_snippet',
        willStart: async function(){
            await rpc.query({
                route: '/latest_events',
            }).then((data) =>{
                this.data = data;
                console.log('data--->',data);
            })
        },

        start: function(){
            var chunks = _.chunk(this.data,4)
            chunks[0].is_active = true
            this.$el.find('#total_booking').html(
            QWeb.render('event_management_snippet.event_carousel',{
                chunks
            })
            )
            },
        })
        publicWidget.registry.js_dynamic_snippet = EventCarousel;
        return EventCarousel
})
