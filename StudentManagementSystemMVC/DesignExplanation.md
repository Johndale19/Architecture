DESIGN EXPLANATION

This project applies common software design patterns to improve code organization, flexibility, and maintainability. 
The Student Management System is built using the MVC architecture and integrates three design patterns: Singleton, Repository, and Strategy.

Singleton Pattern
The Singleton Pattern is used for the database configuration to ensure that only one instance of the database connection exists throughout the application.
This prevents multiple unnecessary connections and provides a centralized access point for shared resources.

Repository Pattern
The Repository Pattern is applied to manage student data. It separates data access logic from business logic by handling all create and retrieve operations in a dedicated repository class. 
This makes the system easier to maintain, test, and extend without affecting other components.

Strategy Pattern

The Strategy Pattern is used to provide interchangeable ways of displaying student information.
Different display strategies can be selected at runtime without modifying the controller code. 
This improves flexibility and supports future enhancements with minimal changes.

Overall Design Benefit
By using these design patterns, the system becomes more modular, reusable, and scalable.
The patterns reduce code duplication, simplify maintenance, and make the application easier to extend as new requirements arise.
