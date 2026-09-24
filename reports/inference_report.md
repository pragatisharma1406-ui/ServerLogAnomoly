# Threat Intelligence Report

Generated from 52,904 parsed log lines. Flagged windows: **184**.

## 192.0.2.38 — 2026-09-01 09:00:00+00:00

**Reason:** 12 unique URLs, avg payload 10772 bytes

**Features:** requests_per_minute=20, error_404_ratio=0.200, unique_urls=12, avg_payload_size=10771.850, post_share=0.150

**Exact log lines:**

```text
192.0.2.38 - - [01/Sep/2026:09:00:12 +0000] "GET /index.html HTTP/1.1" 200 8930 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:13 +0000] "GET /favicon.ico HTTP/1.1" 304 14194 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:14 +0000] "GET /static/style.css HTTP/1.1" 200 8179 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:15 +0000] "GET /contact HTTP/1.1" 200 14233 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:17 +0000] "GET /missing HTTP/1.1" 404 15425 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:19 +0000] "GET /contact HTTP/1.1" 200 7055 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:20 +0000] "GET /missing HTTP/1.1" 404 7555 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:22 +0000] "POST /api/items HTTP/1.1" 401 11337 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:25 +0000] "GET /static/style.css HTTP/1.1" 200 7699 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:26 +0000] "GET /static/app.js HTTP/1.1" 200 6394 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:31 +0000] "GET /api/items HTTP/1.1" 200 14915 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:32 +0000] "POST /api/search HTTP/1.1" 200 12001 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:33 +0000] "GET /about HTTP/1.1" 200 7017 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:33 +0000] "POST /api/items HTTP/1.1" 200 13538 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:35 +0000] "GET /does-not-exist HTTP/1.1" 404 8651 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:36 +0000] "GET /login HTTP/1.1" 200 7497 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:50 +0000] "GET /about HTTP/1.1" 200 12894 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:55 +0000] "GET /favicon.ico HTTP/1.1" 304 17938 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:58 +0000] "GET /missing HTTP/1.1" 404 2327 "-" "Mozilla/5.0"
192.0.2.38 - - [01/Sep/2026:09:00:58 +0000] "GET / HTTP/1.1" 200 17658 "-" "Mozilla/5.0"
```

## 192.0.2.45 — 2026-09-01 09:00:00+00:00

**Reason:** avg payload 12189 bytes

**Features:** requests_per_minute=3, error_404_ratio=0.667, unique_urls=2, avg_payload_size=12189.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.45 - - [01/Sep/2026:09:00:09 +0000] "GET /missing HTTP/1.1" 404 5951 "-" "Mozilla/5.0"
192.0.2.45 - - [01/Sep/2026:09:00:19 +0000] "GET /missing HTTP/1.1" 404 15890 "-" "Mozilla/5.0"
192.0.2.45 - - [01/Sep/2026:09:00:57 +0000] "GET /products/1 HTTP/1.1" 201 14726 "-" "Mozilla/5.0"
```

## 192.0.2.53 — 2026-09-01 09:01:00+00:00

**Reason:** 9 unique URLs

**Features:** requests_per_minute=20, error_404_ratio=0.350, unique_urls=9, avg_payload_size=7272.750, post_share=0.300

**Exact log lines:**

```text
192.0.2.53 - - [01/Sep/2026:09:01:07 +0000] "GET /login HTTP/1.1" 200 3771 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:07 +0000] "GET /about HTTP/1.1" 200 4463 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:11 +0000] "GET /does-not-exist HTTP/1.1" 404 1032 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:12 +0000] "GET /old-page HTTP/1.1" 404 15936 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:12 +0000] "POST /api/items HTTP/1.1" 404 16036 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:30 +0000] "GET /search?q=phone HTTP/1.1" 200 234 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:31 +0000] "POST /login HTTP/1.1" 404 748 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:33 +0000] "GET /products/1 HTTP/1.1" 200 7636 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:40 +0000] "POST /api/items HTTP/1.1" 304 8465 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:42 +0000] "POST /login HTTP/1.1" 404 5187 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:46 +0000] "GET /login HTTP/1.1" 201 14102 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:46 +0000] "GET /products HTTP/1.1" 200 14120 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:49 +0000] "GET /login HTTP/1.1" 403 7297 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:49 +0000] "GET /login HTTP/1.1" 301 14960 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:50 +0000] "GET /login HTTP/1.1" 201 5237 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:51 +0000] "GET /contact HTTP/1.1" 200 13360 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:51 +0000] "GET /does-not-exist HTTP/1.1" 404 383 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:52 +0000] "POST /api/items HTTP/1.1" 200 5666 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:53 +0000] "POST /login HTTP/1.1" 404 6123 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:01:59 +0000] "GET /about HTTP/1.1" 200 699 "-" "Mozilla/5.0"
```

## 192.0.2.17 — 2026-09-01 09:02:00+00:00

**Reason:** 100% POST share

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=3232.000, post_share=1.000

**Exact log lines:**

```text
192.0.2.17 - - [01/Sep/2026:09:02:17 +0000] "POST /api/search HTTP/1.1" 200 3232 "-" "Mozilla/5.0"
```

## 192.0.2.53 — 2026-09-01 09:03:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=2609.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.53 - - [01/Sep/2026:09:03:55 +0000] "GET / HTTP/1.1" 200 1632 "-" "Mozilla/5.0"
192.0.2.53 - - [01/Sep/2026:09:03:57 +0000] "GET /static/style.css HTTP/1.1" 200 3586 "-" "Mozilla/5.0"
```

## 192.0.2.29 — 2026-09-01 09:04:00+00:00

**Reason:** avg payload 13997 bytes

**Features:** requests_per_minute=4, error_404_ratio=0.500, unique_urls=4, avg_payload_size=13996.750, post_share=0.250

**Exact log lines:**

```text
192.0.2.29 - - [01/Sep/2026:09:04:02 +0000] "GET /old-page HTTP/1.1" 404 13273 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:09:04:06 +0000] "POST /api/search HTTP/1.1" 200 15140 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:09:04:20 +0000] "GET /does-not-exist HTTP/1.1" 404 9669 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:09:04:44 +0000] "GET /api/items HTTP/1.1" 200 17905 "-" "Mozilla/5.0"
```

## 192.0.2.44 — 2026-09-01 09:04:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=5738.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.44 - - [01/Sep/2026:09:04:06 +0000] "GET /products/1 HTTP/1.1" 200 4789 "-" "Mozilla/5.0"
192.0.2.44 - - [01/Sep/2026:09:04:12 +0000] "GET /old-page HTTP/1.1" 404 6688 "-" "Mozilla/5.0"
```

## 192.0.2.14 — 2026-09-01 09:05:00+00:00

**Reason:** 11 unique URLs

**Features:** requests_per_minute=17, error_404_ratio=0.176, unique_urls=11, avg_payload_size=5604.000, post_share=0.059

**Exact log lines:**

```text
192.0.2.14 - - [01/Sep/2026:09:05:04 +0000] "GET /search?q=phone HTTP/1.1" 200 11888 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:04 +0000] "GET /products/2 HTTP/1.1" 200 9987 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:07 +0000] "GET /old-page HTTP/1.1" 404 16816 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:10 +0000] "GET /api/items/1 HTTP/1.1" 200 2428 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:11 +0000] "GET /products/1 HTTP/1.1" 200 5753 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:14 +0000] "GET /api/items/1 HTTP/1.1" 403 2566 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:25 +0000] "GET / HTTP/1.1" 204 967 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:26 +0000] "GET /products HTTP/1.1" 304 243 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:27 +0000] "GET /login HTTP/1.1" 200 2584 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:31 +0000] "GET /products/2 HTTP/1.1" 200 11839 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:33 +0000] "GET /old-page HTTP/1.1" 404 3302 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:34 +0000] "POST /login HTTP/1.1" 200 14890 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:36 +0000] "GET /search?q=phone HTTP/1.1" 200 4295 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:38 +0000] "GET /login HTTP/1.1" 200 1156 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:40 +0000] "GET /about HTTP/1.1" 200 1575 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:48 +0000] "GET /does-not-exist HTTP/1.1" 404 2231 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:05:58 +0000] "GET /contact HTTP/1.1" 200 2748 "-" "Mozilla/5.0"
```

## 192.0.2.44 — 2026-09-01 09:05:00+00:00

**Reason:** avg payload 13820 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=13820.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.44 - - [01/Sep/2026:09:05:07 +0000] "GET /about HTTP/1.1" 403 11446 "-" "Mozilla/5.0"
192.0.2.44 - - [01/Sep/2026:09:05:09 +0000] "GET /missing HTTP/1.1" 404 16194 "-" "Mozilla/5.0"
```

## 192.0.2.39 — 2026-09-01 09:06:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=3, avg_payload_size=1657.667, post_share=0.000

**Exact log lines:**

```text
192.0.2.39 - - [01/Sep/2026:09:06:06 +0000] "GET /products HTTP/1.1" 200 2015 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:09:06:14 +0000] "GET / HTTP/1.1" 200 2452 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:09:06:25 +0000] "GET /login HTTP/1.1" 200 506 "-" "Mozilla/5.0"
```

## 192.0.2.34 — 2026-09-01 09:07:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.667, unique_urls=3, avg_payload_size=6156.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.34 - - [01/Sep/2026:09:07:27 +0000] "GET /contact HTTP/1.1" 200 3180 "-" "Mozilla/5.0"
192.0.2.34 - - [01/Sep/2026:09:07:38 +0000] "GET /old-page HTTP/1.1" 404 5941 "-" "Mozilla/5.0"
192.0.2.34 - - [01/Sep/2026:09:07:38 +0000] "GET /does-not-exist HTTP/1.1" 404 9347 "-" "Mozilla/5.0"
```

## 192.0.2.12 — 2026-09-01 09:08:00+00:00

**Reason:** 50% POST share, avg payload 15798 bytes

**Features:** requests_per_minute=4, error_404_ratio=0.250, unique_urls=4, avg_payload_size=15798.250, post_share=0.500

**Exact log lines:**

```text
192.0.2.12 - - [01/Sep/2026:09:08:13 +0000] "GET /static/app.js HTTP/1.1" 204 14910 "-" "Mozilla/5.0"
192.0.2.12 - - [01/Sep/2026:09:08:17 +0000] "GET /about HTTP/1.1" 304 17832 "-" "Mozilla/5.0"
192.0.2.12 - - [01/Sep/2026:09:08:22 +0000] "POST /login HTTP/1.1" 301 15801 "-" "Mozilla/5.0"
192.0.2.12 - - [01/Sep/2026:09:08:24 +0000] "POST /api/search HTTP/1.1" 404 14650 "-" "Mozilla/5.0"
```

## 192.0.2.23 — 2026-09-01 09:09:00+00:00

**Reason:** 11 unique URLs

**Features:** requests_per_minute=18, error_404_ratio=0.056, unique_urls=11, avg_payload_size=7614.278, post_share=0.222

**Exact log lines:**

```text
192.0.2.23 - - [01/Sep/2026:09:09:01 +0000] "GET / HTTP/1.1" 200 5935 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:06 +0000] "GET / HTTP/1.1" 200 14296 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:10 +0000] "GET /static/app.js HTTP/1.1" 200 12186 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:10 +0000] "GET /api/items HTTP/1.1" 200 12731 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:14 +0000] "GET /api/items HTTP/1.1" 200 9814 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:20 +0000] "GET /products/1 HTTP/1.1" 200 13591 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:38 +0000] "GET /index.html HTTP/1.1" 200 3930 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:39 +0000] "GET /index.html HTTP/1.1" 200 4120 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:40 +0000] "GET /api/items/1 HTTP/1.1" 200 2274 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:41 +0000] "GET /favicon.ico HTTP/1.1" 200 3127 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:43 +0000] "POST /api/items HTTP/1.1" 400 5711 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:44 +0000] "GET /about HTTP/1.1" 304 2652 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:47 +0000] "GET /login HTTP/1.1" 400 6993 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:51 +0000] "POST /api/search HTTP/1.1" 404 17665 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:54 +0000] "POST /api/search HTTP/1.1" 200 9380 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:56 +0000] "GET /login HTTP/1.1" 200 367 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:57 +0000] "POST /api/items HTTP/1.1" 200 6137 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:09:59 +0000] "GET /contact HTTP/1.1" 200 6148 "-" "Mozilla/5.0"
```

## 192.0.2.35 — 2026-09-01 09:09:00+00:00

**Reason:** avg payload 14951 bytes

**Features:** requests_per_minute=4, error_404_ratio=0.000, unique_urls=2, avg_payload_size=14950.750, post_share=0.000

**Exact log lines:**

```text
192.0.2.35 - - [01/Sep/2026:09:09:03 +0000] "GET /favicon.ico HTTP/1.1" 200 8852 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:09:10 +0000] "GET /favicon.ico HTTP/1.1" 200 16239 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:09:17 +0000] "GET /favicon.ico HTTP/1.1" 200 17081 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:09:36 +0000] "GET /about HTTP/1.1" 200 17631 "-" "Mozilla/5.0"
```

## 192.0.2.10 — 2026-09-01 09:10:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=2, avg_payload_size=3642.667, post_share=0.000

**Exact log lines:**

```text
192.0.2.10 - - [01/Sep/2026:09:10:17 +0000] "GET /api/items/1 HTTP/1.1" 200 7534 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:09:10:32 +0000] "GET /about HTTP/1.1" 301 1412 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:09:10:36 +0000] "GET /api/items/1 HTTP/1.1" 200 1982 "-" "Mozilla/5.0"
```

## 192.0.2.27 — 2026-09-01 09:10:00+00:00

**Reason:** avg payload 17375 bytes

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=17375.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.27 - - [01/Sep/2026:09:10:54 +0000] "GET / HTTP/1.1" 200 17375 "-" "Mozilla/5.0"
```

## 192.0.2.30 — 2026-09-01 09:10:00+00:00

**Reason:** 50% POST share, avg payload 13418 bytes

**Features:** requests_per_minute=6, error_404_ratio=0.167, unique_urls=3, avg_payload_size=13417.500, post_share=0.500

**Exact log lines:**

```text
192.0.2.30 - - [01/Sep/2026:09:10:07 +0000] "POST /api/items HTTP/1.1" 200 12660 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:09:10:20 +0000] "GET /login HTTP/1.1" 400 12552 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:09:10:31 +0000] "POST /login HTTP/1.1" 200 17249 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:09:10:35 +0000] "GET /static/style.css HTTP/1.1" 401 12353 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:09:10:49 +0000] "GET /static/style.css HTTP/1.1" 304 13372 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:09:10:57 +0000] "POST /api/items HTTP/1.1" 404 12319 "-" "Mozilla/5.0"
```

## 192.0.2.47 — 2026-09-01 09:10:00+00:00

**Reason:** avg payload 13318 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=13318.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.47 - - [01/Sep/2026:09:10:02 +0000] "GET /contact HTTP/1.1" 200 15029 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:09:10:28 +0000] "GET /favicon.ico HTTP/1.1" 200 11607 "-" "Mozilla/5.0"
```

## 192.0.2.25 — 2026-09-01 09:11:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.667, unique_urls=3, avg_payload_size=7010.667, post_share=0.000

**Exact log lines:**

```text
192.0.2.25 - - [01/Sep/2026:09:11:31 +0000] "GET / HTTP/1.1" 200 6581 "-" "Mozilla/5.0"
192.0.2.25 - - [01/Sep/2026:09:11:40 +0000] "GET /missing HTTP/1.1" 404 3797 "-" "Mozilla/5.0"
192.0.2.25 - - [01/Sep/2026:09:11:52 +0000] "GET /old-page HTTP/1.1" 404 10654 "-" "Mozilla/5.0"
```

## 192.0.2.40 — 2026-09-01 09:12:00+00:00

**Reason:** 50% POST share

**Features:** requests_per_minute=4, error_404_ratio=0.500, unique_urls=4, avg_payload_size=9039.750, post_share=0.500

**Exact log lines:**

```text
192.0.2.40 - - [01/Sep/2026:09:12:31 +0000] "POST /api/items HTTP/1.1" 404 7193 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:09:12:34 +0000] "GET /products/2 HTTP/1.1" 200 1523 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:09:12:42 +0000] "POST /api/search HTTP/1.1" 200 17232 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:09:12:44 +0000] "GET /old-page HTTP/1.1" 404 10211 "-" "Mozilla/5.0"
```

## 192.0.2.13 — 2026-09-01 09:13:00+00:00

**Reason:** avg payload 11606 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=11606.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.13 - - [01/Sep/2026:09:13:09 +0000] "GET /static/app.js HTTP/1.1" 200 8524 "-" "Mozilla/5.0"
192.0.2.13 - - [01/Sep/2026:09:13:41 +0000] "GET /old-page HTTP/1.1" 404 14689 "-" "Mozilla/5.0"
```

## 192.0.2.28 — 2026-09-01 09:13:00+00:00

**Reason:** avg payload 13495 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=13495.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.28 - - [01/Sep/2026:09:13:03 +0000] "GET /api/items HTTP/1.1" 204 14173 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:13:11 +0000] "GET /old-page HTTP/1.1" 404 12817 "-" "Mozilla/5.0"
```

## 192.0.2.30 — 2026-09-01 09:13:00+00:00

**Reason:** 100% 404 ratio

**Features:** requests_per_minute=4, error_404_ratio=1.000, unique_urls=3, avg_payload_size=8886.750, post_share=0.250

**Exact log lines:**

```text
192.0.2.30 - - [01/Sep/2026:09:13:42 +0000] "POST /api/search HTTP/1.1" 404 16682 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:09:13:45 +0000] "GET /does-not-exist HTTP/1.1" 404 15129 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:09:13:50 +0000] "GET /does-not-exist HTTP/1.1" 404 476 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:09:13:54 +0000] "GET /old-page HTTP/1.1" 404 3260 "-" "Mozilla/5.0"
```

## 192.0.2.25 — 2026-09-01 09:15:00+00:00

**Reason:** 50% POST share

**Features:** requests_per_minute=4, error_404_ratio=0.500, unique_urls=3, avg_payload_size=8776.000, post_share=0.500

**Exact log lines:**

```text
192.0.2.25 - - [01/Sep/2026:09:15:09 +0000] "GET / HTTP/1.1" 200 8634 "-" "Mozilla/5.0"
192.0.2.25 - - [01/Sep/2026:09:15:43 +0000] "POST /api/items HTTP/1.1" 404 3541 "-" "Mozilla/5.0"
192.0.2.25 - - [01/Sep/2026:09:15:47 +0000] "GET /old-page HTTP/1.1" 404 5108 "-" "Mozilla/5.0"
192.0.2.25 - - [01/Sep/2026:09:15:51 +0000] "POST /api/items HTTP/1.1" 200 17821 "-" "Mozilla/5.0"
```

## 192.0.2.29 — 2026-09-01 09:15:00+00:00

**Reason:** avg payload 15190 bytes

**Features:** requests_per_minute=4, error_404_ratio=0.500, unique_urls=2, avg_payload_size=15190.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.29 - - [01/Sep/2026:09:15:03 +0000] "GET /contact HTTP/1.1" 204 16365 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:09:15:31 +0000] "GET /contact HTTP/1.1" 304 17247 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:09:15:40 +0000] "GET /old-page HTTP/1.1" 404 17921 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:09:15:54 +0000] "GET /old-page HTTP/1.1" 404 9227 "-" "Mozilla/5.0"
```

## 192.0.2.30 — 2026-09-01 09:15:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=5, error_404_ratio=0.600, unique_urls=4, avg_payload_size=4296.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.30 - - [01/Sep/2026:09:15:16 +0000] "GET /missing HTTP/1.1" 404 3778 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:09:15:18 +0000] "GET /old-page HTTP/1.1" 404 2918 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:09:15:30 +0000] "GET /old-page HTTP/1.1" 404 7070 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:09:15:32 +0000] "GET /about HTTP/1.1" 200 7500 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:09:15:39 +0000] "GET /index.html HTTP/1.1" 200 214 "-" "Mozilla/5.0"
```

## 192.0.2.23 — 2026-09-01 09:17:00+00:00

**Reason:** 12 unique URLs, avg payload 11576 bytes

**Features:** requests_per_minute=15, error_404_ratio=0.267, unique_urls=12, avg_payload_size=11576.067, post_share=0.133

**Exact log lines:**

```text
192.0.2.23 - - [01/Sep/2026:09:17:00 +0000] "GET /login HTTP/1.1" 200 16973 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:02 +0000] "GET /favicon.ico HTTP/1.1" 401 6707 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:07 +0000] "GET /search?q=phone HTTP/1.1" 204 3351 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:12 +0000] "GET /contact HTTP/1.1" 200 16001 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:18 +0000] "GET /products HTTP/1.1" 200 17035 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:32 +0000] "GET /static/style.css HTTP/1.1" 304 11098 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:35 +0000] "GET / HTTP/1.1" 200 16681 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:39 +0000] "GET /static/style.css HTTP/1.1" 201 16542 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:45 +0000] "GET /search?q=phone HTTP/1.1" 200 4547 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:46 +0000] "POST /api/items HTTP/1.1" 400 17778 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:48 +0000] "GET /missing HTTP/1.1" 404 9647 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:50 +0000] "GET /does-not-exist HTTP/1.1" 404 11009 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:53 +0000] "POST /login HTTP/1.1" 404 5408 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:54 +0000] "GET /index.html HTTP/1.1" 200 3833 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:17:56 +0000] "GET /old-page HTTP/1.1" 404 17031 "-" "Mozilla/5.0"
```

## 192.0.2.47 — 2026-09-01 09:19:00+00:00

**Reason:** 57% POST share, avg payload 10450 bytes

**Features:** requests_per_minute=7, error_404_ratio=0.429, unique_urls=5, avg_payload_size=10450.000, post_share=0.571

**Exact log lines:**

```text
192.0.2.47 - - [01/Sep/2026:09:19:15 +0000] "POST /api/items HTTP/1.1" 200 10381 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:09:19:32 +0000] "POST /login HTTP/1.1" 200 4614 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:09:19:34 +0000] "POST /login HTTP/1.1" 404 17089 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:09:19:46 +0000] "POST /login HTTP/1.1" 200 10991 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:09:19:47 +0000] "GET /missing HTTP/1.1" 404 5725 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:09:19:48 +0000] "GET /old-page HTTP/1.1" 404 12363 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:09:19:53 +0000] "GET /api/items/1 HTTP/1.1" 201 11987 "-" "Mozilla/5.0"
```

## 192.0.2.58 — 2026-09-01 09:19:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=3, avg_payload_size=3285.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.58 - - [01/Sep/2026:09:19:02 +0000] "GET /products/2 HTTP/1.1" 401 1535 "-" "Mozilla/5.0"
192.0.2.58 - - [01/Sep/2026:09:19:27 +0000] "GET /api/items/1 HTTP/1.1" 200 7382 "-" "Mozilla/5.0"
192.0.2.58 - - [01/Sep/2026:09:19:37 +0000] "GET /products HTTP/1.1" 200 938 "-" "Mozilla/5.0"
```

## 192.0.2.50 — 2026-09-01 09:21:00+00:00

**Reason:** 100% 404 ratio

**Features:** requests_per_minute=2, error_404_ratio=1.000, unique_urls=2, avg_payload_size=8392.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.50 - - [01/Sep/2026:09:21:03 +0000] "GET /old-page HTTP/1.1" 404 2398 "-" "Mozilla/5.0"
192.0.2.50 - - [01/Sep/2026:09:21:56 +0000] "GET /does-not-exist HTTP/1.1" 404 14386 "-" "Mozilla/5.0"
```

## 192.0.2.20 — 2026-09-01 09:22:00+00:00

**Reason:** 12 unique URLs

**Features:** requests_per_minute=13, error_404_ratio=0.231, unique_urls=12, avg_payload_size=5592.231, post_share=0.308

**Exact log lines:**

```text
192.0.2.20 - - [01/Sep/2026:09:22:09 +0000] "POST /login HTTP/1.1" 200 5297 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:22:18 +0000] "GET /static/app.js HTTP/1.1" 200 2515 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:22:21 +0000] "GET / HTTP/1.1" 200 714 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:22:23 +0000] "POST /login HTTP/1.1" 404 4692 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:22:28 +0000] "GET /products HTTP/1.1" 400 5888 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:22:37 +0000] "POST /api/search HTTP/1.1" 200 2830 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:22:41 +0000] "POST /api/items HTTP/1.1" 200 7619 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:22:46 +0000] "GET /api/items/1 HTTP/1.1" 204 610 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:22:49 +0000] "GET /products/1 HTTP/1.1" 301 1607 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:22:50 +0000] "GET /missing HTTP/1.1" 404 14106 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:22:53 +0000] "GET /old-page HTTP/1.1" 404 2623 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:22:54 +0000] "GET /static/style.css HTTP/1.1" 200 17714 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:22:55 +0000] "GET /about HTTP/1.1" 200 6484 "-" "Mozilla/5.0"
```

## 192.0.2.35 — 2026-09-01 09:22:00+00:00

**Reason:** 12 unique URLs

**Features:** requests_per_minute=15, error_404_ratio=0.400, unique_urls=12, avg_payload_size=7587.533, post_share=0.200

**Exact log lines:**

```text
192.0.2.35 - - [01/Sep/2026:09:22:01 +0000] "GET /old-page HTTP/1.1" 404 3778 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:06 +0000] "GET /products/2 HTTP/1.1" 304 5835 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:08 +0000] "GET /products/1 HTTP/1.1" 304 330 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:11 +0000] "GET /missing HTTP/1.1" 404 6998 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:14 +0000] "GET / HTTP/1.1" 304 14436 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:15 +0000] "GET /static/style.css HTTP/1.1" 200 13334 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:17 +0000] "POST /api/search HTTP/1.1" 200 2115 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:28 +0000] "GET /static/style.css HTTP/1.1" 304 2143 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:38 +0000] "GET /favicon.ico HTTP/1.1" 200 2409 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:38 +0000] "POST /login HTTP/1.1" 404 3622 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:50 +0000] "GET /does-not-exist HTTP/1.1" 404 8720 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:51 +0000] "POST /api/items HTTP/1.1" 404 15224 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:54 +0000] "GET /api/items HTTP/1.1" 200 16255 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:59 +0000] "GET /does-not-exist HTTP/1.1" 404 9511 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:22:59 +0000] "GET /about HTTP/1.1" 200 9103 "-" "Mozilla/5.0"
```

## 192.0.2.33 — 2026-09-01 09:23:00+00:00

**Reason:** avg payload 13473 bytes

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=3, avg_payload_size=13472.667, post_share=0.333

**Exact log lines:**

```text
192.0.2.33 - - [01/Sep/2026:09:23:06 +0000] "GET /static/app.js HTTP/1.1" 403 17696 "-" "Mozilla/5.0"
192.0.2.33 - - [01/Sep/2026:09:23:14 +0000] "POST /api/search HTTP/1.1" 500 5092 "-" "Mozilla/5.0"
192.0.2.33 - - [01/Sep/2026:09:23:19 +0000] "GET /products/1 HTTP/1.1" 200 17630 "-" "Mozilla/5.0"
```

## 192.0.2.57 — 2026-09-01 09:23:00+00:00

**Reason:** 50% POST share

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=6709.000, post_share=0.500

**Exact log lines:**

```text
192.0.2.57 - - [01/Sep/2026:09:23:06 +0000] "POST /api/search HTTP/1.1" 200 195 "-" "Mozilla/5.0"
192.0.2.57 - - [01/Sep/2026:09:23:08 +0000] "GET /index.html HTTP/1.1" 200 13223 "-" "Mozilla/5.0"
```

## 192.0.2.59 — 2026-09-01 09:23:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=3, avg_payload_size=5890.000, post_share=0.333

**Exact log lines:**

```text
192.0.2.59 - - [01/Sep/2026:09:23:18 +0000] "POST /api/search HTTP/1.1" 204 1377 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:09:23:27 +0000] "GET /contact HTTP/1.1" 304 15777 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:09:23:53 +0000] "GET /login HTTP/1.1" 200 516 "-" "Mozilla/5.0"
```

## 192.0.2.45 — 2026-09-01 09:24:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=4, error_404_ratio=0.500, unique_urls=3, avg_payload_size=2950.000, post_share=0.250

**Exact log lines:**

```text
192.0.2.45 - - [01/Sep/2026:09:24:17 +0000] "GET /old-page HTTP/1.1" 404 5619 "-" "Mozilla/5.0"
192.0.2.45 - - [01/Sep/2026:09:24:29 +0000] "GET /old-page HTTP/1.1" 404 1752 "-" "Mozilla/5.0"
192.0.2.45 - - [01/Sep/2026:09:24:35 +0000] "GET / HTTP/1.1" 200 2876 "-" "Mozilla/5.0"
192.0.2.45 - - [01/Sep/2026:09:24:53 +0000] "POST /login HTTP/1.1" 200 1553 "-" "Mozilla/5.0"
```

## 192.0.2.17 — 2026-09-01 09:25:00+00:00

**Reason:** avg payload 13776 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=13776.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.17 - - [01/Sep/2026:09:25:16 +0000] "GET /static/app.js HTTP/1.1" 200 12680 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:25:41 +0000] "GET /products HTTP/1.1" 200 14872 "-" "Mozilla/5.0"
```

