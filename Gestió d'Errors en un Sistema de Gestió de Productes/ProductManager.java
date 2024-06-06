package com.example.productmanagement;

import java.util.HashMap;
import java.util.Map;

public class GestorProductes {
    private Map<Integer, Producte> mapaProductes;

    public GestorProductes() {
        this.mapaProductes = new HashMap<>();
    }

    public void afegirProducte(Producte producte) throws ProductAlreadyExistsException {
        if (mapaProductes.containsKey(producte.getId())) {
            throw new ProductAlreadyExistsException("El producte amb ID " + producte.getId() + " ja existeix.");
        }
        mapaProductes.put(producte.getId(), producte);
    }

    public void eliminarProducte(int id) throws ProductNotFoundException {
        if (!mapaProductes.containsKey(id)) {
            throw new ProductNotFoundException("El producte amb ID " + id + " no s'ha trobat.");
        }
        mapaProductes.remove(id);
    }

    public Producte obtenirProducte(int id) throws ProductNotFoundException {
        Producte producte = mapaProductes.get(id);
        if (producte == null) {
            throw new ProductNotFoundException("El producte amb ID " + id + " no s'ha trobat.");
        }
        return producte;
    }
}
