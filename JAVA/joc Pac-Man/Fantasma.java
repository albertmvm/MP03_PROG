public class Fantasma{
    private int posX, posY;
    private String nom;

// Setters per posX, posY i nom:
    public Fantasma(int posX, int posY, String nom) {
        this.setPosX (posX);
        this.setPosY (posY);
        this.setNom (nom);
    }

// Getters per posX, posY i nom:
    public int getPosX() {
        return this.posX;
    }

    public int getPosY() {
        return this.posY;
    }

    public String getNom() {
        return this.nom;
    }

// el fantasma es mou a una nova posició
    public void setMove(int posX, int posY) {
        this.posX = posX;
        this.posY = posY;
    }
}
