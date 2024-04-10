class Coordenada(val x: Int, val y: Int)

fun moureDreta(coordenada: Coordenada): Coordenada {
    return Coordenada(coordenada.x + 1, coordenada.y)
}
fun moureEsquerra(coordenada: Coordenada): Coordenada {
    return Coordenada(coordenada.x - 1, coordenada.y)
}
fun moureAmunt(coordenada: Coordenada): Coordenada {
    return Coordenada(coordenada.x, coordenada.y + 1)
}
fun moureAvall(coordenada: Coordenada): Coordenada {
    return Coordenada(coordenada.x, coordenada.y - 1)
}

fun main() {
    // Coordenada inicial
    val coordenada = Coordenada(0, 0)

    // Executar moviments
    coordenada = moureDreta(coordenada)
    println("Nova coordenada després de moure a la dreta: $coordenada")

    coordenada = moureAmunt(coordenada)
    println("Nova coordenada després de moure a dalt: $coordenada")
}