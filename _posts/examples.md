---
name: "DTT Lib"
short_name: "dttlib"
title: "Financial Timestamping & Microservice Examples"
description: "Real-world code examples using DTT Lib for high-frequency trading and ISO 20022 message timestamps."
keywords: "dttlib examples, financial timestamping rust"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://dttlib.com/examples/index.html"
logo: "https://cloudcdn.pro/dtt/v1/logos/dtt.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "DTT Lib — Date, Time & Timezone Utilities for Rust"
---

# Implementation Examples & Patterns

## 1. ISO 20022 Settlement Timestamp Generation

```rust
use dtt::DateTime;

let payment_timestamp = DateTime::new();
println!("Payment Settlement Timestamp: {}", payment_timestamp.iso_8601);
```
