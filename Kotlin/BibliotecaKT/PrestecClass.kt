class Prestec(val llibre: Llibre, val soci: Soci) {
    fun registrarPrestec(dataPrestec: String) {
        println("Préstec registrat - Llibre: ${llibre.titol}, Soci: ${soci.nom} ${soci.cognom}, Data: $dataPrestec")
        llibre.prestar()
    }

    fun retornarPrestec() {
        println("Devolució de préstec - Llibre: ${llibre.titol}, Soci: ${soci.nom} ${soci.cognom}")
        llibre.devolver()
    }

    fun mostrarInformacio() {
        println("Llibre: ${llibre.titol}, Soci: ${soci.nom} ${soci.cognom}")
    }
}