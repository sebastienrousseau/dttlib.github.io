---
name: "DTT Lib"
short_name: "dttlib"
title: "Core Features: Sub-Nanosecond Parsing & Timezones"
description: "Detailed breakdown of DTT Lib's memory safety, zero-copy parsing, and timezone calculation engine."
keywords: "dttlib features, zero allocation datetime, fast timezone rust"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://dttlib.com/features/index.html"
logo: "https://cloudcdn.pro/dtt/v1/logos/dtt.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "DTT Lib — Date, Time & Timezone Utilities for Rust"
---

# Core Capabilities & Features

<div class="bento-grid my-4">
<div class="bento-card bento-col-6">
<div class="bento-tag">Performance</div>
<h2 class="bento-title">Zero Heap Allocations</h2>
<p class="bento-desc">All date and time calculations occur directly on the CPU stack with zero heap churn.</p>
</div>

<div class="bento-card bento-col-6">
<div class="bento-tag">Compliance</div>
<h2 class="bento-title">Institutional Standard Conformance</h2>
<p class="bento-desc">Strict compliance with ISO 8601, RFC 3339, RFC 2822, and ISO 20022 payment specifications.</p>
</div>

<div class="bento-card bento-col-6">
<div class="bento-tag">Timezones</div>
<h2 class="bento-title">IANA Timezone Calculations</h2>
<p class="bento-desc">Effortlessly convert timestamps across New York (EST/EDT), London (GMT/BST), Tokyo (JST), and UTC.</p>
</div>

<div class="bento-card bento-col-6">
<div class="bento-tag">Architecture</div>
<h2 class="bento-title">`no_std` Embedded Ready</h2>
<p class="bento-desc">Compatible with bare-metal, embedded microcontrollers, and WebAssembly execution contexts.</p>
</div>
</div>
