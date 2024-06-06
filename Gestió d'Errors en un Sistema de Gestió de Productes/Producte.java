package com.example.productmanagement;

public class Producte {
    private int id;
    private String nom;
    private double preu;

    public Producte(int id, String nom, double preu) throws InvalidProductException {
        if (id < 0 || nom == null || nom.trim().isEmpty() || preu < 0) {
            throw new InvalidProductException("Detalls del producte invàlids.");
        }
        this.id = id;
        this.nom = nom;
        this.preu = preu;
    }

    public int getId() {
        return id;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public double getPreu() {
        return preu;
    }

    public void setPreu(double preu) {
        this.preu = preu;
    }

    @Override
    public String toString() {
        return "Producte{id=" + id + ", nom='" + nom + "', preu=" + preu + "}";
    }
}