## 192.0.2.54 — 2026-09-01 09:25:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=2717.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.54 - - [01/Sep/2026:09:25:30 +0000] "GET /api/items/1 HTTP/1.1" 200 2827 "-" "Mozilla/5.0"
192.0.2.54 - - [01/Sep/2026:09:25:44 +0000] "GET /products/2 HTTP/1.1" 200 2608 "-" "Mozilla/5.0"
```

## 192.0.2.10 — 2026-09-01 09:26:00+00:00

**Reason:** 80% 404 ratio

**Features:** requests_per_minute=5, error_404_ratio=0.800, unique_urls=5, avg_payload_size=7714.600, post_share=0.400

**Exact log lines:**

```text
192.0.2.10 - - [01/Sep/2026:09:26:13 +0000] "POST /api/items HTTP/1.1" 404 13335 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:09:26:16 +0000] "GET /does-not-exist HTTP/1.1" 404 5336 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:09:26:24 +0000] "GET /about HTTP/1.1" 200 16218 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:09:26:27 +0000] "POST /api/search HTTP/1.1" 404 2858 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:09:26:50 +0000] "GET /old-page HTTP/1.1" 404 826 "-" "Mozilla/5.0"
```

## 192.0.2.18 — 2026-09-01 09:26:00+00:00

**Reason:** 100% 404 ratio

**Features:** requests_per_minute=2, error_404_ratio=1.000, unique_urls=2, avg_payload_size=7744.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.18 - - [01/Sep/2026:09:26:42 +0000] "GET /missing HTTP/1.1" 404 14359 "-" "Mozilla/5.0"
192.0.2.18 - - [01/Sep/2026:09:26:59 +0000] "GET /does-not-exist HTTP/1.1" 404 1129 "-" "Mozilla/5.0"
```

## 192.0.2.19 — 2026-09-01 09:26:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=3, avg_payload_size=2903.000, post_share=0.333

**Exact log lines:**

```text
192.0.2.19 - - [01/Sep/2026:09:26:21 +0000] "GET /does-not-exist HTTP/1.1" 404 2943 "-" "Mozilla/5.0"
192.0.2.19 - - [01/Sep/2026:09:26:32 +0000] "POST /api/search HTTP/1.1" 200 1792 "-" "Mozilla/5.0"
192.0.2.19 - - [01/Sep/2026:09:26:34 +0000] "GET /login HTTP/1.1" 304 3974 "-" "Mozilla/5.0"
```

## 192.0.2.57 — 2026-09-01 09:26:00+00:00

**Reason:** avg payload 13320 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=13320.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.57 - - [01/Sep/2026:09:26:10 +0000] "GET /products HTTP/1.1" 200 9480 "-" "Mozilla/5.0"
192.0.2.57 - - [01/Sep/2026:09:26:58 +0000] "GET /contact HTTP/1.1" 304 17161 "-" "Mozilla/5.0"
```

## 192.0.2.42 — 2026-09-01 09:27:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=3, avg_payload_size=2581.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.42 - - [01/Sep/2026:09:27:18 +0000] "GET /products/1 HTTP/1.1" 200 1330 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:09:27:26 +0000] "GET /static/style.css HTTP/1.1" 204 1533 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:09:27:42 +0000] "GET /old-page HTTP/1.1" 404 4880 "-" "Mozilla/5.0"
```

## 192.0.2.20 — 2026-09-01 09:28:00+00:00

**Reason:** 50% POST share, avg payload 14177 bytes

**Features:** requests_per_minute=4, error_404_ratio=0.250, unique_urls=3, avg_payload_size=14176.750, post_share=0.500

**Exact log lines:**

```text
192.0.2.20 - - [01/Sep/2026:09:28:06 +0000] "POST /api/search HTTP/1.1" 200 12088 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:28:19 +0000] "GET /products HTTP/1.1" 200 13434 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:28:26 +0000] "GET / HTTP/1.1" 200 16763 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:09:28:37 +0000] "POST /api/search HTTP/1.1" 404 14422 "-" "Mozilla/5.0"
```

## 192.0.2.13 — 2026-09-01 09:30:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=2838.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.13 - - [01/Sep/2026:09:30:36 +0000] "GET / HTTP/1.1" 301 2838 "-" "Mozilla/5.0"
```

## 198.51.100.10 — 2026-09-01 09:30:00+00:00

**Reason:** 100% 404 ratio, 240 requests/min

**Features:** requests_per_minute=240, error_404_ratio=1.000, unique_urls=3, avg_payload_size=270.104, post_share=0.000

**Exact log lines:**

```text
198.51.100.10 - - [01/Sep/2026:09:30:00 +0000] "GET /missing/a HTTP/1.1" 404 203 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:00 +0000] "GET /missing/c HTTP/1.1" 404 52 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:00 +0000] "GET /missing/c HTTP/1.1" 404 89 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:00 +0000] "GET /missing/c HTTP/1.1" 404 228 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:01 +0000] "GET /missing/a HTTP/1.1" 404 109 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:01 +0000] "GET /missing/b HTTP/1.1" 404 137 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:01 +0000] "GET /missing/b HTTP/1.1" 404 270 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:01 +0000] "GET /missing/c HTTP/1.1" 404 406 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:02 +0000] "GET /missing/a HTTP/1.1" 404 92 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:02 +0000] "GET /missing/a HTTP/1.1" 404 164 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:02 +0000] "GET /missing/c HTTP/1.1" 404 296 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:02 +0000] "GET /missing/c HTTP/1.1" 404 326 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:03 +0000] "GET /missing/b HTTP/1.1" 404 226 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:03 +0000] "GET /missing/c HTTP/1.1" 404 173 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:03 +0000] "GET /missing/c HTTP/1.1" 404 414 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:03 +0000] "GET /missing/c HTTP/1.1" 404 428 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:04 +0000] "GET /missing/a HTTP/1.1" 404 379 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:04 +0000] "GET /missing/b HTTP/1.1" 404 249 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:04 +0000] "GET /missing/b HTTP/1.1" 404 470 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:04 +0000] "GET /missing/c HTTP/1.1" 404 221 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:05 +0000] "GET /missing/a HTTP/1.1" 404 89 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:05 +0000] "GET /missing/a HTTP/1.1" 404 96 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:05 +0000] "GET /missing/c HTTP/1.1" 404 392 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:05 +0000] "GET /missing/c HTTP/1.1" 404 392 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:06 +0000] "GET /missing/a HTTP/1.1" 404 130 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:06 +0000] "GET /missing/a HTTP/1.1" 404 358 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:06 +0000] "GET /missing/b HTTP/1.1" 404 133 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:06 +0000] "GET /missing/c HTTP/1.1" 404 375 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:07 +0000] "GET /missing/a HTTP/1.1" 404 320 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:07 +0000] "GET /missing/a HTTP/1.1" 404 483 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:07 +0000] "GET /missing/b HTTP/1.1" 404 378 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:07 +0000] "GET /missing/c HTTP/1.1" 404 449 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:08 +0000] "GET /missing/a HTTP/1.1" 404 155 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:08 +0000] "GET /missing/c HTTP/1.1" 404 129 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:08 +0000] "GET /missing/c HTTP/1.1" 404 212 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:08 +0000] "GET /missing/c HTTP/1.1" 404 448 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:09 +0000] "GET /missing/a HTTP/1.1" 404 72 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:09 +0000] "GET /missing/b HTTP/1.1" 404 199 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:09 +0000] "GET /missing/b HTTP/1.1" 404 209 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:09 +0000] "GET /missing/b HTTP/1.1" 404 412 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:10 +0000] "GET /missing/a HTTP/1.1" 404 321 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:10 +0000] "GET /missing/a HTTP/1.1" 404 349 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:10 +0000] "GET /missing/b HTTP/1.1" 404 477 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:10 +0000] "GET /missing/c HTTP/1.1" 404 254 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:11 +0000] "GET /missing/b HTTP/1.1" 404 303 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:11 +0000] "GET /missing/c HTTP/1.1" 404 112 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:11 +0000] "GET /missing/c HTTP/1.1" 404 239 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:11 +0000] "GET /missing/c HTTP/1.1" 404 382 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:12 +0000] "GET /missing/a HTTP/1.1" 404 185 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:12 +0000] "GET /missing/b HTTP/1.1" 404 113 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:12 +0000] "GET /missing/b HTTP/1.1" 404 131 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:12 +0000] "GET /missing/b HTTP/1.1" 404 139 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:13 +0000] "GET /missing/a HTTP/1.1" 404 459 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:13 +0000] "GET /missing/b HTTP/1.1" 404 448 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:13 +0000] "GET /missing/c HTTP/1.1" 404 60 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:13 +0000] "GET /missing/c HTTP/1.1" 404 395 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:14 +0000] "GET /missing/a HTTP/1.1" 404 354 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:14 +0000] "GET /missing/a HTTP/1.1" 404 366 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:14 +0000] "GET /missing/b HTTP/1.1" 404 323 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:14 +0000] "GET /missing/b HTTP/1.1" 404 396 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:15 +0000] "GET /missing/a HTTP/1.1" 404 65 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:15 +0000] "GET /missing/a HTTP/1.1" 404 80 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:15 +0000] "GET /missing/c HTTP/1.1" 404 92 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:15 +0000] "GET /missing/c HTTP/1.1" 404 377 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:16 +0000] "GET /missing/a HTTP/1.1" 404 130 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:16 +0000] "GET /missing/a HTTP/1.1" 404 187 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:16 +0000] "GET /missing/b HTTP/1.1" 404 56 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:16 +0000] "GET /missing/c HTTP/1.1" 404 130 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:17 +0000] "GET /missing/a HTTP/1.1" 404 395 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:17 +0000] "GET /missing/b HTTP/1.1" 404 431 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:17 +0000] "GET /missing/c HTTP/1.1" 404 149 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:17 +0000] "GET /missing/c HTTP/1.1" 404 336 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:18 +0000] "GET /missing/a HTTP/1.1" 404 118 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:18 +0000] "GET /missing/b HTTP/1.1" 404 223 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:18 +0000] "GET /missing/b HTTP/1.1" 404 480 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:18 +0000] "GET /missing/c HTTP/1.1" 404 270 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:19 +0000] "GET /missing/a HTTP/1.1" 404 348 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:19 +0000] "GET /missing/b HTTP/1.1" 404 439 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:19 +0000] "GET /missing/b HTTP/1.1" 404 447 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:19 +0000] "GET /missing/c HTTP/1.1" 404 144 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:20 +0000] "GET /missing/b HTTP/1.1" 404 167 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:20 +0000] "GET /missing/c HTTP/1.1" 404 133 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:20 +0000] "GET /missing/c HTTP/1.1" 404 319 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:20 +0000] "GET /missing/c HTTP/1.1" 404 361 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:21 +0000] "GET /missing/a HTTP/1.1" 404 266 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:21 +0000] "GET /missing/b HTTP/1.1" 404 181 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:21 +0000] "GET /missing/b HTTP/1.1" 404 356 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:21 +0000] "GET /missing/c HTTP/1.1" 404 326 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:22 +0000] "GET /missing/a HTTP/1.1" 404 123 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:22 +0000] "GET /missing/a HTTP/1.1" 404 351 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:22 +0000] "GET /missing/b HTTP/1.1" 404 341 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:22 +0000] "GET /missing/c HTTP/1.1" 404 488 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:23 +0000] "GET /missing/a HTTP/1.1" 404 159 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:23 +0000] "GET /missing/a HTTP/1.1" 404 473 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:23 +0000] "GET /missing/c HTTP/1.1" 404 50 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:23 +0000] "GET /missing/c HTTP/1.1" 404 297 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:24 +0000] "GET /missing/a HTTP/1.1" 404 216 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:24 +0000] "GET /missing/a HTTP/1.1" 404 282 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:24 +0000] "GET /missing/a HTTP/1.1" 404 310 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:24 +0000] "GET /missing/b HTTP/1.1" 404 185 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:25 +0000] "GET /missing/b HTTP/1.1" 404 196 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:25 +0000] "GET /missing/b HTTP/1.1" 404 284 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:25 +0000] "GET /missing/c HTTP/1.1" 404 150 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:25 +0000] "GET /missing/c HTTP/1.1" 404 381 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:26 +0000] "GET /missing/a HTTP/1.1" 404 81 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:26 +0000] "GET /missing/a HTTP/1.1" 404 120 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:26 +0000] "GET /missing/b HTTP/1.1" 404 234 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:26 +0000] "GET /missing/b HTTP/1.1" 404 383 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:27 +0000] "GET /missing/a HTTP/1.1" 404 85 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:27 +0000] "GET /missing/a HTTP/1.1" 404 346 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:27 +0000] "GET /missing/b HTTP/1.1" 404 489 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:27 +0000] "GET /missing/c HTTP/1.1" 404 164 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:28 +0000] "GET /missing/a HTTP/1.1" 404 92 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:28 +0000] "GET /missing/a HTTP/1.1" 404 371 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:28 +0000] "GET /missing/b HTTP/1.1" 404 58 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:28 +0000] "GET /missing/c HTTP/1.1" 404 67 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:29 +0000] "GET /missing/a HTTP/1.1" 404 92 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:29 +0000] "GET /missing/b HTTP/1.1" 404 136 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:29 +0000] "GET /missing/c HTTP/1.1" 404 92 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:29 +0000] "GET /missing/c HTTP/1.1" 404 225 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:30 +0000] "GET /missing/a HTTP/1.1" 404 273 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:30 +0000] "GET /missing/a HTTP/1.1" 404 416 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:30 +0000] "GET /missing/c HTTP/1.1" 404 205 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:30 +0000] "GET /missing/c HTTP/1.1" 404 462 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:31 +0000] "GET /missing/a HTTP/1.1" 404 229 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:31 +0000] "GET /missing/b HTTP/1.1" 404 87 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:31 +0000] "GET /missing/b HTTP/1.1" 404 463 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:31 +0000] "GET /missing/c HTTP/1.1" 404 489 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:32 +0000] "GET /missing/a HTTP/1.1" 404 182 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:32 +0000] "GET /missing/a HTTP/1.1" 404 292 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:32 +0000] "GET /missing/c HTTP/1.1" 404 130 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:32 +0000] "GET /missing/c HTTP/1.1" 404 196 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:33 +0000] "GET /missing/a HTTP/1.1" 404 52 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:33 +0000] "GET /missing/a HTTP/1.1" 404 289 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:33 +0000] "GET /missing/b HTTP/1.1" 404 235 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:33 +0000] "GET /missing/c HTTP/1.1" 404 332 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:34 +0000] "GET /missing/a HTTP/1.1" 404 99 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:34 +0000] "GET /missing/a HTTP/1.1" 404 121 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:34 +0000] "GET /missing/b HTTP/1.1" 404 205 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:34 +0000] "GET /missing/c HTTP/1.1" 404 165 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:35 +0000] "GET /missing/a HTTP/1.1" 404 377 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:35 +0000] "GET /missing/b HTTP/1.1" 404 325 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:35 +0000] "GET /missing/b HTTP/1.1" 404 468 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:35 +0000] "GET /missing/c HTTP/1.1" 404 314 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:36 +0000] "GET /missing/a HTTP/1.1" 404 111 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:36 +0000] "GET /missing/b HTTP/1.1" 404 295 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:36 +0000] "GET /missing/b HTTP/1.1" 404 304 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:36 +0000] "GET /missing/c HTTP/1.1" 404 419 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:37 +0000] "GET /missing/a HTTP/1.1" 404 434 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:37 +0000] "GET /missing/b HTTP/1.1" 404 441 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:37 +0000] "GET /missing/c HTTP/1.1" 404 150 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:37 +0000] "GET /missing/c HTTP/1.1" 404 460 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:38 +0000] "GET /missing/a HTTP/1.1" 404 361 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:38 +0000] "GET /missing/b HTTP/1.1" 404 368 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:38 +0000] "GET /missing/b HTTP/1.1" 404 415 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:38 +0000] "GET /missing/c HTTP/1.1" 404 466 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:39 +0000] "GET /missing/a HTTP/1.1" 404 219 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:39 +0000] "GET /missing/b HTTP/1.1" 404 344 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:39 +0000] "GET /missing/c HTTP/1.1" 404 60 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:39 +0000] "GET /missing/c HTTP/1.1" 404 437 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:40 +0000] "GET /missing/b HTTP/1.1" 404 282 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:40 +0000] "GET /missing/c HTTP/1.1" 404 213 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:40 +0000] "GET /missing/c HTTP/1.1" 404 272 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:40 +0000] "GET /missing/c HTTP/1.1" 404 396 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:41 +0000] "GET /missing/a HTTP/1.1" 404 249 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:41 +0000] "GET /missing/a HTTP/1.1" 404 330 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:41 +0000] "GET /missing/b HTTP/1.1" 404 68 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:41 +0000] "GET /missing/b HTTP/1.1" 404 134 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:42 +0000] "GET /missing/a HTTP/1.1" 404 384 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:42 +0000] "GET /missing/a HTTP/1.1" 404 437 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:42 +0000] "GET /missing/c HTTP/1.1" 404 380 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:42 +0000] "GET /missing/c HTTP/1.1" 404 392 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:43 +0000] "GET /missing/a HTTP/1.1" 404 75 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:43 +0000] "GET /missing/a HTTP/1.1" 404 456 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:43 +0000] "GET /missing/b HTTP/1.1" 404 248 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:43 +0000] "GET /missing/c HTTP/1.1" 404 454 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:44 +0000] "GET /missing/a HTTP/1.1" 404 190 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:44 +0000] "GET /missing/b HTTP/1.1" 404 187 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:44 +0000] "GET /missing/b HTTP/1.1" 404 445 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:44 +0000] "GET /missing/c HTTP/1.1" 404 467 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:45 +0000] "GET /missing/a HTTP/1.1" 404 253 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:45 +0000] "GET /missing/a HTTP/1.1" 404 319 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:45 +0000] "GET /missing/b HTTP/1.1" 404 125 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:45 +0000] "GET /missing/c HTTP/1.1" 404 253 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:46 +0000] "GET /missing/b HTTP/1.1" 404 395 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:46 +0000] "GET /missing/b HTTP/1.1" 404 427 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:46 +0000] "GET /missing/b HTTP/1.1" 404 433 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:46 +0000] "GET /missing/b HTTP/1.1" 404 454 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:47 +0000] "GET /missing/b HTTP/1.1" 404 55 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:47 +0000] "GET /missing/c HTTP/1.1" 404 277 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:47 +0000] "GET /missing/c HTTP/1.1" 404 463 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:47 +0000] "GET /missing/c HTTP/1.1" 404 474 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:48 +0000] "GET /missing/b HTTP/1.1" 404 421 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:48 +0000] "GET /missing/b HTTP/1.1" 404 458 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:48 +0000] "GET /missing/c HTTP/1.1" 404 245 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:48 +0000] "GET /missing/c HTTP/1.1" 404 300 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:49 +0000] "GET /missing/a HTTP/1.1" 404 206 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:49 +0000] "GET /missing/a HTTP/1.1" 404 324 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:49 +0000] "GET /missing/a HTTP/1.1" 404 455 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:49 +0000] "GET /missing/c HTTP/1.1" 404 87 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:50 +0000] "GET /missing/a HTTP/1.1" 404 222 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:50 +0000] "GET /missing/b HTTP/1.1" 404 249 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:50 +0000] "GET /missing/c HTTP/1.1" 404 142 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:50 +0000] "GET /missing/c HTTP/1.1" 404 266 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:51 +0000] "GET /missing/a HTTP/1.1" 404 283 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:51 +0000] "GET /missing/a HTTP/1.1" 404 362 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:51 +0000] "GET /missing/a HTTP/1.1" 404 470 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:51 +0000] "GET /missing/c HTTP/1.1" 404 426 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:52 +0000] "GET /missing/a HTTP/1.1" 404 216 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:52 +0000] "GET /missing/b HTTP/1.1" 404 110 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:52 +0000] "GET /missing/b HTTP/1.1" 404 460 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:52 +0000] "GET /missing/c HTTP/1.1" 404 79 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:53 +0000] "GET /missing/a HTTP/1.1" 404 315 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:53 +0000] "GET /missing/b HTTP/1.1" 404 120 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:53 +0000] "GET /missing/b HTTP/1.1" 404 222 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:53 +0000] "GET /missing/b HTTP/1.1" 404 400 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:54 +0000] "GET /missing/a HTTP/1.1" 404 110 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:54 +0000] "GET /missing/a HTTP/1.1" 404 187 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:54 +0000] "GET /missing/b HTTP/1.1" 404 251 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:54 +0000] "GET /missing/b HTTP/1.1" 404 448 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:55 +0000] "GET /missing/a HTTP/1.1" 404 144 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:55 +0000] "GET /missing/a HTTP/1.1" 404 208 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:55 +0000] "GET /missing/c HTTP/1.1" 404 79 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:55 +0000] "GET /missing/c HTTP/1.1" 404 124 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:56 +0000] "GET /missing/a HTTP/1.1" 404 165 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:56 +0000] "GET /missing/b HTTP/1.1" 404 405 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:56 +0000] "GET /missing/c HTTP/1.1" 404 161 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:56 +0000] "GET /missing/c HTTP/1.1" 404 341 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:57 +0000] "GET /missing/a HTTP/1.1" 404 130 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:57 +0000] "GET /missing/a HTTP/1.1" 404 298 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:57 +0000] "GET /missing/a HTTP/1.1" 404 447 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:57 +0000] "GET /missing/b HTTP/1.1" 404 246 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:58 +0000] "GET /missing/a HTTP/1.1" 404 82 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:58 +0000] "GET /missing/a HTTP/1.1" 404 260 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:58 +0000] "GET /missing/b HTTP/1.1" 404 83 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:58 +0000] "GET /missing/b HTTP/1.1" 404 248 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:59 +0000] "GET /missing/a HTTP/1.1" 404 340 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:59 +0000] "GET /missing/b HTTP/1.1" 404 368 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:59 +0000] "GET /missing/b HTTP/1.1" 404 390 "-" "Mozilla/5.0"
198.51.100.10 - - [01/Sep/2026:09:30:59 +0000] "GET /missing/c HTTP/1.1" 404 299 "-" "Mozilla/5.0"
```

## 192.0.2.25 — 2026-09-01 09:31:00+00:00

**Reason:** 100% 404 ratio, avg payload 13509 bytes

**Features:** requests_per_minute=1, error_404_ratio=1.000, unique_urls=1, avg_payload_size=13509.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.25 - - [01/Sep/2026:09:31:45 +0000] "GET /old-page HTTP/1.1" 404 13509 "-" "Mozilla/5.0"
```

## 192.0.2.28 — 2026-09-01 09:31:00+00:00

**Reason:** 10 unique URLs, avg payload 10002 bytes

**Features:** requests_per_minute=15, error_404_ratio=0.000, unique_urls=10, avg_payload_size=10001.533, post_share=0.400

**Exact log lines:**

