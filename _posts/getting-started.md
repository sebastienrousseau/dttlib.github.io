---
name: "DTT Lib"
short_name: "dttlib"
title: "Getting Started with DTT Lib: Installation & Quickstart"
description: "How to install DTT Lib via Cargo and perform high-speed date, time, and timezone operations."
keywords: "install dttlib, cargo dtt, rust datetime quickstart"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://dttlib.com/getting-started/index.html"
logo: "https://cloudcdn.pro/dtt/v1/logos/dtt.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "DTT Lib — Date, Time & Timezone Utilities for Rust"
---

# Getting Started with DTT Lib

## 1. Installation

Add `dtt` to your `Cargo.toml`:

```toml
[dependencies]
dtt = "0.0.1"
```

---

## 2. Basic Usage

```rust
use dtt::DateTime;

fn main() {
    // Create new DateTime representing current UTC time
    let dt = DateTime::new();

    println!("ISO 8601: {}", dt.iso_8601);
    println!("RFC 3339: {}", dt.to_rfc3339());
    println!("Unix Timestamp: {}", dt.timestamp);
}
```
