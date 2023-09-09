import 'package:flutter/material.dart';
import 'package:shop_app/controller/cart_controller.dart';
import 'package:get/get.dart';
import 'components/body.dart';
import 'components/check_out_card.dart';

class CartScreen extends StatelessWidget {
  final CartController controller = Get.put(CartController());

  static String routeName = "/cart";
  @override
  Widget build(BuildContext context) {
    return Obx(
      () => Scaffold(
        appBar: buildAppBar(context),
        body: Body(),
        bottomNavigationBar: CheckoutCard(),
      ),
    );
  }

  AppBar buildAppBar(BuildContext context) {
    return AppBar(
      title: Column(
        children: [
          Text(
            "Your Queue",
            style: TextStyle(color: Colors.black),
          ),
          Text(
            "${controller.products.length} items",
            style: Theme.of(context).textTheme.caption,
          ),
        ],
      ),
    );
  }
}
