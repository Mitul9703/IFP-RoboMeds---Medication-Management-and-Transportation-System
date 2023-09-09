import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:shop_app/models/Product.dart';

import '../../../constants.dart';
import '../../../size_config.dart';

class ProductDescription extends StatefulWidget {
  const ProductDescription({
    Key? key,
    required this.product,
    this.pressOnSeeMore,
  }) : super(key: key);

  final Product product;
  final GestureTapCallback? pressOnSeeMore;

  @override
  State<ProductDescription> createState() => _ProductDescriptionState();
}

class _ProductDescriptionState extends State<ProductDescription> {
  TimeOfDay? _mornTime;
  TimeOfDay? _afternoonTime;
  TimeOfDay? _nightTime;

  void _showTimePicker(
    TimeOfDay? initialTime,
    void Function(TimeOfDay) updateFunction,
  ) {
    showTimePicker(
      context: context,
      initialTime: initialTime ?? TimeOfDay.now(),
    ).then((value) {
      if (value != null) {
        setState(() {
          updateFunction(value);
          widget.product.mornTime = _mornTime;
          widget.product.afternoonTime = _afternoonTime;
          widget.product.nightTime = _nightTime;
        });
      }
    });
  }

  @override
  void initState() {
    super.initState();

    _mornTime = widget.product.mornTime;
    _afternoonTime = widget.product.afternoonTime;
    _nightTime = widget.product.nightTime;
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding:
              EdgeInsets.symmetric(horizontal: getProportionateScreenWidth(20)),
          child: Text(
            widget.product.title,
            style: Theme.of(context).textTheme.headline6,
          ),
        ),
        Padding(
          padding: EdgeInsets.only(
            left: getProportionateScreenWidth(20),
            right: getProportionateScreenWidth(64),
          ),
          child: Text(
            widget.product.description,
            maxLines: 3,
          ),
        ),
        Padding(
          padding: EdgeInsets.symmetric(
            horizontal: getProportionateScreenWidth(20),
            vertical: 10,
          ),
          child: GestureDetector(
            onTap: () {},
            child: Column(
              children: [
                Row(
                  children: [
                    Text(
                      "Morning Dose : ",
                      style: TextStyle(
                          fontWeight: FontWeight.w600, color: kPrimaryColor),
                    ),
                    TextButton(
                      onPressed: () => _showTimePicker(
                        _mornTime,
                        (value) => setState(() => _mornTime = value),
                      ),
                      child: Text(
                        _mornTime == null
                            ? "Pick Time"
                            : _mornTime!.format(context).toString(),
                        style: TextStyle(
                            fontWeight: FontWeight.w600, color: Colors.red),
                      ),
                      style: TextButton.styleFrom(
                          side: BorderSide(width: 0.3, color: Colors.red)),
                    )
                  ],
                ),
                Row(
                  children: [
                    Text(
                      "Afternoon Dose : ",
                      style: TextStyle(
                          fontWeight: FontWeight.w600, color: kPrimaryColor),
                    ),
                    TextButton(
                      onPressed: () => _showTimePicker(
                          _afternoonTime, (value) => _afternoonTime = value),
                      child: Text(
                        _afternoonTime == null
                            ? "Pick Time"
                            : _afternoonTime!.format(context).toString(),
                        style: TextStyle(
                            fontWeight: FontWeight.w600, color: Colors.red),
                      ),
                      style: TextButton.styleFrom(
                          side: BorderSide(width: 0.3, color: Colors.red)),
                    )
                  ],
                ),
                Row(
                  children: [
                    Text(
                      "Night Dose : ",
                      style: TextStyle(
                          fontWeight: FontWeight.w600, color: kPrimaryColor),
                    ),
                    TextButton(
                      onPressed: () => _showTimePicker(
                          _nightTime, (value) => _nightTime = value),
                      child: Text(
                        _nightTime == null
                            ? "Pick Time"
                            : _nightTime!.format(context).toString(),
                        style: TextStyle(
                            fontWeight: FontWeight.w600, color: Colors.red),
                      ),
                      style: TextButton.styleFrom(
                          side: BorderSide(width: 0.3, color: Colors.red)),
                    )
                  ],
                )
              ],
            ),
          ),
        )
      ],
    );
  }
}
