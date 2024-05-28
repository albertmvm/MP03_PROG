//UML: Sistema de Gestió d'Universitat

public class Professor {
    private String nom;
    private String departament;
    private List<Curs> cursos;
}

public class Curs {
    private String nom;
    private String codi;
    private Professor professor;
    private List<Estudiant> estudiants;
}

public class Estudiant {
    private String nom;
    private int matricula;
}
