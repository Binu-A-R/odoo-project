odoo.define('pos_category_discount_limit.discount', function (require) {
    "use strict";
    var { PosGlobalState, OrderLIne } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const NewPosGlobalState = (PosGlobalState) => class NewPosGlobalState extends PosGlobalState {

        async _processData(loadedData) {
            await super._processData(...arguments);
            this.res_config_settings = loadedData['res.config.settings'];
            console.log("-------------------------------------------------------------------------", this.res_config_settings)

        }
    }

    Registries.Model.extend(PosGlobalState, NewPosGlobalState)
    const pay = (ProductScreen) =>
        class extends ProductScreen {

            async _onClickPay() {
                console.log("onclick")

                var orderlines = this.currentOrder.get_orderlines()
                console.log(this.currentOrder.get_orderlines())
                console.log(this.env.pos)
                var check = false
                $.each(this.currentOrder.get_orderlines(), (order, b) => {

                    var i
                    var len = this.env.pos.config.category_discount_ids.length
                    for (let i = 0; i < len; i++) {
                        var limit = this.env.pos.config.discount_value * 100
                        console.log('limit------>', limit)
                        console.log('product.pos_categ_id', b.product.pos_categ_id[i])
                        console.log('category_discount_ids', this.env.pos.config.category_discount_ids[i])
                        console.log('disc', b, order)
                        console.log('pos_categ_id', b.product.pos_categ_id)
                        if (b.product.pos_categ_id[0] == this.env.pos.config.category_discount_ids[i]) {
                            console.log('discount------->', b.discount)
                            b.discount += 
                            console.log('discount------->', b.discount)

                            if (b.discount >= limit) {
                                check = true
                                const { confirmed } = this.showPopup('ConfirmPopup', {
                                    title: ('ERROR'),
                                    body: ('Discount amount of ' + b.product.display_name + ' is exceeded the limit ' +limit +'%'),
                                });
                                return false;
                            }

                            else {
                                console.log('discount<limit')
                                check = false
                            }
                        }
                    }


                });
                if (check == false) {
                    console.log('final')
                    return super._onClickPay()
                }

            }

        }

    Registries.Component.extend(ProductScreen, pay);

});

