fun llegirOperacio(): String {
	println("Quina operació vols fer? ( '+', '-', '*', '/': )")
	return readLine()!!.toString()
}

fun llegirEnter(): Int {
	println("Introdueix un enter:")
	return readLine()!!.toInt()
}

fun sumar(a: Int, b: Int): Int {
	return a + b
}

fun restar(a: Int, b: Int): Int {
	return a - b
}

fun multiplicar(a: Int, b: Int): Int {
	return a * b
}

fun dividir(a: Int, b: Int): Int {
	if (b == 0) {
		println("No es pot dividir entre zero")
		return 0
	}
	return a / b
}

fun operar(operacio: String, a: Int, b: Int): Int {
	return when (operacio) {
		"+" -> sumar(a, b)
		"-" -> restar(a, b)
		"*" -> multiplicar(a, b)
		"/" -> dividir(a, b)
		else -> {
			println("Operació no vàlida")
			0
		}
	}
}

fun main() {
	// Llegim l'operació
	val operacio: String = llegirOperacio()

	// Llegim el primer operant
	val a: Int = llegirEnter()

	// Llegim el segon operant
	val b: Int = llegirEnter()

	// Operem
	val resultat: Int = operar(operacio, a, b)

	// Mostrem el resultat
	println("Resultat: $resultat")
}