```text
192.0.2.28 - - [01/Sep/2026:09:31:05 +0000] "POST /api/items HTTP/1.1" 200 2614 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:06 +0000] "GET /products HTTP/1.1" 200 14268 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:07 +0000] "POST /api/search HTTP/1.1" 200 10777 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:13 +0000] "POST /api/items HTTP/1.1" 200 11077 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:14 +0000] "GET /search?q=phone HTTP/1.1" 200 7983 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:19 +0000] "POST /api/items HTTP/1.1" 204 1027 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:22 +0000] "POST /login HTTP/1.1" 200 11167 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:26 +0000] "GET /static/app.js HTTP/1.1" 200 16577 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:29 +0000] "POST /api/search HTTP/1.1" 400 13626 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:31 +0000] "GET /products/2 HTTP/1.1" 200 1537 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:39 +0000] "GET /index.html HTTP/1.1" 200 9356 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:43 +0000] "GET /products HTTP/1.1" 301 14011 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:49 +0000] "GET /api/items/1 HTTP/1.1" 400 13140 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:51 +0000] "GET /contact HTTP/1.1" 200 10072 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:31:53 +0000] "GET /products HTTP/1.1" 200 12791 "-" "Mozilla/5.0"
```

## 192.0.2.42 — 2026-09-01 09:32:00+00:00

**Reason:** 9 unique URLs, 50% POST share, avg payload 10786 bytes

**Features:** requests_per_minute=12, error_404_ratio=0.333, unique_urls=9, avg_payload_size=10785.667, post_share=0.500

**Exact log lines:**

```text
192.0.2.42 - - [01/Sep/2026:09:32:01 +0000] "GET /contact HTTP/1.1" 200 5723 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:09:32:06 +0000] "GET /search?q=phone HTTP/1.1" 200 16912 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:09:32:08 +0000] "POST /api/items HTTP/1.1" 404 13527 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:09:32:16 +0000] "POST /login HTTP/1.1" 200 14465 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:09:32:28 +0000] "GET /favicon.ico HTTP/1.1" 200 15964 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:09:32:29 +0000] "POST /api/items HTTP/1.1" 404 4078 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:09:32:29 +0000] "POST /api/items HTTP/1.1" 200 11423 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:09:32:33 +0000] "POST /api/search HTTP/1.1" 404 12675 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:09:32:46 +0000] "POST /api/items HTTP/1.1" 200 8926 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:09:32:47 +0000] "GET /products/1 HTTP/1.1" 200 8872 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:09:32:47 +0000] "GET /old-page HTTP/1.1" 404 5578 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:09:32:50 +0000] "GET /static/app.js HTTP/1.1" 200 11285 "-" "Mozilla/5.0"
```

## 192.0.2.32 — 2026-09-01 09:33:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=3, avg_payload_size=4075.333, post_share=0.000

**Exact log lines:**

```text
192.0.2.32 - - [01/Sep/2026:09:33:06 +0000] "GET /missing HTTP/1.1" 404 1999 "-" "Mozilla/5.0"
192.0.2.32 - - [01/Sep/2026:09:33:33 +0000] "GET /api/items/1 HTTP/1.1" 301 239 "-" "Mozilla/5.0"
192.0.2.32 - - [01/Sep/2026:09:33:49 +0000] "GET /about HTTP/1.1" 200 9988 "-" "Mozilla/5.0"
```

## 192.0.2.24 — 2026-09-01 09:34:00+00:00

**Reason:** avg payload 13426 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=13426.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.24 - - [01/Sep/2026:09:34:06 +0000] "GET /api/items HTTP/1.1" 200 10780 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:09:34:20 +0000] "GET /does-not-exist HTTP/1.1" 404 16073 "-" "Mozilla/5.0"
```

## 192.0.2.36 — 2026-09-01 09:36:00+00:00

**Reason:** 60% POST share

**Features:** requests_per_minute=5, error_404_ratio=0.000, unique_urls=3, avg_payload_size=9358.000, post_share=0.600

**Exact log lines:**

```text
192.0.2.36 - - [01/Sep/2026:09:36:10 +0000] "POST /api/items HTTP/1.1" 201 16240 "-" "Mozilla/5.0"
192.0.2.36 - - [01/Sep/2026:09:36:16 +0000] "POST /login HTTP/1.1" 304 12676 "-" "Mozilla/5.0"
192.0.2.36 - - [01/Sep/2026:09:36:33 +0000] "GET /login HTTP/1.1" 200 5989 "-" "Mozilla/5.0"
192.0.2.36 - - [01/Sep/2026:09:36:44 +0000] "GET /favicon.ico HTTP/1.1" 401 411 "-" "Mozilla/5.0"
192.0.2.36 - - [01/Sep/2026:09:36:56 +0000] "POST /login HTTP/1.1" 200 11474 "-" "Mozilla/5.0"
```

## 192.0.2.25 — 2026-09-01 09:37:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=3, avg_payload_size=5538.333, post_share=0.333

**Exact log lines:**

```text
192.0.2.25 - - [01/Sep/2026:09:37:33 +0000] "GET /old-page HTTP/1.1" 404 6736 "-" "Mozilla/5.0"
192.0.2.25 - - [01/Sep/2026:09:37:48 +0000] "POST /api/items HTTP/1.1" 200 1101 "-" "Mozilla/5.0"
192.0.2.25 - - [01/Sep/2026:09:37:59 +0000] "GET /static/app.js HTTP/1.1" 200 8778 "-" "Mozilla/5.0"
```

## 192.0.2.45 — 2026-09-01 09:37:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.667, unique_urls=3, avg_payload_size=9273.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.45 - - [01/Sep/2026:09:37:05 +0000] "GET /missing HTTP/1.1" 404 6971 "-" "Mozilla/5.0"
192.0.2.45 - - [01/Sep/2026:09:37:44 +0000] "GET /does-not-exist HTTP/1.1" 404 9609 "-" "Mozilla/5.0"
192.0.2.45 - - [01/Sep/2026:09:37:59 +0000] "GET /contact HTTP/1.1" 200 11239 "-" "Mozilla/5.0"
```

## 192.0.2.16 — 2026-09-01 09:38:00+00:00

**Reason:** avg payload 13819 bytes

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=13819.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.16 - - [01/Sep/2026:09:38:41 +0000] "GET / HTTP/1.1" 304 13819 "-" "Mozilla/5.0"
```

## 192.0.2.14 — 2026-09-01 09:39:00+00:00

**Reason:** avg payload 15539 bytes

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=15539.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.14 - - [01/Sep/2026:09:39:02 +0000] "GET /about HTTP/1.1" 200 15539 "-" "Mozilla/5.0"
```

## 192.0.2.15 — 2026-09-01 09:39:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=2592.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.15 - - [01/Sep/2026:09:39:32 +0000] "GET /search?q=phone HTTP/1.1" 200 2592 "-" "Mozilla/5.0"
```

## 192.0.2.27 — 2026-09-01 09:39:00+00:00

**Reason:** 10 unique URLs

**Features:** requests_per_minute=18, error_404_ratio=0.222, unique_urls=10, avg_payload_size=8243.111, post_share=0.333

**Exact log lines:**

```text
192.0.2.27 - - [01/Sep/2026:09:39:00 +0000] "GET /index.html HTTP/1.1" 204 6683 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:06 +0000] "GET /static/style.css HTTP/1.1" 200 11867 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:13 +0000] "GET /does-not-exist HTTP/1.1" 404 7818 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:17 +0000] "GET /static/style.css HTTP/1.1" 204 4085 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:20 +0000] "GET / HTTP/1.1" 200 286 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:20 +0000] "POST /api/search HTTP/1.1" 200 12490 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:21 +0000] "GET /static/style.css HTTP/1.1" 200 17055 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:24 +0000] "POST /api/search HTTP/1.1" 301 11205 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:24 +0000] "POST /api/items HTTP/1.1" 401 2434 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:25 +0000] "GET /about HTTP/1.1" 200 16354 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:29 +0000] "GET /about HTTP/1.1" 304 6532 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:31 +0000] "POST /api/search HTTP/1.1" 404 5884 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:31 +0000] "POST /api/items HTTP/1.1" 404 14976 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:32 +0000] "GET /static/style.css HTTP/1.1" 401 5137 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:37 +0000] "GET /favicon.ico HTTP/1.1" 200 2907 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:38 +0000] "POST /api/search HTTP/1.1" 200 12444 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:48 +0000] "GET /missing HTTP/1.1" 404 2484 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:39:49 +0000] "GET /login HTTP/1.1" 200 7735 "-" "Mozilla/5.0"
```

## 192.0.2.31 — 2026-09-01 09:39:00+00:00

**Reason:** 50% POST share, avg payload 10867 bytes

**Features:** requests_per_minute=4, error_404_ratio=0.000, unique_urls=4, avg_payload_size=10867.250, post_share=0.500

**Exact log lines:**

```text
192.0.2.31 - - [01/Sep/2026:09:39:33 +0000] "GET /index.html HTTP/1.1" 200 16409 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:09:39:35 +0000] "GET /api/items/1 HTTP/1.1" 200 3362 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:09:39:36 +0000] "POST /api/search HTTP/1.1" 304 13050 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:09:39:39 +0000] "POST /api/items HTTP/1.1" 200 10648 "-" "Mozilla/5.0"
```

## 192.0.2.18 — 2026-09-01 09:40:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.667, unique_urls=3, avg_payload_size=6046.333, post_share=0.333

**Exact log lines:**

```text
192.0.2.18 - - [01/Sep/2026:09:40:04 +0000] "GET /old-page HTTP/1.1" 404 202 "-" "Mozilla/5.0"
192.0.2.18 - - [01/Sep/2026:09:40:47 +0000] "POST /login HTTP/1.1" 200 6956 "-" "Mozilla/5.0"
192.0.2.18 - - [01/Sep/2026:09:40:56 +0000] "GET /does-not-exist HTTP/1.1" 404 10981 "-" "Mozilla/5.0"
```

## 192.0.2.38 — 2026-09-01 09:40:00+00:00

**Reason:** avg payload 12932 bytes

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=12932.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.38 - - [01/Sep/2026:09:40:38 +0000] "GET /static/app.js HTTP/1.1" 200 12932 "-" "Mozilla/5.0"
```

## 198.51.100.11 — 2026-09-01 09:40:00+00:00

**Reason:** 100% 404 ratio, 8 unique URLs

**Features:** requests_per_minute=30, error_404_ratio=1.000, unique_urls=8, avg_payload_size=458.333, post_share=0.000

**Exact log lines:**

```text
198.51.100.11 - - [01/Sep/2026:09:40:00 +0000] "GET /admin HTTP/1.1" 404 58 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:02 +0000] "GET /.env HTTP/1.1" 404 181 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:04 +0000] "GET /wp-login.php HTTP/1.1" 404 654 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:06 +0000] "GET /admin/login HTTP/1.1" 404 584 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:08 +0000] "GET /.git/config HTTP/1.1" 404 775 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:10 +0000] "GET /phpmyadmin HTTP/1.1" 404 294 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:12 +0000] "GET /server-status HTTP/1.1" 404 836 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:14 +0000] "GET /backup.zip HTTP/1.1" 404 496 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:16 +0000] "GET /admin HTTP/1.1" 404 675 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:18 +0000] "GET /.env HTTP/1.1" 404 81 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:20 +0000] "GET /wp-login.php HTTP/1.1" 404 299 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:22 +0000] "GET /admin/login HTTP/1.1" 404 761 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:24 +0000] "GET /.git/config HTTP/1.1" 404 647 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:26 +0000] "GET /phpmyadmin HTTP/1.1" 404 209 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:28 +0000] "GET /server-status HTTP/1.1" 404 304 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:30 +0000] "GET /backup.zip HTTP/1.1" 404 643 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:32 +0000] "GET /admin HTTP/1.1" 404 52 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:34 +0000] "GET /.env HTTP/1.1" 404 117 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:36 +0000] "GET /wp-login.php HTTP/1.1" 404 757 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:38 +0000] "GET /admin/login HTTP/1.1" 404 343 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:40 +0000] "GET /.git/config HTTP/1.1" 404 253 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:42 +0000] "GET /phpmyadmin HTTP/1.1" 404 147 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:44 +0000] "GET /server-status HTTP/1.1" 404 898 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:46 +0000] "GET /backup.zip HTTP/1.1" 404 412 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:48 +0000] "GET /admin HTTP/1.1" 404 757 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:50 +0000] "GET /.env HTTP/1.1" 404 723 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:52 +0000] "GET /wp-login.php HTTP/1.1" 404 898 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:54 +0000] "GET /admin/login HTTP/1.1" 404 205 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:56 +0000] "GET /.git/config HTTP/1.1" 404 504 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:40:58 +0000] "GET /phpmyadmin HTTP/1.1" 404 187 "-" "Mozilla/5.0"
```

## 192.0.2.51 — 2026-09-01 09:41:00+00:00

**Reason:** 12 unique URLs, avg payload 11254 bytes

**Features:** requests_per_minute=16, error_404_ratio=0.250, unique_urls=12, avg_payload_size=11254.375, post_share=0.062

**Exact log lines:**

```text
192.0.2.51 - - [01/Sep/2026:09:41:01 +0000] "GET /old-page HTTP/1.1" 404 17383 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:08 +0000] "GET /static/app.js HTTP/1.1" 200 6525 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:09 +0000] "GET /old-page HTTP/1.1" 404 17840 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:10 +0000] "POST /api/items HTTP/1.1" 500 14088 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:16 +0000] "GET /does-not-exist HTTP/1.1" 404 8657 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:17 +0000] "GET /index.html HTTP/1.1" 200 14636 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:20 +0000] "GET /static/style.css HTTP/1.1" 200 17957 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:22 +0000] "GET /static/app.js HTTP/1.1" 304 16329 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:29 +0000] "GET / HTTP/1.1" 204 8204 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:33 +0000] "GET /does-not-exist HTTP/1.1" 404 15795 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:34 +0000] "GET /about HTTP/1.1" 200 4868 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:40 +0000] "GET /favicon.ico HTTP/1.1" 200 585 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:43 +0000] "GET /products HTTP/1.1" 304 8979 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:46 +0000] "GET /search?q=phone HTTP/1.1" 201 15263 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:50 +0000] "GET /contact HTTP/1.1" 200 7824 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:41:53 +0000] "GET /favicon.ico HTTP/1.1" 200 5137 "-" "Mozilla/5.0"
```

## 192.0.2.52 — 2026-09-01 09:41:00+00:00

**Reason:** 13 unique URLs

**Features:** requests_per_minute=17, error_404_ratio=0.353, unique_urls=13, avg_payload_size=7535.647, post_share=0.176

**Exact log lines:**

```text
192.0.2.52 - - [01/Sep/2026:09:41:02 +0000] "GET /api/items HTTP/1.1" 200 1047 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:03 +0000] "GET /does-not-exist HTTP/1.1" 404 9467 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:04 +0000] "GET /search?q=phone HTTP/1.1" 200 367 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:06 +0000] "GET /contact HTTP/1.1" 200 12089 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:07 +0000] "GET /about HTTP/1.1" 200 12931 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:11 +0000] "POST /api/search HTTP/1.1" 404 1828 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:14 +0000] "GET /old-page HTTP/1.1" 404 10730 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:18 +0000] "GET /products HTTP/1.1" 200 8273 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:25 +0000] "GET /old-page HTTP/1.1" 404 17880 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:33 +0000] "GET /favicon.ico HTTP/1.1" 401 4549 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:36 +0000] "POST /api/search HTTP/1.1" 404 8853 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:39 +0000] "POST /api/items HTTP/1.1" 404 8499 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:46 +0000] "GET /api/items HTTP/1.1" 201 8457 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:47 +0000] "GET /static/app.js HTTP/1.1" 200 8881 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:49 +0000] "GET /products/2 HTTP/1.1" 200 1902 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:50 +0000] "GET /products/1 HTTP/1.1" 200 189 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:41:52 +0000] "GET /api/items/1 HTTP/1.1" 301 12164 "-" "Mozilla/5.0"
```

## 198.51.100.11 — 2026-09-01 09:41:00+00:00

**Reason:** 100% 404 ratio, 8 unique URLs

**Features:** requests_per_minute=30, error_404_ratio=1.000, unique_urls=8, avg_payload_size=471.867, post_share=0.000

**Exact log lines:**

```text
198.51.100.11 - - [01/Sep/2026:09:41:00 +0000] "GET /server-status HTTP/1.1" 404 450 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:02 +0000] "GET /backup.zip HTTP/1.1" 404 557 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:04 +0000] "GET /admin HTTP/1.1" 404 294 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:06 +0000] "GET /.env HTTP/1.1" 404 580 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:08 +0000] "GET /wp-login.php HTTP/1.1" 404 636 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:10 +0000] "GET /admin/login HTTP/1.1" 404 376 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:12 +0000] "GET /.git/config HTTP/1.1" 404 459 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:14 +0000] "GET /phpmyadmin HTTP/1.1" 404 701 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:16 +0000] "GET /server-status HTTP/1.1" 404 186 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:18 +0000] "GET /backup.zip HTTP/1.1" 404 55 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:20 +0000] "GET /admin HTTP/1.1" 404 436 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:22 +0000] "GET /.env HTTP/1.1" 404 499 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:24 +0000] "GET /wp-login.php HTTP/1.1" 404 606 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:26 +0000] "GET /admin/login HTTP/1.1" 404 117 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:28 +0000] "GET /.git/config HTTP/1.1" 404 705 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:30 +0000] "GET /phpmyadmin HTTP/1.1" 404 212 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:32 +0000] "GET /server-status HTTP/1.1" 404 240 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:34 +0000] "GET /backup.zip HTTP/1.1" 404 468 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:36 +0000] "GET /admin HTTP/1.1" 404 661 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:38 +0000] "GET /.env HTTP/1.1" 404 568 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:40 +0000] "GET /wp-login.php HTTP/1.1" 404 539 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:42 +0000] "GET /admin/login HTTP/1.1" 404 142 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:44 +0000] "GET /.git/config HTTP/1.1" 404 349 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:46 +0000] "GET /phpmyadmin HTTP/1.1" 404 757 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:48 +0000] "GET /server-status HTTP/1.1" 404 660 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:50 +0000] "GET /backup.zip HTTP/1.1" 404 126 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:52 +0000] "GET /admin HTTP/1.1" 404 714 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:54 +0000] "GET /.env HTTP/1.1" 404 462 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:56 +0000] "GET /wp-login.php HTTP/1.1" 404 859 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:41:58 +0000] "GET /admin/login HTTP/1.1" 404 742 "-" "Mozilla/5.0"
```

## 192.0.2.11 — 2026-09-01 09:42:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=5634.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.11 - - [01/Sep/2026:09:42:11 +0000] "GET /static/app.js HTTP/1.1" 200 248 "-" "Mozilla/5.0"
192.0.2.11 - - [01/Sep/2026:09:42:20 +0000] "GET /api/items/1 HTTP/1.1" 304 11020 "-" "Mozilla/5.0"
```

## 198.51.100.11 — 2026-09-01 09:42:00+00:00

**Reason:** 100% 404 ratio

**Features:** requests_per_minute=4, error_404_ratio=1.000, unique_urls=4, avg_payload_size=540.250, post_share=0.000

**Exact log lines:**

```text
198.51.100.11 - - [01/Sep/2026:09:42:00 +0000] "GET /.git/config HTTP/1.1" 404 455 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:42:02 +0000] "GET /phpmyadmin HTTP/1.1" 404 538 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:42:04 +0000] "GET /server-status HTTP/1.1" 404 455 "-" "Mozilla/5.0"
198.51.100.11 - - [01/Sep/2026:09:42:06 +0000] "GET /backup.zip HTTP/1.1" 404 713 "-" "Mozilla/5.0"
```

## 192.0.2.34 — 2026-09-01 09:43:00+00:00

**Reason:** 50% POST share

**Features:** requests_per_minute=4, error_404_ratio=0.250, unique_urls=3, avg_payload_size=7494.000, post_share=0.500

**Exact log lines:**

```text
192.0.2.34 - - [01/Sep/2026:09:43:04 +0000] "GET /index.html HTTP/1.1" 200 3794 "-" "Mozilla/5.0"
192.0.2.34 - - [01/Sep/2026:09:43:26 +0000] "POST /api/search HTTP/1.1" 201 9555 "-" "Mozilla/5.0"
192.0.2.34 - - [01/Sep/2026:09:43:36 +0000] "POST /api/search HTTP/1.1" 404 11686 "-" "Mozilla/5.0"
192.0.2.34 - - [01/Sep/2026:09:43:39 +0000] "GET /api/items HTTP/1.1" 200 4941 "-" "Mozilla/5.0"
```

## 192.0.2.28 — 2026-09-01 09:44:00+00:00

**Reason:** avg payload 14933 bytes

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=2, avg_payload_size=14933.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.28 - - [01/Sep/2026:09:44:17 +0000] "GET /about HTTP/1.1" 200 17194 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:44:50 +0000] "GET /api/items/1 HTTP/1.1" 200 14514 "-" "Mozilla/5.0"
192.0.2.28 - - [01/Sep/2026:09:44:54 +0000] "GET /about HTTP/1.1" 400 13091 "-" "Mozilla/5.0"
```

## 192.0.2.37 — 2026-09-01 09:44:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=4, error_404_ratio=0.000, unique_urls=3, avg_payload_size=3160.750, post_share=0.250

**Exact log lines:**

```text
192.0.2.37 - - [01/Sep/2026:09:44:02 +0000] "GET /products HTTP/1.1" 301 5391 "-" "Mozilla/5.0"
192.0.2.37 - - [01/Sep/2026:09:44:15 +0000] "GET /search?q=phone HTTP/1.1" 204 3884 "-" "Mozilla/5.0"
192.0.2.37 - - [01/Sep/2026:09:44:16 +0000] "POST /api/items HTTP/1.1" 200 687 "-" "Mozilla/5.0"
192.0.2.37 - - [01/Sep/2026:09:44:30 +0000] "GET /api/items HTTP/1.1" 304 2681 "-" "Mozilla/5.0"
```

## 192.0.2.51 — 2026-09-01 09:44:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=5, error_404_ratio=0.600, unique_urls=4, avg_payload_size=5029.800, post_share=0.000

**Exact log lines:**

```text
192.0.2.51 - - [01/Sep/2026:09:44:15 +0000] "GET /static/style.css HTTP/1.1" 200 2839 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:44:38 +0000] "GET /does-not-exist HTTP/1.1" 404 3532 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:44:42 +0000] "GET /index.html HTTP/1.1" 200 4672 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:44:47 +0000] "GET /old-page HTTP/1.1" 404 5012 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:09:44:54 +0000] "GET /does-not-exist HTTP/1.1" 404 9094 "-" "Mozilla/5.0"
```

## 192.0.2.29 — 2026-09-01 09:45:00+00:00

**Reason:** avg payload 10284 bytes

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=2, avg_payload_size=10283.667, post_share=0.333

**Exact log lines:**

```text
192.0.2.29 - - [01/Sep/2026:09:45:06 +0000] "GET /api/items HTTP/1.1" 401 15066 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:09:45:32 +0000] "POST /api/items HTTP/1.1" 301 11151 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:09:45:50 +0000] "GET /static/style.css HTTP/1.1" 201 4634 "-" "Mozilla/5.0"
```

## 192.0.2.55 — 2026-09-01 09:45:00+00:00

**Reason:** 100% 404 ratio

**Features:** requests_per_minute=1, error_404_ratio=1.000, unique_urls=1, avg_payload_size=6709.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.55 - - [01/Sep/2026:09:45:27 +0000] "GET /does-not-exist HTTP/1.1" 404 6709 "-" "Mozilla/5.0"
```

## 192.0.2.27 — 2026-09-01 09:46:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=4, error_404_ratio=0.500, unique_urls=2, avg_payload_size=8917.250, post_share=0.250

**Exact log lines:**

```text
192.0.2.27 - - [01/Sep/2026:09:46:30 +0000] "GET /old-page HTTP/1.1" 404 16704 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:46:30 +0000] "POST /api/items HTTP/1.1" 404 4730 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:46:39 +0000] "GET /api/items HTTP/1.1" 200 3799 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:09:46:51 +0000] "GET /api/items HTTP/1.1" 403 10436 "-" "Mozilla/5.0"
```

## 192.0.2.17 — 2026-09-01 09:48:00+00:00

**Reason:** 13 unique URLs, avg payload 10133 bytes

**Features:** requests_per_minute=16, error_404_ratio=0.125, unique_urls=13, avg_payload_size=10132.625, post_share=0.062

**Exact log lines:**

```text
192.0.2.17 - - [01/Sep/2026:09:48:03 +0000] "GET /about HTTP/1.1" 201 13662 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:06 +0000] "GET /products HTTP/1.1" 304 8292 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:07 +0000] "GET /login HTTP/1.1" 201 13088 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:10 +0000] "GET /old-page HTTP/1.1" 404 2366 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:12 +0000] "GET /contact HTTP/1.1" 304 2607 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:14 +0000] "GET /login HTTP/1.1" 301 6231 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:20 +0000] "POST /api/search HTTP/1.1" 200 15178 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:24 +0000] "GET /api/items HTTP/1.1" 200 12645 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:25 +0000] "GET /favicon.ico HTTP/1.1" 200 1531 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:32 +0000] "GET /contact HTTP/1.1" 304 14639 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:38 +0000] "GET /products/1 HTTP/1.1" 200 16068 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:42 +0000] "GET /missing HTTP/1.1" 404 15531 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:44 +0000] "GET /static/style.css HTTP/1.1" 200 11184 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:44 +0000] "GET /search?q=phone HTTP/1.1" 500 11802 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:52 +0000] "GET /contact HTTP/1.1" 200 14318 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:48:57 +0000] "GET /products/2 HTTP/1.1" 301 2980 "-" "Mozilla/5.0"
```

## 192.0.2.31 — 2026-09-01 09:48:00+00:00

**Reason:** avg payload 14106 bytes

**Features:** requests_per_minute=4, error_404_ratio=0.500, unique_urls=4, avg_payload_size=14106.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.31 - - [01/Sep/2026:09:48:00 +0000] "GET /does-not-exist HTTP/1.1" 404 10334 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:09:48:16 +0000] "GET /login HTTP/1.1" 304 17309 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:09:48:20 +0000] "GET /old-page HTTP/1.1" 404 15497 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:09:48:36 +0000] "GET / HTTP/1.1" 200 13286 "-" "Mozilla/5.0"
```

## 192.0.2.35 — 2026-09-01 09:49:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=4, error_404_ratio=0.750, unique_urls=4, avg_payload_size=8313.250, post_share=0.250

