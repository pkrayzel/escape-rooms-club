import requests
from bs4 import BeautifulSoup
import typing


class EscapeRoom(typing.NamedTuple):
    name: str
    description: str
    detail_url: str
    provider: str
    provider_url: str
    price_info: str
    image_url: str


def get_escape_rooms():
    # page = requests.get("https://www.exitgames.cz/Seznam-unikovych-her")
    # soup = BeautifulSoup(page.content, 'html.parser')
    content = open("examples/exit_games.htm")
    soup = BeautifulSoup(content.read(), 'html.parser')

    escape_rooms = soup.find_all('div', class_="product")

    result = []

    for i, item in enumerate(escape_rooms):
        try:
            room = parse_exit_game(item)
            result.append(room)
        except Exception as e:
            print(e)

    return result


def _parse_exit_game_from_html_string(content):
    soup = BeautifulSoup(content, 'html.parser')
    return parse_exit_game(soup)


def parse_exit_game(soup):
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

    a_name = soup.find("div", class_="name").find("a")
    a_partner = soup.find("div", class_="partner").find("a")
    description = soup.find("div", class_="description").get_text()
    price = soup.find("div", class_="price").find("span", class_="value").get_text()
    image = soup.find("img")

    return EscapeRoom(
        name=a_name.get_text(),
        description=description,
        detail_url=a_name["href"],
        provider=a_partner.get_text(),
        provider_url=a_partner["href"],
        price_info=price,
        image_url=image["src"],
    )
