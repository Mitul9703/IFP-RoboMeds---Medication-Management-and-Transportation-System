import 'package:flutter/material.dart';

class Product {
  final int id;
  final String title, description;
  final List<String> images;
  final double rating, price;
  final bool isFavourite, isPopular;
  TimeOfDay? mornTime;
  TimeOfDay? afternoonTime;
  TimeOfDay? nightTime;

  Product({
    required this.id,
    required this.images,
    this.rating = 0.0,
    this.isFavourite = false,
    this.isPopular = false,
    required this.title,
    required this.price,
    required this.description,
    this.mornTime,
    this.afternoonTime,
    this.nightTime,
  });
}

// Our demo Products

List<Product> demoProducts = [
  Product(
    id: 1,
    images: ["assets/images/Dolo.png"],
    title: "Dolo 650",
    price: 10,
    description:
        "Dolo 650 Tablet is used in the treatment of Pain relief,Fever.",
    rating: 4.8,
    isFavourite: false,
    isPopular: true,
  ),
  Product(
    id: 2,
    images: [
      "assets/images/Mox.jpg",
    ],
    title: "Mox 500",
    price: 10,
    description:
        'Mox 500mg Capsule is used in the treatment of Bacterial infections.',
    rating: 4.1,
    isPopular: true,
  ),
  Product(
    id: 3,
    images: [
      "assets/images/Gelusil.jpg",
    ],
    title: "Gelusil",
    price: 10,
    description:
        'This medication is used to treat the symptoms of too much stomach acid such as stomach upset, heartburn, and acid indigestion.',
    rating: 4.1,
    isFavourite: false,
    isPopular: true,
  ),
];
