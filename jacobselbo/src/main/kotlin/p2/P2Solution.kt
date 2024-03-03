package p2

import java.io.File
import java.io.FileNotFoundException

fun solution(filePath: String): Int {
    val file = File(filePath)

    if (!file.exists()) { throw FileNotFoundException() }

    var sum = 0

    file.forEachLine { line ->
        val charArray = line.toCharArray()
        var passkey = 0

        // Find first number
        for (char: Char in charArray) {
            if (char.isDigit()) {
                passkey = char.digitToInt() * 10
                break
            }
        }

        // Find last number
        for (i in charArray.size - 1 downTo 0) {
            val char = charArray[i]

            if (char.isDigit()) {
                passkey += char.digitToInt()
                break
            }
        }

        sum += passkey
    }

    return sum
}