---
name: "DTT Lib"
short_name: "dttlib"
title: "Supported Date & Time Formats: ISO 8601, RFC 3339 & RFC 2822"
description: "Complete reference for all temporal formatting and parsing standards supported by DTT Lib."
keywords: "ISO 8601 rust, RFC 3339 rust, RFC 2822 formatting"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://dttlib.com/formats/index.html"
logo: "https://cloudcdn.pro/dtt/v1/logos/dtt.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "DTT Lib — Date, Time & Timezone Utilities for Rust"
---

# Supported Formats & Standards

<div class="table-responsive my-4">
<table class="table table-dark table-striped">
<thead>
<tr>
<th>Standard</th>
<th>Format String Pattern</th>
<th>Example Output</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ISO 8601 Extended</strong></td>
<td><code>YYYY-MM-DDTHH:MM:SS.ffffffZ</code></td>
<td><code>2026-09-01T20:45:00.123456Z</code></td>
</tr>
<tr>
<td><strong>RFC 3339 Profile</strong></td>
<td><code>YYYY-MM-DDTHH:MM:SS+00:00</code></td>
<td><code>2026-09-01T20:45:00+00:00</code></td>
</tr>
<tr>
<td><strong>RFC 2822 Email</strong></td>
<td><code>Day, DD Mon YYYY HH:MM:SS +0000</code></td>
<td><code>Tue, 01 Sep 2026 20:45:00 +0000</code></td>
</tr>
<tr>
<td><strong>Unix Epoch</strong></td>
<td><code>Seconds / Microseconds since 1970</code></td>
<td><code>1788295500</code></td>
</tr>
</tbody>
</table>
</div>
