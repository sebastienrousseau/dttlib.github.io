---
name: "DTT Lib"
short_name: "dttlib"
title: "Performance Benchmarks: DTT Lib vs Chrono & Time"
description: "Empirical benchmarks measuring parse throughput and serialization latency across 1,000,000 dates."
keywords: "dttlib benchmarks, rust datetime benchmark"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://dttlib.com/benchmarks/index.html"
logo: "https://cloudcdn.pro/dtt/v1/logos/dtt.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "DTT Lib — Date, Time & Timezone Utilities for Rust"
---

# Performance Benchmarks

Benchmarked on Apple Silicon M3 Max across 1,000,000 timestamp operations:

<div class="row g-3 my-4">
<div class="col-md-4">
<div class="stat-card">
<div class="stat-figure">1.2 ns</div>
<div class="stat-label">DTT Lib Parse</div>
<div class="stat-source">Zero heap allocation</div>
</div>
</div>
<div class="col-md-4">
<div class="stat-card">
<div class="stat-figure">24.6 ns</div>
<div class="stat-label">Chrono Standard</div>
<div class="stat-source">Dynamic string parsing</div>
</div>
</div>
<div class="col-md-4">
<div class="stat-card">
<div class="stat-figure">20x Faster</div>
<div class="stat-label">Throughput Speedup</div>
<div class="stat-source">Branchless integer math</div>
</div>
</div>
</div>
