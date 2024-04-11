package Biblioteca

class Soci(val nom: String, val cognom: String, val numeroSoci: Int) {

    fun sol·licitarPrestec(llibre: Llibre, dataPrestec: String) {
        println("Sol·licitud de préstec feta per $nom $cognom, Número de Soci: $numeroSoci")
        val prestec = Prestec(llibre, this)
        prestec.registrarPrestec(dataPrestec)
    }

    fun retornarPrestec(llibre: Llibre) {
        println("Devolució de préstec feta per $nom $cognom, Número de Soci: $numeroSoci")
        val prestec = Prestec(llibre, this)
        prestec.retornarPrestec()
    }

    fun informacio() {
        println("Nom: $nom, Cognom: $cognom, Número de Soci: $numeroSoci")
    }
}
