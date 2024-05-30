package com.example.database;

import com.example.database.models.Estudiante;

public class Principal {
    public static void main(String[] args) {
        GestorBaseDades gestorBD = new GestorBaseDades();
        gestorBD.connectar();

        // Crear un nou estudiant
        Estudiant estudiant = new Estudiant(1, "Joan", "Garcia");
        gestorBD.afegirEstudiant(estudiant);

        // Recuperar estudiant
        Estudiant estudiantRecuperat = gestorBD.obtenirEstudiant(1);
        System.out.println(estudiantRecuperat);

        // Actualitzar estudiant
        estudiant.setCognom("Martínez");
        gestorBD.actualitzarEstudiant(estudiant);

        // Eliminar estudiant
        gestorBD.eliminarEstudiant(1);

        gestorBD.desconnectar();
    }
}