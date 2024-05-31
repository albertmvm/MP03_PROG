package library;

import library.models.Llibre;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Crear una instància de GestorBaseDades
        GestorBaseDades gestorBD = new GestorBaseDades();

        // Connectar amb la base de dades
        gestorBD.connectar();

        // Afegir un nou llibre
        Llibre nouLlibre = new Llibre(1, "El principe de las nieblas", "Carlos Ruiz Zafon", 2010);
        gestorBD.afegirLlibre(nouLlibre);

        // Recuperar la llista de llibres
        List<Llibre> llistaLlibres = gestorBD.obtenirLlistaLlibres();
        for (Llibre llibre : llistaLlibres) {
            System.out.println(llibre);
        }

        // Actualitzar la informació d'un llibre
        Llibre llibreAActualitzar = llistaLlibres.get(0); // Suposem que volem actualitzar el primer llibre de la llista
        llibreAActualitzar.setTitol("Luces de Septiembre");
        gestorBD.actualitzarLlibre(llibreAActualitzar);

        // Eliminar un llibre
        Llibre llibreAEliminar = llistaLlibres.get(1); // Suposem que volem eliminar el segon llibre de la llista
        gestorBD.eliminarLlibre(llibreAEliminar.getId());

        // Desconnectar de la base de dades
        gestorBD.desconnectar();
    }
}
