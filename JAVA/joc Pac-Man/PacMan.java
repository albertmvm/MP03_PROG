public class PacMan {
    private int posX, posY, score, lives;
    private boolean powerMode;
// indiquem els valors per cada variable.
// el boolea "powerMode" indica si Pac-Man esta en mode de poder temporal.


// Setters posX, posY, score, lives i powerMode.
    public PacMan(int posX, int posY, int lives) {
        this.setPosX = (posX);
        this.setPosY = (posY);
        this.setScore = (score);
        this.setLives = (lives);
        this.setPowerMode = false;
    }

// Getters posX, posY, score, lives i powerMode.
    public int getPosX() {
        return this.posX;
    }

    public int getPosY() {
        return this.posY;
    }

    public int getScore() {
        return this.score;
    }

    public int getLives() {
        return this.lives;
    }

    public boolean isPowerMode() {
        return this.powerMode;
    }


// pac-man es mou a una nova posició
public void setMove(int posX, int posY) {
        this.posX = posX;
        this.posY = posY;
    }

// Recol·lecta una bola normal i augmenta la puntuació.
    public void setPickupBola() {
        score += 10;
    }

// Recol·lecta una bola especial i atorga poder temporal a Pac-Man.
    public void setPickupBolaEspecial() {
        powerMode = true;
    }
    
// Recol·lecta una fruita i augmenta la puntuació.
    public void setPickupFruita() {
        score += 100;
    }

    
// 1 vida (-) quan és capturat per un fantasma.
    public void setLoseLife() {
        lives--;
    }

    public void setDetectColisionFantasma(Fantasma fantasma) {
    }

}
