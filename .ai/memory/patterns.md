---
id: patterns
version: 1.0.0
confidence: 0.95
success_rate: 0.87
last_updated: 2026-06-29
tags:
  - patterns
  - design-patterns
  - template
---

# Design Patterns

## Purpose

A catalog of design patterns used in the project and guidance on when to apply each
one. Patterns provide a shared vocabulary for design decisions and proven solutions
to recurring problems.

---

## Creational Patterns

Patterns that control object creation mechanisms.

| Pattern | When to Use | Example in This Project |
|---------|-------------|------------------------|
| **Factory Method** | When a class cannot anticipate the type of objects it must create; when subclasses should specify the types. | [Describe where used or mark as TBD] |
| **Abstract Factory** | When a system should be independent of how its products are created, composed, or represented. | [TBD] |
| **Builder** | When constructing complex objects with many optional parameters or a multi-step construction process. | [TBD] |
| **Singleton** | When exactly one instance of a class is needed and it must be globally accessible. Use sparingly — consider dependency injection instead. | [TBD] |
| **Prototype** | When creating new objects by copying an existing instance is more efficient than creating from scratch. | [TBD] |
| **Dependency Injection** | When objects should receive their dependencies rather than creating them internally. Preferred over Service Locator. | [TBD] |

## Structural Patterns

Patterns that compose classes and objects into larger structures.

| Pattern | When to Use | Example in This Project |
|---------|-------------|------------------------|
| **Adapter** | When you need to make an existing interface work with another interface without modifying either. | [TBD] |
| **Bridge** | When you want to decouple an abstraction from its implementation so they can vary independently. | [TBD] |
| **Composite** | When you need to treat individual objects and compositions of objects uniformly (tree structures). | [TBD] |
| **Decorator** | When you need to add responsibilities to objects dynamically without affecting other objects. | [TBD] |
| **Facade** | When you need to provide a simplified interface to a complex subsystem. | [TBD] |
| **Proxy** | When you need to control access to an object (lazy loading, access control, logging). | [TBD] |

## Behavioral Patterns

Patterns that define how objects communicate and collaborate.

| Pattern | When to Use | Example in This Project |
|---------|-------------|------------------------|
| **Chain of Responsibility** | When multiple handlers can process a request, and the handler is determined at runtime. | [TBD] |
| **Command** | When you need to parameterize objects with operations, queue operations, or support undo. | [TBD] |
| **Iterator** | When you need to traverse a collection without exposing its internal representation. | [TBD] |
| **Observer / Event Emitter** | When an object needs to notify multiple other objects about state changes without coupling them. | [TBD] |
| **Strategy** | When you need to swap algorithms at runtime; when you have multiple ways to accomplish a task. | [TBD] |
| **Template Method** | When subclasses should define parts of an algorithm without changing its structure. | [TBD] |
| **Visitor** | When you need to perform operations on objects of a fixed set of types without modifying their classes. | [TBD] |
| **State** | When an object's behavior depends on its internal state and should change at runtime. | [TBD] |
| **Mediator** | When you need to reduce chaotic coupling between many objects by centralizing their communication. | [TBD] |
| **Memento** | When you need to capture and restore an object's internal state without violating encapsulation. | [TBD] |

## Architectural Patterns

| Pattern | When to Use |
|---------|-------------|
| **Layered Architecture** | Standard enterprise applications with clear separation of concerns. |
| **Hexagonal / Ports & Adapters** | Applications where the domain should be completely isolated from infrastructure. |
| **CQRS** | When read and write workloads have different shapes or scale independently. |
| **Event Sourcing** | When you need a complete audit trail or the ability to rebuild state from events. |
| **Saga** | When a transaction spans multiple services and needs a rollback strategy. |
| **Repository** | When you need to abstract data access behind a collection-like interface. |
| **Unit of Work** | When you need to coordinate multiple writes into a single transaction. |

---

## Decision Framework for Choosing a Pattern

1. **Identify the problem:** What specific design challenge are you solving?
2. **Consider the simplest solution:** Can you solve this without a formal pattern?
3. **Evaluate the trade-off:** Patterns add structure but also complexity. Is the
   benefit worth the overhead?
4. **Check consistency:** Does the pattern align with existing patterns in the codebase?
   Consistency is preferred over introducing a new pattern for a marginal benefit.
5. **Document the choice:** If you introduce a new pattern, record the decision in
   an ADR and add the pattern to this catalog.

---

*Add patterns as they are introduced to the project. Mark as TBD until a concrete
example exists in the codebase.*
