## Домашнее задание 3 (дедлайн 28.09 14:40)

1. (3 балла) Проверьте следующие языки на регулярность, за каждое 1 балл. Либо докажите их нерегулярность, либо регулярность.

    * ![equation](https://latex.codecogs.com/gif.latex?%5C%7Buabv%20%7C%20u%20%5Cin%20%5C%7Ba%2C%20b%5C%7D*%2C%20v%20%5Cin%20%5C%7Ba%2C%20b%5C%7D*%2C%20%7Cu%7C%20%3D%20%7Cv%7C%2C%20u%20%5Cneq%20v%5ER%5C%7D)
    
    Данное выражение не является регулярным. Проверим для него отрицание леммы о накачке, рассмотрим слово ```w=aa...abb...b``` -- в нём n букв ```a``` и n букв ```b```. Чтобы наше слово не лежало в языке надо найти такое k, что ```ac^kb``` не принадлежит этому языку. При k=0, если у нас |y|=l, то получаем слово ```aa...abb...b```-- в нём n-l букв ```a``` и n букв ```b```, а оно нашему языку не принадлежит (не подошло под условие длины).

    * ![equation](https://latex.codecogs.com/gif.latex?%5C%7Ba%5Ekc%5Eme%5En%20%7C%20k%20%5Cge%200%2C%20n%20%5Cge%200%2C%20m%20%3D%20k%20&plus;%20n%20&plus;%201%5C%7D)
    
    Данное выражение не является регулярным. Проверим для него отрицание леммы о накачке, рассмотрим слово ```w=aa...abb...bee...e``` -- в нём n букв ```a``` и n букв ```e```, ```b``` -- 2n+1. Если у нас |y|=l,а k=0, то получаем слово ```aa...abb...bee...e```-- в нём n-l букв ```a```, n букв ```e``` и 2n+1 букв ```b```, а оно нашему языку не принадлежит.

    * ![equation](https://latex.codecogs.com/gif.latex?%5C%7Ba%5En%20%7C%20%5Cexists%20p%20%5Cge%20n%3A%20p%7E%5Ctexttt%7Bprime%7D%7E%5Ctexttt%7Band%7D%7Ep%20&plus;%202%7E%5Ctexttt%7Bprime%7D%5D%5C%7D)
    
    В независимости от того, сколько простых чисел близнецов, мы всегда можем построить регулярное выражение (если их бесконечно a*, иначе мы можем перечислить все такие слова, что их длина не больше p, где p--"первый из двух максимальных братьев близнецов". Значит язык регулярный.

3. (5 баллов) Реализуйте на любом языке программирования (кроме Хаскелля) парсинг с помощью производных. Сами регулярки парсить из строки не нужно, просто объявите в коде несколько (не меньше 5) регулярок и тестите с их помощью. Программе на вход подаётся строка, на выход true/false &mdash; подходит ли эта строка под захардкоженную регулярку.

    За саму реализацию того же, что было на паре (и прикреплено в файле) даётся максимум 2 балла. Тесты обязательны, без них решение вообще не будет оцениваться. Дальше своё решение нужно дополнять:

    * (+1 балл) Оптимизируйте алгоритм:

        * `nullable` мы на доске определяли как функцию из регулярки в регулярку. Это удобно в теории, чтобы написать правило для `derivative a (Concat s t)`, но на практике лучше, чтобы `nullable` возвращал true/false, принимает ли данная регулярка пустую строку.

        * Основная проблема в производительности, как было сказано на паре &mdash; разрастание регулярок. Предлагается каждый раз, когда мы строим регулярку, проверять, можем ли мы обойтись более простой регуляркой. Для этого воспользуемся следующими равенствами:

            ```
            ØR = Ø
            RØ = Ø
            εR = R
            Rε = R
            Ø|R = R
            R|Ø = R
            R|ε = R if nullable(R)
            ε|R = R if nullable(R)
            R|Q = R if R = Q
            Ø* = Ø
            ε* = ε
            R** = R*
            ```


        * Если вы придумаете свою оптимизацию, опишете её в отчёте и докажете, что стало работать быстрее, за это возможны допбаллы.

    * (+1 балл) Замерьте на тестах время работы до оптимизаций и после. Сделайте выводы, стало ли лучше. Включите всё это в отчёт.

    * (+1 балл) Найдите несколько входных данных (регулярка и строка) адекватного размера, на котором даже после оптимизаций ваше решение работает больше 2 секунд. Приведите эти данные в отчёте. Исследуйте причины медленной работы (на конкретных тестах), изложите эти причины в отчёте.
