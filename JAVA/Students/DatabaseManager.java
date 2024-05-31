package com.example.database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import com.example.database.models.Estudiante;

public class GestorBaseDades {
    private Connection connexio;

    public void connectar() {
        try {
            connexio = DriverManager.getConnection("jdbc:postgresql://172.17.0.2:5432/student", "postgres", "mysecretpassword");
            System.out.println("Connexió establerta.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public Estudiant obtenirEstudiant(int id) {
        String consulta = "SELECT * FROM students WHERE id = ?";
        Estudiant estudiant = null;

        try {
            PreparedStatement stmt = connexio.prepareStatement(consulta);
            stmt.setInt(1, id);
            ResultSet rs = stmt.executeQuery();

            if (rs.next()) {
                estudiant = new Estudiant(rs.getInt("id"), rs.getString("first_name"), rs.getString("last_name"));
            }
            rs.close();
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return estudiant;
    }

    public void afegirEstudiant(Estudiant estudiant) {
        String consulta = "INSERT INTO students (id, first_name, last_name) VALUES (?, ?, ?)";

        try {
            PreparedStatement stmt = connexio.prepareStatement(consulta);
            stmt.setInt(1, estudiant.getId());
            stmt.setString(2, estudiant.getNom());
            stmt.setString(3, estudiant.getCognom());
            stmt.executeUpdate();
            System.out.println("Estudiant afegit.");
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void actualitzarEstudiant(Estudiant estudiant) {
        String consulta = "UPDATE students SET first_name = ?, last_name = ? WHERE id = ?";

        try {
            PreparedStatement stmt = connexio.prepareStatement(consulta);
            stmt.setString(1, estudiant.getNom());
            stmt.setString(2, estudiant.getCognom());
            stmt.setInt(3, estudiant.getId());
            stmt.executeUpdate();
            System.out.println("Estudiant modificat.");
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void eliminarEstudiant(int id) {
        String consulta = "DELETE FROM students WHERE id = ?";

        try {
            PreparedStatement stmt = connexio.prepareStatement(consulta);
            stmt.setInt(1, id);
            stmt.executeUpdate();
            System.out.println("Estudiant eliminat.");
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void desconnectar() {
        try {
            if (connexio != null && !connexio.isClosed()) {
                connexio.close();
                System.out.println("Connexió tancada");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}