* Реализовать алгоритм BubbleSort, SelectionSort или InsertionSort (два на выбор) - 2 байта +
* Реализовать алгоритм ShellSort с тремя вариантами выбора шагов - 3 байта
* Реализовать алгоритм HeapSort - 3 байта +
* Простестировать алгоритмы, заполнить таблицу по результатам измерений, написать свой вывод сравнения, какой алгоритм
  лучше - 2 байта +-

Тестовые данные. На первой строчке указан размер массива, на второй строчке через пробел перечислены элементы массива. В
файл результата записать числа из отсортированный массив в одну строчку через пробел.

Тестировать алгоритмы следует на массивах таких размеров: 1, 10, 100, 1.000, 10.000, 100.000, 1.000.000, 10.000.000 - 
!два последних выполнены только для HeapSort!

И с различным характером данных: а) random - массив их случайных чисел б)
digits - массив из случайных цифр в) sorted - на 99% отсортированный массив г)
revers - обратно-отсортированный массив

### Test Results

|Test Type|Length Array|Test №|Bubble sort|Insertion sort|Selection sort|Shell sort|Heap sort|
|---|---|---|---|---|---|---|---|
|random|1|0|0.0 ms|0.0 ms|0.0 ms|Too much ms|0.0 ms|
|random|10|1|0.0 ms|0.0 ms|0.0 ms|Too much ms|0.0 ms|
|random|100|2|0.0 ms|0.0 ms|0.0 ms|Too much ms|1.002 ms|
|random|1000|3|62.504000000000005 ms|15.626000000000001 ms|31.252000000000002 ms|Too much ms|4.005 ms|
|random|10000|4|5759.469 ms|1977.404 ms|3656.526 ms|Too much ms|51.047000000000004 ms|
|random|100000|5|659351.154 ms|225749.298 ms|361863.082 ms|Too much ms|646.586 ms|
|random|1000000|6|Too much ms|Too much ms|Too much ms|Too much ms|8436.090999999999 ms|
|random|10000000|7|Too much ms|Too much ms|Too much ms|Too much ms|112639.58 ms|
|digits|1|0|15.625 ms|2.003 ms|0.0 ms|Too much ms|159.144 ms|
|digits|10|1|0.0 ms|2.002 ms|0.0 ms|Too much ms|409.373 ms|
|digits|100|2|0.998 ms|0.0 ms|0.0 ms|Too much ms|0.0 ms|
|digits|1000|3|47.324999999999996 ms|21.019 ms|31.253000000000004 ms|Too much ms|3.003 ms|
|digits|10000|4|5470.570000000001 ms|2017.058 ms|3215.324 ms|Too much ms|45.04 ms|
|digits|100000|5|546719.6579999999 ms|198308.693 ms|319523.343 ms|Too much ms|564.513 ms|
|digits|1000000|6|Too much ms|Too much ms|Too much ms|Too much ms|6690.089 ms|
|digits|10000000|7|Too much ms|Too much ms|Too much ms|Too much ms|77532.804 ms|
|sorted|1|0|0.0 ms|15.626000000000001 ms|15.626000000000001 ms|Too much ms|46.883 ms|
|sorted|10|1|0.0 ms|0.0 ms|0.0 ms|Too much ms|15.625 ms|
|sorted|100|2|0.0 ms|0.0 ms|0.0 ms|Too much ms|0.0 ms|
|sorted|1000|3|31.25 ms|15.626999999999999 ms|0.0 ms|Too much ms|0.0 ms|
|sorted|10000|4|2859.6 ms|1953.2730000000001 ms|109.38199999999999 ms|Too much ms|62.504000000000005 ms|
|sorted|100000|5|366402.2 ms|240924.299 ms|9578.859 ms|Too much ms|671.924 ms|
|sorted|1000000|6|Too much ms|Too much ms|Too much ms|Too much ms|7795.373 ms|
|sorted|10000000|7|Too much ms|Too much ms|Too much ms|Too much ms|90565.804 ms|
|revers|1|0|15.625 ms|0.0 ms|0.0 ms|Too much ms|125.01 ms|
|revers|10|1|0.0 ms|0.0 ms|0.0 ms|Too much ms|109.38199999999999 ms|
|revers|100|2|15.623 ms|0.0 ms|0.0 ms|Too much ms|0.0 ms|
|revers|1000|3|62.504000000000005 ms|31.253999999999998 ms|62.503 ms|Too much ms|0.0 ms|
|revers|10000|4|8424.954 ms|2078.2799999999997 ms|7122.919 ms|Too much ms|46.876 ms|
|revers|100000|5|939963.603 ms|246296.212 ms|717374.9269999999 ms|Too much ms|609.4209999999999 ms|
|revers|1000000|6|Too much ms|Too much ms|Too much ms|Too much ms|7328.677 ms|
|revers|10000000|7|Too much ms|Too much ms|Too much ms|Too much ms|86094.814 ms|