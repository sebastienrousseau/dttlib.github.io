import glob
import html
import os
import re
import shutil

# Utility pages: reachable, but not search results.
SITEMAP_SKIP = {"/404/", "/offline/"}

CANONICAL_RE = re.compile(r'<link rel="canonical" href="([^"]+)"')


def canonical_urls(output_dir, base_url):
    """Return the canonical URL of every indexable page, sorted.

    The URL is the page's own <link rel="canonical">, so the sitemap lists
    exactly what each page declares (https://dttlib.com/about/, never
    /about/index.html). Pages with no canonical, on another host, marked
    noindex, or in SITEMAP_SKIP are left out.
    """
    urls = set()
    for html_file in glob.glob(f"{output_dir}/**/*.html", recursive=True):
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()
        match = CANONICAL_RE.search(content)
        if not match or 'content="noindex' in content:
            continue
        url = match.group(1)
        path = url[len(base_url):] if url.startswith(base_url + "/") else None
        if path is not None and path not in SITEMAP_SKIP:
            urls.add(url)
    return sorted(urls)


def write_sitemap(output_dir, targets, base_url):
    """Write sitemap.xml to each target directory; return its URLs."""
    urls = canonical_urls(output_dir, base_url)
    body = "".join(f"  <url>\n    <loc>{html.escape(u)}</loc>\n  </url>\n" for u in urls)
    sitemap_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}</urlset>\n"
    )
    for d in targets:
        with open(os.path.join(d, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(sitemap_xml)
    return urls


def mirror_output(output_dir, docs_dir):
    """Copy the ssg output into docs/, replacing what was there."""
    os.makedirs(docs_dir, exist_ok=True)
    for item in os.listdir(output_dir):
        s = os.path.join(output_dir, item)
        d = os.path.join(docs_dir, item)
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)


def write_text(targets, name, text):
    for d in targets:
        with open(os.path.join(d, name), "w", encoding="utf-8") as f:
            f.write(text)


def llms_txt(base_url):
    return f"""# DTT Lib
> Deterministic date, time, and timezone manipulation library for Rust with zero heap allocations, sub-nanosecond precision, and full ISO 8601/RFC 3339 compliance.

## Core Documentation & Resources
- Homepage: {base_url}/
- Getting Started: {base_url}/getting-started/index.html
- Formats & ISO: {base_url}/formats/index.html
- Features: {base_url}/features/index.html
- API Reference: {base_url}/documentation/index.html
- Examples: {base_url}/examples/index.html
- Benchmarks: {base_url}/benchmarks/index.html
- Architecture: {base_url}/architecture/index.html
- Security: {base_url}/security/index.html
- About Sebastien Rousseau: {base_url}/about/index.html
"""


RAW_HTML_MARKERS = ('<div', '<section', '<details', '<table')
CODE_BLOCK_RES = (
    r'<pre><code><span class="text plain">(.*?)</span></code></pre>',
    r'<pre><code class="language-html">(.*?)</code></pre>',
    r'<pre><code>(.*?)</code></pre>',
)
ESCAPED_TAG_RE = r'&lt;/?(section|div|details|summary|table|thead|tbody|tr|th|td|form|label|input|textarea|button|svg|circle|line|path|polyline|kbd|span class|h2|h3|h4|p class|a class|img class).*?&gt;'


def unwrap_raw_html(match):
    """Unwrap a code block that holds layout HTML rather than code."""
    inner = match.group(1)
    return inner if any(m in inner for m in RAW_HTML_MARKERS) else match.group(0)


def fix_html_tags(match):
    tag = match.group(0)
    for ent, val in [("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&#39;", "'"), ("&#x27;", "'")]:
        tag = tag.replace(ent, val)
    return tag


def clean_html(content, base_url):
    content = content.replace("http://127.0.0.1:8000", base_url)
    content = content.replace("http://localhost:8000", base_url)
    for pattern in CODE_BLOCK_RES:
        content = re.sub(pattern, unwrap_raw_html, content, flags=re.DOTALL)
    return re.sub(ESCAPED_TAG_RE, fix_html_tags, content, flags=re.DOTALL)


def clean_html_files(targets, base_url):
    for base_path in targets:
        for html_file in glob.glob(f"{base_path}/**/*.html", recursive=True):
            with open(html_file, "r", encoding="utf-8") as f:
                content = f.read()
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(clean_html(content, base_url))


def post_build():
    output_dir = "public"
    docs_dir = "docs"
    base_url = "https://dttlib.com"
    targets = [output_dir, docs_dir]

    mirror_output(output_dir, docs_dir)
    write_text(targets, "CNAME", "dttlib.com\n")
    write_text(targets, "llms.txt", llms_txt(base_url))
    clean_html_files(targets, base_url)
    # After cleaning, so each URL is the canonical the page finally carries.
    all_pages = write_sitemap(output_dir, targets, base_url)

    print(f"Post-build optimization complete ({len(all_pages)} URLs).")


if __name__ == "__main__":
    post_build()
