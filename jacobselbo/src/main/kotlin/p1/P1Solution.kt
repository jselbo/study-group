package p1

fun solution(num1: String, num2: String): String {
    var (largestNumCharArray, smallestNumCharArray) =
        if (num1.length >= num2.length)
            num1.toCharArray() to num2.toCharArray()
            else num2.toCharArray() to num1.toCharArray()
    var difference = largestNumCharArray.size - smallestNumCharArray.size

    fun handle(digitResult: Int, largestIndex: Int) {
        if (digitResult > 9) {
            if (largestIndex - 1 < 0) {
                largestNumCharArray[largestIndex] = Character.forDigit((digitResult % 10), 10)
                largestNumCharArray = charArrayOf('1') + largestNumCharArray

                difference += 1
            } else {
                largestNumCharArray[largestIndex] = Character.forDigit((digitResult % 10), 10)

                val newDigitResult = largestNumCharArray[largestIndex - 1].digitToInt() + 1

                handle(newDigitResult, largestIndex - 1)
            }
        } else {
            largestNumCharArray[largestIndex] = Character.forDigit(digitResult, 10)
        }
    }

    for (index in smallestNumCharArray.size - 1 downTo  0) {
        val digitResult =
            largestNumCharArray[index + difference].digitToInt() +
                    smallestNumCharArray[index].digitToInt()

        handle(digitResult, index + difference)
    }

    return largestNumCharArray.joinToString("")
}