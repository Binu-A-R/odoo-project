odoo.define('product_grade.receipt', function (require) {
"use strict";

    var { Orderline } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');


    const ProductGrade = (Orderline) => class ProductGrade extends Orderline {
        export_for_printing() {
            var line = super.export_for_printing(...arguments);
            line.product_grade = this.get_product().product_grade;
            return line;
        }
}
Registries.Model.extend(Orderline, ProductGrade);

});
