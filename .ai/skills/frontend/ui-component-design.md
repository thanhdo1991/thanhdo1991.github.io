---
id: ui-component-design
version: 2.0.0
confidence: 0.80
success_rate: 0.76
last_updated: 2026-06-29
tags:
  - frontend
  - ui
  - components
  - flexible
---

# UI Component Design

> Flexible skill. Design reusable UI components following single responsibility, composability, and clear interfaces. Build a consistent, maintainable component library.

## Overview

UI components are the building blocks of a frontend application. Well-designed components are reusable, testable, and maintainable. They encapsulate markup, style, and behavior behind a clear interface, allowing teams to build consistent UIs at scale.

**Core Principle**: Each component should do one thing and do it well. If a component has multiple responsibilities, split it. If it has too many props, compose it.

## Step-by-Step Process

### Phase 1: Identify the Component
1. Draw boxes around UI elements. Each box is a candidate component.
2. Ask: "Can this element be reused elsewhere?" If yes, it should be a reusable component.
3. Ask: "Does this element have internal state or logic?" If yes, it should be a component, not a styled div.
4. Classify: atomic (Button, Input), molecular (FormField, Card), organism (Header, DataTable).

### Phase 2: Define the Interface
1. Name props clearly: use domain language, not implementation details.
2. Prefer boolean props for options, enum props for modes.
3. Never expose internal HTML attributes directly unless the component is a wrapper.
4. Every component should have a reasonable default state (no required props that are always "true").

### Phase 3: Implement
1. Start with the rendered output. Write the minimal markup that satisfies the design.
2. Add styling: use the project's styling approach (CSS modules, Tailwind, styled-components).
3. Add behavior: event handlers, state management, effects.
4. Handle states:
   - **Default**: The component renders with no special props.
   - **Disabled**: The component is rendered but non-interactive.
   - **Error**: The component displays validation or error feedback.
   - **Empty**: The component handles the case of no data gracefully.
   - **Loading**: The component shows a loading state.

### Phase 4: Compose
1. Combine atomic components into molecular components.
2. Use children/slots for flexible content insertion.
3. Use render props or component injection for polymorphic behavior.
4. Avoid prop drilling: if a prop passes through 3+ layers, use composition or context.

## Common Mistakes

- **Too many props**: A component with 15+ props is doing too much. Split it or use composition.
- **Prop drilling**: Passing props through intermediate components that don't use them. Use context or component composition.
- **Tight coupling to data fetching**: Components should accept data, not fetch it internally. Separate data fetching from presentation.
- **CSS in JS performance issues**: Dynamic styles that change every render defeat caching. Use static styles when possible.
- **Ignoring accessibility**: Every interactive component must be keyboard-accessible and screen-reader friendly. aria-* attributes are not optional.

## Quality Gates

- [ ] Component renders without errors with default props.
- [ ] Component is keyboard navigable (focus, Tab, Enter, Escape).
- [ ] Component has a clear, documented prop interface (TypeScript types or PropTypes).
- [ ] Component handles loading, error, empty, and disabled states where applicable.
- [ ] Component is not tightly coupled to a specific data source or routing library.
