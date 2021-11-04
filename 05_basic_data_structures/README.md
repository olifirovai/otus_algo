### Динамические массивы, неполный массив, очередь с приоритетом.

#### Цель:

Создание разных алгоритмов для реализации Динамического массива и сравнение их
производительности. Создание приоритетной очереди или неполного массива.

* 1 задание. Динамические массивы. +3 байта
    * Написать метод добавления и удаления элементов во все варианты
      динамических массивов: +
        * void add(T item, int index)
        * T remove(int index); // возвращает удаляемый элемент по индексу
    * Динамические массивы: +
        * SingleArray
        * VectorArray
        * FactorArray
        * MatrixArray


* 2 задание. Таблица сравнения производительности. +3 байта
    * Сравнить время выполнения разных операций для разных массивов с разным
      порядком значений. +
    * Сделать обёртку над ArrayList() и тоже сравнить.
    * Составить таблицу и приложить её скриншот. +
    * Сделать выводы и сформулировать их в нескольких предложениях.


* 3 задание. Приоритетная очередь (на выбор). Написать реализацию
  PriorityQueue. +4 байта
    * Варианты реализации:
        * список списков
        * массив списков
    * Методы к реализации:
        * enqueue(int priority, T item) - поместить элемент в очередь T
        * dequeue() - выбрать элемент из очереди


* 4 задание. Неполный массив (на выбор). Написать Реализацию класса SpaceArray
  массив массивов с неполным заполнением. Делать на основе одного из уже
  созданных массивов и/или списков. +4 байта дополнительно.

### Таблица сравнения производительности

