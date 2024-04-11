import Biblioteca.Llibre
import Biblioteca.Soci

class Aplicacio {
    fun executar() {
        // Crear llibres
        var llibre1 = Llibre("Wonder", "Raquel", 203)
        var llibre2 = Llibre("Las Luces de Septiempre", "Carlos Ruiz Zafón", 155)

        // Crear socis
        val soci1 = Soci("Albert", "Marquez", 20)
        val soci2 = Soci("Eric", "Rodriguez", 102)

        // Realitzar accions
        llibre1.mostrarInformacio()
        soci1.demanarPrestec(llibre1, "2024-06-20")
        llibre1.mostrarInformacio()
        llibre2.mostrarInformacio()
        soci2.demanarPrestec(llibre2, "2024-06-29")
        llibre2.mostrarInformacio()
        llibre1.mostrarInformacio()
        soci1.devolverPrestec(llibre1)
        llibre1.mostrarInformacio()
    }
}

fun main() {
    Aplicacio().executar()
}