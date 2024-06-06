package com.example.productmanagement;

public class Main {
    public static void main(String[] args) {
        GestorProductes gestorProductes = new GestorProductes();

        try {
            Producte producte1 = new Producte(1, "Portàtil", 1500.0);
            gestorProductes.afegirProducte(producte1);

            Producte producte2 = new Producte(2, "Telefon", 800.0);
            gestorProductes.afegirProducte(producte2);

            // Intentar afegir un producte amb el mateix ID
            try {
                Producte producteDuplicat = new Producte(1, "Tauleta", 400.0);
                gestorProductes.afegirProducte(producteDuplicat);
            } catch (ProductAlreadyExistsException e) {
                System.out.println(e.getMessage());
            }

            // Recuperar i mostrar un producte
            Producte producteRecuperat = gestorProductes.obtenirProducte(1);
            System.out.println(producteRecuperat);

            // Intentar recuperar un producte que no existeix
            try {
                Producte producteInexistent = gestorProductes.obtenirProducte(3);
            } catch (ProductNotFoundException e) {
                System.out.println(e.getMessage());
            }

            // Actualitzar un producte
            producte1.setNom("Portàtil Gaming");
            producte1.setPreu(2000.0);
            gestorProductes.afegirProducte(producte1);

            // Eliminar un producte
            gestorProductes.eliminarProducte(2);

            // Intentar eliminar un producte que no existeix
            try {
                gestorProductes.eliminarProducte(2);
            } catch (ProductNotFoundException e) {
                System.out.println(e.getMessage());
            }

        } catch (InvalidProductException | ProductAlreadyExistsException | ProductNotFoundException e) {
            e.printStackTrace();
        }
    }
}
