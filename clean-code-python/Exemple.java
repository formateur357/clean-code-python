// Principe ISP : Interface Segregation Principle

// Mauvais code

interface Machine {
    void imprimer();
    void scanner();
    void faxer();
}

class ImprimanteBasique implements Machine {
    public void imprimer() { ... }
    public void scanner() { ... }
    public void faxer() { ... }
}

// Bon code

interface Imprimante { void imprimer(); }
interface Scanner { void scanner(); }
interface Fax { void faxer(); }

class ImprimanteBasique implements Imprimante {
    public void imprimer() { ... }
}