---
description: "Perform automated accessibility audits using WCAG standards."
---

# Accessibility Audit Skill

## When to Use
Use this skill to verify that the application is accessible to users with disabilities, focusing on WCAG 2.1 Level AA compliance. Run this during the initial testing phase or when UI components are updated.

## Steps
1. **Identify Target Pages**: Select key user workflows (Login, Checkout, Profile).
2. **Execute Audit**: Use Playwright with `axe-playwright` to scan the page.
3. **Capture Context**: Note the specific component or DOM element failing.
4. **Categorize Violations**: Group by impact (Critical, Serious, Moderate, Minor).
5. **Report Findings**: Provide the rule violated, the element involved, and a suggested fix.

## Example Output
### Accessibility Audit: Homepage
- **Score**: 85/100
- **Critical Issues**: 1
  - **Rule**: `image-alt` (Images must have alternate text)
  - **Element**: `<img src="/logo.png">`
  - **Fix**: Add `alt="Company Logo"` attribute.
- **Serious Issues**: 2
  - **Rule**: `color-contrast` (Text must have sufficient contrast)
  - **Element**: `.footer-text`
