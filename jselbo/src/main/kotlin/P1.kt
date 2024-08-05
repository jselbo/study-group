fun p1(args: Array<String>) {
    val n1 = args[0]
    val n2 = args[1]

    val resultDigits = mutableListOf<Int>()
    var n1Counter = n1.length - 1
    var n2Counter = n2.length - 1
    var carry = 0
    while (n1Counter >= 0 || n2Counter >= 0) {
        val n1Digit = if (n1Counter >= 0) n1[n1Counter].digitToInt() else 0
        val n2Digit = if (n2Counter >= 0) n2[n2Counter].digitToInt() else 0

        var digitSum = n1Digit + n2Digit + carry
        if (digitSum >= 10) {
            digitSum -= 10
            carry = 1
        } else {
            carry = 0
        }
        resultDigits.add(digitSum)
        n1Counter--
        n2Counter--
    }
    println(resultDigits.reversed().joinToString(""))
}