**Exact log lines:**

```text
192.0.2.35 - - [01/Sep/2026:09:49:04 +0000] "GET /does-not-exist HTTP/1.1" 404 2679 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:49:15 +0000] "POST /api/items HTTP/1.1" 404 11255 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:49:22 +0000] "GET /products HTTP/1.1" 200 17338 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:09:49:40 +0000] "GET /old-page HTTP/1.1" 404 1981 "-" "Mozilla/5.0"
```

## 192.0.2.41 — 2026-09-01 09:49:00+00:00

**Reason:** avg payload 10420 bytes

**Features:** requests_per_minute=8, error_404_ratio=0.750, unique_urls=4, avg_payload_size=10420.250, post_share=0.000

**Exact log lines:**

```text
192.0.2.41 - - [01/Sep/2026:09:49:00 +0000] "GET /does-not-exist HTTP/1.1" 404 8649 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:09:49:06 +0000] "GET /does-not-exist HTTP/1.1" 404 7045 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:09:49:08 +0000] "GET /does-not-exist HTTP/1.1" 404 2908 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:09:49:09 +0000] "GET /does-not-exist HTTP/1.1" 404 10294 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:09:49:18 +0000] "GET /search?q=phone HTTP/1.1" 200 5918 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:09:49:29 +0000] "GET / HTTP/1.1" 204 14941 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:09:49:32 +0000] "GET /missing HTTP/1.1" 404 15619 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:09:49:55 +0000] "GET /does-not-exist HTTP/1.1" 404 17988 "-" "Mozilla/5.0"
```

## 192.0.2.14 — 2026-09-01 09:50:00+00:00

**Reason:** avg payload 13361 bytes

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=13361.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.14 - - [01/Sep/2026:09:50:42 +0000] "GET /about HTTP/1.1" 200 13361 "-" "Mozilla/5.0"
```

## 192.0.2.52 — 2026-09-01 09:50:00+00:00

**Reason:** 50% POST share, avg payload 11519 bytes

**Features:** requests_per_minute=6, error_404_ratio=0.000, unique_urls=4, avg_payload_size=11519.000, post_share=0.500

**Exact log lines:**

```text
192.0.2.52 - - [01/Sep/2026:09:50:06 +0000] "GET /products HTTP/1.1" 200 15553 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:50:07 +0000] "POST /api/items HTTP/1.1" 400 8411 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:50:11 +0000] "POST /login HTTP/1.1" 301 17340 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:50:16 +0000] "POST /login HTTP/1.1" 200 1691 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:50:36 +0000] "GET /api/items HTTP/1.1" 200 13247 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:09:50:57 +0000] "GET /contact HTTP/1.1" 200 12872 "-" "Mozilla/5.0"
```

## 192.0.2.14 — 2026-09-01 09:51:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=1, avg_payload_size=6341.333, post_share=0.000

**Exact log lines:**

```text
192.0.2.14 - - [01/Sep/2026:09:51:13 +0000] "GET /api/items HTTP/1.1" 200 9287 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:51:33 +0000] "GET /api/items HTTP/1.1" 400 8409 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:51:36 +0000] "GET /api/items HTTP/1.1" 200 1328 "-" "Mozilla/5.0"
```

## 192.0.2.19 — 2026-09-01 09:51:00+00:00

**Reason:** 50% POST share, avg payload 10076 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=10076.500, post_share=0.500

**Exact log lines:**

```text
192.0.2.19 - - [01/Sep/2026:09:51:13 +0000] "POST /login HTTP/1.1" 200 10680 "-" "Mozilla/5.0"
192.0.2.19 - - [01/Sep/2026:09:51:54 +0000] "GET /products HTTP/1.1" 200 9473 "-" "Mozilla/5.0"
```

## 192.0.2.13 — 2026-09-01 09:52:00+00:00

**Reason:** avg payload 13190 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=13189.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.13 - - [01/Sep/2026:09:52:02 +0000] "GET /api/items HTTP/1.1" 200 10306 "-" "Mozilla/5.0"
192.0.2.13 - - [01/Sep/2026:09:52:47 +0000] "GET /missing HTTP/1.1" 404 16073 "-" "Mozilla/5.0"
```

## 192.0.2.17 — 2026-09-01 09:52:00+00:00

**Reason:** avg payload 11904 bytes

**Features:** requests_per_minute=4, error_404_ratio=0.750, unique_urls=4, avg_payload_size=11904.000, post_share=0.250

**Exact log lines:**

```text
192.0.2.17 - - [01/Sep/2026:09:52:23 +0000] "GET /does-not-exist HTTP/1.1" 404 15769 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:52:34 +0000] "POST /login HTTP/1.1" 404 1850 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:52:34 +0000] "GET /about HTTP/1.1" 200 13459 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:09:52:43 +0000] "GET /old-page HTTP/1.1" 404 16538 "-" "Mozilla/5.0"
```

## 192.0.2.30 — 2026-09-01 09:53:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=5826.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.30 - - [01/Sep/2026:09:53:34 +0000] "GET /static/app.js HTTP/1.1" 204 5472 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:09:53:50 +0000] "GET /index.html HTTP/1.1" 204 6181 "-" "Mozilla/5.0"
```

## 192.0.2.45 — 2026-09-01 09:53:00+00:00

**Reason:** avg payload 16289 bytes

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=3, avg_payload_size=16289.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.45 - - [01/Sep/2026:09:53:07 +0000] "GET /favicon.ico HTTP/1.1" 200 17506 "-" "Mozilla/5.0"
192.0.2.45 - - [01/Sep/2026:09:53:09 +0000] "GET /index.html HTTP/1.1" 200 17852 "-" "Mozilla/5.0"
192.0.2.45 - - [01/Sep/2026:09:53:13 +0000] "GET /about HTTP/1.1" 200 13509 "-" "Mozilla/5.0"
```

## 192.0.2.59 — 2026-09-01 09:55:00+00:00

**Reason:** 56% POST share, avg payload 11497 bytes

**Features:** requests_per_minute=9, error_404_ratio=0.333, unique_urls=5, avg_payload_size=11497.111, post_share=0.556

**Exact log lines:**

```text
192.0.2.59 - - [01/Sep/2026:09:55:04 +0000] "GET /static/app.js HTTP/1.1" 200 6436 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:09:55:05 +0000] "POST /api/search HTTP/1.1" 200 14138 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:09:55:07 +0000] "POST /api/items HTTP/1.1" 204 8825 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:09:55:24 +0000] "POST /api/items HTTP/1.1" 404 17654 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:09:55:28 +0000] "GET /old-page HTTP/1.1" 404 7714 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:09:55:33 +0000] "GET /static/style.css HTTP/1.1" 200 16575 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:09:55:39 +0000] "GET /static/app.js HTTP/1.1" 200 4962 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:09:55:54 +0000] "POST /api/items HTTP/1.1" 200 15004 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:09:55:59 +0000] "POST /api/search HTTP/1.1" 404 12166 "-" "Mozilla/5.0"
```

## 192.0.2.11 — 2026-09-01 09:56:00+00:00

**Reason:** avg payload 10852 bytes

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=10852.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.11 - - [01/Sep/2026:09:56:20 +0000] "GET /search?q=phone HTTP/1.1" 301 10852 "-" "Mozilla/5.0"
```

## 192.0.2.19 — 2026-09-01 09:56:00+00:00

**Reason:** 75% POST share, avg payload 14986 bytes

**Features:** requests_per_minute=4, error_404_ratio=0.000, unique_urls=3, avg_payload_size=14985.500, post_share=0.750

**Exact log lines:**

```text
192.0.2.19 - - [01/Sep/2026:09:56:23 +0000] "GET /about HTTP/1.1" 200 13792 "-" "Mozilla/5.0"
192.0.2.19 - - [01/Sep/2026:09:56:38 +0000] "POST /api/search HTTP/1.1" 200 17599 "-" "Mozilla/5.0"
192.0.2.19 - - [01/Sep/2026:09:56:39 +0000] "POST /api/search HTTP/1.1" 200 11983 "-" "Mozilla/5.0"
192.0.2.19 - - [01/Sep/2026:09:56:50 +0000] "POST /login HTTP/1.1" 200 16568 "-" "Mozilla/5.0"
```

## 192.0.2.15 — 2026-09-01 09:57:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=5, error_404_ratio=0.000, unique_urls=5, avg_payload_size=2265.600, post_share=0.400

**Exact log lines:**

```text
192.0.2.15 - - [01/Sep/2026:09:57:01 +0000] "GET / HTTP/1.1" 304 1144 "-" "Mozilla/5.0"
192.0.2.15 - - [01/Sep/2026:09:57:06 +0000] "GET /about HTTP/1.1" 400 3275 "-" "Mozilla/5.0"
192.0.2.15 - - [01/Sep/2026:09:57:11 +0000] "POST /api/search HTTP/1.1" 200 226 "-" "Mozilla/5.0"
192.0.2.15 - - [01/Sep/2026:09:57:16 +0000] "GET /contact HTTP/1.1" 200 3426 "-" "Mozilla/5.0"
192.0.2.15 - - [01/Sep/2026:09:57:57 +0000] "POST /login HTTP/1.1" 200 3257 "-" "Mozilla/5.0"
```

## 192.0.2.22 — 2026-09-01 09:57:00+00:00

**Reason:** avg payload 10787 bytes

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=3, avg_payload_size=10786.667, post_share=0.333

**Exact log lines:**

```text
192.0.2.22 - - [01/Sep/2026:09:57:04 +0000] "GET /index.html HTTP/1.1" 200 17872 "-" "Mozilla/5.0"
192.0.2.22 - - [01/Sep/2026:09:57:17 +0000] "POST /login HTTP/1.1" 200 600 "-" "Mozilla/5.0"
192.0.2.22 - - [01/Sep/2026:09:57:31 +0000] "GET /missing HTTP/1.1" 404 13888 "-" "Mozilla/5.0"
```

## 192.0.2.46 — 2026-09-01 09:57:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=3, avg_payload_size=2938.333, post_share=0.333

**Exact log lines:**

```text
192.0.2.46 - - [01/Sep/2026:09:57:07 +0000] "POST /login HTTP/1.1" 200 4045 "-" "Mozilla/5.0"
192.0.2.46 - - [01/Sep/2026:09:57:08 +0000] "GET /static/style.css HTTP/1.1" 200 1905 "-" "Mozilla/5.0"
192.0.2.46 - - [01/Sep/2026:09:57:23 +0000] "GET /index.html HTTP/1.1" 400 2865 "-" "Mozilla/5.0"
```

## 192.0.2.15 — 2026-09-01 09:58:00+00:00

**Reason:** avg payload 11447 bytes

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=3, avg_payload_size=11447.333, post_share=0.333

**Exact log lines:**

```text
192.0.2.15 - - [01/Sep/2026:09:58:34 +0000] "GET /api/items HTTP/1.1" 200 16196 "-" "Mozilla/5.0"
192.0.2.15 - - [01/Sep/2026:09:58:38 +0000] "POST /login HTTP/1.1" 404 17502 "-" "Mozilla/5.0"
192.0.2.15 - - [01/Sep/2026:09:58:49 +0000] "GET /products HTTP/1.1" 200 644 "-" "Mozilla/5.0"
```

## 192.0.2.23 — 2026-09-01 09:58:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=3, avg_payload_size=3231.000, post_share=0.333

**Exact log lines:**

```text
192.0.2.23 - - [01/Sep/2026:09:58:07 +0000] "GET /api/items/1 HTTP/1.1" 200 2696 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:58:24 +0000] "POST /api/search HTTP/1.1" 301 5348 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:09:58:49 +0000] "GET /about HTTP/1.1" 304 1649 "-" "Mozilla/5.0"
```

## 192.0.2.14 — 2026-09-01 09:59:00+00:00

**Reason:** 6 unique URLs, avg payload 15437 bytes

**Features:** requests_per_minute=7, error_404_ratio=0.571, unique_urls=6, avg_payload_size=15436.857, post_share=0.143

**Exact log lines:**

```text
192.0.2.14 - - [01/Sep/2026:09:59:27 +0000] "GET /about HTTP/1.1" 200 17048 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:59:30 +0000] "GET /missing HTTP/1.1" 404 16496 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:59:34 +0000] "GET /missing HTTP/1.1" 404 16803 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:59:41 +0000] "POST /login HTTP/1.1" 404 17316 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:59:44 +0000] "GET /api/items HTTP/1.1" 200 14303 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:59:55 +0000] "GET /products HTTP/1.1" 403 15449 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:09:59:59 +0000] "GET /does-not-exist HTTP/1.1" 404 10643 "-" "Mozilla/5.0"
```

## 192.0.2.24 — 2026-09-01 09:59:00+00:00

**Reason:** 100% 404 ratio, 50% POST share, avg payload 11666 bytes

**Features:** requests_per_minute=2, error_404_ratio=1.000, unique_urls=2, avg_payload_size=11665.500, post_share=0.500

**Exact log lines:**

```text
192.0.2.24 - - [01/Sep/2026:09:59:17 +0000] "POST /login HTTP/1.1" 404 13809 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:09:59:19 +0000] "GET /does-not-exist HTTP/1.1" 404 9522 "-" "Mozilla/5.0"
```

## 192.0.2.44 — 2026-09-01 10:02:00+00:00

**Reason:** 50% POST share, avg payload 11240 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=11240.000, post_share=0.500

**Exact log lines:**

```text
192.0.2.44 - - [01/Sep/2026:10:02:41 +0000] "POST /api/items HTTP/1.1" 500 17162 "-" "Mozilla/5.0"
192.0.2.44 - - [01/Sep/2026:10:02:44 +0000] "GET /static/app.js HTTP/1.1" 200 5318 "-" "Mozilla/5.0"
```

## 192.0.2.59 — 2026-09-01 10:02:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=3293.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.59 - - [01/Sep/2026:10:02:12 +0000] "GET /index.html HTTP/1.1" 200 1623 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:02:13 +0000] "GET /products/2 HTTP/1.1" 200 4963 "-" "Mozilla/5.0"
```

## 192.0.2.29 — 2026-09-01 10:03:00+00:00

**Reason:** avg payload 15840 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=15839.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.29 - - [01/Sep/2026:10:03:36 +0000] "GET /about HTTP/1.1" 201 17141 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:03:59 +0000] "GET /products/1 HTTP/1.1" 200 14538 "-" "Mozilla/5.0"
```

## 192.0.2.30 — 2026-09-01 10:04:00+00:00

**Reason:** 50% POST share

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=3450.000, post_share=0.500

**Exact log lines:**

```text
192.0.2.30 - - [01/Sep/2026:10:04:14 +0000] "POST /api/items HTTP/1.1" 200 6055 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:10:04:42 +0000] "GET /does-not-exist HTTP/1.1" 404 845 "-" "Mozilla/5.0"
```

## 192.0.2.35 — 2026-09-01 10:04:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=9157.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.35 - - [01/Sep/2026:10:04:45 +0000] "GET /static/app.js HTTP/1.1" 200 9157 "-" "Mozilla/5.0"
```

## 192.0.2.40 — 2026-09-01 10:04:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=3, avg_payload_size=6101.667, post_share=0.333

**Exact log lines:**

```text
192.0.2.40 - - [01/Sep/2026:10:04:08 +0000] "GET /search?q=phone HTTP/1.1" 200 2700 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:04:23 +0000] "POST /api/search HTTP/1.1" 404 1658 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:04:39 +0000] "GET /products/1 HTTP/1.1" 200 13947 "-" "Mozilla/5.0"
```

## 192.0.2.23 — 2026-09-01 10:05:00+00:00

**Reason:** 12 unique URLs, avg payload 12211 bytes

**Features:** requests_per_minute=15, error_404_ratio=0.267, unique_urls=12, avg_payload_size=12211.467, post_share=0.200

**Exact log lines:**

```text
192.0.2.23 - - [01/Sep/2026:10:05:10 +0000] "GET /products/2 HTTP/1.1" 200 4193 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:16 +0000] "GET /old-page HTTP/1.1" 404 10964 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:17 +0000] "GET /contact HTTP/1.1" 201 14502 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:18 +0000] "GET /contact HTTP/1.1" 201 17860 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:20 +0000] "GET /missing HTTP/1.1" 404 11880 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:22 +0000] "GET /static/app.js HTTP/1.1" 204 11236 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:31 +0000] "GET /does-not-exist HTTP/1.1" 404 10021 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:35 +0000] "GET /search?q=phone HTTP/1.1" 200 8008 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:38 +0000] "POST /api/items HTTP/1.1" 200 17846 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:38 +0000] "POST /api/search HTTP/1.1" 200 4433 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:41 +0000] "GET /login HTTP/1.1" 200 15856 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:44 +0000] "POST /api/search HTTP/1.1" 404 6353 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:52 +0000] "GET /favicon.ico HTTP/1.1" 500 17989 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:54 +0000] "GET /login HTTP/1.1" 204 15785 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:05:56 +0000] "GET / HTTP/1.1" 200 16246 "-" "Mozilla/5.0"
```

## 192.0.2.52 — 2026-09-01 10:06:00+00:00

**Reason:** 12 unique URLs, avg payload 11852 bytes

**Features:** requests_per_minute=17, error_404_ratio=0.176, unique_urls=12, avg_payload_size=11851.588, post_share=0.059

**Exact log lines:**

```text
192.0.2.52 - - [01/Sep/2026:10:06:01 +0000] "GET /old-page HTTP/1.1" 404 15892 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:02 +0000] "GET /missing HTTP/1.1" 404 17765 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:06 +0000] "POST /api/search HTTP/1.1" 404 16014 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:09 +0000] "GET /products HTTP/1.1" 200 13367 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:22 +0000] "GET /favicon.ico HTTP/1.1" 200 15127 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:23 +0000] "GET /favicon.ico HTTP/1.1" 200 16532 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:27 +0000] "GET /contact HTTP/1.1" 301 4237 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:32 +0000] "GET /index.html HTTP/1.1" 200 10713 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:35 +0000] "GET /about HTTP/1.1" 200 12671 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:37 +0000] "GET /products/2 HTTP/1.1" 200 12821 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:41 +0000] "GET /index.html HTTP/1.1" 204 7416 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:44 +0000] "GET / HTTP/1.1" 200 6397 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:46 +0000] "GET /login HTTP/1.1" 200 17069 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:50 +0000] "GET /api/items HTTP/1.1" 200 3871 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:50 +0000] "GET /favicon.ico HTTP/1.1" 200 11327 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:52 +0000] "GET /products/2 HTTP/1.1" 200 12455 "-" "Mozilla/5.0"
192.0.2.52 - - [01/Sep/2026:10:06:55 +0000] "GET /index.html HTTP/1.1" 200 7803 "-" "Mozilla/5.0"
```

## 192.0.2.10 — 2026-09-01 10:08:00+00:00

**Reason:** 12 unique URLs, avg payload 12233 bytes

**Features:** requests_per_minute=15, error_404_ratio=0.200, unique_urls=12, avg_payload_size=12233.000, post_share=0.133

**Exact log lines:**

```text
192.0.2.10 - - [01/Sep/2026:10:08:04 +0000] "GET /missing HTTP/1.1" 404 17244 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:04 +0000] "GET /products HTTP/1.1" 200 13800 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:09 +0000] "POST /api/search HTTP/1.1" 200 14265 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:19 +0000] "GET /missing HTTP/1.1" 404 14495 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:21 +0000] "POST /login HTTP/1.1" 204 17129 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:22 +0000] "GET / HTTP/1.1" 200 8317 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:29 +0000] "GET /search?q=phone HTTP/1.1" 200 17665 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:33 +0000] "GET /missing HTTP/1.1" 404 11014 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:38 +0000] "GET /about HTTP/1.1" 200 15392 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:40 +0000] "GET /contact HTTP/1.1" 301 10435 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:42 +0000] "GET /contact HTTP/1.1" 304 15006 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:43 +0000] "GET /static/app.js HTTP/1.1" 200 2227 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:44 +0000] "GET /favicon.ico HTTP/1.1" 200 7347 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:45 +0000] "GET /api/items/1 HTTP/1.1" 200 6059 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:08:56 +0000] "GET /products/2 HTTP/1.1" 200 13100 "-" "Mozilla/5.0"
```

## 192.0.2.47 — 2026-09-01 10:09:00+00:00

**Reason:** 80% 404 ratio, avg payload 11395 bytes

**Features:** requests_per_minute=5, error_404_ratio=0.800, unique_urls=3, avg_payload_size=11395.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.47 - - [01/Sep/2026:10:09:01 +0000] "GET /does-not-exist HTTP/1.1" 404 15601 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:09:15 +0000] "GET /does-not-exist HTTP/1.1" 404 3078 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:09:26 +0000] "GET /does-not-exist HTTP/1.1" 404 15099 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:09:51 +0000] "GET /old-page HTTP/1.1" 404 9095 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:09:51 +0000] "GET /products/2 HTTP/1.1" 201 14102 "-" "Mozilla/5.0"
```

## 192.0.2.11 — 2026-09-01 10:12:00+00:00

**Reason:** avg payload 13878 bytes

**Features:** requests_per_minute=5, error_404_ratio=0.000, unique_urls=4, avg_payload_size=13878.000, post_share=0.400

**Exact log lines:**

```text
192.0.2.11 - - [01/Sep/2026:10:12:01 +0000] "GET /index.html HTTP/1.1" 200 10606 "-" "Mozilla/5.0"
192.0.2.11 - - [01/Sep/2026:10:12:18 +0000] "GET /products HTTP/1.1" 200 17507 "-" "Mozilla/5.0"
192.0.2.11 - - [01/Sep/2026:10:12:51 +0000] "POST /login HTTP/1.1" 403 16180 "-" "Mozilla/5.0"
192.0.2.11 - - [01/Sep/2026:10:12:54 +0000] "GET /products HTTP/1.1" 200 13841 "-" "Mozilla/5.0"
192.0.2.11 - - [01/Sep/2026:10:12:54 +0000] "POST /api/items HTTP/1.1" 200 11256 "-" "Mozilla/5.0"
```

## 192.0.2.59 — 2026-09-01 10:12:00+00:00

**Reason:** 100% 404 ratio, 100% POST share, avg payload 12013 bytes

**Features:** requests_per_minute=1, error_404_ratio=1.000, unique_urls=1, avg_payload_size=12013.000, post_share=1.000

**Exact log lines:**

```text
192.0.2.59 - - [01/Sep/2026:10:12:45 +0000] "POST /api/search HTTP/1.1" 404 12013 "-" "Mozilla/5.0"
```

## 192.0.2.23 — 2026-09-01 10:13:00+00:00

**Reason:** 100% 404 ratio

**Features:** requests_per_minute=2, error_404_ratio=1.000, unique_urls=2, avg_payload_size=6072.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.23 - - [01/Sep/2026:10:13:26 +0000] "GET /does-not-exist HTTP/1.1" 404 3874 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:13:54 +0000] "GET /old-page HTTP/1.1" 404 8271 "-" "Mozilla/5.0"
```

## 192.0.2.41 — 2026-09-01 10:13:00+00:00

**Reason:** 60% POST share, avg payload 12376 bytes

**Features:** requests_per_minute=5, error_404_ratio=0.200, unique_urls=4, avg_payload_size=12375.800, post_share=0.600

**Exact log lines:**

```text
192.0.2.41 - - [01/Sep/2026:10:13:06 +0000] "GET /about HTTP/1.1" 200 14323 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:10:13:09 +0000] "GET /static/style.css HTTP/1.1" 200 17002 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:10:13:25 +0000] "POST /api/items HTTP/1.1" 404 12069 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:10:13:40 +0000] "POST /api/search HTTP/1.1" 204 13388 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:10:13:46 +0000] "POST /api/search HTTP/1.1" 403 5097 "-" "Mozilla/5.0"
```

## 192.0.2.50 — 2026-09-01 10:13:00+00:00

**Reason:** avg payload 14637 bytes

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=2, avg_payload_size=14637.000, post_share=0.333

**Exact log lines:**

```text
192.0.2.50 - - [01/Sep/2026:10:13:14 +0000] "GET /login HTTP/1.1" 200 16162 "-" "Mozilla/5.0"
192.0.2.50 - - [01/Sep/2026:10:13:41 +0000] "POST /login HTTP/1.1" 404 11516 "-" "Mozilla/5.0"
192.0.2.50 - - [01/Sep/2026:10:13:44 +0000] "GET /index.html HTTP/1.1" 200 16233 "-" "Mozilla/5.0"
```

## 192.0.2.42 — 2026-09-01 10:14:00+00:00

