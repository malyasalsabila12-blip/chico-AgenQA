---
description: "Detect pixel-perfect UI changes and layout shifts."
---

# Visual Regression Skill

## When to Use
Use this skill after CSS changes, framework updates, or when ensuring UI consistency across different browsers and screen sizes.

## Steps
1. **Define Baselines**: Capture "Gold Standard" screenshots of key pages.
2. **Perform Comparison**: Run tests against the current environment and compare pixels.
3. **Threshold Analysis**: Ignore minor anti-aliasing differences (set threshold, e.g., 0.1%).
4. **Identify Shifts**: Pinpoint layout shifts or color changes.
5. **Verify Evidence**: Attach a "Diff" image showing the mismatch in red/magenta.

## Example Output
### Visual Regression Report: Checkout Page
- **Status**: FAIL (1.2% mismatch detected)
- **Difference Found**: The "Place Order" button shifted 5px to the right.
- **Environment**: Chrome (1920x1080)
- **Evidence**: `visual_diff_checkout_TC-05.png`
