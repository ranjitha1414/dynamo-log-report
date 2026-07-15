# Access log report

Analyze the Apache-style access log at `/app/access.log` and write a JSON report to
`/app/report.json`.

Success criteria:

1. `/app/report.json` exists and contains one valid JSON object.
2. The object has exactly these keys: `total_requests`, `unique_ips`, and `top_path`.
3. `total_requests` is the integer number of non-empty request lines in the log.
4. `unique_ips` is the integer number of distinct client IP addresses in the log.
5. `top_path` is the string request path that occurs most often. If multiple paths
   are tied, use the path whose first occurrence appears earliest in the log.
