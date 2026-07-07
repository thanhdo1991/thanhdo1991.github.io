---
id: accessibility-review
version: 2.0.0
confidence: 0.70
success_rate: 0.65
last_updated: 2026-06-29
tags:
  - quality
  - accessibility
  - flexible
---

# Accessibility Review

> Flexible skill. Evaluate web interfaces against WCAG 2.1 AA standards. Cover semantic HTML, keyboard navigation, screen reader compatibility, color contrast, and focus management.

## Overview

Accessibility (a11y) ensures that people with disabilities can perceive, understand, navigate, and interact with your application. It is not a feature toggle; it is a design requirement that applies to every component. 15-20% of the global population has some form of disability.

**Core Principle**: Accessibility is not a feature. It's a fundamental requirement of the user experience. Build accessibly from the start, not as an afterthought.

## Step-by-Step Process

### Phase 1: Semantic Structure
1. Verify the document has a logical heading hierarchy (h1 > h2 > h3, no skips).
2. Check that landmarks are used: `<nav>`, `<main>`, `<aside>`, `<footer>`.
3. Ensure lists are marked up as `<ul>`/`<ol>` with `<li>`, not divs with bullets.
4. Verify tables have `<th>` elements with `scope` attributes for data tables.

### Phase 2: Keyboard Navigation
1. Tab through the page: can all interactive elements be reached?
2. Check that Tab order follows visual order (no positive `tabindex` values above 0).
3. Verify focus indicators are visible (not `outline: none` without replacement).
4. Test custom components: do they support arrow keys, Enter, Escape, Space?
5. Check for keyboard traps: elements that capture focus and won't let it leave.

### Phase 3: Screen Reader
1. Test with a screen reader (NVDA on Windows, VoiceOver on Mac).
2. Verify all images have meaningful `alt` text (or `alt=""` for decorative images).
3. Check that ARIA labels are used where native semantics are insufficient.
4. Verify error messages are announced: use `aria-live` regions, `role="alert"`.
5. Ensure dynamic content updates are announced.

### Phase 4: Visual and Interaction
1. Check color contrast: WCAG AA requires 4.5:1 for normal text, 3:1 for large text.
2. Verify the site works at 200% zoom without loss of content or functionality.
3. Check that text can be resized without loss of content (no fixed font sizes that break layout).
4. Ensure touch targets are at least 44x44 pixels on mobile.

## Common Mistakes

- **`outline: none` on focus**: Always provide a visible focus indicator. Never remove outlines without replacement.
- **Missing form labels**: Every `<input>`, `<select>`, and `<textarea>` needs an associated `<label>`.
- **Non-descriptive link text**: "Click here" and "Read more" are meaningless to screen readers. Use descriptive link text.
- **Relying solely on color**: Never use color alone to convey status, differences, or errors. Add icons, text, or patterns.
- **ARIA overuse**: First rule of ARIA: if you can use a native HTML element, use it. ARIA should supplement, not replace, semantics.

## Quality Gates

- [ ] Page passes automated a11y scan (axe-core, Lighthouse, WAVE).
- [ ] No elements with `outline: none` present without a visible focus alternative.
- [ ] Heading hierarchy is logical with no skipped levels.
- [ ] All form inputs have associated labels.
- [ ] Color contrast meets WCAG AA minimum (4.5:1 for normal text).
- [ ] Full keyboard navigation is functional and logical.
- [ ] Page works at 200% zoom without horizontal scrolling or content loss.
