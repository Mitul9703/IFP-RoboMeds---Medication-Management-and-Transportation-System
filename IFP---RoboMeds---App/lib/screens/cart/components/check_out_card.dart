import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:shop_app/components/default_button.dart';
import 'package:shop_app/controller/cart_controller.dart';
import 'package:get/get.dart';
import 'package:shop_app/screens/loading/loadingscreen.dart';
import '../../../constants.dart';
import 'package:shop_app/screens/cart/cart_screen.dart';
import '../../../size_config.dart';

class CheckoutCard extends StatefulWidget {
  CheckoutCard({
    Key? key,
  }) : super(key: key);

  @override
  State<CheckoutCard> createState() => _CheckoutCardState();
}

class _CheckoutCardState extends State<CheckoutCard> {
  bool loading = false;

  final CartController controller = Get.put(CartController());

  @override
  Widget build(BuildContext context) {
    return Obx(
      () => Container(
        padding: EdgeInsets.symmetric(
          vertical: getProportionateScreenWidth(15),
          horizontal: getProportionateScreenWidth(30),
        ),
        // height: 174,
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.only(
            topLeft: Radius.circular(30),
            topRight: Radius.circular(30),
          ),
          boxShadow: [
            BoxShadow(
              offset: Offset(0, -15),
              blurRadius: 20,
              color: Color(0xFFDADADA).withOpacity(0.15),
            )
          ],
        ),
        child: SafeArea(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Spacer(),
                ],
              ),
              SizedBox(height: getProportionateScreenHeight(20)),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text.rich(
                    TextSpan(
                      text: "",
                      children: [
                        TextSpan(
                          text: "${controller.getTotalPrice()}",
                          style: TextStyle(fontSize: 1, color: Colors.black),
                        ),
                      ],
                    ),
                  ),
                  SizedBox(
                    width: getProportionateScreenWidth(310),
                    child: DefaultButton(
                      text: "Get Items",
                      press: () async {
                        if (controller.products.length == 0) {
                          Get.snackbar('Failed to Add', 'No items in Queue',
                              snackPosition: SnackPosition.BOTTOM,
                              duration: Duration(milliseconds: 2000));
                        } else {
                          // setState(() => loading = true);
                          Navigator.push(
                              context,
                              MaterialPageRoute(
                                  builder: (context) => Loading()));
                          await controller.createCart();
                          Navigator.pop(context);
                          // setState(() => loading = false);
                        }
                      },
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
