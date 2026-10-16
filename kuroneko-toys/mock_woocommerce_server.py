#!/usr/bin/env python3
"""
WooCommerce REST API Mock Server para Kuro Neko Toys
Simula com fidelidade o endpoint oficial do WooCommerce:
GET /wp-json/wc/v3/products
"""

import http.server
import socketserver
import json
import urllib.parse

PORT = 8086

# Base simulada de produtos no formato oficial do WooCommerce v3
PRODUCTS = [
    {
        "id": 101,
        "name": "Monkey D. Luffy — Gear 5 Sun God",
        "slug": "luffy-gear-5-sun-god",
        "permalink": "https://kuronekotoys.com.br/produto/luffy-gear-5",
        "type": "simple",
        "status": "publish",
        "featured": True,
        "description": "<p>Action figure espetacular com efeitos translúcidos em PVC de alta resistência. Linha Grandista oficial.</p>",
        "short_description": "PVC de alta fidelidade • Linha Grandista • Efeitos translúcidos de nuvens celestiais",
        "sku": "KNT-OP-001",
        "price": "289.90",
        "regular_price": "319.90",
        "sale_price": "289.90",
        "on_sale": True,
        "purchasable": True,
        "stock_status": "instock",
        "stock_quantity": 4,
        "categories": [
            {"id": 10, "name": "Shonen & Animes", "slug": "shonen"}
        ],
        "tags": [
            {"id": 1, "name": "Original Banpresto", "slug": "banpresto"}
        ],
        "images": [
            {"id": 1, "src": "🏴‍☠️", "name": "Luffy", "alt": "Luffy Gear 5"}
        ],
        "attributes": [
            {"id": 1, "name": "Escala", "options": ["22cm"]}
        ]
    },
    {
        "id": 102,
        "name": "Kamado Tanjiro — Hinokami Kagura Dance",
        "slug": "kamado-tanjiro-hinokami",
        "permalink": "https://kuronekotoys.com.br/produto/tanjiro-hinokami",
        "type": "simple",
        "status": "publish",
        "featured": True,
        "description": "<p>Edição especial com escultura de fogo translúcido e riqueza milimétrica nos trajes do esquadrão de caçadores.</p>",
        "short_description": "Rica em detalhes • Chamas de fogo esculpidas em resina • Base de suporte reforçada",
        "sku": "KNT-DS-002",
        "price": "249.90",
        "regular_price": "249.90",
        "sale_price": "",
        "on_sale": False,
        "purchasable": True,
        "stock_status": "instock",
        "stock_quantity": 3,
        "categories": [
            {"id": 10, "name": "Shonen & Animes", "slug": "shonen"}
        ],
        "tags": [
            {"id": 2, "name": "Edição Especial", "slug": "especial"}
        ],
        "images": [
            {"id": 2, "src": "⚔️", "name": "Tanjiro", "alt": "Tanjiro Hinokami"}
        ],
        "attributes": [
            {"id": 1, "name": "Escala", "options": ["18cm"]}
        ]
    },
    {
        "id": 103,
        "name": "Son Goku Super Saiyan 3 — Masterlise Extra",
        "slug": "son-goku-ssj3-masterlise",
        "permalink": "https://kuronekotoys.com.br/produto/goku-ssj3",
        "type": "simple",
        "status": "publish",
        "featured": True,
        "description": "<p>Peça imponente da coleção Masterlise com pintura de estúdio e cabelo volumoso clássico dos anos 90.</p>",
        "short_description": "Pintura fosca premium • Textura anatômica dos músculos e cabelo clássico",
        "sku": "KNT-DBZ-003",
        "price": "349.90",
        "regular_price": "379.90",
        "sale_price": "349.90",
        "on_sale": True,
        "purchasable": True,
        "stock_status": "instock",
        "stock_quantity": 1,
        "categories": [
            {"id": 10, "name": "Shonen & Animes", "slug": "shonen"}
        ],
        "tags": [
            {"id": 3, "name": "Linha Masterlise", "slug": "masterlise"}
        ],
        "images": [
            {"id": 3, "src": "💥", "name": "Goku SSJ3", "alt": "Goku Super Saiyan 3"}
        ],
        "attributes": [
            {"id": 1, "name": "Escala", "options": ["25cm"]}
        ]
    },
    {
        "id": 104,
        "name": "Gundam Aerial — HG 1/144 The Witch from Mercury",
        "slug": "gundam-aerial-hg-144",
        "permalink": "https://kuronekotoys.com.br/produto/gundam-aerial",
        "type": "simple",
        "status": "publish",
        "featured": False,
        "description": "<p>Kit de montagem Gunpla original Bandai Spirits com partes coloridas injetadas e articulações de alto desempenho.</p>",
        "short_description": "Kit de montagem oficial Bandai • Articulações completas • Não necessita cola",
        "sku": "KNT-GUN-004",
        "price": "199.90",
        "regular_price": "199.90",
        "sale_price": "",
        "on_sale": False,
        "purchasable": True,
        "stock_status": "instock",
        "stock_quantity": 5,
        "categories": [
            {"id": 20, "name": "Games & Mecha", "slug": "gamer"}
        ],
        "tags": [
            {"id": 4, "name": "Bandai Spirits", "slug": "bandai"}
        ],
        "images": [
            {"id": 4, "src": "🤖", "name": "Gundam Aerial", "alt": "Gundam Gunpla"}
        ],
        "attributes": [
            {"id": 1, "name": "Escala", "options": ["1/144"]}
        ]
    },
    {
        "id": 105,
        "name": "Link & Hylian Shield — Tears of the Kingdom Collector",
        "slug": "link-zelda-totk",
        "permalink": "https://kuronekotoys.com.br/produto/link-totk",
        "type": "simple",
        "status": "publish",
        "featured": True,
        "description": "<p>Estátua rica do herói de Hyrule com detalhes em pedra arcaica e o lendário Hylian Shield empunhado.</p>",
        "short_description": "Braço Rauru translúcido com luz LED integrada • Escultura oficial Nintendo",
        "sku": "KNT-ZEL-005",
        "price": "329.90",
        "regular_price": "349.90",
        "sale_price": "329.90",
        "on_sale": True,
        "purchasable": True,
        "stock_status": "instock",
        "stock_quantity": 2,
        "categories": [
            {"id": 20, "name": "Games & Mecha", "slug": "gamer"}
        ],
        "tags": [
            {"id": 5, "name": "First 4 Figures", "slug": "f4f"}
        ],
        "images": [
            {"id": 5, "src": "🛡️", "name": "Link TotK", "alt": "Link Zelda"}
        ],
        "attributes": [
            {"id": 1, "name": "Escala", "options": ["20cm"]}
        ]
    },
    {
        "id": 106,
        "name": "Kuro Neko Jiji — Relógio de Mesa Vintage Ghibli",
        "slug": "kuro-neko-jiji-relogio",
        "permalink": "https://kuronekotoys.com.br/produto/kuro-neko-jiji",
        "type": "simple",
        "status": "publish",
        "featured": True,
        "description": "<p>Mascote oficial Kuro Neko em edição de colecionador Studio Ghibli com relógio analógico de quartzo embutido.</p>",
        "short_description": "O gato preto clássico em resina moldada com mini relógio funcional analógico",
        "sku": "KNT-GHB-006",
        "price": "169.90",
        "regular_price": "189.90",
        "sale_price": "169.90",
        "on_sale": True,
        "purchasable": True,
        "stock_status": "instock",
        "stock_quantity": 6,
        "categories": [
            {"id": 30, "name": "Kuro Neko & Ghibli", "slug": "ghibli"}
        ],
        "tags": [
            {"id": 6, "name": "Kiki Delivery", "slug": "ghibli-tag"}
        ],
        "images": [
            {"id": 6, "src": "🐾", "name": "Kuro Neko Jiji", "alt": "Kuro Neko Ghibli"}
        ],
        "attributes": [
            {"id": 1, "name": "Escala", "options": ["15cm"]}
        ]
    }
]

class WooCommerceMockHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Habilita CORS para permitir que a landing page na porta 8084 consuma a porta 8086
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        
        # Endpoint padrão do WooCommerce REST API v3
        if path == '/wp-json/wc/v3/products':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(PRODUCTS, ensure_ascii=False).encode('utf-8'))
        elif path == '/wp-json/wc/v3/system_status':
            self.send_response(200)
            self.end_headers()
            status = {
                "environment": {
                    "home_url": "http://localhost:8086",
                    "version": "8.5.1",
                    "server_info": "Hostinger Cloud / Nginx + PHP 8.2 Mock"
                }
            }
            self.wfile.write(json.dumps(status, ensure_ascii=False).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps({"code": "woocommerce_rest_cannot_view", "message": "Endpoint não encontrado"}, ensure_ascii=False).encode('utf-8'))

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), WooCommerceMockHandler) as httpd:
        print(f"WooCommerce Mock API Server rodando em http://localhost:{PORT}")
        print(f"Endpoint de Produtos: http://localhost:{PORT}/wp-json/wc/v3/products")
        httpd.serve_forever()
