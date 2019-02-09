from escape_rooms_club.model import EscapeRoom


def get_all_escape_rooms(scraper_object):
    escape_rooms = scraper_object.find_all('div', class_="product")

    result = []

    for i, item in enumerate(escape_rooms):
        try:
            room = parse_single_escape_room(item)
            result.append(room)
        except Exception as e:
            print(e)

    return result


def parse_single_escape_room(scraper_object):
    """
        <div class="product">
            <div class="flags">
                <div class="flag-featured"><span>TOP</span></div>
                <div class="rating rating-small rating-5"></div>
                <div class="difficulty difficulty-small difficulty-3">
                    <span class="icon-bulb"></span>
                    <span class="icon-bulb"></span>
                    <span class="icon-bulb"></span>
                    <span class="icon-bulb-empty"></span>
                    <span class="icon-bulb-empty"></span>
                </div>
            </div>
            <div class="image">
                <a href="https://www.exitgames.cz/praha-the-chamber-dum-duchu" title="Dům duchů">
                    <img alt="Dům duchů" src="https://www.exitgames.cz/image/cache/data/TCR_dum_duchu/dum-duchu-male-3-e1479292532150-280x210crop.jpg"/>
                </a>
            </div>
            <div class="info">
                <div class="name"><a href="https://www.exitgames.cz/praha-the-chamber-dum-duchu">Dům duchů</a></div>
                <div class="partner"><a href="https://www.exitgames.cz/seznam-unikovych-her/the-chamber">The Chamber</a></div>
                <div class="description">Ten dům byl téměř půl století opuštěný. Všichni se od něj drželi dál, mnozí neměli ani odvahu se podívat do zatažených oken. Stigma, které si nesl, bylo moc...</div>
                <div class="btn-detail">
                    <div class="price">Cena od: <span class="value">1 590 Kč / skupina</span></div>
                    <a class="btn btn-small-filled" href="https://www.exitgames.cz/praha-the-chamber-dum-duchu" title="Dům duchů">zobrazit hru</a>
                </div>
            </div>
        </div>
    """

    a_name = scraper_object.find("div", class_="name").find("a")
    a_partner = scraper_object.find("div", class_="partner").find("a")
    description = scraper_object.find("div", class_="description").get_text()
    price = scraper_object.find("div", class_="price").find("span", class_="value").get_text()
    image = scraper_object.find("img")

    return EscapeRoom(
        name=a_name.get_text(),
        description=description,
        detail_url=a_name["href"],
        provider=a_partner.get_text(),
        provider_url=a_partner["href"],
        price_info=price,
        image_url=image["src"],
    )


# <a href="javascript:;" id="next_products" class="btn btn-border">NAČÍST DALŠÍ</a>