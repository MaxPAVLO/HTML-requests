from requests_html import HTMLSession, HTML

session = HTMLSession()
r = session.get("https://coreyms.com/")

article = r.html.find("h2", first = True)
headline = article.find(".entry-title-link", first = True).text

print(headline)

session_num2 = HTMLSession()
r = session_num2.get("https://ru.investing.com/crypto/bitcoin/btc-usd")

article_num2 = r.html.find("span.text-2xl", first = True)
headline_num2 = article_num2.find(".text-2xl", first = True).text

print(headline_num2)

r = session.get("https://ru.investing.com/crypto/ethereum/eth-usd")

article = r.html.find("span.text-2xl", first = True)
headline = article.find(".text-2xl", first = True).text

print(headline)

r = session.get("http://www.statdata.ru/naselenie-moskvy-po-okrugam-i-rajonam")

article = r.html.find("div.wprt-container", first = True)
headline = article.find("p")[2]
print("Население Москвы:", headline.find("strong", first = True).text)

