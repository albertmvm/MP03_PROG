fun demanaOperacio(): String {
    println("¿Quina operació vols fer? '+', '-', '*', '/':")
    val operacio = readLine()?.takeIf { it in "+-*/" }
    if (operacio == null) {
        println("Operació no vàlida.")
        return ""
    }
    return operacio
}

fun demanaNumero(missatge: String): Int {
    print(missatge)
    val numero = readLine()?.toIntOrNull()
    if (numero == null) {
        println("Entrada no vàlida.")
        return 0
    }
    return numero
}

fun sumar(a: Int, b: Int) = a + b
fun resta(a: Int, b: Int) = a - b
fun multiplicar(a: Int, b: Int) = a * b
fun dividir(a: Int, b: Int): Int {
    if (b == 0) {
        println("No es pot dividir entre zero!!!")
        return 0
    }
    return a / b
}

fun main() {
    val operacio = demanaOperacio()
    if (operacio.isEmpty()) return

    val primerNumero = demanaNumero("Introduce el primer número: ")
    val segundoNumero = demanaNumero("Introduce el segundo número: ")

    val resultat = when (operacio) {
        "+" -> sumar(primerNumero, segundoNumero)
        "-" -> resta(primerNumero, segundoNumero)
        "*" -> multiplicar(primerNumero, segundoNumero)
        "/" -> dividir(primerNumero, segundoNumero)
        else -> {
            println("<<<< ERROR. >>>>")
            return
        }
    }

    println("El resultat es: $resultat")
}
