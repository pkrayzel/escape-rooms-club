from . import exit_games


def test_parse_first_exit_game():
    content = """
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
    </div>"""

    converted_result = exit_games._parse_exit_game_from_html_string(content)

    assert converted_result.name == "Dům duchů"
    assert converted_result.description == "Ten dům byl téměř půl století opuštěný. Všichni se od něj drželi dál, mnozí neměli ani odvahu se podívat do zatažených oken. Stigma, které si nesl, bylo moc..."
    assert converted_result.detail_url == "https://www.exitgames.cz/praha-the-chamber-dum-duchu"
    assert converted_result.provider == "The Chamber"
    assert converted_result.provider_url == "https://www.exitgames.cz/seznam-unikovych-her/the-chamber"
    assert converted_result.price_info == "1 590 Kč / skupina"
    assert converted_result.image_url == "https://www.exitgames.cz/image/cache/data/TCR_dum_duchu/dum-duchu-male-3-e1479292532150-280x210crop.jpg"


def test_test_parse_third_exit_game():
    content = """
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
            <a href="https://www.exitgames.cz/praha-chess-key-room-doupe-neresti" title="Doupě neřesti (hra nejen pro páry)">
            <img alt="Doupě neřesti (hra nejen pro páry)" src="https://www.exitgames.cz/image/cache/data/Chess_Key_Room/Doupě neřesti_poháry-280x210crop.jpg"/>
            </a>
        </div>
        <div class="info">
            <div class="name"><a href="https://www.exitgames.cz/praha-chess-key-room-doupe-neresti">Doupě neřesti (hra nejen pro páry)</a></div>
            <div class="partner"><a href="https://www.exitgames.cz/seznam-unikovych-her/chess-key-room">Chess KEY Room</a></div>
            <div class="description">První úniková hra, která je tak trochu hanbatá, a proto ji doporučujeme také pro DVA!
            Věk: 18+
            Při rezervaci uveďte do poznámky "Doupě neřesti"


            Nevinná dívka,...</div>
            <div class="btn-detail">
                <div class="price">Cena od: <span class="value">1 100 Kč / skupina</span></div>
                <a class="btn btn-small-filled" href="https://www.exitgames.cz/praha-chess-key-room-doupe-neresti" title="Doupě neřesti (hra nejen pro páry)">zobrazit hru</a>
            </div>
        </div>
    </div>"""

    converted_result = exit_games._parse_exit_game_from_html_string(content)

    assert converted_result.description == """První úniková hra, která je tak trochu hanbatá, a proto ji doporučujeme také pro DVA!
            Věk: 18+
            Při rezervaci uveďte do poznámky "Doupě neřesti"


            Nevinná dívka,..."""
    assert converted_result.name == "Doupě neřesti (hra nejen pro páry)"
    assert converted_result.detail_url == "https://www.exitgames.cz/praha-chess-key-room-doupe-neresti"
    assert converted_result.provider == "Chess KEY Room"
    assert converted_result.provider_url == "https://www.exitgames.cz/seznam-unikovych-her/chess-key-room"
    assert converted_result.price_info == "1 100 Kč / skupina"
    assert converted_result.image_url == "https://www.exitgames.cz/image/cache/data/Chess_Key_Room/Doupě neřesti_poháry-280x210crop.jpg"


def test_scraping_escape_rooms_first():
    the_chamber_ghost_house = exit_games.get_escape_rooms()[0]

    assert the_chamber_ghost_house.name == "Dům duchů"
    assert the_chamber_ghost_house.description == "Ten dům byl téměř půl století opuštěný. Všichni se od něj drželi dál, mnozí neměli ani odvahu se podívat do zatažených oken. Stigma, které si nesl, bylo moc..."
    assert the_chamber_ghost_house.detail_url == "https://www.exitgames.cz/praha-the-chamber-dum-duchu"
    assert the_chamber_ghost_house.provider == "The Chamber"
    assert the_chamber_ghost_house.provider_url == "https://www.exitgames.cz/seznam-unikovych-her/the-chamber"
    assert the_chamber_ghost_house.price_info == "1 590 Kč / skupina"
    assert the_chamber_ghost_house.image_url == "./Seznam únikových her_files/dum-duchu-male-3-e1479292532150-280x210crop.jpg"
