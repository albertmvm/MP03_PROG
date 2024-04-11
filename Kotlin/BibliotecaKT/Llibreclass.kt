package Biblio

class Llibre(val titol: String, val autor: String, var exemplarsDisponibles: Int) {
    fun prestar() {
        if (exemplarsDisponibles > 0) {
            exemplarsDisponibles--
            println("El llibre $titol de l'autor $autor s'ha prestat.")
        } else {
            println("No hi ha exemplars disponibles del llibre $titol.")
        }
    }

    fun devolver() {
        exemplarsDisponibles++
        println("El llibre $titol de l'autor $autor s'ha retornat.")
    }

    fun mostrarInformacio() {
        println("Títol: $titol, Autor: $autor, Exemplars disponibles: $exemplarsDisponibles")
    }
} 