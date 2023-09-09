import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:shop_app/constants.dart';

class Loading extends StatelessWidget {
  static String routeName = "/loading";
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Color.fromARGB(255, 223, 247, 255),
      child: Center(
        child: SpinKitChasingDots(
          color: kPrimaryColor,
          size: 50.0,
        ),
      ),
    );
  }
}
