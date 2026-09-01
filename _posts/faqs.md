---
name: "DTT Lib"
short_name: "dttlib"
title: "Frequently Asked Questions (FAQ): DTT Lib"
description: "Answers to common questions about DTT Lib temporal calculations, leap seconds, and license."
keywords: "dttlib FAQ, rust datetime questions"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "faqs"
permalink: "https://dttlib.com/faqs/index.html"
logo: "https://cloudcdn.pro/dtt/v1/logos/dtt.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "DTT Lib — Date, Time & Timezone Utilities for Rust"
---

# Frequently Asked Questions

<div class="apple-faq-section my-4">
<div class="apple-faq-header">
<h2 class="apple-faq-title">Questions? Answers.</h2>
<button type="button" class="apple-faq-expand-btn" id="faqExpandAllBtn" aria-expanded="false">
<span class="apple-faq-btn-text">Expand all</span>
<svg class="apple-faq-expand-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
</button>
</div>

<div class="apple-faq-list">
<details class="apple-faq-item">
<summary class="apple-faq-summary">
<span class="apple-faq-question">How are leap years calculated?</span>
<span class="apple-faq-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
</summary>
<div class="apple-faq-body">
<p>DTT Lib follows standard Gregorian calendar rules: a year is a leap year if divisible by 4, unless divisible by 100, unless also divisible by 400.</p>
</div>
</details>

<details class="apple-faq-item">
<summary class="apple-faq-summary">
<span class="apple-faq-question">Can I format custom date strings?</span>
<span class="apple-faq-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
</summary>
<div class="apple-faq-body">
<p>Yes. DTT Lib provides custom format specifiers for year, month, day, hours, minutes, seconds, and microseconds.</p>
</div>
</details>
</div>
</div>
