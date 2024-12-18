# didactic-octo-adventure
Convertir les données Odoo pour un feed sur Merchant Center

## Correspondance des tables Odoo et Google Merchant Center

| Champ Google         | Champ Odoo                                               | Exemple de données                                                   | Remarques              |
|----------------------|----------------------------------------------------------|----------------------------------------------------------------------|------------------------|
| id                   | Product/ID                                               | 117268 -> USEDFR117268                                               | Identifiant unique     |
| brand                | Brand                                                    |  ARCTIC CAT                                                          |   marque du fabricant  |
| npm                  | Internal Reference                                       | 1702-074                                                             | reference fabricant  |  
| title                | Name                                                     | (+ 2602-271) SPROCKET,22T REV 13W-W/BRG-ASSY                         | titre du produit       |
| description          | Brand + Internal Reference + Description for the website | ARCTIC CAT - 1702-074 - (+ 2602-271) SPROCKET,22T REV 13W-W/BRG-ASSY | description du produit |
| link                 | {{domaine}}/shop/68082-absorber-assy-rear-shock-black    | https://www.micpartsonline.com/shop/68082-absorber-assy-rear-shock.. | lien du produit        |
| image_link | {{domaine}}/web/image/product.product/`{{Product/ID}}/image_1024   | https://www.micpartsonline.com/web/image/product.product/67753/image_1024 | image produit     |
| additional_image_link| Product Images/Image URL                                 | https://www.micpartsonline.com/lf/i/NTU5MDE=                         | images produit       |
| price                | Google Sales Price *{{coef}}                             | 199.90 CAD                               | prix du produit  varie en fonction de la condition |
| sale_price           | Google Sales Price                                       | 99.95 CAD                                                | voir comment est calculé ce champ | 
| availability         | Quantity On Hand                                         | 2.0 -> in_stock                                          | in_stock par default
| condition            | {{paramétre}}                                            | used or new                                              | varie en fonction du paramétre |



## fournir un gtin

dev en cours
