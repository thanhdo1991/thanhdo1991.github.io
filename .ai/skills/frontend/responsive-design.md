---
id: responsive-design
version: 2.0.0
confidence: 0.75
success_rate: 0.72
last_updated: 2026-06-29
tags:
  - frontend
  - responsive
  - css
  - flexible
---

# Responsive Design

> Flexible skill. Build applications that work across mobile, tablet, and desktop. Mobile-first approach with fluid layouts, appropriate breakpoints, and touch-friendly interactions.

## Overview

Responsive design ensures that your application provides an optimal viewing and interaction experience across a wide range of devices. The mobile-first approach starts with the smallest screen and adds complexity for larger screens, ensuring the core experience works everywhere.

**Core Principle**: Start with the smallest screen and add complexity as space allows. Mobile constraints force prioritization; don't treat mobile as a stripped-down desktop version.

## Step-by-Step Process

### Phase 1: Layout Strategy
1. Use fluid grids: CSS Grid or Flexbox. Avoid pixel-perfect layouts.
2. Define relative units (rem, em, %, vw, vh) over fixed pixels.
3. Min-width instead of max-width: the layout expands, it never shrinks.
4. Use CSS Grid for page-level layout (header, sidebar, main, footer).

### Phase 2: Breakpoints
1. Define breakpoints based on content, not device sizes:
   - Mobile: default (no query needed).
   - Tablet: min-width 48rem (768px).
   - Desktop: min-width 64rem (1024px).
   - Wide: min-width 80rem (1280px).
2. Test at every breakpoint and at intermediate widths between breakpoints.
3. Avoid device-specific breakpoints. An iPad Pro in landscape is not a meaningful target.

### Phase 3: Typography and Spacing
1. Use a fluid type scale: the base font size scales with viewport.
2. Line height: 1.5 for body text, 1.2 for headings. Adjust for mobile (larger line height improves readability).
3. Spacing: use a consistent spacing scale (4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px).
4. Touch targets: minimum 44x44px for interactive elements on mobile.

### Phase 4: Images and Media
1. Use `srcset` and `<picture>` for responsive images. Serve the right size for the viewport.
2. Lazy-load below-the-fold images with `loading="lazy"`.
3. Videos: `max-width: 100%` with intrinsic aspect ratio.

### Phase 5: Navigation and Interaction
1. Navigation: hamburger menu at mobile, horizontal nav at desktop.
2. Touch: support both touch and mouse. Hover-only interactions don't work on touch devices.
3. Swipe: for carousels and list actions, but provide visible alternatives.
4. Forms: use the correct `input type` (email, tel, number) for appropriate mobile keyboard.

## Common Mistakes

- **Pixels everywhere**: Pixel values don't scale with user font size preferences. Use relative units.
- **Mobile as an afterthought**: Desktop-first designs are hard to retroactively squeeze into mobile. Design mobile-first.
- **Fixed widths/height**: A fixed width container causes horizontal scrolling on small screens.
- **Hover-reliant interactions**: Dropdowns and tooltips that appear on hover don't work on touch devices. Use click/tap instead.
- **No touch feedback**: Buttons on mobile need visual feedback (touch ripple, opacity change) for the 200ms delay before the action.

## Quality Gates

- [ ] Layout uses relative units (rem, em, %, vw, vh) consistently.
- [ ] Application is fully functional at 320px width (minimum supported).
- [ ] All interactive elements are at least 44x44px touch targets.
- [ ] No horizontal scroll at any supported breakpoint.
- [ ] Images are responsive (serve correct size per viewport).
- [ ] Navigation works without hover (tap on mobile, click on desktop).
