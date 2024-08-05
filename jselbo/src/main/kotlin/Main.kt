typealias Solver = (Array<String>) -> Unit

fun main(args: Array<String>) {
    val fn: Solver = when (val problemNum = args[0].toInt()) {
        1 -> ::p1
        else -> throw RuntimeException("Unhandled problem: $problemNum")
    }
    val remainingArgs = args.drop(1).toTypedArray()
    fn(remainingArgs)
}
