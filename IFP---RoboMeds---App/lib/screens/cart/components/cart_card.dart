import 'package:flutter/material.dart';
import 'package:shop_app/controller/cart_controller.dart';
import 'package:shop_app/models/Cart.dart';
import 'package:shop_app/models/Product.dart';

import '../../../constants.dart';
import '../../../size_config.dart';

class CartCard extends StatelessWidget {
  final CartController controller;
  final Product product;
  final int quantity;
  final int index;

  const CartCard({
    Key? key,
    required this.controller,
    required this.product,
    required this.quantity,
    required this.index,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        SizedBox(
          width: 88,
          child: AspectRatio(
            aspectRatio: 0.88,
            child: Container(
              padding: EdgeInsets.all(getProportionateScreenWidth(10)),
              decoration: BoxDecoration(
                color: Color(0xFFF5F6F9),
                borderRadius: BorderRadius.circular(15),
              ),
              child: Image.asset(product.images[0]),
            ),
          ),
        ),
        SizedBox(width: 20),
        Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              product.title,
              style: TextStyle(color: kPrimaryColor, fontSize: 20),
              maxLines: 2,
            ),
            // SizedBox(height: 10),
            // Text.rich(
            //   TextSpan(
            //     text: "\Rs.${product.price}",
            //     style: TextStyle(
            //         fontWeight: FontWeight.w600, color: kPrimaryColor),
            //     children: [
            //       TextSpan(
            //           text: " x${quantity}",
            //           style: Theme.of(context).textTheme.bodyText1),
            //     ],
            //   ),
            // ),
            TextButton(
              onPressed: () {
                controller.removeProduct(product);
              },
              child: Text(
                "Remove",
                style:
                    TextStyle(fontWeight: FontWeight.w100, color: Colors.red),
              ),
              style: TextButton.styleFrom(
                  side: BorderSide(width: 0.3, color: Colors.red)),
            )
          ],
        ),
      ],
    );
  }
}
