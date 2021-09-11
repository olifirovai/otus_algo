2 байта Реализовать алгоритм BubbleSort, SelectionSort или InsertionSort (два
на выбор). 3 байта Реализовать алгоритм ShellSort с тремя вариантами выбора
шагов. 3 байта Реализовать алгоритм HeapSort. 2 байта Простестировать
алгоритмы, заполнить таблицу по результатам измерений, написать свой вывод
сравнения, какой алгоритм лучше.

Файл с тестами приложен к заданию (563 мегабайта). На первой строчке указан
размер массива, на второй строчке через пробел перечислены элементы массива. В
файл результата записать числа из отсортированный массив в одну строчку через
пробел.

Тестировать алгоритмы следует на массивах таких размеров: 1, 10, 100, 1.000,
10.000, 100.000, 1.000.000, 10.000.000 (этот по желанию)

И с различным характером данных: а) random - массив их случайных чисел б)
digits - массив из случайных цифр в) sorted - на 99% отсортированный массив г)
revers - обратно-отсортированный массив

|Test Type|Test №|Bubble sort|Insertion sort|Selection sort|Shell sort|Heap sort|
|---|---|---|---|---|---|---|
|random|0|0.0 ms|4.0 ms|0.9990000000000001 ms|time ms|0.0 ms|
|random|1|0.0 ms|7.998999999999999 ms|5.999 ms|time ms|0.0 ms|
|random|2|1.0 ms|13.001000000000001 ms|7.001 ms|time ms|0.0 ms|
|random|3|91.0 ms|206.0 ms|142.999 ms|time ms|0.0 ms|
|random|4|8912.993 ms|18181.684 ms|12461.966999999999 ms|time ms|93.719 ms|
|random|5|888212.853 ms|1781425.668 ms|1222537.002 ms|time ms|1093.753 ms|
|random|6|time ms|time ms|time ms|time ms|13250.002999999999 ms|
|random|7|time ms|time ms|time ms|time ms|1236175.222 ms|
|digits|0|0.969 ms|6.968 ms|1.9689999999999999 ms|time ms|31.249 ms|
|digits|1|0.0 ms|6.0 ms|4.0 ms|time ms|46.903 ms|
|digits|2|1.0 ms|11.68 ms|6.0 ms|time ms|0.0 ms|
|digits|3|83.009 ms|213.49 ms|151.49099999999999 ms|time ms|0.0 ms|
|digits|4|8174.035999999999 ms|16490.221999999998 ms|11486.537999999999 ms|time ms|62.53 ms|
|digits|5|839262.777 ms|1686142.1709999999 ms|1181925.006 ms|time ms|1374.997 ms|
|digits|6|time ms|time ms|time ms|time ms|10890.591 ms|
|digits|7|time ms|time ms|time ms|time ms|189997.42 ms|
|sorted|0|0.9990000000000001 ms|44.984 ms|16.968 ms|time ms|15.596 ms|
|sorted|1|0.0 ms|21.114 ms|20.115000000000002 ms|time ms|0.0 ms|
|sorted|2|1.003 ms|30.071 ms|25.070999999999998 ms|time ms|0.0 ms|
|sorted|3|47.008 ms|97.025 ms|88.041 ms|time ms|0.0 ms|
|sorted|4|4906.237 ms|8379.871 ms|8192.371 ms|time ms|93.751 ms|
|sorted|5|506538.415 ms|time ms|time ms|time ms|1250.031 ms|
|sorted|6|time ms|time ms|time ms|time ms|12157.529 ms|
|sorted|7|time ms|time ms|time ms|time ms|344565.45999999996 ms|
|revers|0|1.001 ms|33.986000000000004 ms|1.97 ms|time ms|31.253000000000004 ms|
|revers|1|1.014 ms|28.597 ms|22.598 ms|time ms|15.626999999999999 ms|
|revers|2|1.001 ms|38.732 ms|31.735 ms|time ms|0.0 ms|
|revers|3|117.826 ms|280.826 ms|166.826 ms|time ms|0.0 ms|
|revers|4|12369.799 ms|26730.433 ms|15869.799 ms|time ms|78.091 ms|
|revers|5|time ms|2971043.726 ms|1738660.471 ms|time ms|1640.624 ms|
|revers|6|time ms|time ms|time ms|time ms|11579.357 ms|
|revers|7|time ms|time ms|time ms|time ms|337787.674 ms|