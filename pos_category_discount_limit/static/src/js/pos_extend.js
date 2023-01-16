odoo.define('discount_limit.discount', function (require) {
"use strict";
var {PosGlobalState,OrderLIne} = require('point_of_sale.models');
const Registries = require('point_of_sale.Registries');
const ProductScreen = require('point_of_sale.ProductScreen');
const NewPosGlobalState = (PosGlobalState) => class NewPosGlobalState extends PosGlobalState {

     async _processData(loadedData){
        await super._processData(...arguments);
        this.res_config_settings = loadedData['res.config.settings'];
        console.log("-------------------------------------",this.res_config_settings)

    }
}

Registries.Model.extend(PosGlobalState,NewPosGlobalState)
  const pay = (ProductScreen) =>
  class extends ProductScreen {

     async _onClickPay(){
       console.log("onclick")
        var limit =  this.env.pos.config.discount_value * 100
       console.log('limit------>', limit)
       var category = this.env.pos.config.category_discount_ids
       console.log('category',category)

       var orderlines = this.currentOrder.get_orderlines()
       console.log(this.currentOrder.get_orderlines())
       console.log(this.env.pos)
       var check = false
       $.each(this.currentOrder.get_orderlines(),(order,b) => {
        console.log('product.pos_categ_id', b.product.pos_categ_id[1])
        console.log('category_discount_ids', this.env.pos.config.category_discount_ids[0])
        console.log('disc', b, order)
        console.log('pos_categ_id', b.product.pos_categ_id)

        if (b.product.pos_categ_id[0] == this.env.pos.config.category_discount_ids[0]){
            console.log('true')
            console.log('discount------->',b.discount)
                if ( b.discount > limit ){
                     console.log('check---->True')

                    check = true
                    console.log('check---->True')
                    const { confirmed } =  this.showPopup('ConfirmPopup', {
                        title:('ERROR'),
                        body:('Discount amount of '+ b.product.display_name +' is exceed the limit'),
                    });
                    return false;b.product.pos_categ_id[0]
                                    console.log('check---->false')

                }
                else
                {
                console.log('discount<limit')
                check = false
            }
          }

        });
        if (check == false){
            console.log('final')
           return super._onClickPay()
           }

       }

     }

    Registries.Component.extend(ProductScreen, pay);

});

