<div align="center">

<img src="assets/logo-512.png" width="96" alt="staticgen">

# staticgen

**A static site generator in Python with no dependencies.**

[![CI](https://github.com/marcus-beauregard/staticgen/actions/workflows/ci.yml/badge.svg)](https://github.com/marcus-beauregard/staticgen/actions/workflows/ci.yml)
[![License: GPL-2.0-or-later](https://img.shields.io/badge/license-GPL--2.0--or--later-blue.svg)](LICENSE)

</div>

## Quick start

```bash
python3 gen.py posts dist --template template.html
```

It reads every ```.md``` in ```posts/```, renders it through the template, and writes ```dist/<name>.html```. No install step, no virtualenv, no packages.

```bash
python3 -m pip install -e .   # optional: gives you the marcus-staticgen command
```

## What it does

| Argument | Meaning |
|---|---|
| ```src``` | a directory of markdown files (this repo ships @@posts@@) |
| ```out``` | where the HTML goes; created if missing |
| ```--template``` | the HTML shell, default ```template.html``` |

Markdown support is deliberately small: paragraphs, ```**bold**```, ```# headings```. Anything else passes through as text.

## Develop

```bash
pytest -q
```

## Known rough edges

Template substitution is two naive string replaces (#8), title parsing strips inner tags (#1), and output is emitted unescaped (#3). Each is small and well-scoped.

## Contributing

Humans and automated agents are both welcome. There is no CLA — every commit carries a [DCO](https://developercertificate.org/) sign-off (**git commit -s**).

Start with a [good first issue](https://github.com/marcus-beauregard/staticgen/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22), or read [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

GPL-2.0-or-later — see [LICENSE](LICENSE). Copyright (C) 2026 Marcus Beauregard.

Versions published before 2026-11-19 remain available under MIT; this licence applies to the current tree and every release from here.
