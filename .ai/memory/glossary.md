---
id: glossary
version: 1.0.0
confidence: 0.95
success_rate: 0.85
last_updated: 2026-06-29
tags:
  - glossary
  - template
  - reference
---

# Glossary

## Purpose

A common vocabulary reduces misunderstandings across the team. This glossary defines
terms as they are used within the project. Some terms may have broader definitions
in the industry — this document captures the project-specific meaning.

---

## General Software Engineering Terms

| Term | Definition |
|------|------------|
| **Abstraction** | Hiding implementation details behind a simplified interface. A fundamental tool for managing complexity. |
| **Adapter** | A structural pattern that allows incompatible interfaces to work together through a wrapper. |
| **Aggregate** | A cluster of domain objects treated as a single unit for data changes, with one root entity enforcing invariants. |
| **API** | Application Programming Interface — the contract through which components or services interact. |
| **Callback** | A function passed as an argument to another function, to be executed after an operation completes. |
| **Cohesion** | The degree to which elements inside a module belong together. High cohesion is preferred. |
| **Coupling** | The degree of dependency between modules. Loose coupling is preferred. |
| **DTO** | Data Transfer Object — a simple object that carries data between processes or layers without behavior. |
| **Edge Case** | A scenario that occurs at an extreme (minimum or maximum) of operating parameters. |
| **Idempotent** | An operation that produces the same result regardless of how many times it is executed. |
| **Invariant** | A condition that must always hold true for a system to be in a valid state. |
| **Middleware** | Software that sits between request and response, handling cross-cutting concerns. |
| **Monad** | A design pattern that wraps a value and defines how to apply functions to it (e.g., Optional, Result). |
| **Polyfill** | Code that implements a newer feature in an older environment where it is not natively available. |
| **Repository** | A pattern that mediates between the domain and data mapping layers, acting like an in-memory collection. |
| **Side Effect** | Any state change that occurs outside a function's local scope (I/O, DB writes, etc.). |
| **Smoke Test** | A shallow test that verifies critical paths work without exhaustive validation. |
| **Technical Debt** | The implied cost of additional rework caused by choosing an easy solution now instead of a better approach that would take longer. |
| **Transaction** | A sequence of operations treated as a single unit of work that must either fully complete or fully roll back. |
| **Value Object** | An immutable object whose equality is based on its attributes rather than identity. |
| **Waterfall** | A sequential development model where each phase must complete before the next begins. (Contrast with Agile.) |

## Project-Specific Terms

| Term | Definition |
|------|------------|
| [Term] | [Project-specific definition] |
| [Term] | [Project-specific definition] |

---

## Domain Language

If this project has a specialized domain (finance, healthcare, logistics, gaming,
etc.), define the key domain terms here:

| Domain Term | Definition |
|-------------|------------|
| [Term] | [Definition] |
| [Term] | [Definition] |

## Abbreviations & Acronyms

| Abbreviation | Expansion | Context |
|--------------|-----------|---------|
| ADR | Architecture Decision Record | Documented architectural choice |
| CI/CD | Continuous Integration / Continuous Delivery | Automated build, test, and deploy pipeline |
| IaC | Infrastructure as Code | Managing infrastructure through configuration files |
| SLA | Service Level Agreement | Committed performance or uptime target |
| SLO | Service Level Objective | Internal performance target |
| SSOT | Single Source of Truth | The authoritative location for a given piece of data |

---

*Add new terms as they arise. Keep definitions concise and project-relevant.*