**Reason:** avg payload 12976 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=12976.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.42 - - [01/Sep/2026:10:14:08 +0000] "GET /old-page HTTP/1.1" 404 12374 "-" "Mozilla/5.0"
192.0.2.42 - - [01/Sep/2026:10:14:17 +0000] "GET / HTTP/1.1" 200 13578 "-" "Mozilla/5.0"
```

## 192.0.2.13 — 2026-09-01 10:15:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=4, error_404_ratio=0.750, unique_urls=3, avg_payload_size=7606.000, post_share=0.250

**Exact log lines:**

```text
192.0.2.13 - - [01/Sep/2026:10:15:21 +0000] "GET /missing HTTP/1.1" 404 7191 "-" "Mozilla/5.0"
192.0.2.13 - - [01/Sep/2026:10:15:32 +0000] "GET /missing HTTP/1.1" 404 7993 "-" "Mozilla/5.0"
192.0.2.13 - - [01/Sep/2026:10:15:39 +0000] "GET /does-not-exist HTTP/1.1" 404 4676 "-" "Mozilla/5.0"
192.0.2.13 - - [01/Sep/2026:10:15:53 +0000] "POST /api/search HTTP/1.1" 304 10564 "-" "Mozilla/5.0"
```

## 192.0.2.41 — 2026-09-01 10:15:00+00:00

**Reason:** 6 unique URLs, avg payload 14781 bytes

**Features:** requests_per_minute=6, error_404_ratio=0.500, unique_urls=6, avg_payload_size=14780.833, post_share=0.167

**Exact log lines:**

```text
192.0.2.41 - - [01/Sep/2026:10:15:22 +0000] "POST /login HTTP/1.1" 404 17442 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:10:15:24 +0000] "GET /old-page HTTP/1.1" 404 14139 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:10:15:26 +0000] "GET /products/2 HTTP/1.1" 200 10682 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:10:15:39 +0000] "GET /does-not-exist HTTP/1.1" 404 16788 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:10:15:45 +0000] "GET /products HTTP/1.1" 200 14898 "-" "Mozilla/5.0"
192.0.2.41 - - [01/Sep/2026:10:15:45 +0000] "GET /api/items/1 HTTP/1.1" 200 14736 "-" "Mozilla/5.0"
```

## 192.0.2.55 — 2026-09-01 10:16:00+00:00

**Reason:** 67% POST share

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=3, avg_payload_size=4762.667, post_share=0.667

**Exact log lines:**

```text
192.0.2.55 - - [01/Sep/2026:10:16:11 +0000] "GET /products/2 HTTP/1.1" 200 4760 "-" "Mozilla/5.0"
192.0.2.55 - - [01/Sep/2026:10:16:12 +0000] "POST /api/search HTTP/1.1" 403 5002 "-" "Mozilla/5.0"
192.0.2.55 - - [01/Sep/2026:10:16:13 +0000] "POST /login HTTP/1.1" 404 4526 "-" "Mozilla/5.0"
```

## 192.0.2.16 — 2026-09-01 10:17:00+00:00

**Reason:** 9 unique URLs, avg payload 11274 bytes

**Features:** requests_per_minute=16, error_404_ratio=0.062, unique_urls=9, avg_payload_size=11274.125, post_share=0.312

**Exact log lines:**

```text
192.0.2.16 - - [01/Sep/2026:10:17:00 +0000] "GET /products/2 HTTP/1.1" 200 4342 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:03 +0000] "GET /static/app.js HTTP/1.1" 200 17303 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:03 +0000] "GET / HTTP/1.1" 201 15789 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:04 +0000] "POST /api/search HTTP/1.1" 200 2924 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:05 +0000] "POST /api/search HTTP/1.1" 401 1972 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:09 +0000] "GET /login HTTP/1.1" 201 15457 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:11 +0000] "GET /api/items HTTP/1.1" 403 10437 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:11 +0000] "POST /api/search HTTP/1.1" 200 15645 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:15 +0000] "POST /api/search HTTP/1.1" 200 15701 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:18 +0000] "GET /static/app.js HTTP/1.1" 304 14912 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:23 +0000] "GET /products HTTP/1.1" 200 17593 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:26 +0000] "GET /products/2 HTTP/1.1" 200 8125 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:29 +0000] "GET /search?q=phone HTTP/1.1" 201 15301 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:36 +0000] "GET /does-not-exist HTTP/1.1" 404 9237 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:47 +0000] "GET / HTTP/1.1" 200 13662 "-" "Mozilla/5.0"
192.0.2.16 - - [01/Sep/2026:10:17:56 +0000] "POST /login HTTP/1.1" 200 1986 "-" "Mozilla/5.0"
```

## 192.0.2.22 — 2026-09-01 10:18:00+00:00

**Reason:** 100% 404 ratio

**Features:** requests_per_minute=3, error_404_ratio=1.000, unique_urls=2, avg_payload_size=8962.333, post_share=0.000

**Exact log lines:**

```text
192.0.2.22 - - [01/Sep/2026:10:18:02 +0000] "GET /old-page HTTP/1.1" 404 10598 "-" "Mozilla/5.0"
192.0.2.22 - - [01/Sep/2026:10:18:22 +0000] "GET /old-page HTTP/1.1" 404 9781 "-" "Mozilla/5.0"
192.0.2.22 - - [01/Sep/2026:10:18:59 +0000] "GET /does-not-exist HTTP/1.1" 404 6508 "-" "Mozilla/5.0"
```

## 192.0.2.51 — 2026-09-01 10:20:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.667, unique_urls=2, avg_payload_size=7790.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.51 - - [01/Sep/2026:10:20:01 +0000] "GET /old-page HTTP/1.1" 404 17010 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:10:20:42 +0000] "GET /old-page HTTP/1.1" 404 169 "-" "Mozilla/5.0"
192.0.2.51 - - [01/Sep/2026:10:20:52 +0000] "GET /about HTTP/1.1" 200 6191 "-" "Mozilla/5.0"
```

## 198.51.100.12 — 2026-09-01 10:20:00+00:00

**Reason:** 600 requests/min

**Features:** requests_per_minute=600, error_404_ratio=0.000, unique_urls=1, avg_payload_size=2512.292, post_share=0.000

**Exact log lines:**

```text
198.51.100.12 - - [01/Sep/2026:10:20:00 +0000] "GET /api/items HTTP/1.1" 200 1454 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:00 +0000] "GET /api/items HTTP/1.1" 200 3748 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:00 +0000] "GET /api/items HTTP/1.1" 200 3096 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:00 +0000] "GET /api/items HTTP/1.1" 200 1108 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:00 +0000] "GET /api/items HTTP/1.1" 200 2517 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:00 +0000] "GET /api/items HTTP/1.1" 200 3720 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:00 +0000] "GET /api/items HTTP/1.1" 200 3878 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:00 +0000] "GET /api/items HTTP/1.1" 200 2870 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:00 +0000] "GET /api/items HTTP/1.1" 200 110 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:00 +0000] "GET /api/items HTTP/1.1" 200 1380 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:01 +0000] "GET /api/items HTTP/1.1" 200 3026 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:01 +0000] "GET /api/items HTTP/1.1" 200 2911 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:01 +0000] "GET /api/items HTTP/1.1" 200 4802 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:01 +0000] "GET /api/items HTTP/1.1" 200 3001 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:01 +0000] "GET /api/items HTTP/1.1" 200 1722 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:01 +0000] "GET /api/items HTTP/1.1" 200 4800 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:01 +0000] "GET /api/items HTTP/1.1" 200 592 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:01 +0000] "GET /api/items HTTP/1.1" 200 3736 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:01 +0000] "GET /api/items HTTP/1.1" 200 1143 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:01 +0000] "GET /api/items HTTP/1.1" 200 925 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:02 +0000] "GET /api/items HTTP/1.1" 200 869 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:02 +0000] "GET /api/items HTTP/1.1" 200 2422 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:02 +0000] "GET /api/items HTTP/1.1" 200 2393 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:02 +0000] "GET /api/items HTTP/1.1" 200 302 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:02 +0000] "GET /api/items HTTP/1.1" 200 3131 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:02 +0000] "GET /api/items HTTP/1.1" 200 931 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:02 +0000] "GET /api/items HTTP/1.1" 200 3480 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:02 +0000] "GET /api/items HTTP/1.1" 200 4561 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:02 +0000] "GET /api/items HTTP/1.1" 200 3096 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:02 +0000] "GET /api/items HTTP/1.1" 200 4188 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:03 +0000] "GET /api/items HTTP/1.1" 200 4530 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:03 +0000] "GET /api/items HTTP/1.1" 200 2876 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:03 +0000] "GET /api/items HTTP/1.1" 200 4948 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:03 +0000] "GET /api/items HTTP/1.1" 200 3128 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:03 +0000] "GET /api/items HTTP/1.1" 200 963 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:03 +0000] "GET /api/items HTTP/1.1" 200 1659 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:03 +0000] "GET /api/items HTTP/1.1" 200 3863 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:03 +0000] "GET /api/items HTTP/1.1" 200 3660 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:03 +0000] "GET /api/items HTTP/1.1" 200 4266 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:03 +0000] "GET /api/items HTTP/1.1" 200 2313 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:04 +0000] "GET /api/items HTTP/1.1" 200 2001 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:04 +0000] "GET /api/items HTTP/1.1" 200 4291 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:04 +0000] "GET /api/items HTTP/1.1" 200 329 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:04 +0000] "GET /api/items HTTP/1.1" 200 2125 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:04 +0000] "GET /api/items HTTP/1.1" 200 435 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:04 +0000] "GET /api/items HTTP/1.1" 200 3951 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:04 +0000] "GET /api/items HTTP/1.1" 200 2035 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:04 +0000] "GET /api/items HTTP/1.1" 200 461 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:04 +0000] "GET /api/items HTTP/1.1" 200 2014 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:04 +0000] "GET /api/items HTTP/1.1" 200 4390 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:05 +0000] "GET /api/items HTTP/1.1" 200 2063 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:05 +0000] "GET /api/items HTTP/1.1" 200 2726 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:05 +0000] "GET /api/items HTTP/1.1" 200 3897 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:05 +0000] "GET /api/items HTTP/1.1" 200 709 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:05 +0000] "GET /api/items HTTP/1.1" 200 496 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:05 +0000] "GET /api/items HTTP/1.1" 200 208 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:05 +0000] "GET /api/items HTTP/1.1" 200 2231 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:05 +0000] "GET /api/items HTTP/1.1" 200 912 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:05 +0000] "GET /api/items HTTP/1.1" 200 1055 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:05 +0000] "GET /api/items HTTP/1.1" 200 1666 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:06 +0000] "GET /api/items HTTP/1.1" 200 1299 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:06 +0000] "GET /api/items HTTP/1.1" 200 3831 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:06 +0000] "GET /api/items HTTP/1.1" 200 3950 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:06 +0000] "GET /api/items HTTP/1.1" 200 4287 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:06 +0000] "GET /api/items HTTP/1.1" 200 279 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:06 +0000] "GET /api/items HTTP/1.1" 200 3499 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:06 +0000] "GET /api/items HTTP/1.1" 200 3042 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:06 +0000] "GET /api/items HTTP/1.1" 200 654 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:06 +0000] "GET /api/items HTTP/1.1" 200 3746 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:06 +0000] "GET /api/items HTTP/1.1" 200 2033 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:07 +0000] "GET /api/items HTTP/1.1" 200 1605 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:07 +0000] "GET /api/items HTTP/1.1" 200 3528 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:07 +0000] "GET /api/items HTTP/1.1" 200 4263 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:07 +0000] "GET /api/items HTTP/1.1" 200 544 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:07 +0000] "GET /api/items HTTP/1.1" 200 1609 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:07 +0000] "GET /api/items HTTP/1.1" 200 2526 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:07 +0000] "GET /api/items HTTP/1.1" 200 2876 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:07 +0000] "GET /api/items HTTP/1.1" 200 2191 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:07 +0000] "GET /api/items HTTP/1.1" 200 1650 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:07 +0000] "GET /api/items HTTP/1.1" 200 4770 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:08 +0000] "GET /api/items HTTP/1.1" 200 4671 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:08 +0000] "GET /api/items HTTP/1.1" 200 718 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:08 +0000] "GET /api/items HTTP/1.1" 200 1183 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:08 +0000] "GET /api/items HTTP/1.1" 200 2093 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:08 +0000] "GET /api/items HTTP/1.1" 200 1701 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:08 +0000] "GET /api/items HTTP/1.1" 200 249 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:08 +0000] "GET /api/items HTTP/1.1" 200 3878 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:08 +0000] "GET /api/items HTTP/1.1" 200 4985 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:08 +0000] "GET /api/items HTTP/1.1" 200 2174 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:08 +0000] "GET /api/items HTTP/1.1" 200 3933 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:09 +0000] "GET /api/items HTTP/1.1" 200 1418 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:09 +0000] "GET /api/items HTTP/1.1" 200 1236 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:09 +0000] "GET /api/items HTTP/1.1" 200 373 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:09 +0000] "GET /api/items HTTP/1.1" 200 2780 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:09 +0000] "GET /api/items HTTP/1.1" 200 857 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:09 +0000] "GET /api/items HTTP/1.1" 200 4787 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:09 +0000] "GET /api/items HTTP/1.1" 200 1784 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:09 +0000] "GET /api/items HTTP/1.1" 200 669 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:09 +0000] "GET /api/items HTTP/1.1" 200 1105 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:09 +0000] "GET /api/items HTTP/1.1" 200 1978 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:10 +0000] "GET /api/items HTTP/1.1" 200 4765 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:10 +0000] "GET /api/items HTTP/1.1" 200 2666 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:10 +0000] "GET /api/items HTTP/1.1" 200 1052 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:10 +0000] "GET /api/items HTTP/1.1" 200 175 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:10 +0000] "GET /api/items HTTP/1.1" 200 4125 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:10 +0000] "GET /api/items HTTP/1.1" 200 4109 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:10 +0000] "GET /api/items HTTP/1.1" 200 3154 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:10 +0000] "GET /api/items HTTP/1.1" 200 4438 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:10 +0000] "GET /api/items HTTP/1.1" 200 2781 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:10 +0000] "GET /api/items HTTP/1.1" 200 2212 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:11 +0000] "GET /api/items HTTP/1.1" 200 1878 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:11 +0000] "GET /api/items HTTP/1.1" 200 1389 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:11 +0000] "GET /api/items HTTP/1.1" 200 3225 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:11 +0000] "GET /api/items HTTP/1.1" 200 3828 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:11 +0000] "GET /api/items HTTP/1.1" 200 1292 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:11 +0000] "GET /api/items HTTP/1.1" 200 1154 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:11 +0000] "GET /api/items HTTP/1.1" 200 1231 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:11 +0000] "GET /api/items HTTP/1.1" 200 2589 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:11 +0000] "GET /api/items HTTP/1.1" 200 3569 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:11 +0000] "GET /api/items HTTP/1.1" 200 4250 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:12 +0000] "GET /api/items HTTP/1.1" 200 3414 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:12 +0000] "GET /api/items HTTP/1.1" 200 2762 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:12 +0000] "GET /api/items HTTP/1.1" 200 3342 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:12 +0000] "GET /api/items HTTP/1.1" 200 3051 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:12 +0000] "GET /api/items HTTP/1.1" 200 3092 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:12 +0000] "GET /api/items HTTP/1.1" 200 2347 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:12 +0000] "GET /api/items HTTP/1.1" 200 2924 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:12 +0000] "GET /api/items HTTP/1.1" 200 4128 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:12 +0000] "GET /api/items HTTP/1.1" 200 3676 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:12 +0000] "GET /api/items HTTP/1.1" 200 4171 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:13 +0000] "GET /api/items HTTP/1.1" 200 3270 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:13 +0000] "GET /api/items HTTP/1.1" 200 3289 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:13 +0000] "GET /api/items HTTP/1.1" 200 4078 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:13 +0000] "GET /api/items HTTP/1.1" 200 4263 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:13 +0000] "GET /api/items HTTP/1.1" 200 2151 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:13 +0000] "GET /api/items HTTP/1.1" 200 2467 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:13 +0000] "GET /api/items HTTP/1.1" 200 549 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:13 +0000] "GET /api/items HTTP/1.1" 200 1665 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:13 +0000] "GET /api/items HTTP/1.1" 200 3074 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:13 +0000] "GET /api/items HTTP/1.1" 200 1622 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:14 +0000] "GET /api/items HTTP/1.1" 200 2274 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:14 +0000] "GET /api/items HTTP/1.1" 200 2032 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:14 +0000] "GET /api/items HTTP/1.1" 200 957 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:14 +0000] "GET /api/items HTTP/1.1" 200 625 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:14 +0000] "GET /api/items HTTP/1.1" 200 2356 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:14 +0000] "GET /api/items HTTP/1.1" 200 3604 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:14 +0000] "GET /api/items HTTP/1.1" 200 4739 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:14 +0000] "GET /api/items HTTP/1.1" 200 1841 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:14 +0000] "GET /api/items HTTP/1.1" 200 3838 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:14 +0000] "GET /api/items HTTP/1.1" 200 3638 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:15 +0000] "GET /api/items HTTP/1.1" 200 4814 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:15 +0000] "GET /api/items HTTP/1.1" 200 3802 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:15 +0000] "GET /api/items HTTP/1.1" 200 4910 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:15 +0000] "GET /api/items HTTP/1.1" 200 524 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:15 +0000] "GET /api/items HTTP/1.1" 200 3149 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:15 +0000] "GET /api/items HTTP/1.1" 200 1074 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:15 +0000] "GET /api/items HTTP/1.1" 200 1036 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:15 +0000] "GET /api/items HTTP/1.1" 200 557 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:15 +0000] "GET /api/items HTTP/1.1" 200 1815 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:15 +0000] "GET /api/items HTTP/1.1" 200 4390 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:16 +0000] "GET /api/items HTTP/1.1" 200 705 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:16 +0000] "GET /api/items HTTP/1.1" 200 4877 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:16 +0000] "GET /api/items HTTP/1.1" 200 2944 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:16 +0000] "GET /api/items HTTP/1.1" 200 2476 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:16 +0000] "GET /api/items HTTP/1.1" 200 4297 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:16 +0000] "GET /api/items HTTP/1.1" 200 1385 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:16 +0000] "GET /api/items HTTP/1.1" 200 1929 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:16 +0000] "GET /api/items HTTP/1.1" 200 1230 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:16 +0000] "GET /api/items HTTP/1.1" 200 4592 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:16 +0000] "GET /api/items HTTP/1.1" 200 4456 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:17 +0000] "GET /api/items HTTP/1.1" 200 3077 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:17 +0000] "GET /api/items HTTP/1.1" 200 3182 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:17 +0000] "GET /api/items HTTP/1.1" 200 2760 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:17 +0000] "GET /api/items HTTP/1.1" 200 2023 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:17 +0000] "GET /api/items HTTP/1.1" 200 905 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:17 +0000] "GET /api/items HTTP/1.1" 200 1991 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:17 +0000] "GET /api/items HTTP/1.1" 200 3961 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:17 +0000] "GET /api/items HTTP/1.1" 200 382 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:17 +0000] "GET /api/items HTTP/1.1" 200 384 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:17 +0000] "GET /api/items HTTP/1.1" 200 469 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:18 +0000] "GET /api/items HTTP/1.1" 200 2339 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:18 +0000] "GET /api/items HTTP/1.1" 200 1927 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:18 +0000] "GET /api/items HTTP/1.1" 200 3228 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:18 +0000] "GET /api/items HTTP/1.1" 200 3295 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:18 +0000] "GET /api/items HTTP/1.1" 200 4595 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:18 +0000] "GET /api/items HTTP/1.1" 200 1053 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:18 +0000] "GET /api/items HTTP/1.1" 200 1467 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:18 +0000] "GET /api/items HTTP/1.1" 200 168 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:18 +0000] "GET /api/items HTTP/1.1" 200 2386 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:18 +0000] "GET /api/items HTTP/1.1" 200 1250 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:19 +0000] "GET /api/items HTTP/1.1" 200 1108 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:19 +0000] "GET /api/items HTTP/1.1" 200 1696 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:19 +0000] "GET /api/items HTTP/1.1" 200 3290 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:19 +0000] "GET /api/items HTTP/1.1" 200 4633 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:19 +0000] "GET /api/items HTTP/1.1" 200 1481 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:19 +0000] "GET /api/items HTTP/1.1" 200 1032 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:19 +0000] "GET /api/items HTTP/1.1" 200 4650 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:19 +0000] "GET /api/items HTTP/1.1" 200 2375 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:19 +0000] "GET /api/items HTTP/1.1" 200 487 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:19 +0000] "GET /api/items HTTP/1.1" 200 3121 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:20 +0000] "GET /api/items HTTP/1.1" 200 150 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:20 +0000] "GET /api/items HTTP/1.1" 200 3533 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:20 +0000] "GET /api/items HTTP/1.1" 200 3121 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:20 +0000] "GET /api/items HTTP/1.1" 200 2742 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:20 +0000] "GET /api/items HTTP/1.1" 200 4317 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:20 +0000] "GET /api/items HTTP/1.1" 200 291 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:20 +0000] "GET /api/items HTTP/1.1" 200 4251 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:20 +0000] "GET /api/items HTTP/1.1" 200 1985 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:20 +0000] "GET /api/items HTTP/1.1" 200 2146 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:20 +0000] "GET /api/items HTTP/1.1" 200 4827 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:21 +0000] "GET /api/items HTTP/1.1" 200 2292 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:21 +0000] "GET /api/items HTTP/1.1" 200 2660 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:21 +0000] "GET /api/items HTTP/1.1" 200 4584 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:21 +0000] "GET /api/items HTTP/1.1" 200 1885 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:21 +0000] "GET /api/items HTTP/1.1" 200 3490 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:21 +0000] "GET /api/items HTTP/1.1" 200 4101 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:21 +0000] "GET /api/items HTTP/1.1" 200 1409 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:21 +0000] "GET /api/items HTTP/1.1" 200 2613 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:21 +0000] "GET /api/items HTTP/1.1" 200 256 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:21 +0000] "GET /api/items HTTP/1.1" 200 263 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:22 +0000] "GET /api/items HTTP/1.1" 200 178 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:22 +0000] "GET /api/items HTTP/1.1" 200 336 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:22 +0000] "GET /api/items HTTP/1.1" 200 3676 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:22 +0000] "GET /api/items HTTP/1.1" 200 2344 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:22 +0000] "GET /api/items HTTP/1.1" 200 144 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:22 +0000] "GET /api/items HTTP/1.1" 200 3645 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:22 +0000] "GET /api/items HTTP/1.1" 200 4351 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:22 +0000] "GET /api/items HTTP/1.1" 200 1895 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:22 +0000] "GET /api/items HTTP/1.1" 200 4163 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:22 +0000] "GET /api/items HTTP/1.1" 200 2101 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:23 +0000] "GET /api/items HTTP/1.1" 200 2159 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:23 +0000] "GET /api/items HTTP/1.1" 200 3450 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:23 +0000] "GET /api/items HTTP/1.1" 200 4035 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:23 +0000] "GET /api/items HTTP/1.1" 200 397 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:23 +0000] "GET /api/items HTTP/1.1" 200 2983 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:23 +0000] "GET /api/items HTTP/1.1" 200 4812 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:23 +0000] "GET /api/items HTTP/1.1" 200 3600 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:23 +0000] "GET /api/items HTTP/1.1" 200 4880 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:23 +0000] "GET /api/items HTTP/1.1" 200 4310 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:23 +0000] "GET /api/items HTTP/1.1" 200 341 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:24 +0000] "GET /api/items HTTP/1.1" 200 295 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:24 +0000] "GET /api/items HTTP/1.1" 200 4617 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:24 +0000] "GET /api/items HTTP/1.1" 200 1195 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:24 +0000] "GET /api/items HTTP/1.1" 200 4299 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:24 +0000] "GET /api/items HTTP/1.1" 200 4870 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:24 +0000] "GET /api/items HTTP/1.1" 200 510 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:24 +0000] "GET /api/items HTTP/1.1" 200 1755 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:24 +0000] "GET /api/items HTTP/1.1" 200 707 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:24 +0000] "GET /api/items HTTP/1.1" 200 3175 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:24 +0000] "GET /api/items HTTP/1.1" 200 2784 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:25 +0000] "GET /api/items HTTP/1.1" 200 3445 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:25 +0000] "GET /api/items HTTP/1.1" 200 2903 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:25 +0000] "GET /api/items HTTP/1.1" 200 1071 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:25 +0000] "GET /api/items HTTP/1.1" 200 4868 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:25 +0000] "GET /api/items HTTP/1.1" 200 1963 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:25 +0000] "GET /api/items HTTP/1.1" 200 2146 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:25 +0000] "GET /api/items HTTP/1.1" 200 3963 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:25 +0000] "GET /api/items HTTP/1.1" 200 3390 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:25 +0000] "GET /api/items HTTP/1.1" 200 2712 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:25 +0000] "GET /api/items HTTP/1.1" 200 782 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:26 +0000] "GET /api/items HTTP/1.1" 200 1294 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:26 +0000] "GET /api/items HTTP/1.1" 200 2207 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:26 +0000] "GET /api/items HTTP/1.1" 200 3194 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:26 +0000] "GET /api/items HTTP/1.1" 200 623 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:26 +0000] "GET /api/items HTTP/1.1" 200 1425 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:26 +0000] "GET /api/items HTTP/1.1" 200 4796 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:26 +0000] "GET /api/items HTTP/1.1" 200 1351 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:26 +0000] "GET /api/items HTTP/1.1" 200 817 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:26 +0000] "GET /api/items HTTP/1.1" 200 3762 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:26 +0000] "GET /api/items HTTP/1.1" 200 3034 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:27 +0000] "GET /api/items HTTP/1.1" 200 1697 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:27 +0000] "GET /api/items HTTP/1.1" 200 1107 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:27 +0000] "GET /api/items HTTP/1.1" 200 1155 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:27 +0000] "GET /api/items HTTP/1.1" 200 412 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:27 +0000] "GET /api/items HTTP/1.1" 200 4508 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:27 +0000] "GET /api/items HTTP/1.1" 200 260 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:27 +0000] "GET /api/items HTTP/1.1" 200 2832 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:27 +0000] "GET /api/items HTTP/1.1" 200 3207 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:27 +0000] "GET /api/items HTTP/1.1" 200 2215 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:27 +0000] "GET /api/items HTTP/1.1" 200 4736 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:28 +0000] "GET /api/items HTTP/1.1" 200 4727 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:28 +0000] "GET /api/items HTTP/1.1" 200 422 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:28 +0000] "GET /api/items HTTP/1.1" 200 4471 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:28 +0000] "GET /api/items HTTP/1.1" 200 1012 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:28 +0000] "GET /api/items HTTP/1.1" 200 4415 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:28 +0000] "GET /api/items HTTP/1.1" 200 2340 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:28 +0000] "GET /api/items HTTP/1.1" 200 371 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:28 +0000] "GET /api/items HTTP/1.1" 200 396 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:28 +0000] "GET /api/items HTTP/1.1" 200 1062 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:28 +0000] "GET /api/items HTTP/1.1" 200 1031 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:29 +0000] "GET /api/items HTTP/1.1" 200 4399 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:29 +0000] "GET /api/items HTTP/1.1" 200 2537 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:29 +0000] "GET /api/items HTTP/1.1" 200 3198 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:29 +0000] "GET /api/items HTTP/1.1" 200 1012 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:29 +0000] "GET /api/items HTTP/1.1" 200 955 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:29 +0000] "GET /api/items HTTP/1.1" 200 2359 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:29 +0000] "GET /api/items HTTP/1.1" 200 3349 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:29 +0000] "GET /api/items HTTP/1.1" 200 1161 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:29 +0000] "GET /api/items HTTP/1.1" 200 985 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:29 +0000] "GET /api/items HTTP/1.1" 200 367 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:30 +0000] "GET /api/items HTTP/1.1" 200 1641 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:30 +0000] "GET /api/items HTTP/1.1" 200 2858 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:30 +0000] "GET /api/items HTTP/1.1" 200 4276 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:30 +0000] "GET /api/items HTTP/1.1" 200 1728 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:30 +0000] "GET /api/items HTTP/1.1" 200 4898 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:30 +0000] "GET /api/items HTTP/1.1" 200 3172 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:30 +0000] "GET /api/items HTTP/1.1" 200 166 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:30 +0000] "GET /api/items HTTP/1.1" 200 2360 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:30 +0000] "GET /api/items HTTP/1.1" 200 4562 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:30 +0000] "GET /api/items HTTP/1.1" 200 2717 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:31 +0000] "GET /api/items HTTP/1.1" 200 4169 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:31 +0000] "GET /api/items HTTP/1.1" 200 4698 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:31 +0000] "GET /api/items HTTP/1.1" 200 4756 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:31 +0000] "GET /api/items HTTP/1.1" 200 3350 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:31 +0000] "GET /api/items HTTP/1.1" 200 1828 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:31 +0000] "GET /api/items HTTP/1.1" 200 2052 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:31 +0000] "GET /api/items HTTP/1.1" 200 252 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:31 +0000] "GET /api/items HTTP/1.1" 200 3429 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:31 +0000] "GET /api/items HTTP/1.1" 200 2686 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:31 +0000] "GET /api/items HTTP/1.1" 200 879 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:32 +0000] "GET /api/items HTTP/1.1" 200 867 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:32 +0000] "GET /api/items HTTP/1.1" 200 4852 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:32 +0000] "GET /api/items HTTP/1.1" 200 2013 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:32 +0000] "GET /api/items HTTP/1.1" 200 4813 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:32 +0000] "GET /api/items HTTP/1.1" 200 552 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:32 +0000] "GET /api/items HTTP/1.1" 200 2118 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:32 +0000] "GET /api/items HTTP/1.1" 200 1345 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:32 +0000] "GET /api/items HTTP/1.1" 200 2091 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:32 +0000] "GET /api/items HTTP/1.1" 200 615 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:32 +0000] "GET /api/items HTTP/1.1" 200 486 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:33 +0000] "GET /api/items HTTP/1.1" 200 219 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:33 +0000] "GET /api/items HTTP/1.1" 200 379 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:33 +0000] "GET /api/items HTTP/1.1" 200 4891 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:33 +0000] "GET /api/items HTTP/1.1" 200 1674 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:33 +0000] "GET /api/items HTTP/1.1" 200 4124 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:33 +0000] "GET /api/items HTTP/1.1" 200 1700 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:33 +0000] "GET /api/items HTTP/1.1" 200 1424 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:33 +0000] "GET /api/items HTTP/1.1" 200 2128 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:33 +0000] "GET /api/items HTTP/1.1" 200 2446 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:33 +0000] "GET /api/items HTTP/1.1" 200 114 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:34 +0000] "GET /api/items HTTP/1.1" 200 3150 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:34 +0000] "GET /api/items HTTP/1.1" 200 122 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:34 +0000] "GET /api/items HTTP/1.1" 200 1068 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:34 +0000] "GET /api/items HTTP/1.1" 200 3567 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:34 +0000] "GET /api/items HTTP/1.1" 200 1999 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:34 +0000] "GET /api/items HTTP/1.1" 200 639 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:34 +0000] "GET /api/items HTTP/1.1" 200 1487 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:34 +0000] "GET /api/items HTTP/1.1" 200 3188 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:34 +0000] "GET /api/items HTTP/1.1" 200 3573 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:34 +0000] "GET /api/items HTTP/1.1" 200 818 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:35 +0000] "GET /api/items HTTP/1.1" 200 2523 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:35 +0000] "GET /api/items HTTP/1.1" 200 4694 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:35 +0000] "GET /api/items HTTP/1.1" 200 779 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:35 +0000] "GET /api/items HTTP/1.1" 200 3526 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:35 +0000] "GET /api/items HTTP/1.1" 200 2450 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:35 +0000] "GET /api/items HTTP/1.1" 200 4837 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:35 +0000] "GET /api/items HTTP/1.1" 200 2673 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:35 +0000] "GET /api/items HTTP/1.1" 200 2382 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:35 +0000] "GET /api/items HTTP/1.1" 200 2610 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:35 +0000] "GET /api/items HTTP/1.1" 200 4119 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:36 +0000] "GET /api/items HTTP/1.1" 200 2679 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:36 +0000] "GET /api/items HTTP/1.1" 200 3845 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:36 +0000] "GET /api/items HTTP/1.1" 200 2970 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:36 +0000] "GET /api/items HTTP/1.1" 200 4139 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:36 +0000] "GET /api/items HTTP/1.1" 200 3234 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:36 +0000] "GET /api/items HTTP/1.1" 200 551 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:36 +0000] "GET /api/items HTTP/1.1" 200 266 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:36 +0000] "GET /api/items HTTP/1.1" 200 4146 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:36 +0000] "GET /api/items HTTP/1.1" 200 3082 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:36 +0000] "GET /api/items HTTP/1.1" 200 212 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:37 +0000] "GET /api/items HTTP/1.1" 200 1747 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:37 +0000] "GET /api/items HTTP/1.1" 200 2122 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:37 +0000] "GET /api/items HTTP/1.1" 200 4084 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:37 +0000] "GET /api/items HTTP/1.1" 200 1291 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:37 +0000] "GET /api/items HTTP/1.1" 200 1625 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:37 +0000] "GET /api/items HTTP/1.1" 200 3233 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:37 +0000] "GET /api/items HTTP/1.1" 200 2805 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:37 +0000] "GET /api/items HTTP/1.1" 200 2891 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:37 +0000] "GET /api/items HTTP/1.1" 200 651 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:37 +0000] "GET /api/items HTTP/1.1" 200 2075 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:38 +0000] "GET /api/items HTTP/1.1" 200 3633 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:38 +0000] "GET /api/items HTTP/1.1" 200 4736 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:38 +0000] "GET /api/items HTTP/1.1" 200 4068 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:38 +0000] "GET /api/items HTTP/1.1" 200 2367 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:38 +0000] "GET /api/items HTTP/1.1" 200 4256 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:38 +0000] "GET /api/items HTTP/1.1" 200 4283 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:38 +0000] "GET /api/items HTTP/1.1" 200 4616 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:38 +0000] "GET /api/items HTTP/1.1" 200 1007 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:38 +0000] "GET /api/items HTTP/1.1" 200 2442 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:38 +0000] "GET /api/items HTTP/1.1" 200 3134 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:39 +0000] "GET /api/items HTTP/1.1" 200 3505 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:39 +0000] "GET /api/items HTTP/1.1" 200 4920 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:39 +0000] "GET /api/items HTTP/1.1" 200 1077 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:39 +0000] "GET /api/items HTTP/1.1" 200 2659 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:39 +0000] "GET /api/items HTTP/1.1" 200 1173 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:39 +0000] "GET /api/items HTTP/1.1" 200 4965 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:39 +0000] "GET /api/items HTTP/1.1" 200 3162 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:39 +0000] "GET /api/items HTTP/1.1" 200 1006 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:39 +0000] "GET /api/items HTTP/1.1" 200 4024 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:39 +0000] "GET /api/items HTTP/1.1" 200 1624 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:40 +0000] "GET /api/items HTTP/1.1" 200 3970 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:40 +0000] "GET /api/items HTTP/1.1" 200 4079 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:40 +0000] "GET /api/items HTTP/1.1" 200 4907 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:40 +0000] "GET /api/items HTTP/1.1" 200 261 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:40 +0000] "GET /api/items HTTP/1.1" 200 4451 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:40 +0000] "GET /api/items HTTP/1.1" 200 4752 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:40 +0000] "GET /api/items HTTP/1.1" 200 3692 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:40 +0000] "GET /api/items HTTP/1.1" 200 603 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:40 +0000] "GET /api/items HTTP/1.1" 200 3371 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:40 +0000] "GET /api/items HTTP/1.1" 200 3145 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:41 +0000] "GET /api/items HTTP/1.1" 200 779 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:41 +0000] "GET /api/items HTTP/1.1" 200 3992 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:41 +0000] "GET /api/items HTTP/1.1" 200 127 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:41 +0000] "GET /api/items HTTP/1.1" 200 3223 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:41 +0000] "GET /api/items HTTP/1.1" 200 3686 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:41 +0000] "GET /api/items HTTP/1.1" 200 4839 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:41 +0000] "GET /api/items HTTP/1.1" 200 3631 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:41 +0000] "GET /api/items HTTP/1.1" 200 2495 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:41 +0000] "GET /api/items HTTP/1.1" 200 2118 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:41 +0000] "GET /api/items HTTP/1.1" 200 3587 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:42 +0000] "GET /api/items HTTP/1.1" 200 2457 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:42 +0000] "GET /api/items HTTP/1.1" 200 2493 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:42 +0000] "GET /api/items HTTP/1.1" 200 3590 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:42 +0000] "GET /api/items HTTP/1.1" 200 2854 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:42 +0000] "GET /api/items HTTP/1.1" 200 1816 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:42 +0000] "GET /api/items HTTP/1.1" 200 1341 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:42 +0000] "GET /api/items HTTP/1.1" 200 753 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:42 +0000] "GET /api/items HTTP/1.1" 200 4735 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:42 +0000] "GET /api/items HTTP/1.1" 200 639 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:42 +0000] "GET /api/items HTTP/1.1" 200 2473 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:43 +0000] "GET /api/items HTTP/1.1" 200 1175 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:43 +0000] "GET /api/items HTTP/1.1" 200 4562 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:43 +0000] "GET /api/items HTTP/1.1" 200 337 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:43 +0000] "GET /api/items HTTP/1.1" 200 1915 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:43 +0000] "GET /api/items HTTP/1.1" 200 693 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:43 +0000] "GET /api/items HTTP/1.1" 200 615 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:43 +0000] "GET /api/items HTTP/1.1" 200 582 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:43 +0000] "GET /api/items HTTP/1.1" 200 2405 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:43 +0000] "GET /api/items HTTP/1.1" 200 4059 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:43 +0000] "GET /api/items HTTP/1.1" 200 1936 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:44 +0000] "GET /api/items HTTP/1.1" 200 1042 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:44 +0000] "GET /api/items HTTP/1.1" 200 206 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:44 +0000] "GET /api/items HTTP/1.1" 200 3275 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:44 +0000] "GET /api/items HTTP/1.1" 200 435 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:44 +0000] "GET /api/items HTTP/1.1" 200 588 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:44 +0000] "GET /api/items HTTP/1.1" 200 4799 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:44 +0000] "GET /api/items HTTP/1.1" 200 1167 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:44 +0000] "GET /api/items HTTP/1.1" 200 4085 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:44 +0000] "GET /api/items HTTP/1.1" 200 624 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:44 +0000] "GET /api/items HTTP/1.1" 200 4829 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:45 +0000] "GET /api/items HTTP/1.1" 200 1163 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:45 +0000] "GET /api/items HTTP/1.1" 200 3164 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:45 +0000] "GET /api/items HTTP/1.1" 200 1097 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:45 +0000] "GET /api/items HTTP/1.1" 200 804 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:45 +0000] "GET /api/items HTTP/1.1" 200 1185 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:45 +0000] "GET /api/items HTTP/1.1" 200 1258 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:45 +0000] "GET /api/items HTTP/1.1" 200 1473 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:45 +0000] "GET /api/items HTTP/1.1" 200 1285 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:45 +0000] "GET /api/items HTTP/1.1" 200 2288 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:45 +0000] "GET /api/items HTTP/1.1" 200 739 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:46 +0000] "GET /api/items HTTP/1.1" 200 3822 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:46 +0000] "GET /api/items HTTP/1.1" 200 712 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:46 +0000] "GET /api/items HTTP/1.1" 200 2927 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:46 +0000] "GET /api/items HTTP/1.1" 200 4899 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:46 +0000] "GET /api/items HTTP/1.1" 200 4754 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:46 +0000] "GET /api/items HTTP/1.1" 200 959 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:46 +0000] "GET /api/items HTTP/1.1" 200 4532 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:46 +0000] "GET /api/items HTTP/1.1" 200 3524 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:46 +0000] "GET /api/items HTTP/1.1" 200 3851 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:46 +0000] "GET /api/items HTTP/1.1" 200 3639 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:47 +0000] "GET /api/items HTTP/1.1" 200 2678 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:47 +0000] "GET /api/items HTTP/1.1" 200 1683 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:47 +0000] "GET /api/items HTTP/1.1" 200 4264 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:47 +0000] "GET /api/items HTTP/1.1" 200 1828 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:47 +0000] "GET /api/items HTTP/1.1" 200 1004 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:47 +0000] "GET /api/items HTTP/1.1" 200 2103 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:47 +0000] "GET /api/items HTTP/1.1" 200 1218 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:47 +0000] "GET /api/items HTTP/1.1" 200 1228 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:47 +0000] "GET /api/items HTTP/1.1" 200 1917 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:47 +0000] "GET /api/items HTTP/1.1" 200 2896 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:48 +0000] "GET /api/items HTTP/1.1" 200 1814 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:48 +0000] "GET /api/items HTTP/1.1" 200 1949 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:48 +0000] "GET /api/items HTTP/1.1" 200 846 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:48 +0000] "GET /api/items HTTP/1.1" 200 2723 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:48 +0000] "GET /api/items HTTP/1.1" 200 3270 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:48 +0000] "GET /api/items HTTP/1.1" 200 1377 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:48 +0000] "GET /api/items HTTP/1.1" 200 2551 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:48 +0000] "GET /api/items HTTP/1.1" 200 435 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:48 +0000] "GET /api/items HTTP/1.1" 200 4623 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:48 +0000] "GET /api/items HTTP/1.1" 200 849 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:49 +0000] "GET /api/items HTTP/1.1" 200 3169 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:49 +0000] "GET /api/items HTTP/1.1" 200 2509 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:49 +0000] "GET /api/items HTTP/1.1" 200 345 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:49 +0000] "GET /api/items HTTP/1.1" 200 4773 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:49 +0000] "GET /api/items HTTP/1.1" 200 1657 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:49 +0000] "GET /api/items HTTP/1.1" 200 2517 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:49 +0000] "GET /api/items HTTP/1.1" 200 407 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:49 +0000] "GET /api/items HTTP/1.1" 200 228 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:49 +0000] "GET /api/items HTTP/1.1" 200 4847 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:49 +0000] "GET /api/items HTTP/1.1" 200 3800 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:50 +0000] "GET /api/items HTTP/1.1" 200 2714 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:50 +0000] "GET /api/items HTTP/1.1" 200 2049 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:50 +0000] "GET /api/items HTTP/1.1" 200 4699 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:50 +0000] "GET /api/items HTTP/1.1" 200 2057 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:50 +0000] "GET /api/items HTTP/1.1" 200 2474 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:50 +0000] "GET /api/items HTTP/1.1" 200 2474 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:50 +0000] "GET /api/items HTTP/1.1" 200 4227 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:50 +0000] "GET /api/items HTTP/1.1" 200 976 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:50 +0000] "GET /api/items HTTP/1.1" 200 2851 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:50 +0000] "GET /api/items HTTP/1.1" 200 1427 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:51 +0000] "GET /api/items HTTP/1.1" 200 2975 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:51 +0000] "GET /api/items HTTP/1.1" 200 3233 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:51 +0000] "GET /api/items HTTP/1.1" 200 2866 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:51 +0000] "GET /api/items HTTP/1.1" 200 3987 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:51 +0000] "GET /api/items HTTP/1.1" 200 851 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:51 +0000] "GET /api/items HTTP/1.1" 200 1100 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:51 +0000] "GET /api/items HTTP/1.1" 200 3223 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:51 +0000] "GET /api/items HTTP/1.1" 200 1590 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:51 +0000] "GET /api/items HTTP/1.1" 200 3111 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:51 +0000] "GET /api/items HTTP/1.1" 200 2949 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:52 +0000] "GET /api/items HTTP/1.1" 200 3141 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:52 +0000] "GET /api/items HTTP/1.1" 200 3889 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:52 +0000] "GET /api/items HTTP/1.1" 200 4915 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:52 +0000] "GET /api/items HTTP/1.1" 200 4701 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:52 +0000] "GET /api/items HTTP/1.1" 200 2290 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:52 +0000] "GET /api/items HTTP/1.1" 200 3074 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:52 +0000] "GET /api/items HTTP/1.1" 200 3828 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:52 +0000] "GET /api/items HTTP/1.1" 200 3327 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:52 +0000] "GET /api/items HTTP/1.1" 200 314 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:52 +0000] "GET /api/items HTTP/1.1" 200 3353 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:53 +0000] "GET /api/items HTTP/1.1" 200 4670 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:53 +0000] "GET /api/items HTTP/1.1" 200 4228 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:53 +0000] "GET /api/items HTTP/1.1" 200 2010 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:53 +0000] "GET /api/items HTTP/1.1" 200 2872 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:53 +0000] "GET /api/items HTTP/1.1" 200 4537 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:53 +0000] "GET /api/items HTTP/1.1" 200 4863 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:53 +0000] "GET /api/items HTTP/1.1" 200 3775 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:53 +0000] "GET /api/items HTTP/1.1" 200 3683 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:53 +0000] "GET /api/items HTTP/1.1" 200 4553 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:53 +0000] "GET /api/items HTTP/1.1" 200 2299 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:54 +0000] "GET /api/items HTTP/1.1" 200 2815 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:54 +0000] "GET /api/items HTTP/1.1" 200 1276 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:54 +0000] "GET /api/items HTTP/1.1" 200 3360 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:54 +0000] "GET /api/items HTTP/1.1" 200 3462 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:54 +0000] "GET /api/items HTTP/1.1" 200 443 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:54 +0000] "GET /api/items HTTP/1.1" 200 4927 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:54 +0000] "GET /api/items HTTP/1.1" 200 3967 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:54 +0000] "GET /api/items HTTP/1.1" 200 1882 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:54 +0000] "GET /api/items HTTP/1.1" 200 2065 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:54 +0000] "GET /api/items HTTP/1.1" 200 2919 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:55 +0000] "GET /api/items HTTP/1.1" 200 852 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:55 +0000] "GET /api/items HTTP/1.1" 200 4962 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:55 +0000] "GET /api/items HTTP/1.1" 200 197 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:55 +0000] "GET /api/items HTTP/1.1" 200 3129 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:55 +0000] "GET /api/items HTTP/1.1" 200 4335 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:55 +0000] "GET /api/items HTTP/1.1" 200 1748 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:55 +0000] "GET /api/items HTTP/1.1" 200 1170 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:55 +0000] "GET /api/items HTTP/1.1" 200 169 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:55 +0000] "GET /api/items HTTP/1.1" 200 2050 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:55 +0000] "GET /api/items HTTP/1.1" 200 1615 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:56 +0000] "GET /api/items HTTP/1.1" 200 3566 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:56 +0000] "GET /api/items HTTP/1.1" 200 4955 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:56 +0000] "GET /api/items HTTP/1.1" 200 208 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:56 +0000] "GET /api/items HTTP/1.1" 200 3752 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:56 +0000] "GET /api/items HTTP/1.1" 200 3401 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:56 +0000] "GET /api/items HTTP/1.1" 200 4317 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:56 +0000] "GET /api/items HTTP/1.1" 200 3180 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:56 +0000] "GET /api/items HTTP/1.1" 200 1872 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:56 +0000] "GET /api/items HTTP/1.1" 200 1843 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:56 +0000] "GET /api/items HTTP/1.1" 200 3998 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:57 +0000] "GET /api/items HTTP/1.1" 200 4028 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:57 +0000] "GET /api/items HTTP/1.1" 200 3853 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:57 +0000] "GET /api/items HTTP/1.1" 200 2479 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:57 +0000] "GET /api/items HTTP/1.1" 200 3962 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:57 +0000] "GET /api/items HTTP/1.1" 200 4029 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:57 +0000] "GET /api/items HTTP/1.1" 200 2510 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:57 +0000] "GET /api/items HTTP/1.1" 200 2289 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:57 +0000] "GET /api/items HTTP/1.1" 200 911 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:57 +0000] "GET /api/items HTTP/1.1" 200 2754 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:57 +0000] "GET /api/items HTTP/1.1" 200 3574 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:58 +0000] "GET /api/items HTTP/1.1" 200 2137 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:58 +0000] "GET /api/items HTTP/1.1" 200 109 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:58 +0000] "GET /api/items HTTP/1.1" 200 3129 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:58 +0000] "GET /api/items HTTP/1.1" 200 3517 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:58 +0000] "GET /api/items HTTP/1.1" 200 1253 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:58 +0000] "GET /api/items HTTP/1.1" 200 2467 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:58 +0000] "GET /api/items HTTP/1.1" 200 4381 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:58 +0000] "GET /api/items HTTP/1.1" 200 1742 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:58 +0000] "GET /api/items HTTP/1.1" 200 2119 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:58 +0000] "GET /api/items HTTP/1.1" 200 1112 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:59 +0000] "GET /api/items HTTP/1.1" 200 554 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:59 +0000] "GET /api/items HTTP/1.1" 200 1289 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:59 +0000] "GET /api/items HTTP/1.1" 200 932 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:59 +0000] "GET /api/items HTTP/1.1" 200 942 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:59 +0000] "GET /api/items HTTP/1.1" 200 3687 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:59 +0000] "GET /api/items HTTP/1.1" 200 4591 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:59 +0000] "GET /api/items HTTP/1.1" 200 307 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:59 +0000] "GET /api/items HTTP/1.1" 200 3655 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:59 +0000] "GET /api/items HTTP/1.1" 200 3559 "-" "Mozilla/5.0"
198.51.100.12 - - [01/Sep/2026:10:20:59 +0000] "GET /api/items HTTP/1.1" 200 274 "-" "Mozilla/5.0"
```

