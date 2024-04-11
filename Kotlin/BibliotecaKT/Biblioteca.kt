class Llibre(val titol: String, val autor: String, var exemplarsDisponibles: Int) {
    fun obtenirInformacio(): String {
        return "Títol: $titol, Autor: $autor, Exemplars disponibles: $exemplarsDisponibles"
    }
}

class Soci(val nom: String, val cognom: String, val numeroSoci: Int) {
    fun sollicitarPrestec(llibre: Llibre): Boolean {
        if (llibre.exemplarsDisponibles > 0) {
            llibre.exemplarsDisponibles--
            println("$nom $cognom ha sol·licitat un préstec de $titol")
            return true
        } else {
            println("$titol no està disponible en aquest moment")
            return false
        }
    }

    fun retornarPrestec(llibre: Llibre) {
        llibre.exemplarsDisponibles++
        println("$nom $cognom ha retornat $titol")
    }

    fun mostrarInformacio(): String {
        return "Nom: $nom, Cognom: $cognom, Número de soci: $numeroSoci"
    }
}

class Prestec(val llibre: Llibre, val soci: Soci, val dataPrestec: LocalDate)

fun main() {
    val llibre1 = Llibre("Wonder", "Raquel Palacio", 200)
    val llibre2 = Llibre("El Principe de la Niebla", "Carlos Ruiz Zafón", 155)

    val soci1 = Soci("Albert", "Martinez", 122)
    val soci2 = Soci("Eric", "Rodriguez", 300)

    soci1.sollicitarPrestec(llibre1)
    soci2.sollicitarPrestec(llibre2)

    println(llibre1.obtenirInformacio())
    println(soci1.mostrarInformacio())

    soci1.retornarPrestec(llibre1)

    println(llibre1.obtenirInformacio())
    println(soci1.mostrarInformacio())
}