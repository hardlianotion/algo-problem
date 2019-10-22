To run unit tests, use

```
python ./test_baked_goods.py
```

Solution code is in `baked_goods.py`.

Implementation remarks:

 - Outcomes from faulty inputs (seller schedules with
   unordered, repeated date inputs and the like) are _undefined_.
 - `total_days` is not assumed to be greater than all dates in `sellers`.