## 192.0.2.30 — 2026-09-01 10:21:00+00:00

**Reason:** 50% POST share, avg payload 15785 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=15785.000, post_share=0.500

**Exact log lines:**

```text
192.0.2.30 - - [01/Sep/2026:10:21:08 +0000] "GET /about HTTP/1.1" 400 16154 "-" "Mozilla/5.0"
192.0.2.30 - - [01/Sep/2026:10:21:34 +0000] "POST /api/search HTTP/1.1" 304 15416 "-" "Mozilla/5.0"
```

## 192.0.2.60 — 2026-09-01 10:21:00+00:00

**Reason:** 12 unique URLs

**Features:** requests_per_minute=17, error_404_ratio=0.176, unique_urls=12, avg_payload_size=5940.647, post_share=0.059

**Exact log lines:**

```text
192.0.2.60 - - [01/Sep/2026:10:21:03 +0000] "GET /search?q=phone HTTP/1.1" 500 12299 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:08 +0000] "GET / HTTP/1.1" 304 3291 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:08 +0000] "GET /index.html HTTP/1.1" 200 4425 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:10 +0000] "GET /static/app.js HTTP/1.1" 200 8024 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:11 +0000] "GET /api/items/1 HTTP/1.1" 201 2407 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:21 +0000] "GET /api/items HTTP/1.1" 200 4135 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:24 +0000] "GET /products/1 HTTP/1.1" 403 4124 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:25 +0000] "GET /api/items HTTP/1.1" 200 1713 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:40 +0000] "GET /contact HTTP/1.1" 200 12888 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:47 +0000] "GET /old-page HTTP/1.1" 404 4456 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:48 +0000] "GET /does-not-exist HTTP/1.1" 404 1074 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:48 +0000] "GET /login HTTP/1.1" 304 11696 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:49 +0000] "GET /search?q=phone HTTP/1.1" 200 1047 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:50 +0000] "GET /does-not-exist HTTP/1.1" 404 4170 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:51 +0000] "GET /static/app.js HTTP/1.1" 200 12215 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:54 +0000] "POST /api/search HTTP/1.1" 401 6321 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:21:58 +0000] "GET /static/app.js HTTP/1.1" 200 6706 "-" "Mozilla/5.0"
```

## 192.0.2.29 — 2026-09-01 10:22:00+00:00

**Reason:** 13 unique URLs

**Features:** requests_per_minute=19, error_404_ratio=0.263, unique_urls=13, avg_payload_size=8853.000, post_share=0.105

**Exact log lines:**

```text
192.0.2.29 - - [01/Sep/2026:10:22:00 +0000] "GET /search?q=phone HTTP/1.1" 201 2090 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:02 +0000] "POST /api/items HTTP/1.1" 200 1076 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:09 +0000] "GET /search?q=phone HTTP/1.1" 204 1965 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:10 +0000] "GET /missing HTTP/1.1" 404 12459 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:14 +0000] "GET /favicon.ico HTTP/1.1" 200 8700 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:16 +0000] "GET /about HTTP/1.1" 200 16920 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:17 +0000] "GET /old-page HTTP/1.1" 404 4508 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:19 +0000] "GET /products/2 HTTP/1.1" 200 15074 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:20 +0000] "GET /old-page HTTP/1.1" 404 9837 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:22 +0000] "POST /api/search HTTP/1.1" 301 8106 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:22 +0000] "GET /does-not-exist HTTP/1.1" 404 14376 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:22 +0000] "GET /search?q=phone HTTP/1.1" 200 1901 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:24 +0000] "GET /products HTTP/1.1" 200 1893 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:28 +0000] "GET /static/style.css HTTP/1.1" 200 14408 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:32 +0000] "GET /about HTTP/1.1" 200 16021 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:33 +0000] "GET /index.html HTTP/1.1" 201 160 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:35 +0000] "GET / HTTP/1.1" 200 16740 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:41 +0000] "GET /static/style.css HTTP/1.1" 201 10536 "-" "Mozilla/5.0"
192.0.2.29 - - [01/Sep/2026:10:22:53 +0000] "GET /old-page HTTP/1.1" 404 11437 "-" "Mozilla/5.0"
```

## 192.0.2.60 — 2026-09-01 10:22:00+00:00

**Reason:** 13 unique URLs

**Features:** requests_per_minute=18, error_404_ratio=0.222, unique_urls=13, avg_payload_size=8581.000, post_share=0.167

**Exact log lines:**