|Class|Count|Function|Time ms|
|---|---|---|---|
|Single Array|10|Put at the end|0.0|
|Vector Array|10|Put at the end|0.0|
|Factor Array|10|Put at the end|0.0|
|Matrix Array|10|Put at the end|0.0|
|------------|-------------|------------|-------------|
|Single Array|10|Put at the middle index|0.0|
|Vector Array|10|Put at the middle index|0.0|
|Factor Array|10|Put at the middle index|0.0|
|Matrix Array|10|Put at the middle index|0.0|
|------------|-------------|------------|-------------|
|Single Array|10|Put at the 0 index|0.0|
|Vector Array|10|Put at the 0 index|0.0|
|Factor Array|10|Put at the 0 index|0.0|
|Matrix Array|10|Put at the 0 index|0.0|
|------------|-------------|------------|-------------|
|Single Array|10|Delete end index|0.0|
|Vector Array|10|Delete end index|0.0|
|Factor Array|10|Delete end index|0.0|
|Matrix Array|10|Delete end index|0.0|
|------------|-------------|------------|-------------|
|Single Array|10|Delete middle index|0.0|
|Vector Array|10|Delete middle index|0.0|
|Factor Array|10|Delete middle index|0.0|
|Matrix Array|10|Delete middle index|0.0|
|------------|-------------|------------|-------------|
|Single Array|10|Delete 0 index|0.0|
|Vector Array|10|Delete 0 index|0.0|
|Factor Array|10|Delete 0 index|0.0|
|Matrix Array|10|Delete 0 index|0.0|
|------------|-------------|------------|-------------|
|Single Array|100|Put at the end|0.0|
|Vector Array|100|Put at the end|0.0|
|Factor Array|100|Put at the end|0.0|
|Matrix Array|100|Put at the end|0.0|
|------------|-------------|------------|-------------|
|Single Array|100|Put at the middle index|0.0|
|Vector Array|100|Put at the middle index|0.0|
|Factor Array|100|Put at the middle index|0.0|
|Matrix Array|100|Put at the middle index|0.0|
|------------|-------------|------------|-------------|
|Single Array|100|Put at the 0 index|0.0|
|Vector Array|100|Put at the 0 index|0.0|
|Factor Array|100|Put at the 0 index|0.0|
|Matrix Array|100|Put at the 0 index|0.0|
|------------|-------------|------------|-------------|
|Single Array|100|Delete end index|0.0|
|Vector Array|100|Delete end index|0.0|
|Factor Array|100|Delete end index|0.0|
|Matrix Array|100|Delete end index|0.0|
|------------|-------------|------------|-------------|
|Single Array|100|Delete middle index|0.0|
|Vector Array|100|Delete middle index|0.0|
|Factor Array|100|Delete middle index|0.0|
|Matrix Array|100|Delete middle index|0.0|
|------------|-------------|------------|-------------|
|Single Array|100|Delete 0 index|0.0|
|Vector Array|100|Delete 0 index|0.0|
|Factor Array|100|Delete 0 index|0.0|
|Matrix Array|100|Delete 0 index|0.0|
|------------|-------------|------------|-------------|
|Single Array|1000|Put at the end|21.692|
|Vector Array|1000|Put at the end|0.0|
|Factor Array|1000|Put at the end|0.0|
|Matrix Array|1000|Put at the end|0.0|
|------------|-------------|------------|-------------|
|Single Array|1000|Put at the middle index|31.213|
|Vector Array|1000|Put at the middle index|0.0|
|Factor Array|1000|Put at the middle index|15.625|
|Matrix Array|1000|Put at the middle index|227.495|
|------------|-------------|------------|-------------|
|Single Array|1000|Put at the 0 index|15.739|
|Vector Array|1000|Put at the 0 index|0.0|
|Factor Array|1000|Put at the 0 index|0.0|
|Matrix Array|1000|Put at the 0 index|459.437|
|------------|-------------|------------|-------------|
|Single Array|1000|Delete end index|0.0|
|Vector Array|1000|Delete end index|0.0|
|Factor Array|1000|Delete end index|0.0|
|Matrix Array|1000|Delete end index|0.0|
|------------|-------------|------------|-------------|
|Single Array|1000|Delete middle index|0.0|
|Vector Array|1000|Delete middle index|0.0|
|Factor Array|1000|Delete middle index|0.0|
|Matrix Array|1000|Delete middle index|113.95|
|------------|-------------|------------|-------------|
|Single Array|1000|Delete 0 index|0.0|
|Vector Array|1000|Delete 0 index|15.62|
|Factor Array|1000|Delete 0 index|0.0|
|Matrix Array|1000|Delete 0 index|227.496|
|------------|-------------|------------|-------------|
|Single Array|10000|Put at the end|1768.938|
|Vector Array|10000|Put at the end|175.692|
|Factor Array|10000|Put at the end|0.0|
|Matrix Array|10000|Put at the end|8.191|
|------------|-------------|------------|-------------|
|Single Array|10000|Put at the middle index|2028.081|
|Vector Array|10000|Put at the middle index|445.006|
|Factor Array|10000|Put at the middle index|310.333|
|Matrix Array|10000|Put at the middle index|22272.349|
|------------|-------------|------------|-------------|
|Single Array|10000|Put at the 0 index|1964.701|
|Vector Array|10000|Put at the 0 index|454.908|
|Factor Array|10000|Put at the 0 index|281.22|
|Matrix Array|10000|Put at the 0 index|44154.347|
|------------|-------------|------------|-------------|
|Single Array|10000|Delete end index|82.444|
|Vector Array|10000|Delete end index|0.0|
|Factor Array|10000|Delete end index|0.0|
|Matrix Array|10000|Delete end index|10.098|
|------------|-------------|------------|-------------|
|Single Array|10000|Delete middle index|165.687|
|Vector Array|10000|Delete middle index|198.513|
|Factor Array|10000|Delete middle index|372.147|
|Matrix Array|10000|Delete middle index|11158.341|
|------------|-------------|------------|-------------|
|Single Array|10000|Delete 0 index|165.551|
|Vector Array|10000|Delete 0 index|277.106|
|Factor Array|10000|Delete 0 index|372.38|
|Matrix Array|10000|Delete 0 index|23372.383|
|------------|-------------|------------|-------------|