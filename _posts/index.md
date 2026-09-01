---
name: "DTT Lib"
short_name: "dttlib"
title: "DTT Lib: Deterministic Date, Time & Timezone Engine in Rust"
description: "High-performance date, time, and timezone manipulation library for Rust with zero heap allocations, sub-nanosecond precision, and full ISO 8601/RFC 3339 compliance."
keywords: "dttlib, rust datetime, date time timezone rust, ISO 8601 rust, zero allocation datetime"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "index"
permalink: "https://dttlib.com/"
logo: "https://cloudcdn.pro/dtt/v1/logos/dtt.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "DTT Lib — Date, Time & Timezone Utilities for Rust"
---

<section class="hero-editorial">
<div class="eyebrow-badge">
<span class="eyebrow-pulse"></span>
<span>Temporal Engineering · Open Source · Rust · Updated September 2026</span>
</div>
<h1>Deterministic date, time & timezone engine.<br>Sub-nanosecond precision. Zero allocations.</h1>
<p class="hero-lead">An open-source, high-throughput Rust library engineered for institutional financial transactions, distributed clock synchronization, and high-frequency temporal parsing with zero heap allocations and full ISO 8601 / RFC 3339 conformance.</p>
<div class="hero-actions">
<a href="/getting-started/index.html" class="btn-primary-quantum">Get Started (Crate & CLI) →</a>
<a href="/features/index.html" class="btn-secondary-quantum">Explore Capabilities</a>
</div>
</section>

<!-- SECTION 2: KEY STATS TICKER -->
<section class="clock-ticker-section my-5" aria-label="Performance Benchmarks">
<div class="row g-3">
<div class="col-md-4 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">&lt; 1.2 ns</div>
<div class="stat-label">Parse Latency</div>
<div class="stat-source">Zero-allocation byte parser · <a href="/benchmarks/index.html">Benchmark Specs ↗</a></div>
</div>
</div>

<div class="col-md-4 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">100% ISO 8601</div>
<div class="stat-label">RFC 3339 & 2822</div>
<div class="stat-source">Strict temporal standards · <a href="/formats/index.html">Format Matrix ↗</a></div>
</div>
</div>

<div class="col-md-4 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">0 Bytes</div>
<div class="stat-label">Heap Allocation</div>
<div class="stat-source">Stack-only no_std ready · <a href="/architecture/index.html">Memory Model ↗</a></div>
</div>
</div>

<div class="col-md-6 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">FinTech Ready</div>
<div class="stat-label">ISO 20022 Timestamping</div>
<div class="stat-source">pain.001 & pacs.008 support · <a href="/examples/index.html">Financial Use Cases ↗</a></div>
</div>
</div>

<div class="col-md-6 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">Dual Apache/MIT</div>
<div class="stat-label">Open Source License</div>
<div class="stat-source">Enterprise friendly · <a href="https://github.com/sebastienrousseau/dttlib.github.io" target="_blank" rel="noopener noreferrer">GitHub Repo ↗</a></div>
</div>
</div>
</div>
</section>

<!-- SECTION 3: CORE CAPABILITIES BENTO GRID -->
<section class="my-5" aria-label="Core Capabilities">
<div class="text-center mb-4">
<h2 class="h3 fw-bold">Engineered for Microsecond Precision</h2>
<p class="text-muted">Solve timezone ambiguity, daylight saving drift, and parsing latency across distributed architectures.</p>
</div>

<div class="bento-grid">
<div class="bento-card bento-col-4">
<div>
<div class="bento-tag">Parsing Engine</div>
<h3 class="bento-title">High-Speed ISO 8601 Parser</h3>
<p class="bento-desc">Parse RFC 3339, RFC 2822, and custom financial timestamp strings directly from byte slices without string copying or heap allocations.</p>
</div>
<a href="/formats/index.html" class="author-link">View Formatting Specs →</a>
</div>

