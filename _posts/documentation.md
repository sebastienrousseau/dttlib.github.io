---
name: "DTT Lib"
short_name: "dttlib"
title: "API Reference & DateTime Struct Reference"
description: "Comprehensive Rust API documentation for DateTime, TimeZone, Date, and Time structs."
keywords: "dttlib API, rust datetime documentation"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://dttlib.com/documentation/index.html"
logo: "https://cloudcdn.pro/dtt/v1/logos/dtt.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "DTT Lib — Date, Time & Timezone Utilities for Rust"
---

# API Reference

## `struct DateTime`

```rust
pub struct DateTime {
    pub year: i32,
    pub month: u8,
    pub day: u8,
    pub hour: u8,
    pub minute: u8,
    pub second: u8,
    pub microsecond: u32,
    pub timestamp: i64,
    pub iso_8601: String,
}
```

### Methods
- `DateTime::new() -> DateTime`: Instantiates a `DateTime` with current UTC clock time.
- `DateTime::from_timestamp(i64) -> DateTime`: Construct `DateTime` from Unix epoch seconds.
- `dt.iso_8601() -> &str`: Returns ISO 8601 string representation.
- `dt.to_rfc3339() -> String`: Returns RFC 3339 formatted string.
