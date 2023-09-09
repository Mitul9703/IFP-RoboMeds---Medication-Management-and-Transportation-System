import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:get/get.dart';
import 'package:provider/provider.dart';
import 'package:shop_app/models/Product.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:shop_app/screens/cart/cart_screen.dart';
import 'package:flutter/material.dart';

class CartController extends GetxController {
  List mylist = [];

  final _db = FirebaseFirestore.instance;
  var _products = {}.obs;

  void addProduct(Product product) {
    if (_products.containsKey(product)) {
      Get.snackbar('${product.title} can\'t be added', 'Item already in Queue',
          snackPosition: SnackPosition.BOTTOM,
          duration: Duration(milliseconds: 800));
    } else {
      _products[product] = 1;
      Get.snackbar(
        '${product.title} Added',
        'You have added the ${product.title} to the Queue',
        snackPosition: SnackPosition.BOTTOM,
        duration: Duration(milliseconds: 800),
      );
    }
  }

  void removeProduct(Product product) {
    if (_products.containsKey(product) && _products[product] == 1) {
      _products.removeWhere((key, value) => key == product);
    } else {
      _products[product] -= 1;
    }
  }

  Future<void> createCart() async {
    Map<String, Map<String, String?>> productsMap = {};

    for (var k in _products.keys) {
      productsMap[k.title] = {
        'MorningTime': k.mornTime.toString(),
        'AfternoonTime': k.afternoonTime.toString(),
        'NightTime': k.nightTime.toString(),
      };
    }

    await _db.collection('products').doc('${DateTime.now()}').set({
      'Products': productsMap,
    }).whenComplete(
      () => Get.snackbar('Success', 'Activated Queue',
          snackPosition: SnackPosition.BOTTOM,
          duration: Duration(milliseconds: 1000)),
    );

    // await _db.collection('products').add(productModel.toJson()).whenComplete(
    //     () => Get.snackbar('Success', 'Added',
    //         snackPosition: SnackPosition.BOTTOM,
    //         duration: Duration(seconds: 1)));
  }
  // getPM() {
  //   List myList = [];
  //   var ProductWithTime;

  //   for (var k in _products.keys) {
  //     // ProductWithTime = {
  //     //   "Product": k.title,
  //     //   "MorningTime": k.mornTime,
  //     //   "AfternoonTime": k.afternoonTime,
  //     //   "NightTime": k.nightTime
  //     // };
  //     // mylist.add(ProductWithTime);
  //     myList.add(k.title);
  //   }
  //   // return ProductModel(listofproducts: myList);
  // }

  get products => _products;

  get productSubtotal => _products.entries
      .map((product) => product.key.price * product.value)
      .toList();

  getTotalPrice() {
    num total = 0;

    for (var k in productSubtotal) {
      total += k;
    }
    return total;
  }

  // int total() {
  //   mylist = _products.entries
  //       .map((product) => product.key.price * product.value)
  //       .toList();
  //   final result = mylist.reduce((sum, element) => sum = element);
  //   return result;
  // }

  // get total => _products.entries
  //     .map((product) => product.key.price * product.value)
  //     .toList()
  //     .reduce((value, element) => value + element)
  //     .toString();
}

// class ProductModel {
//   final List listofproducts;

//   const ProductModel({required this.listofproducts});

//   toJson() {
//     return {'Products': listofproducts};
//   }
// }

class ProductModel {
  final String product;
  final String? morningTime;
  final String? afternoonTime;
  final String? nightTime;

  ProductModel({
    required this.product,
    this.morningTime,
    this.afternoonTime,
    this.nightTime,
  });

  Map<String, dynamic> toJson() {
    return {
      'product': product,
      'morningTime': morningTime,
      'afternoonTime': afternoonTime,
      'nightTime': nightTime,
    };
  }
}
