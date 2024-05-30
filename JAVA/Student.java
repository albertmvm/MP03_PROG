package com.example.database.models;

public class Estudiant {
    private int id;
    private String nom;
    private String cognom;

    public Estudiant(int id, String nom, String cognom) {
        this.id = id;
        this.nom = nom;
        this.cognom = cognom;
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

    public String getCognom() {
        return cognom;
    }

    public void setCognom(String cognom) {
        this.cognom = cognom;
    }

    @Override
    public String toString() {
        return "Estudiant{id=" + id + ", nom='" + nom + "', cognom='" + cognom + "'}";
    }
}