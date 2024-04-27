public class Main {
    public static void main(String[] args) {
        // crear una instància de pacman amb posició inicial i vides:
        PacMan pacman = new PacMan(0, 0, 3);

//fantasmes amb posicions inicials i noms:
        Fantasma[] fantasmes = {
            new Fantasma(1, 1, "Blinky"),
            new Fantasma(2, 2, "Pinky"),
            new Fantasma(3, 3, "Inky"),
            new Fantasma(4, 4, "Clyde")
        };

        // bucle principal del joc
        while (pacman.getLives() > 0) {
            // moure Pac-Man:
            pacman.setMove(pacman.getPosX() + 1, pacman.getPosY());

            // moure fantasmes:
            for (Fantasma fantasma : fantasmes) {
                fantasma.setMove(fantasma.getPosX() + 1, fantasma.getPosY());
            }

        // missatge x panatalla quan pacman perd totes les vides
        System.out.println("~~THE END~~ ja no t'ens vides!!");
    }
}
}