<div class="bento-card bento-col-4">
<div>
<div class="bento-tag">Timezones & DST</div>
<h3 class="bento-title">IANA Timezone Conversions</h3>
<p class="bento-desc">Deterministic offset lookups and daylight saving transitions across all global financial market hours with zero external runtime dependencies.</p>
</div>
<a href="/features/index.html" class="author-link">Explore Timezone Engine →</a>
</div>

<div class="bento-card bento-col-4">
<div>
<div class="bento-tag">FinTech Rails</div>
<h3 class="bento-title">ISO 20022 Temporal Validation</h3>
<p class="bento-desc">Ensure strict transaction settlement timestamp formatting (`CreationDateTime`, `SettlementDate`) required for FedNow, SEPA, and CHAPS payment messages.</p>
</div>
<a href="/examples/index.html" class="author-link">Explore FinTech Patterns →</a>
</div>
</div>
</section>

<!-- SECTION 4: TERMINAL QUICKSTART -->
<section class="my-5" aria-label="Developer Quickstart">
<div class="card-surface p-4 p-md-5">
<div class="row align-items-center g-4">
<div class="col-lg-6">
<div class="eyebrow-badge">Developer Quickstart</div>
<h2 class="h3 fw-bold text-headline mb-3">Add DTT Lib to Your Cargo.toml</h2>
<p class="text-muted mb-4">Integrate high-speed date and time manipulation into your Rust services with zero unsafe code.</p>
<div class="d-flex gap-3 flex-wrap">
<a href="/getting-started/index.html" class="btn-primary-quantum">Quickstart Guide →</a>
<a href="/documentation/index.html" class="btn-secondary-quantum">API Reference</a>
</div>
</div>
<div class="col-lg-6">
<div class="hero-visual-terminal">
<div class="terminal-header">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">rust — dttlib</span>
</div>
<pre><code><span class="text-muted">// 1. Add dependency</span>
[dependencies]
dtt = "0.0.1"

<span class="text-muted">// 2. Create and format DateTime</span>
use dtt::DateTime;

let dt = DateTime::new();
println!("ISO 8601: {}", dt.iso_8601());
println!("Unix Timestamp: {}", dt.timestamp);</code></pre>
</div>
</div>
</div>
</div>
</section>

<!-- SECTION 5: QUESTIONS? ANSWERS. -->
<section class="my-5" aria-label="Frequently Asked Questions">
<div class="apple-faq-section">
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
<span class="apple-faq-question">How does DTT Lib compare to Chrono or Time crate?</span>
<span class="apple-faq-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
</summary>
<div class="apple-faq-body">
<p>DTT Lib is specifically engineered for high-throughput institutional trading systems and payment rails where zero allocations, instant compile times, strict ISO 8601 conformance, and minimal dependency trees are paramount.</p>
</div>
</details>

<details class="apple-faq-item">
<summary class="apple-faq-summary">
<span class="apple-faq-question">Does DTT Lib support `no_std` environments?</span>
<span class="apple-faq-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
</summary>
<div class="apple-faq-body">
<p>Yes. By disabling default features, DTT Lib operates seamlessly in embedded and `no_std` environments without requiring an operating system allocator.</p>
</div>
</details>
</div>
</div>
</section>

<!-- SECTION 6: NEXT STEPS -->
<section class="card-surface p-4 p-md-5 my-5 text-center" aria-label="Conversion Next Steps">
<h2 class="h2 fw-bold text-headline mb-3">Optimize Your Temporal Data Pipelines Today</h2>
<p class="text-muted fs-5 mb-4 max-w-2xl mx-auto">Get started in minutes with the Rust crate or explore comprehensive formatting guides:</p>
<div class="d-flex justify-content-center gap-3 flex-wrap">
<a href="/getting-started/index.html" class="btn-primary-quantum">Get Started (Install) →</a>
<a href="https://github.com/sebastienrousseau/dttlib.github.io" target="_blank" rel="noopener noreferrer" class="btn-secondary-quantum">View on GitHub (Stars & Code) ↗</a>
<a href="/documentation/index.html" class="btn-secondary-quantum">API Reference</a>
</div>
</section>