```text
192.0.2.60 - - [01/Sep/2026:10:22:02 +0000] "POST /login HTTP/1.1" 200 3610 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:03 +0000] "POST /api/items HTTP/1.1" 200 14383 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:10 +0000] "GET /products/2 HTTP/1.1" 200 7279 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:11 +0000] "POST /login HTTP/1.1" 200 5119 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:15 +0000] "GET /static/app.js HTTP/1.1" 201 197 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:23 +0000] "GET /favicon.ico HTTP/1.1" 304 11567 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:29 +0000] "GET /products HTTP/1.1" 200 17802 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:32 +0000] "GET /static/app.js HTTP/1.1" 200 3041 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:39 +0000] "GET /index.html HTTP/1.1" 200 4122 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:39 +0000] "GET /old-page HTTP/1.1" 404 8282 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:40 +0000] "GET /old-page HTTP/1.1" 404 5451 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:41 +0000] "GET /products/2 HTTP/1.1" 201 15062 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:46 +0000] "GET /api/items/1 HTTP/1.1" 200 14882 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:48 +0000] "GET /products HTTP/1.1" 304 16998 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:48 +0000] "GET /does-not-exist HTTP/1.1" 404 12679 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:51 +0000] "GET / HTTP/1.1" 200 5934 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:52 +0000] "GET /missing HTTP/1.1" 404 1689 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:22:56 +0000] "GET /contact HTTP/1.1" 201 6361 "-" "Mozilla/5.0"
```

## 192.0.2.47 — 2026-09-01 10:23:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=2, avg_payload_size=5625.000, post_share=0.333

**Exact log lines:**

```text
192.0.2.47 - - [01/Sep/2026:10:23:17 +0000] "POST /login HTTP/1.1" 404 12011 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:23:18 +0000] "GET /login HTTP/1.1" 201 2656 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:23:43 +0000] "GET /about HTTP/1.1" 200 2208 "-" "Mozilla/5.0"
```

## 192.0.2.15 — 2026-09-01 10:24:00+00:00

**Reason:** avg payload 12268 bytes

**Features:** requests_per_minute=6, error_404_ratio=0.667, unique_urls=5, avg_payload_size=12268.500, post_share=0.333

**Exact log lines:**

```text
192.0.2.15 - - [01/Sep/2026:10:24:04 +0000] "POST /login HTTP/1.1" 200 14348 "-" "Mozilla/5.0"
192.0.2.15 - - [01/Sep/2026:10:24:07 +0000] "GET /missing HTTP/1.1" 404 15371 "-" "Mozilla/5.0"
192.0.2.15 - - [01/Sep/2026:10:24:33 +0000] "GET /does-not-exist HTTP/1.1" 404 11868 "-" "Mozilla/5.0"
192.0.2.15 - - [01/Sep/2026:10:24:37 +0000] "GET /products/2 HTTP/1.1" 200 15982 "-" "Mozilla/5.0"
192.0.2.15 - - [01/Sep/2026:10:24:37 +0000] "POST /api/search HTTP/1.1" 404 15130 "-" "Mozilla/5.0"
192.0.2.15 - - [01/Sep/2026:10:24:42 +0000] "GET /missing HTTP/1.1" 404 912 "-" "Mozilla/5.0"
```

## 192.0.2.18 — 2026-09-01 10:25:00+00:00

**Reason:** 67% POST share, avg payload 12079 bytes

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=2, avg_payload_size=12078.667, post_share=0.667

**Exact log lines:**

```text
192.0.2.18 - - [01/Sep/2026:10:25:22 +0000] "POST /api/search HTTP/1.1" 200 10823 "-" "Mozilla/5.0"
192.0.2.18 - - [01/Sep/2026:10:25:35 +0000] "POST /api/search HTTP/1.1" 200 16924 "-" "Mozilla/5.0"
192.0.2.18 - - [01/Sep/2026:10:25:36 +0000] "GET /old-page HTTP/1.1" 404 8489 "-" "Mozilla/5.0"
```

## 192.0.2.26 — 2026-09-01 10:25:00+00:00

**Reason:** 50% POST share, avg payload 12138 bytes

**Features:** requests_per_minute=6, error_404_ratio=0.167, unique_urls=4, avg_payload_size=12137.500, post_share=0.500

**Exact log lines:**

```text
192.0.2.26 - - [01/Sep/2026:10:25:04 +0000] "POST /login HTTP/1.1" 404 11346 "-" "Mozilla/5.0"
192.0.2.26 - - [01/Sep/2026:10:25:10 +0000] "POST /api/search HTTP/1.1" 200 13918 "-" "Mozilla/5.0"
192.0.2.26 - - [01/Sep/2026:10:25:27 +0000] "GET /search?q=phone HTTP/1.1" 200 14438 "-" "Mozilla/5.0"
192.0.2.26 - - [01/Sep/2026:10:25:34 +0000] "GET /static/app.js HTTP/1.1" 200 12868 "-" "Mozilla/5.0"
192.0.2.26 - - [01/Sep/2026:10:25:43 +0000] "POST /api/search HTTP/1.1" 304 8367 "-" "Mozilla/5.0"
192.0.2.26 - - [01/Sep/2026:10:25:50 +0000] "GET /login HTTP/1.1" 304 11888 "-" "Mozilla/5.0"
```

## 192.0.2.31 — 2026-09-01 10:25:00+00:00

**Reason:** 50% POST share, avg payload 13878 bytes

**Features:** requests_per_minute=4, error_404_ratio=0.250, unique_urls=4, avg_payload_size=13878.500, post_share=0.500

**Exact log lines:**

```text
192.0.2.31 - - [01/Sep/2026:10:25:25 +0000] "POST /api/items HTTP/1.1" 200 12790 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:10:25:40 +0000] "GET /products/1 HTTP/1.1" 304 13324 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:10:25:51 +0000] "POST /api/search HTTP/1.1" 200 13047 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:10:25:58 +0000] "GET /old-page HTTP/1.1" 404 16353 "-" "Mozilla/5.0"
```

## 192.0.2.12 — 2026-09-01 10:26:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=9020.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.12 - - [01/Sep/2026:10:26:18 +0000] "GET /old-page HTTP/1.1" 404 9209 "-" "Mozilla/5.0"
192.0.2.12 - - [01/Sep/2026:10:26:41 +0000] "GET /static/app.js HTTP/1.1" 304 8832 "-" "Mozilla/5.0"
```

## 192.0.2.18 — 2026-09-01 10:27:00+00:00

**Reason:** 50% POST share

**Features:** requests_per_minute=4, error_404_ratio=0.500, unique_urls=4, avg_payload_size=6916.000, post_share=0.500

**Exact log lines:**

```text
192.0.2.18 - - [01/Sep/2026:10:27:02 +0000] "GET /missing HTTP/1.1" 404 3745 "-" "Mozilla/5.0"
192.0.2.18 - - [01/Sep/2026:10:27:15 +0000] "GET /products/1 HTTP/1.1" 200 12935 "-" "Mozilla/5.0"
192.0.2.18 - - [01/Sep/2026:10:27:35 +0000] "POST /api/search HTTP/1.1" 404 7992 "-" "Mozilla/5.0"
192.0.2.18 - - [01/Sep/2026:10:27:39 +0000] "POST /api/items HTTP/1.1" 201 2992 "-" "Mozilla/5.0"
```

## 192.0.2.27 — 2026-09-01 10:27:00+00:00

**Reason:** 11 unique URLs

**Features:** requests_per_minute=15, error_404_ratio=0.333, unique_urls=11, avg_payload_size=8264.067, post_share=0.400

**Exact log lines:**

```text
192.0.2.27 - - [01/Sep/2026:10:27:05 +0000] "POST /api/search HTTP/1.1" 404 12250 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:07 +0000] "GET /products/1 HTTP/1.1" 200 2997 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:08 +0000] "GET /products HTTP/1.1" 200 15630 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:09 +0000] "GET /api/items/1 HTTP/1.1" 301 14540 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:10 +0000] "GET /products HTTP/1.1" 200 10084 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:18 +0000] "GET /index.html HTTP/1.1" 500 8072 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:19 +0000] "POST /api/search HTTP/1.1" 404 8279 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:28 +0000] "POST /api/items HTTP/1.1" 404 1775 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:30 +0000] "GET / HTTP/1.1" 200 15324 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:32 +0000] "GET /static/style.css HTTP/1.1" 200 718 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:34 +0000] "GET /old-page HTTP/1.1" 404 1398 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:37 +0000] "POST /login HTTP/1.1" 404 14909 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:37 +0000] "POST /login HTTP/1.1" 200 4877 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:39 +0000] "POST /login HTTP/1.1" 200 2758 "-" "Mozilla/5.0"
192.0.2.27 - - [01/Sep/2026:10:27:50 +0000] "GET /products/2 HTTP/1.1" 200 10350 "-" "Mozilla/5.0"
```

## 192.0.2.48 — 2026-09-01 10:27:00+00:00

**Reason:** 10 unique URLs, avg payload 12489 bytes

**Features:** requests_per_minute=16, error_404_ratio=0.375, unique_urls=10, avg_payload_size=12488.875, post_share=0.188

**Exact log lines:**

```text
192.0.2.48 - - [01/Sep/2026:10:27:01 +0000] "GET / HTTP/1.1" 200 17796 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:04 +0000] "POST /api/search HTTP/1.1" 404 15343 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:05 +0000] "GET /old-page HTTP/1.1" 404 10252 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:06 +0000] "GET /old-page HTTP/1.1" 404 16077 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:13 +0000] "GET /products/1 HTTP/1.1" 200 16469 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:15 +0000] "GET /does-not-exist HTTP/1.1" 404 14558 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:22 +0000] "GET /does-not-exist HTTP/1.1" 404 10252 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:23 +0000] "GET / HTTP/1.1" 200 16512 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:25 +0000] "GET /old-page HTTP/1.1" 404 10740 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:31 +0000] "GET /api/items/1 HTTP/1.1" 200 10790 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:35 +0000] "GET /products HTTP/1.1" 401 15662 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:43 +0000] "GET /about HTTP/1.1" 200 1105 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:46 +0000] "POST /api/search HTTP/1.1" 200 16940 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:55 +0000] "POST /api/items HTTP/1.1" 200 6490 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:57 +0000] "GET / HTTP/1.1" 200 7581 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:27:58 +0000] "GET /products/2 HTTP/1.1" 304 13255 "-" "Mozilla/5.0"
```

## 192.0.2.20 — 2026-09-01 10:28:00+00:00

**Reason:** 12 unique URLs

**Features:** requests_per_minute=16, error_404_ratio=0.188, unique_urls=12, avg_payload_size=5591.562, post_share=0.062

**Exact log lines:**

```text
192.0.2.20 - - [01/Sep/2026:10:28:00 +0000] "GET /index.html HTTP/1.1" 200 2427 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:06 +0000] "GET /static/style.css HTTP/1.1" 200 12544 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:14 +0000] "GET /search?q=phone HTTP/1.1" 200 3917 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:15 +0000] "POST /login HTTP/1.1" 200 6025 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:15 +0000] "GET /products/1 HTTP/1.1" 200 296 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:17 +0000] "GET /api/items HTTP/1.1" 304 11641 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:19 +0000] "GET / HTTP/1.1" 200 12346 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:24 +0000] "GET /products/2 HTTP/1.1" 200 3219 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:24 +0000] "GET /old-page HTTP/1.1" 404 3153 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:25 +0000] "GET /login HTTP/1.1" 204 1582 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:28 +0000] "GET /api/items HTTP/1.1" 201 7228 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:33 +0000] "GET /static/style.css HTTP/1.1" 201 1545 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:44 +0000] "GET / HTTP/1.1" 200 8153 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:45 +0000] "GET /does-not-exist HTTP/1.1" 404 2896 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:48 +0000] "GET /api/items/1 HTTP/1.1" 200 3045 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:28:51 +0000] "GET /missing HTTP/1.1" 404 9448 "-" "Mozilla/5.0"
```

## 192.0.2.24 — 2026-09-01 10:28:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=4, error_404_ratio=0.750, unique_urls=3, avg_payload_size=8450.250, post_share=0.250

**Exact log lines:**

```text
192.0.2.24 - - [01/Sep/2026:10:28:03 +0000] "GET /favicon.ico HTTP/1.1" 200 10515 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:28:05 +0000] "GET /missing HTTP/1.1" 404 14886 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:28:26 +0000] "POST /api/items HTTP/1.1" 404 4163 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:28:39 +0000] "GET /missing HTTP/1.1" 404 4237 "-" "Mozilla/5.0"
```

## 192.0.2.15 — 2026-09-01 10:29:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=6036.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.15 - - [01/Sep/2026:10:29:22 +0000] "GET /static/app.js HTTP/1.1" 304 8619 "-" "Mozilla/5.0"
192.0.2.15 - - [01/Sep/2026:10:29:54 +0000] "GET /contact HTTP/1.1" 200 3453 "-" "Mozilla/5.0"
```

## 192.0.2.23 — 2026-09-01 10:29:00+00:00

**Reason:** avg payload 13931 bytes

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=2, avg_payload_size=13931.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.23 - - [01/Sep/2026:10:29:06 +0000] "GET /login HTTP/1.1" 200 9259 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:29:24 +0000] "GET / HTTP/1.1" 200 16805 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:29:33 +0000] "GET /login HTTP/1.1" 200 15729 "-" "Mozilla/5.0"
```

## 192.0.2.59 — 2026-09-01 10:30:00+00:00

**Reason:** 11 unique URLs, avg payload 10532 bytes

**Features:** requests_per_minute=19, error_404_ratio=0.158, unique_urls=11, avg_payload_size=10531.895, post_share=0.211

**Exact log lines:**

```text
192.0.2.59 - - [01/Sep/2026:10:30:04 +0000] "GET /api/items/1 HTTP/1.1" 200 8841 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:09 +0000] "GET /static/app.js HTTP/1.1" 200 515 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:10 +0000] "GET /old-page HTTP/1.1" 404 10957 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:11 +0000] "GET /products/1 HTTP/1.1" 200 15558 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:13 +0000] "POST /api/items HTTP/1.1" 404 9031 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:14 +0000] "GET /products HTTP/1.1" 304 4041 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:15 +0000] "GET /about HTTP/1.1" 200 15376 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:18 +0000] "POST /login HTTP/1.1" 400 14036 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:28 +0000] "GET /login HTTP/1.1" 200 17125 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:39 +0000] "GET /login HTTP/1.1" 304 13335 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:40 +0000] "POST /login HTTP/1.1" 200 15562 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:41 +0000] "GET /api/items HTTP/1.1" 200 6750 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:43 +0000] "GET /does-not-exist HTTP/1.1" 404 17841 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:44 +0000] "GET /static/app.js HTTP/1.1" 200 13286 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:46 +0000] "POST /api/items HTTP/1.1" 301 3570 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:49 +0000] "GET /about HTTP/1.1" 200 11525 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:50 +0000] "GET /index.html HTTP/1.1" 304 4794 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:53 +0000] "GET /index.html HTTP/1.1" 200 5528 "-" "Mozilla/5.0"
192.0.2.59 - - [01/Sep/2026:10:30:56 +0000] "GET /favicon.ico HTTP/1.1" 200 12435 "-" "Mozilla/5.0"
```

## 192.0.2.18 — 2026-09-01 10:31:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=3, avg_payload_size=2264.333, post_share=0.000

**Exact log lines:**

```text
192.0.2.18 - - [01/Sep/2026:10:31:04 +0000] "GET /products HTTP/1.1" 204 3426 "-" "Mozilla/5.0"
192.0.2.18 - - [01/Sep/2026:10:31:37 +0000] "GET /products/1 HTTP/1.1" 500 1645 "-" "Mozilla/5.0"
192.0.2.18 - - [01/Sep/2026:10:31:57 +0000] "GET /old-page HTTP/1.1" 404 1722 "-" "Mozilla/5.0"
```

## 192.0.2.47 — 2026-09-01 10:31:00+00:00

**Reason:** 13 unique URLs

**Features:** requests_per_minute=18, error_404_ratio=0.278, unique_urls=13, avg_payload_size=8434.278, post_share=0.000

**Exact log lines:**

```text
192.0.2.47 - - [01/Sep/2026:10:31:00 +0000] "GET /api/items/1 HTTP/1.1" 200 6380 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:02 +0000] "GET /products HTTP/1.1" 200 6634 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:08 +0000] "GET /missing HTTP/1.1" 404 630 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:12 +0000] "GET /does-not-exist HTTP/1.1" 404 1484 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:14 +0000] "GET /favicon.ico HTTP/1.1" 201 223 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:25 +0000] "GET /static/app.js HTTP/1.1" 403 9454 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:30 +0000] "GET /old-page HTTP/1.1" 404 15558 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:34 +0000] "GET /missing HTTP/1.1" 404 15056 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:34 +0000] "GET /login HTTP/1.1" 304 1933 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:37 +0000] "GET /products HTTP/1.1" 201 10890 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:38 +0000] "GET /index.html HTTP/1.1" 200 15607 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:42 +0000] "GET /search?q=phone HTTP/1.1" 301 3089 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:43 +0000] "GET /about HTTP/1.1" 304 14021 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:43 +0000] "GET /static/style.css HTTP/1.1" 201 16829 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:48 +0000] "GET /products/1 HTTP/1.1" 200 7124 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:55 +0000] "GET /products/1 HTTP/1.1" 304 7555 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:55 +0000] "GET /products HTTP/1.1" 200 11540 "-" "Mozilla/5.0"
192.0.2.47 - - [01/Sep/2026:10:31:59 +0000] "GET /old-page HTTP/1.1" 404 7810 "-" "Mozilla/5.0"
```

## 192.0.2.43 — 2026-09-01 10:32:00+00:00

**Reason:** 13 unique URLs, avg payload 10740 bytes

**Features:** requests_per_minute=17, error_404_ratio=0.118, unique_urls=13, avg_payload_size=10740.294, post_share=0.176

**Exact log lines:**

```text
192.0.2.43 - - [01/Sep/2026:10:32:01 +0000] "POST /api/items HTTP/1.1" 200 8210 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:03 +0000] "GET /old-page HTTP/1.1" 404 12977 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:07 +0000] "GET /products/1 HTTP/1.1" 200 12161 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:07 +0000] "GET /login HTTP/1.1" 200 7741 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:08 +0000] "POST /api/items HTTP/1.1" 200 6314 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:10 +0000] "GET /products/2 HTTP/1.1" 200 186 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:11 +0000] "POST /api/search HTTP/1.1" 204 16727 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:15 +0000] "GET / HTTP/1.1" 400 6902 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:19 +0000] "GET /products HTTP/1.1" 201 3850 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:22 +0000] "GET /missing HTTP/1.1" 404 12236 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:27 +0000] "GET /static/style.css HTTP/1.1" 200 16174 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:28 +0000] "GET /contact HTTP/1.1" 200 17359 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:33 +0000] "GET /favicon.ico HTTP/1.1" 200 13858 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:37 +0000] "GET /static/app.js HTTP/1.1" 200 14210 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:42 +0000] "GET /contact HTTP/1.1" 200 16868 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:45 +0000] "GET /favicon.ico HTTP/1.1" 200 13030 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:32:53 +0000] "GET /contact HTTP/1.1" 200 3782 "-" "Mozilla/5.0"
```

## 192.0.2.57 — 2026-09-01 10:32:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=3210.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.57 - - [01/Sep/2026:10:32:18 +0000] "GET /login HTTP/1.1" 200 4803 "-" "Mozilla/5.0"
192.0.2.57 - - [01/Sep/2026:10:32:53 +0000] "GET /favicon.ico HTTP/1.1" 200 1618 "-" "Mozilla/5.0"
```

## 192.0.2.54 — 2026-09-01 10:33:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=1558.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.54 - - [01/Sep/2026:10:33:45 +0000] "GET /products/2 HTTP/1.1" 200 852 "-" "Mozilla/5.0"
192.0.2.54 - - [01/Sep/2026:10:33:49 +0000] "GET /old-page HTTP/1.1" 404 2264 "-" "Mozilla/5.0"
```

## 192.0.2.14 — 2026-09-01 10:34:00+00:00

**Reason:** 60% POST share

**Features:** requests_per_minute=5, error_404_ratio=0.200, unique_urls=4, avg_payload_size=4556.000, post_share=0.600

**Exact log lines:**

```text
192.0.2.14 - - [01/Sep/2026:10:34:00 +0000] "GET /does-not-exist HTTP/1.1" 404 5758 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:10:34:08 +0000] "POST /api/items HTTP/1.1" 200 2179 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:10:34:13 +0000] "POST /api/search HTTP/1.1" 200 4902 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:10:34:18 +0000] "POST /api/search HTTP/1.1" 200 6958 "-" "Mozilla/5.0"
192.0.2.14 - - [01/Sep/2026:10:34:46 +0000] "GET /contact HTTP/1.1" 500 2983 "-" "Mozilla/5.0"
```

## 192.0.2.33 — 2026-09-01 10:34:00+00:00

**Reason:** avg payload 14318 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=14318.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.33 - - [01/Sep/2026:10:34:32 +0000] "GET /missing HTTP/1.1" 404 11445 "-" "Mozilla/5.0"
192.0.2.33 - - [01/Sep/2026:10:34:51 +0000] "GET /static/app.js HTTP/1.1" 200 17191 "-" "Mozilla/5.0"
```

## 192.0.2.44 — 2026-09-01 10:36:00+00:00

**Reason:** avg payload 11535 bytes

**Features:** requests_per_minute=3, error_404_ratio=0.667, unique_urls=2, avg_payload_size=11534.667, post_share=0.000

**Exact log lines:**

```text
192.0.2.44 - - [01/Sep/2026:10:36:27 +0000] "GET /missing HTTP/1.1" 404 3255 "-" "Mozilla/5.0"
192.0.2.44 - - [01/Sep/2026:10:36:38 +0000] "GET /missing HTTP/1.1" 404 15933 "-" "Mozilla/5.0"
192.0.2.44 - - [01/Sep/2026:10:36:58 +0000] "GET /static/style.css HTTP/1.1" 301 15416 "-" "Mozilla/5.0"
```

## 192.0.2.46 — 2026-09-01 10:36:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=4, error_404_ratio=0.750, unique_urls=3, avg_payload_size=7190.750, post_share=0.000

**Exact log lines:**

```text
192.0.2.46 - - [01/Sep/2026:10:36:00 +0000] "GET /api/items HTTP/1.1" 200 6878 "-" "Mozilla/5.0"
192.0.2.46 - - [01/Sep/2026:10:36:01 +0000] "GET /does-not-exist HTTP/1.1" 404 4662 "-" "Mozilla/5.0"
192.0.2.46 - - [01/Sep/2026:10:36:15 +0000] "GET /old-page HTTP/1.1" 404 11699 "-" "Mozilla/5.0"
192.0.2.46 - - [01/Sep/2026:10:36:45 +0000] "GET /does-not-exist HTTP/1.1" 404 5524 "-" "Mozilla/5.0"
```

## 192.0.2.54 — 2026-09-01 10:36:00+00:00

**Reason:** 50% POST share

**Features:** requests_per_minute=6, error_404_ratio=0.667, unique_urls=5, avg_payload_size=8291.667, post_share=0.500

**Exact log lines:**

```text
192.0.2.54 - - [01/Sep/2026:10:36:17 +0000] "POST /login HTTP/1.1" 404 13846 "-" "Mozilla/5.0"
192.0.2.54 - - [01/Sep/2026:10:36:19 +0000] "GET /missing HTTP/1.1" 404 11880 "-" "Mozilla/5.0"
192.0.2.54 - - [01/Sep/2026:10:36:20 +0000] "POST /api/items HTTP/1.1" 404 7102 "-" "Mozilla/5.0"
192.0.2.54 - - [01/Sep/2026:10:36:43 +0000] "GET /api/items/1 HTTP/1.1" 200 6318 "-" "Mozilla/5.0"
192.0.2.54 - - [01/Sep/2026:10:36:53 +0000] "GET /about HTTP/1.1" 200 8906 "-" "Mozilla/5.0"
192.0.2.54 - - [01/Sep/2026:10:36:55 +0000] "POST /api/items HTTP/1.1" 404 1698 "-" "Mozilla/5.0"
```

## 192.0.2.50 — 2026-09-01 10:37:00+00:00

**Reason:** avg payload 14314 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=14313.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.50 - - [01/Sep/2026:10:37:19 +0000] "GET /missing HTTP/1.1" 404 15360 "-" "Mozilla/5.0"
192.0.2.50 - - [01/Sep/2026:10:37:55 +0000] "GET /static/app.js HTTP/1.1" 200 13267 "-" "Mozilla/5.0"
```

## 192.0.2.57 — 2026-09-01 10:37:00+00:00

**Reason:** 50% POST share, avg payload 12629 bytes

**Features:** requests_per_minute=4, error_404_ratio=0.250, unique_urls=3, avg_payload_size=12629.000, post_share=0.500

**Exact log lines:**

```text
192.0.2.57 - - [01/Sep/2026:10:37:15 +0000] "GET /does-not-exist HTTP/1.1" 404 13743 "-" "Mozilla/5.0"
192.0.2.57 - - [01/Sep/2026:10:37:28 +0000] "POST /api/search HTTP/1.1" 200 17803 "-" "Mozilla/5.0"
192.0.2.57 - - [01/Sep/2026:10:37:35 +0000] "GET /index.html HTTP/1.1" 304 17218 "-" "Mozilla/5.0"
192.0.2.57 - - [01/Sep/2026:10:37:56 +0000] "POST /api/search HTTP/1.1" 200 1752 "-" "Mozilla/5.0"
```

## 192.0.2.31 — 2026-09-01 10:39:00+00:00

**Reason:** 50% POST share

**Features:** requests_per_minute=6, error_404_ratio=0.333, unique_urls=4, avg_payload_size=5419.333, post_share=0.500

**Exact log lines:**

```text
192.0.2.31 - - [01/Sep/2026:10:39:06 +0000] "POST /api/search HTTP/1.1" 204 11731 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:10:39:08 +0000] "GET /missing HTTP/1.1" 404 2655 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:10:39:11 +0000] "POST /api/search HTTP/1.1" 200 4064 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:10:39:18 +0000] "GET /products HTTP/1.1" 304 7821 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:10:39:56 +0000] "GET /old-page HTTP/1.1" 404 983 "-" "Mozilla/5.0"
192.0.2.31 - - [01/Sep/2026:10:39:57 +0000] "POST /api/search HTTP/1.1" 304 5262 "-" "Mozilla/5.0"
```

## 192.0.2.34 — 2026-09-01 10:39:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=2, avg_payload_size=8145.000, post_share=0.333

**Exact log lines:**

```text
192.0.2.34 - - [01/Sep/2026:10:39:12 +0000] "POST /api/items HTTP/1.1" 200 16686 "-" "Mozilla/5.0"
192.0.2.34 - - [01/Sep/2026:10:39:44 +0000] "GET /api/items/1 HTTP/1.1" 200 6981 "-" "Mozilla/5.0"
192.0.2.34 - - [01/Sep/2026:10:39:48 +0000] "GET /api/items HTTP/1.1" 200 768 "-" "Mozilla/5.0"
```

## 192.0.2.43 — 2026-09-01 10:39:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=435.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.43 - - [01/Sep/2026:10:39:49 +0000] "GET / HTTP/1.1" 200 435 "-" "Mozilla/5.0"
```

