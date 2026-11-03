---
description: "Mengecek fitur lama tidak rusak setelah perubahan"
---

# Regression Check Skill

## Kapan Digunakan
Gunakan skill ini setelah ada update kode atau bug fix untuk memastikan fungsionalitas yang ada tetap berjalan normal.

## Langkah-langkah
1. Identifikasi area yang terdampak oleh perubahan.
2. Jalankan test suite regresi pada area tersebut.
3. Bandingkan hasil dengan baseline sebelumnya.

## Contoh Output
### Regression Report: Checkout Flow
- **Feature**: Add to Cart - **Status**: PASS
- **Feature**: Payment Selection - **Status**: PASS
- **Feature**: Order Summary - **Status**: PASS
