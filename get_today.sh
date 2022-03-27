#!/bin/sh
#curl https://www.americanexpress.com/content/dam/amex/uk/legal/fx-ecb-comparison/markets-data.json > /home/stemnic/scripts/amex_exchange/$(date --iso-8601).json
curl 'https://www.americanexpress.com/gemservices/gcdt/ecbrates/?market=NO' \
  -X 'POST' \
  -H 'authority: www.americanexpress.com' \
  -H 'content-length: 0' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"' \
  -H 'accept: */*' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'origin: https://www.americanexpress.com' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.americanexpress.com/no/legal/fx-ecb-sammenligning/?inav=no_footer_fx_ecb_sammenligning' \
  -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
  --compressed > /home/stemnic/scripts/amex_exchange/data/$(date --iso-8601).json
cd /home/stemnic/scripts/amex_exchange/ && git add . && git commit -m "Data for $(date --iso-8601)" && git push
