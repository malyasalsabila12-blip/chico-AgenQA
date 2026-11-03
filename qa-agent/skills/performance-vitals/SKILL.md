---
description: "Monitor Core Web Vitals and application performance metrics."
---

# Performance Vitals Skill

## When to Use
Use this skill to identify performance regressions, slow-loading pages, or layout shifts that affect user experience.

## Steps
1. **Load Page with Metrics**: Use Playwright's CDPSession to capture performance entries.
2. **Capture Core Vitals**:
   - **LCP** (Largest Contentful Paint)
   - **FID** (First Input Delay)
   - **CLS** (Cumulative Layout Shift)
3. **Analyze Network**: Identify heavy assets or slow API calls.
4. **Benchmark**: Compare against thresholds (e.g., LCP < 2.5s).
5. **Summarize**: Report on the "Speed Index" of the workflow.

## Example Output
### Performance Report: Product List
- **LCP**: 1.8s (Good)
- **CLS**: 0.05 (Good)
- **TBT** (Total Blocking Time): 120ms
- **Recommendation**: Optimize `hero-banner.jpg` (size: 2.4MB) to improve load time further.
