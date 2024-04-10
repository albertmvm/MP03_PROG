class Viatge(val id: Int, val destinacio: String, val data: String, val preu: Double)
class Client(val id: Int, val nom: String, val email: String)
class Reserva(val id: Int, val clientId: Int, val viatgeId: Int)

class GestioViatges {
    private val viatges = mutableListOf<Viatge>()

    fun afegirViatge(viatge: Viatge) {
        viatges.add(viatge)
    }

    fun obtenirInformacioResumida(): List<Viatge> {
        return viatges.toList()
    }

    fun obtenirInformacioDetallada(viatgeId: Int): Viatge? {
        return viatges.find { it.id == viatgeId }
    }
}

class GestioClients {
    private val clients = mutableListOf<Client>()
    private var idClient = 1

    fun registrarClient(nom: String, email: String): Int {
        val nouClient = Client(idClient++, nom, email)
        clients.add(nouClient)
        return nouClient.id
    }
}

class GestioReserves {
    private val reserves = mutableListOf<Reserva>()
    private var idReserva = 1

    fun ferReserva(clientId: Int, viatgeId: Int): Int {
        val novaReserva = Reserva(idReserva++, clientId, viatgeId)
        reserves.add(novaReserva)
        return novaReserva.id
    }

    fun obtenirInformacioDetallada(reservaId: Int): Reserva? {
        return reserves.find { it.id == reservaId }
    }
}

class InterficieUsuari {
    private val gestioViatges = GestioViatges()
    private val gestioClients = GestioClients()
    private val gestioReserves = GestioReserves()

    fun mostrarMenu() {
        println("1. Gestió de viatges")
        println("2. Gestió de clients")
        println("3. Gestió de reserves")
        println("0. Sortir")
    }

    fun executarAccio(opcio: Int) {
        when (opcio) {
            1 -> gestioViatgesMenu()
            2 -> gestioClientsMenu()
            3 -> gestioReservesMenu()
            0 -> println("Sortint...")
            else -> println("Opció no vàlida")
        }
    }

    private fun gestioViatgesMenu() {
        println("1. Afegir viatge")
        println("2. Obtenir informació resumida")
        println("3. Obtenir informació detallada")
        println("0. Tornar al menú principal")

        val opcio = readLine()!!.toInt()
        when (opcio) {
            1 -> afegirViatge()
            2 -> obtenirInformacioResumida()
            3 -> obtenirInformacioDetallada()
            0 -> println("Tornant al menú principal...")
            else -> println("Opció no vàlida")
        }
    }

    private fun afegirViatge() {
        print("Introdueix la destinació: ")
        val destinacio = readLine()!!
        print("Introdueix la data (format DD-MM-YYYY): ")
        val data = readLine()!!
        print("Introdueix el preu: ")
        val preu = readLine()!!.toDouble()

        val nouViatge = Viatge(gestioViatges.viatges.size + 1, destinacio, data, preu)
        gestioViatges.afegirViatge(nouViatge)