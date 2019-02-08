from escape_rooms_club.scrapers import exit_games


def test_parse_first_exit_game(scraper_input_exitgamescz_ghost_house):
    converted_result = exit_games.parse_exit_game(scraper_input_exitgamescz_ghost_house)

    assert converted_result.name == "Dům duchů"
    assert converted_result.description == "Ten dům byl téměř půl století opuštěný. Všichni se od něj drželi dál, mnozí neměli ani odvahu se podívat do zatažených oken. Stigma, které si nesl, bylo moc..."
    assert converted_result.detail_url == "https://www.exitgames.cz/praha-the-chamber-dum-duchu"
    assert converted_result.provider == "The Chamber"
    assert converted_result.provider_url == "https://www.exitgames.cz/seznam-unikovych-her/the-chamber"
    assert converted_result.price_info == "1 590 Kč / skupina"
    assert converted_result.image_url == "https://www.exitgames.cz/image/cache/data/TCR_dum_duchu/dum-duchu-male-3-e1479292532150-280x210crop.jpg"


def test_test_parse_third_exit_game(scraper_input_exitgamescz_lair_of_vice):#
    converted_result = exit_games.parse_exit_game(scraper_input_exitgamescz_lair_of_vice)

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


def test_scraping_escape_rooms(scraper_input_exitgamescz_home_page):
    the_chamber_ghost_house = exit_games.get_escape_rooms(scraper_input_exitgamescz_home_page)[0]

    assert the_chamber_ghost_house.name == "Dům duchů"
    assert the_chamber_ghost_house.description == "Ten dům byl téměř půl století opuštěný. Všichni se od něj drželi dál, mnozí neměli ani odvahu se podívat do zatažených oken. Stigma, které si nesl, bylo moc..."
    assert the_chamber_ghost_house.detail_url == "https://www.exitgames.cz/praha-the-chamber-dum-duchu"
    assert the_chamber_ghost_house.provider == "The Chamber"
    assert the_chamber_ghost_house.provider_url == "https://www.exitgames.cz/seznam-unikovych-her/the-chamber"
    assert the_chamber_ghost_house.price_info == "1 590 Kč / skupina"
    assert the_chamber_ghost_house.image_url == "./Seznam únikových her_files/dum-duchu-male-3-e1479292532150-280x210crop.jpg"
