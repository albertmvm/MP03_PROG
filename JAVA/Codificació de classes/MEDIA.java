public class Media{
    private String nom, autor;
    private int duradaSegons;


    public Media(String nom, String autor, int duradaSegons){
        this.setNom(nom);
        this.setAutor(autor);
        this.setDuradaSegons(duradaSegons);

    }

    public String getNom(){
        return this.nom;
    }

    public String getAutor(){
        return this.autor;
    }

    public int getDuradaSegons(){
        return this.duradaSegons;
    }

    public void setMedia(String nom, String autor, int duradaSegons){
        this.nom = nom;
        this.autor = autor;
        this.duradaSegons = temps;
    }
}