## 192.0.2.39 — 2026-09-01 10:40:00+00:00

**Reason:** 13 unique URLs

**Features:** requests_per_minute=19, error_404_ratio=0.211, unique_urls=13, avg_payload_size=8047.895, post_share=0.000

**Exact log lines:**

```text
192.0.2.39 - - [01/Sep/2026:10:40:05 +0000] "GET /static/style.css HTTP/1.1" 200 17751 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:09 +0000] "GET /products/1 HTTP/1.1" 304 3894 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:12 +0000] "GET /old-page HTTP/1.1" 404 4521 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:13 +0000] "GET /products HTTP/1.1" 200 15779 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:13 +0000] "GET /api/items HTTP/1.1" 200 958 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:13 +0000] "GET /contact HTTP/1.1" 200 9842 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:18 +0000] "GET /index.html HTTP/1.1" 200 1180 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:20 +0000] "GET /about HTTP/1.1" 200 12887 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:25 +0000] "GET /api/items HTTP/1.1" 201 4743 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:28 +0000] "GET /api/items HTTP/1.1" 400 4247 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:29 +0000] "GET /api/items HTTP/1.1" 200 14664 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:30 +0000] "GET / HTTP/1.1" 403 12288 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:31 +0000] "GET /old-page HTTP/1.1" 404 14556 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:32 +0000] "GET /static/style.css HTTP/1.1" 200 236 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:39 +0000] "GET /login HTTP/1.1" 200 11034 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:41 +0000] "GET /products/2 HTTP/1.1" 304 480 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:56 +0000] "GET /old-page HTTP/1.1" 404 12734 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:58 +0000] "GET /does-not-exist HTTP/1.1" 404 8760 "-" "Mozilla/5.0"
192.0.2.39 - - [01/Sep/2026:10:40:58 +0000] "GET /api/items/1 HTTP/1.1" 201 2356 "-" "Mozilla/5.0"
```

## 192.0.2.58 — 2026-09-01 10:40:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=5, error_404_ratio=0.400, unique_urls=3, avg_payload_size=6039.600, post_share=0.400

**Exact log lines:**

```text
192.0.2.58 - - [01/Sep/2026:10:40:10 +0000] "POST /login HTTP/1.1" 200 7529 "-" "Mozilla/5.0"
192.0.2.58 - - [01/Sep/2026:10:40:14 +0000] "POST /login HTTP/1.1" 200 8198 "-" "Mozilla/5.0"
192.0.2.58 - - [01/Sep/2026:10:40:16 +0000] "GET /does-not-exist HTTP/1.1" 404 10886 "-" "Mozilla/5.0"
192.0.2.58 - - [01/Sep/2026:10:40:45 +0000] "GET /products/2 HTTP/1.1" 200 3332 "-" "Mozilla/5.0"
192.0.2.58 - - [01/Sep/2026:10:40:46 +0000] "GET /does-not-exist HTTP/1.1" 404 253 "-" "Mozilla/5.0"
```

## 192.0.2.12 — 2026-09-01 10:41:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=3, avg_payload_size=4590.333, post_share=0.333

**Exact log lines:**

```text
192.0.2.12 - - [01/Sep/2026:10:41:37 +0000] "GET /login HTTP/1.1" 301 6670 "-" "Mozilla/5.0"
192.0.2.12 - - [01/Sep/2026:10:41:42 +0000] "POST /api/search HTTP/1.1" 301 3041 "-" "Mozilla/5.0"
192.0.2.12 - - [01/Sep/2026:10:41:44 +0000] "GET /about HTTP/1.1" 200 4060 "-" "Mozilla/5.0"
```

## 192.0.2.17 — 2026-09-01 10:41:00+00:00

**Reason:** 100% 404 ratio, avg payload 11924 bytes

**Features:** requests_per_minute=4, error_404_ratio=1.000, unique_urls=2, avg_payload_size=11924.500, post_share=0.250

**Exact log lines:**

```text
192.0.2.17 - - [01/Sep/2026:10:41:24 +0000] "GET /old-page HTTP/1.1" 404 13764 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:10:41:44 +0000] "GET /old-page HTTP/1.1" 404 16265 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:10:41:46 +0000] "GET /old-page HTTP/1.1" 404 9907 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:10:41:47 +0000] "POST /api/items HTTP/1.1" 404 7762 "-" "Mozilla/5.0"
```

## 192.0.2.44 — 2026-09-01 10:41:00+00:00

**Reason:** avg payload 11723 bytes

**Features:** requests_per_minute=3, error_404_ratio=0.000, unique_urls=2, avg_payload_size=11722.667, post_share=0.333

**Exact log lines:**

```text
192.0.2.44 - - [01/Sep/2026:10:41:03 +0000] "GET /login HTTP/1.1" 400 14861 "-" "Mozilla/5.0"
192.0.2.44 - - [01/Sep/2026:10:41:20 +0000] "GET /login HTTP/1.1" 200 17935 "-" "Mozilla/5.0"
192.0.2.44 - - [01/Sep/2026:10:41:31 +0000] "POST /api/items HTTP/1.1" 400 2372 "-" "Mozilla/5.0"
```

## 192.0.2.48 — 2026-09-01 10:41:00+00:00

**Reason:** 50% POST share

**Features:** requests_per_minute=6, error_404_ratio=0.333, unique_urls=3, avg_payload_size=8717.000, post_share=0.500

**Exact log lines:**

```text
192.0.2.48 - - [01/Sep/2026:10:41:03 +0000] "POST /api/items HTTP/1.1" 400 13687 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:41:14 +0000] "GET /missing HTTP/1.1" 404 2024 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:41:14 +0000] "GET /favicon.ico HTTP/1.1" 200 5824 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:41:25 +0000] "POST /api/items HTTP/1.1" 200 12998 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:41:27 +0000] "POST /api/items HTTP/1.1" 404 16195 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:41:37 +0000] "GET /api/items HTTP/1.1" 403 1574 "-" "Mozilla/5.0"
```

## 192.0.2.20 — 2026-09-01 10:42:00+00:00

**Reason:** 50% POST share

**Features:** requests_per_minute=4, error_404_ratio=0.000, unique_urls=3, avg_payload_size=8991.750, post_share=0.500

**Exact log lines:**

```text
192.0.2.20 - - [01/Sep/2026:10:42:22 +0000] "POST /api/search HTTP/1.1" 200 9090 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:42:24 +0000] "POST /login HTTP/1.1" 200 7470 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:42:38 +0000] "GET /search?q=phone HTTP/1.1" 301 15376 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:42:58 +0000] "GET /login HTTP/1.1" 200 4031 "-" "Mozilla/5.0"
```

## 192.0.2.43 — 2026-09-01 10:42:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=3, avg_payload_size=6724.333, post_share=0.333

**Exact log lines:**

```text
192.0.2.43 - - [01/Sep/2026:10:42:02 +0000] "GET /contact HTTP/1.1" 200 9900 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:42:37 +0000] "POST /api/items HTTP/1.1" 200 4256 "-" "Mozilla/5.0"
192.0.2.43 - - [01/Sep/2026:10:42:50 +0000] "GET /does-not-exist HTTP/1.1" 404 6017 "-" "Mozilla/5.0"
```

## 192.0.2.56 — 2026-09-01 10:43:00+00:00

**Reason:** avg payload 13628 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=13628.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.56 - - [01/Sep/2026:10:43:16 +0000] "GET / HTTP/1.1" 200 15374 "-" "Mozilla/5.0"
192.0.2.56 - - [01/Sep/2026:10:43:31 +0000] "GET /does-not-exist HTTP/1.1" 404 11883 "-" "Mozilla/5.0"
```

## 192.0.2.24 — 2026-09-01 10:44:00+00:00

**Reason:** 11 unique URLs, avg payload 11042 bytes

**Features:** requests_per_minute=18, error_404_ratio=0.389, unique_urls=11, avg_payload_size=11041.556, post_share=0.000

**Exact log lines:**

```text
192.0.2.24 - - [01/Sep/2026:10:44:00 +0000] "GET /favicon.ico HTTP/1.1" 200 2442 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:01 +0000] "GET /old-page HTTP/1.1" 404 14745 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:10 +0000] "GET /search?q=phone HTTP/1.1" 200 17485 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:12 +0000] "GET /products HTTP/1.1" 200 14666 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:14 +0000] "GET /old-page HTTP/1.1" 404 11141 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:19 +0000] "GET /api/items/1 HTTP/1.1" 200 5812 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:22 +0000] "GET /missing HTTP/1.1" 404 12532 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:23 +0000] "GET /old-page HTTP/1.1" 404 16051 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:26 +0000] "GET /missing HTTP/1.1" 404 14483 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:31 +0000] "GET /does-not-exist HTTP/1.1" 404 15688 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:31 +0000] "GET /static/app.js HTTP/1.1" 401 2383 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:36 +0000] "GET /products/1 HTTP/1.1" 201 10907 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:38 +0000] "GET /old-page HTTP/1.1" 404 6158 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:40 +0000] "GET /api/items HTTP/1.1" 200 11066 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:45 +0000] "GET /products/1 HTTP/1.1" 200 12824 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:45 +0000] "GET /search?q=phone HTTP/1.1" 401 15860 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:51 +0000] "GET /search?q=phone HTTP/1.1" 403 1066 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:10:44:52 +0000] "GET /static/style.css HTTP/1.1" 204 13439 "-" "Mozilla/5.0"
```

## 192.0.2.21 — 2026-09-01 10:45:00+00:00

**Reason:** 13 unique URLs

**Features:** requests_per_minute=19, error_404_ratio=0.105, unique_urls=13, avg_payload_size=9443.737, post_share=0.105

**Exact log lines:**

```text
192.0.2.21 - - [01/Sep/2026:10:45:00 +0000] "GET /login HTTP/1.1" 304 7293 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:01 +0000] "GET /contact HTTP/1.1" 200 17570 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:11 +0000] "GET /login HTTP/1.1" 200 1001 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:12 +0000] "GET /api/items HTTP/1.1" 204 9174 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:20 +0000] "GET /products/2 HTTP/1.1" 200 4723 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:20 +0000] "GET /static/app.js HTTP/1.1" 304 16940 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:21 +0000] "GET /about HTTP/1.1" 201 5156 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:26 +0000] "GET /about HTTP/1.1" 200 5377 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:27 +0000] "GET /products/1 HTTP/1.1" 200 11782 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:28 +0000] "GET /static/style.css HTTP/1.1" 403 8049 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:28 +0000] "GET /login HTTP/1.1" 301 14534 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:30 +0000] "GET /products HTTP/1.1" 204 7506 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:33 +0000] "GET /index.html HTTP/1.1" 201 17229 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:39 +0000] "POST /api/search HTTP/1.1" 200 14387 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:40 +0000] "GET /missing HTTP/1.1" 404 16769 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:48 +0000] "GET /index.html HTTP/1.1" 200 5009 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:49 +0000] "GET /products HTTP/1.1" 200 7836 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:58 +0000] "GET /does-not-exist HTTP/1.1" 404 4894 "-" "Mozilla/5.0"
192.0.2.21 - - [01/Sep/2026:10:45:58 +0000] "POST /api/items HTTP/1.1" 301 4202 "-" "Mozilla/5.0"
```

## 192.0.2.10 — 2026-09-01 10:48:00+00:00

**Reason:** 12 unique URLs

**Features:** requests_per_minute=18, error_404_ratio=0.222, unique_urls=12, avg_payload_size=9724.944, post_share=0.222

**Exact log lines:**

```text
192.0.2.10 - - [01/Sep/2026:10:48:05 +0000] "GET /missing HTTP/1.1" 404 981 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:07 +0000] "GET /products HTTP/1.1" 200 10516 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:11 +0000] "POST /api/items HTTP/1.1" 200 2904 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:15 +0000] "GET /does-not-exist HTTP/1.1" 404 17815 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:16 +0000] "POST /api/search HTTP/1.1" 400 246 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:17 +0000] "GET /products/2 HTTP/1.1" 200 8582 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:20 +0000] "GET /about HTTP/1.1" 304 10595 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:22 +0000] "GET /products/1 HTTP/1.1" 200 7119 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:23 +0000] "GET /login HTTP/1.1" 200 14956 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:27 +0000] "POST /api/items HTTP/1.1" 404 506 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:33 +0000] "GET /static/app.js HTTP/1.1" 200 14457 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:34 +0000] "GET /static/app.js HTTP/1.1" 200 7628 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:39 +0000] "GET /index.html HTTP/1.1" 200 14181 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:39 +0000] "GET /products HTTP/1.1" 200 15440 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:49 +0000] "GET /search?q=phone HTTP/1.1" 304 15026 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:50 +0000] "GET /api/items HTTP/1.1" 304 14924 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:53 +0000] "POST /api/items HTTP/1.1" 404 3932 "-" "Mozilla/5.0"
192.0.2.10 - - [01/Sep/2026:10:48:56 +0000] "GET /login HTTP/1.1" 200 15241 "-" "Mozilla/5.0"
```

## 192.0.2.33 — 2026-09-01 10:48:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=5675.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.33 - - [01/Sep/2026:10:48:58 +0000] "GET /static/style.css HTTP/1.1" 200 5675 "-" "Mozilla/5.0"
```

## 192.0.2.20 — 2026-09-01 10:49:00+00:00

**Reason:** avg payload 11966 bytes

**Features:** requests_per_minute=4, error_404_ratio=0.750, unique_urls=3, avg_payload_size=11966.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.20 - - [01/Sep/2026:10:49:11 +0000] "GET /old-page HTTP/1.1" 404 13319 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:49:35 +0000] "GET /does-not-exist HTTP/1.1" 404 13523 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:49:44 +0000] "GET /contact HTTP/1.1" 200 14245 "-" "Mozilla/5.0"
192.0.2.20 - - [01/Sep/2026:10:49:45 +0000] "GET /old-page HTTP/1.1" 404 6779 "-" "Mozilla/5.0"
```

## 192.0.2.46 — 2026-09-01 10:49:00+00:00

**Reason:** 50% POST share

**Features:** requests_per_minute=4, error_404_ratio=0.500, unique_urls=3, avg_payload_size=8535.750, post_share=0.500

**Exact log lines:**

```text
192.0.2.46 - - [01/Sep/2026:10:49:27 +0000] "GET /products/1 HTTP/1.1" 200 4255 "-" "Mozilla/5.0"
192.0.2.46 - - [01/Sep/2026:10:49:32 +0000] "POST /login HTTP/1.1" 404 7831 "-" "Mozilla/5.0"
192.0.2.46 - - [01/Sep/2026:10:49:34 +0000] "POST /api/items HTTP/1.1" 404 5212 "-" "Mozilla/5.0"
192.0.2.46 - - [01/Sep/2026:10:49:49 +0000] "GET /products/1 HTTP/1.1" 200 16845 "-" "Mozilla/5.0"
```

## 192.0.2.17 — 2026-09-01 10:51:00+00:00

**Reason:** 50% POST share, avg payload 12652 bytes

**Features:** requests_per_minute=4, error_404_ratio=0.250, unique_urls=4, avg_payload_size=12652.250, post_share=0.500

**Exact log lines:**

```text
192.0.2.17 - - [01/Sep/2026:10:51:08 +0000] "GET / HTTP/1.1" 200 8980 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:10:51:35 +0000] "POST /api/items HTTP/1.1" 200 16592 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:10:51:43 +0000] "POST /login HTTP/1.1" 400 9420 "-" "Mozilla/5.0"
192.0.2.17 - - [01/Sep/2026:10:51:51 +0000] "GET /does-not-exist HTTP/1.1" 404 15617 "-" "Mozilla/5.0"
```

## 192.0.2.48 — 2026-09-01 10:51:00+00:00

**Reason:** 12 unique URLs, avg payload 12911 bytes

**Features:** requests_per_minute=14, error_404_ratio=0.143, unique_urls=12, avg_payload_size=12910.786, post_share=0.071

**Exact log lines:**

```text
192.0.2.48 - - [01/Sep/2026:10:51:01 +0000] "GET /index.html HTTP/1.1" 200 13310 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:51:02 +0000] "GET /old-page HTTP/1.1" 404 13861 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:51:10 +0000] "GET /static/app.js HTTP/1.1" 200 7608 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:51:13 +0000] "GET /api/items/1 HTTP/1.1" 200 17667 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:51:15 +0000] "GET /search?q=phone HTTP/1.1" 200 14215 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:51:16 +0000] "GET /products HTTP/1.1" 200 17096 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:51:22 +0000] "POST /api/items HTTP/1.1" 200 17577 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:51:31 +0000] "GET /products/2 HTTP/1.1" 200 15867 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:51:35 +0000] "GET /products/1 HTTP/1.1" 200 1823 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:51:42 +0000] "GET /login HTTP/1.1" 200 15699 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:51:44 +0000] "GET /search?q=phone HTTP/1.1" 304 16527 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:51:50 +0000] "GET /products/2 HTTP/1.1" 500 2118 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:51:51 +0000] "GET /missing HTTP/1.1" 404 9943 "-" "Mozilla/5.0"
192.0.2.48 - - [01/Sep/2026:10:51:58 +0000] "GET /static/style.css HTTP/1.1" 403 17440 "-" "Mozilla/5.0"
```

## 192.0.2.40 — 2026-09-01 10:52:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=4, error_404_ratio=0.500, unique_urls=4, avg_payload_size=3337.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.40 - - [01/Sep/2026:10:52:05 +0000] "GET /products/2 HTTP/1.1" 204 5592 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:52:14 +0000] "GET /does-not-exist HTTP/1.1" 404 2991 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:52:23 +0000] "GET /index.html HTTP/1.1" 200 1197 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:52:55 +0000] "GET /old-page HTTP/1.1" 404 3568 "-" "Mozilla/5.0"
```

## 192.0.2.49 — 2026-09-01 10:54:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=3, error_404_ratio=0.333, unique_urls=3, avg_payload_size=5536.000, post_share=0.333

**Exact log lines:**

```text
192.0.2.49 - - [01/Sep/2026:10:54:27 +0000] "GET /products HTTP/1.1" 200 1693 "-" "Mozilla/5.0"
192.0.2.49 - - [01/Sep/2026:10:54:28 +0000] "POST /login HTTP/1.1" 200 13937 "-" "Mozilla/5.0"
192.0.2.49 - - [01/Sep/2026:10:54:34 +0000] "GET /old-page HTTP/1.1" 404 978 "-" "Mozilla/5.0"
```

## 192.0.2.40 — 2026-09-01 10:56:00+00:00

**Reason:** 12 unique URLs, avg payload 10164 bytes

**Features:** requests_per_minute=16, error_404_ratio=0.312, unique_urls=12, avg_payload_size=10163.875, post_share=0.000

**Exact log lines:**

```text
192.0.2.40 - - [01/Sep/2026:10:56:00 +0000] "GET /index.html HTTP/1.1" 500 17107 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:05 +0000] "GET / HTTP/1.1" 201 17750 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:05 +0000] "GET /favicon.ico HTTP/1.1" 200 15197 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:10 +0000] "GET /missing HTTP/1.1" 404 11638 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:11 +0000] "GET /login HTTP/1.1" 204 957 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:16 +0000] "GET /contact HTTP/1.1" 304 16256 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:25 +0000] "GET /missing HTTP/1.1" 404 11521 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:25 +0000] "GET /static/app.js HTTP/1.1" 200 17493 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:29 +0000] "GET /missing HTTP/1.1" 404 3338 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:29 +0000] "GET /missing HTTP/1.1" 404 2903 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:33 +0000] "GET / HTTP/1.1" 200 14290 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:40 +0000] "GET /products/1 HTTP/1.1" 200 5047 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:45 +0000] "GET /products/2 HTTP/1.1" 200 8321 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:48 +0000] "GET /products HTTP/1.1" 200 3545 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:51 +0000] "GET /api/items HTTP/1.1" 200 1726 "-" "Mozilla/5.0"
192.0.2.40 - - [01/Sep/2026:10:56:52 +0000] "GET /old-page HTTP/1.1" 404 15533 "-" "Mozilla/5.0"
```

## 192.0.2.57 — 2026-09-01 10:56:00+00:00

**Reason:** avg payload 14874 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=14874.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.57 - - [01/Sep/2026:10:56:20 +0000] "GET /api/items HTTP/1.1" 200 17498 "-" "Mozilla/5.0"
192.0.2.57 - - [01/Sep/2026:10:56:40 +0000] "GET /products/1 HTTP/1.1" 200 12251 "-" "Mozilla/5.0"
```

## 192.0.2.60 — 2026-09-01 10:56:00+00:00

**Reason:** 80% POST share, avg payload 10197 bytes

**Features:** requests_per_minute=5, error_404_ratio=0.200, unique_urls=3, avg_payload_size=10196.800, post_share=0.800

**Exact log lines:**

```text
192.0.2.60 - - [01/Sep/2026:10:56:02 +0000] "GET /products/2 HTTP/1.1" 200 4230 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:56:04 +0000] "POST /api/search HTTP/1.1" 200 11700 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:56:04 +0000] "POST /login HTTP/1.1" 200 12259 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:56:26 +0000] "POST /login HTTP/1.1" 404 16985 "-" "Mozilla/5.0"
192.0.2.60 - - [01/Sep/2026:10:56:28 +0000] "POST /api/search HTTP/1.1" 200 5810 "-" "Mozilla/5.0"
```

## 192.0.2.23 — 2026-09-01 10:57:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=2685.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.23 - - [01/Sep/2026:10:57:00 +0000] "GET /products HTTP/1.1" 403 3509 "-" "Mozilla/5.0"
192.0.2.23 - - [01/Sep/2026:10:57:29 +0000] "GET /static/app.js HTTP/1.1" 200 1862 "-" "Mozilla/5.0"
```

## 192.0.2.34 — 2026-09-01 10:58:00+00:00

**Reason:** avg payload 12618 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=12617.500, post_share=0.000

**Exact log lines:**

```text
192.0.2.34 - - [01/Sep/2026:10:58:00 +0000] "GET /products/2 HTTP/1.1" 304 7703 "-" "Mozilla/5.0"
192.0.2.34 - - [01/Sep/2026:10:58:17 +0000] "GET /contact HTTP/1.1" 200 17532 "-" "Mozilla/5.0"
```

## 192.0.2.24 — 2026-09-01 11:00:00+00:00

**Reason:** avg payload 14693 bytes

**Features:** requests_per_minute=2, error_404_ratio=0.000, unique_urls=2, avg_payload_size=14693.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.24 - - [01/Sep/2026:11:00:00 +0000] "GET /static/app.js HTTP/1.1" 204 15737 "-" "Mozilla/5.0"
192.0.2.24 - - [01/Sep/2026:11:00:00 +0000] "GET /about HTTP/1.1" 201 13649 "-" "Mozilla/5.0"
```

## 192.0.2.27 — 2026-09-01 11:00:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=8751.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.27 - - [01/Sep/2026:11:00:00 +0000] "GET /contact HTTP/1.1" 200 8751 "-" "Mozilla/5.0"
```

## 192.0.2.31 — 2026-09-01 11:00:00+00:00

**Reason:** 100% 404 ratio

**Features:** requests_per_minute=1, error_404_ratio=1.000, unique_urls=1, avg_payload_size=6895.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.31 - - [01/Sep/2026:11:00:00 +0000] "GET /missing HTTP/1.1" 404 6895 "-" "Mozilla/5.0"
```

## 192.0.2.35 — 2026-09-01 11:00:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=2, error_404_ratio=0.500, unique_urls=2, avg_payload_size=9358.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.35 - - [01/Sep/2026:11:00:00 +0000] "GET /missing HTTP/1.1" 404 4245 "-" "Mozilla/5.0"
192.0.2.35 - - [01/Sep/2026:11:00:00 +0000] "GET /products/2 HTTP/1.1" 200 14471 "-" "Mozilla/5.0"
```

## 192.0.2.38 — 2026-09-01 11:00:00+00:00

**Reason:** 100% 404 ratio, avg payload 16838 bytes

**Features:** requests_per_minute=1, error_404_ratio=1.000, unique_urls=1, avg_payload_size=16838.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.38 - - [01/Sep/2026:11:00:00 +0000] "GET /old-page HTTP/1.1" 404 16838 "-" "Mozilla/5.0"
```

## 192.0.2.47 — 2026-09-01 11:00:00+00:00

**Reason:** Isolation Forest anomaly score

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=3700.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.47 - - [01/Sep/2026:11:00:00 +0000] "GET /products/1 HTTP/1.1" 200 3700 "-" "Mozilla/5.0"
```

## 192.0.2.49 — 2026-09-01 11:00:00+00:00

**Reason:** avg payload 10076 bytes

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=10076.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.49 - - [01/Sep/2026:11:00:00 +0000] "GET /favicon.ico HTTP/1.1" 200 10076 "-" "Mozilla/5.0"
```

## 192.0.2.56 — 2026-09-01 11:00:00+00:00

**Reason:** avg payload 16746 bytes

**Features:** requests_per_minute=1, error_404_ratio=0.000, unique_urls=1, avg_payload_size=16746.000, post_share=0.000

**Exact log lines:**

```text
192.0.2.56 - - [01/Sep/2026:11:00:00 +0000] "GET /search?q=phone HTTP/1.1" 200 16746 "-" "Mozilla/5.0"
```

