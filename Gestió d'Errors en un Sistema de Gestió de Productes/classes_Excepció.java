package com.example.productmanagement;

// Excepció per a productes que ja existeixen
public class ProductAlreadyExistsException extends Exception {
    public ProductAlreadyExistsException(String message) {
        super(message);
    }
}

// Excepció per a productes no trobats
public class ProductNotFoundException extends Exception {
    public ProductNotFoundException(String message) {
        super(message);
    }
}

// Excepció per a productes invàlids
public class InvalidProductException extends Exception {
    public InvalidProductException(String message) {
        super(message);
    }
}
