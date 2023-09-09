import 'package:flutter/material.dart';
import 'package:shop_app/screens/cart/cart_screen.dart';
import 'package:get/get.dart';
import 'package:shop_app/controller/cart_controller.dart';
import '../../../size_config.dart';
import 'icon_btn_with_counter.dart';
import 'search_field.dart';

class HomeHeader extends StatelessWidget {
  final CartController controller = Get.put(CartController());
  HomeHeader({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Obx(
      () => Padding(
        padding:
            EdgeInsets.symmetric(horizontal: getProportionateScreenWidth(20)),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            SearchField(),
            IconBtnWithCounter(
              svgSrc: "assets/icons/pill_icon.svg",
              numOfitem: controller.products.length,
              press: () => Navigator.pushNamed(context, CartScreen.routeName),
            ),
          ],
        ),
      ),
    );
  }
}
