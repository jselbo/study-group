import java.io.File

fun isDigit(char: Char) = char in '0'..'9'

fun p2(args: Array<String>) {
    val file = args[0]
    var sum = 0
    for (line in File(file).readLines()) {
        val chars = line.toCharArray()

        val firstDigit = chars.first(::isDigit)
        val lastDigit = chars.last(::isDigit)
        sum += (firstDigit.toString() + lastDigit).toInt()
    }
    println(sum)
}