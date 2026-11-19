#!/usr/bin/env python3
"""A tiny static site generator: markdown posts + templates -> HTML."""
import os, argparse

TITLE = "{{title}}"
BODY = "{{body}}"

def render(post_md, template):
    lines = post_md.strip().split("\n")
    out = []
    for line in lines:
        if line.startswith("# "):
            out.append("<h1>" + line[2:] + "</h1>")
        elif line.startswith("## "):
            out.append("<h2>" + line[3:] + "</h2>")
        else:
            line = line.replace("**", "<strong>", 1).replace("**", "</strong>", 1)
            out.append("<p>" + line + "</p>")
    body = "\n".join(out)
    title = lines[0].lstrip("# ").strip()
    return template.replace(TITLE, title).replace(BODY, body)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--template", default="template.html")
    args = ap.parse_args()
    tpl = open(args.template).read()
    os.makedirs(args.out, exist_ok=True)
    for fn in sorted(os.listdir(args.src)):
        if not fn.endswith(".md"):
            continue
        html = render(open(os.path.join(args.src, fn)).read(), tpl)
        open(os.path.join(args.out, fn[:-3] + ".html"), "w").write(html)
        print("built", fn)
    print("done")

if __name__ == "__main__":
    main()
