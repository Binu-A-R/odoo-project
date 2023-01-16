odoo.define('product_owner.receipt', function (require) {
"use strict";

    var { Orderline } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');


    const ProductOwner = (Orderline) => class ProductOwner extends Orderline {
        export_for_printing() {
            var line = super.export_for_printing(...arguments);
            line.product_owner_id = this.get_product().product_owner_id;
            return line;
        }
}
Registries.Model.extend(Orderline, ProductOwner);

});
