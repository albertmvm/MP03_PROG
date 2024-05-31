package library;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import com.example.library.models.Llibre;

public class GestorBaseDades {
    private Connection connexio;

    public void connectar() {
        try {
            connexio = DriverManager.getConnection("jdbc:mysql://localhost:3306/biblioteca", "usuari", "contrasenya");
            System.out.println("Connexió establerta.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Llibre> obtenirLlistaLlibres() {
        List<Llibre> llistaLlibres = new ArrayList<>();
        String consulta = "SELECT * FROM llibres";

        try {
            PreparedStatement stmt = connexio.prepareStatement(consulta);
            ResultSet rs = stmt.executeQuery();

            while (rs.next()) {
                Llibre llibre = new Llibre(rs.getInt("id"), rs.getString("titol"), rs.getString("autor"), rs.getInt("any_publicacio"));
                llistaLlibres.add(llibre);
            }

            rs.close();
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return llistaLlibres;
    }

    public void afegirLlibre(Llibre llibre) {
        String consulta = "INSERT INTO llibres (titol, autor, any_publicacio) VALUES (?, ?, ?)";

        try {
            PreparedStatement stmt = connexio.prepareStatement(consulta);
            stmt.setString(1, llibre.getTitol());
            stmt.setString(2, llibre.getAutor());
            stmt.setInt(3, llibre.getAnyPublicacio());
            stmt.executeUpdate();
            System.out.println("Llibre afegit.");
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void actualitzarLlibre(Llibre llibre) {
        String consulta = "UPDATE llibres SET titol = ?, autor = ?, any_publicacio = ? WHERE id = ?";

        try {
            PreparedStatement stmt = connexio.prepareStatement(consulta);
            stmt.setString(1, llibre.getTitol());
            stmt.setString(2, llibre.getAutor());
            stmt.setInt(3, llibre.getAnyPublicacio());
            stmt.setInt(4, llibre.getId());
            stmt.executeUpdate();
            System.out.println("Llibre actualitzat.");
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void eliminarLlibre(int id) {
        String consulta = "DELETE FROM llibres WHERE id = ?";

        try {
            PreparedStatement stmt = connexio.prepareStatement(consulta);
            stmt.setInt(1, id);
            stmt.executeUpdate();
            System.out.println("Llibre eliminat.");
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void desconnectar() {
        try {
            if (connexio != null && !connexio.isClosed()) {
                connexio.close();
                System.out.println("Connexió tancada.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
