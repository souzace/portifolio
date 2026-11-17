#!/usr/bin/env python3
import re
from html.parser import HTMLParser

class OGChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {}

    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            d = dict(attrs)
            key = d.get("property") or d.get("name")
            if key and "content" in d:
                self.meta[key] = d["content"]

def main():
    parser = OGChecker()
    with open("desentupidora-sao-bento/index.html", "r", encoding="utf-8") as f:
        parser.feed(f.read())

    print("\n" + "=" * 65)
    print(" 🔍 AUDITORIA OPEN GRAPH & METATAGS - DESENTUPIDORA SÃO BENTO")
    print("=" * 65)

    required_tags = [
        ("og:title", 60),
        ("og:description", 165),
        ("og:image", None),
        ("og:url", None),
        ("og:type", None),
        ("og:site_name", None),
        ("og:locale", None),
        ("twitter:card", None),
        ("twitter:title", 60),
        ("twitter:description", 165),
        ("twitter:image", None),
    ]

    all_ok = True
    for tag, max_len in required_tags:
        val = parser.meta.get(tag)
        if not val:
            print(f"❌ [FALTANDO] {tag}")
            all_ok = False
        else:
            length_info = f"({len(val)} caracteres)" if max_len else ""
            status = "✅"
            if max_len and len(val) > max_len:
                status = f"⚠️ [ATENÇÃO: > {max_len} chars]"
                all_ok = False
            print(f"{status} {tag:20} -> {val[:60]}... {length_info}")

    print("=" * 65)
    if all_ok:
        print("🎉 TODOS OS METADADOS OPEN GRAPH ESTÃO 100% VALIDADOS!")
    else:
        print("⚠️ Verifique os avisos acima.")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    main()
