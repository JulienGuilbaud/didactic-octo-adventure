# didactic-octo-adventure
Convertir les données Odoo pour un feed sur Merchant Center

## Correspondance des tables Odoo et Google Merchant Center

| Champ Google         | Champ Odoo                                               | exemple de données                                                   | Remarques              |
|----------------------|----------------------------------------------------------|----------------------------------------------------------------------|------------------------|
| id                   | Product/ID                                               | 117268 -> USEDFR117268                                               | Identifiant unique     |
| brand                | Brand                                                    |  ARCTIC CAT                                                          |   marque du fabricant  |
| npm                  | Internal Reference                                       | 1702-074                                                             | reference fabricant    |  
| title                | Name                                                     | (+ 2602-271) SPROCKET,22T REV 13W-W/BRG-ASSY                         | titre du produit       |
| description          | Brand + Internal Reference + Description for the website | ARCTIC CAT - 1702-074 - (+ 2602-271) SPROCKET,22T REV 13W-W/BRG-ASSY | description du produit |
| link                 |
| image_link           |
| additional_image_link|
| price                |
| sale_price           |
| vailability          |
| condition            | 



## fournir un gtin
