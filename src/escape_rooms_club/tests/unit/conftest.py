import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def scraper_input_exitgamescz_ghost_house():
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
    return BeautifulSoup(content, 'html.parser')


@pytest.fixture
def scraper_input_exitgamescz_lair_of_vice():
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
    return BeautifulSoup(content, 'html.parser')


@pytest.fixture
def scraper_input_exitgamescz_home_page():
    content = """
    <!DOCTYPE html>
<!-- saved from url=(0045)https://www.exitgames.cz/Seznam-unikovych-her -->
<html dir="ltr" lang="cs"><head itemscope="" itemtype="http://schema.org/WebSite"><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        
        
                   <meta name="robots" content="index,follow">
           <meta name="googlebot" content="index,follow">
                
        <meta name="viewport" content="width=device-width, initial-scale=1">     
        <meta name="author" content="ExitGames.cz">
        <title itemprop="name">Seznam únikových her</title>
        <!--<base href="https://www.exitgames.cz/">--><base href=".">

                <meta name="description" content="Vyberte si z řady únikových her ve Vaší lokalitě...">
        
                <meta name="keywords" content="únikové hry, exitgames,">
        
                <link href="https://www.exitgames.cz/image/data/favicon.png" rel="icon">
        
                <link href="https://www.exitgames.cz/seznam-unikovych-her" rel="canonical">
              
        <script src="./Seznam únikových her_files/125793861350502" async=""></script><script src="./Seznam únikových her_files/sdk.js" async=""></script><script id="facebook-jssdk" src="./Seznam únikových her_files/sdk(1).js"></script><script async="" src="./Seznam únikových her_files/analytics.js"></script><script async="" src="./Seznam únikových her_files/gtm.js"></script><script async="" src="./Seznam únikových her_files/fbevents.js"></script><script type="text/javascript" src="./Seznam únikových her_files/jquery-1.11.3.min.js"></script>
        <script type="text/javascript" src="./Seznam únikových her_files/jquery-ui.min.js"></script>
        <script type="text/javascript" src="./Seznam únikových her_files/bootstrap.min.js"></script>
        <script type="text/javascript" src="./Seznam únikových her_files/jquery.validate.min.js"></script>
        <script type="text/javascript" src="./Seznam únikových her_files/messages_cs.min.js"></script>
        <script type="text/javascript" src="./Seznam únikových her_files/jquery.magnific-popup.min.js"></script> 
        <script type="text/javascript" src="./Seznam únikových her_files/js"></script>
        <script type="text/javascript" src="./Seznam únikových her_files/slick.min.js"></script>
        <script type="text/javascript" src="./Seznam únikových her_files/imageMapResizer.min.js"></script>
                <script type="text/javascript" src="./Seznam únikových her_files/common.js"></script>
        
        <!--[if lte IE 8]>
            <script type="text/javascript" src="catalog/view/javascript/map-resizer/ie8.polyfil.min.js"></script>
        <![endif]-->

        
        <link rel="stylesheet" type="text/css" href="./Seznam únikových her_files/font-awesome.min.css">
        <link rel="stylesheet" type="text/css" href="./Seznam únikových her_files/jquery-ui.min.css">
        <link rel="stylesheet" type="text/css" href="./Seznam únikových her_files/jquery-ui.theme.min.css">
        <link rel="stylesheet" type="text/css" href="./Seznam únikových her_files/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="./Seznam únikových her_files/magnific-popup.css">
                <link rel="stylesheet" type="text/css" href="./Seznam únikových her_files/template.css">
        <link rel="stylesheet" type="text/css" href="./Seznam únikových her_files/responsive.css">
        
        <link href="./Seznam únikových her_files/css" rel="stylesheet" type="text/css">
        <link href="./Seznam únikových her_files/css(1)" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="./Seznam únikových her_files/slick.css">
        <link rel="stylesheet" type="text/css" href="./Seznam únikových her_files/slick-theme.css">

        
        
        <!-- Facebook Pixel Code -->
        <script>
            !function (f, b, e, v, n, t, s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
        n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
        n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
        t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
                    document, 'script', '//connect.facebook.net/en_US/fbevents.js');

            fbq('init', '125793861350502');
            fbq('track', "PageView");</script>
    <noscript><img height="1" width="1" style="display:none"
                   src="https://www.facebook.com/tr?id=125793861350502&ev=PageView&noscript=1"
                   /></noscript>
    <!-- End Facebook Pixel Code -->

    <!--[if IE 7]> 
    <link rel="stylesheet" type="text/css" href="catalog/view/theme/default/stylesheet/ie7.css" />
    <![endif]-->
    <!--[if lt IE 7]>
    <link rel="stylesheet" type="text/css" href="catalog/view/theme/default/stylesheet/ie6.css" />
    <script type="text/javascript" src="catalog/view/javascript/DD_belatedPNG_0.0.8a-min.js"></script>
    <script type="text/javascript">
    DD_belatedPNG.fix('#logo img');
    </script>
    <![endif]-->
    
    <!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-PZJPZVV');</script>
<!-- End Google Tag Manager -->
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PZJPZVV"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->


    <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-70820035-1', 'auto');
  ga('send', 'pageview');

</script><script src="./Seznam únikových her_files/f.txt"></script><style type="text/css">.fb_hidden{position:absolute;top:-10000px;z-index:10001}.fb_reposition{overflow:hidden;position:relative}.fb_invisible{display:none}.fb_reset{background:none;border:0;border-spacing:0;color:#000;cursor:auto;direction:ltr;font-family:"lucida grande", tahoma, verdana, arial, sans-serif;font-size:11px;font-style:normal;font-variant:normal;font-weight:normal;letter-spacing:normal;line-height:1;margin:0;overflow:visible;padding:0;text-align:left;text-decoration:none;text-indent:0;text-shadow:none;text-transform:none;visibility:visible;white-space:normal;word-spacing:normal}.fb_reset>div{overflow:hidden}@keyframes fb_transform{from{opacity:0;transform:scale(.95)}to{opacity:1;transform:scale(1)}}.fb_animate{animation:fb_transform .3s forwards}
.fb_dialog{background:rgba(82, 82, 82, .7);position:absolute;top:-10000px;z-index:10001}.fb_dialog_advanced{border-radius:8px;padding:10px}.fb_dialog_content{background:#fff;color:#373737}.fb_dialog_close_icon{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 0 transparent;cursor:pointer;display:block;height:15px;position:absolute;right:18px;top:17px;width:15px}.fb_dialog_mobile .fb_dialog_close_icon{left:5px;right:auto;top:5px}.fb_dialog_padding{background-color:transparent;position:absolute;width:1px;z-index:-1}.fb_dialog_close_icon:hover{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 -15px transparent}.fb_dialog_close_icon:active{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 -30px transparent}.fb_dialog_iframe{line-height:0}.fb_dialog_content .dialog_title{background:#6d84b4;border:1px solid #365899;color:#fff;font-size:14px;font-weight:bold;margin:0}.fb_dialog_content .dialog_title>span{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yd/r/Cou7n-nqK52.gif) no-repeat 5px 50%;float:left;padding:5px 0 7px 26px}body.fb_hidden{height:100%;left:0;margin:0;overflow:visible;position:absolute;top:-10000px;transform:none;width:100%}.fb_dialog.fb_dialog_mobile.loading{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ya/r/3rhSv5V8j3o.gif) white no-repeat 50% 50%;min-height:100%;min-width:100%;overflow:hidden;position:absolute;top:0;z-index:10001}.fb_dialog.fb_dialog_mobile.loading.centered{background:none;height:auto;min-height:initial;min-width:initial;width:auto}.fb_dialog.fb_dialog_mobile.loading.centered #fb_dialog_loader_spinner{width:100%}.fb_dialog.fb_dialog_mobile.loading.centered .fb_dialog_content{background:none}.loading.centered #fb_dialog_loader_close{clear:both;color:#fff;display:block;font-size:18px;padding-top:20px}#fb-root #fb_dialog_ipad_overlay{background:rgba(0, 0, 0, .4);bottom:0;left:0;min-height:100%;position:absolute;right:0;top:0;width:100%;z-index:10000}#fb-root #fb_dialog_ipad_overlay.hidden{display:none}.fb_dialog.fb_dialog_mobile.loading iframe{visibility:hidden}.fb_dialog_mobile .fb_dialog_iframe{position:sticky;top:0}.fb_dialog_content .dialog_header{background:linear-gradient(from(#738aba), to(#2c4987));border-bottom:1px solid;border-color:#1d3c78;box-shadow:white 0 1px 1px -1px inset;color:#fff;font:bold 14px Helvetica, sans-serif;text-overflow:ellipsis;text-shadow:rgba(0, 30, 84, .296875) 0 -1px 0;vertical-align:middle;white-space:nowrap}.fb_dialog_content .dialog_header table{height:43px;width:100%}.fb_dialog_content .dialog_header td.header_left{font-size:12px;padding-left:5px;vertical-align:middle;width:60px}.fb_dialog_content .dialog_header td.header_right{font-size:12px;padding-right:5px;vertical-align:middle;width:60px}.fb_dialog_content .touchable_button{background:linear-gradient(from(#4267B2), to(#2a4887));background-clip:padding-box;border:1px solid #29487d;border-radius:3px;display:inline-block;line-height:18px;margin-top:3px;max-width:85px;padding:4px 12px;position:relative}.fb_dialog_content .dialog_header .touchable_button input{background:none;border:none;color:#fff;font:bold 12px Helvetica, sans-serif;margin:2px -12px;padding:2px 6px 3px 6px;text-shadow:rgba(0, 30, 84, .296875) 0 -1px 0}.fb_dialog_content .dialog_header .header_center{color:#fff;font-size:16px;font-weight:bold;line-height:18px;text-align:center;vertical-align:middle}.fb_dialog_content .dialog_content{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/jKEcVPZFk-2.gif) no-repeat 50% 50%;border:1px solid #4a4a4a;border-bottom:0;border-top:0;height:150px}.fb_dialog_content .dialog_footer{background:#f5f6f7;border:1px solid #4a4a4a;border-top-color:#ccc;height:40px}#fb_dialog_loader_close{float:left}.fb_dialog.fb_dialog_mobile .fb_dialog_close_button{text-shadow:rgba(0, 30, 84, .296875) 0 -1px 0}.fb_dialog.fb_dialog_mobile .fb_dialog_close_icon{visibility:hidden}#fb_dialog_loader_spinner{animation:rotateSpinner 1.2s linear infinite;background-color:transparent;background-image:url(https://static.xx.fbcdn.net/rsrc.php/v3/yD/r/t-wz8gw1xG1.png);background-position:50% 50%;background-repeat:no-repeat;height:24px;width:24px}@keyframes rotateSpinner{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
.fb_iframe_widget{display:inline-block;position:relative}.fb_iframe_widget span{display:inline-block;position:relative;text-align:justify}.fb_iframe_widget iframe{position:absolute}.fb_iframe_widget_fluid_desktop,.fb_iframe_widget_fluid_desktop span,.fb_iframe_widget_fluid_desktop iframe{max-width:100%}.fb_iframe_widget_fluid_desktop iframe{min-width:220px;position:relative}.fb_iframe_widget_lift{z-index:1}.fb_iframe_widget_fluid{display:inline}.fb_iframe_widget_fluid span{width:100%}</style><script type="text/javascript" charset="UTF-8" src="./Seznam únikových her_files/common(1).js"></script><script type="text/javascript" charset="UTF-8" src="./Seznam únikových her_files/util.js"></script></head>
<body class="product_category scrolled"><div id="StayFocusd-infobar" style="display: none; top: 640px;">
    <img src="chrome-extension://laankejkbhbdhmipfmgcngdelahlfoji/common/img/eye_19x19_red.png">
    <span id="StayFocusd-infobar-msg"></span>
    <span id="StayFocusd-infobar-links">
        <a id="StayFocusd-infobar-never-show">hide forever</a>&nbsp;&nbsp;|&nbsp;&nbsp;
        <a id="StayFocusd-infobar-hide">hide once</a>
    </span>
</div>

    <div id="fb-root" class=" fb_reset"><div style="position: absolute; top: -10000px; width: 0px; height: 0px;"><div><iframe name="fb_xdm_frame_https" frameborder="0" allowtransparency="true" allowfullscreen="true" scrolling="no" allow="encrypted-media" id="fb_xdm_frame_https" aria-hidden="true" title="Facebook Cross Domain Communication Frame" tabindex="-1" src="./Seznam únikových her_files/vy-MhgbfL4v.html" style="border: none;"></iframe></div><div></div></div></div>
    <script>(function (d, s, id) {
            var js, fjs = d.getElementsByTagName(s)[0];
            if (d.getElementById(id))
                return;
            js = d.createElement(s);
            js.id = id;
            js.src = "//connect.facebook.net/cs_CZ/sdk.js#xfbml=1&version=v2.4&appId=470081443178894";
            fjs.parentNode.insertBefore(js, fjs);
        }(document, 'script', 'facebook-jssdk'));</script>

    <div class="page">
        <div id="header">
            <div class="container">
                <div class="row">
                                        <div class="logo col-md-2 col-sm-6">
                        <a href="https://www.exitgames.cz/">
                            <img src="./Seznam únikových her_files/logo-2x.png" title="ExitGames.cz" alt="ExitGames.cz">
                            <h1>ExitGames.cz</h1>
                        </a>
                    </div>
                                        <div class="col-md-10 col-sm-6 menu">
                        <div class="claim">„Všechny únikové hry v ČR <em>na jednom místě!“</em></div>
                        <button class="c-hamburger c-hamburger-htx">
                            <span>toggle menu</span>
                        </button>
                        <ul class="main-menu">
                            <li class="hidden-sm"><a data-section="#jak-postupovat" href="https://www.exitgames.cz/#jak-postupovat">Jak zakoupit hru</a></li>
                            <li><a href="https://www.exitgames.cz/seznam-unikovych-her">Seznam únikových her</a></li>
                            <li><a href="https://www.exitgames.cz/last-minute-unikove-hry">LAST MINUTE hry</a></li>
                            <li><a href="https://www.exitgames.cz/galerie">Galerie</a></li>
                            <li class="hidden-sm"><a href="https://www.exitgames.cz/Casto-kladene-dotazy-i11">FAQ</a></li>
                            <li class="hidden-sm"><a href="https://www.exitgames.cz/kontakty">Kontakty</a></li>
                                                        <li><a class="login" href="https://www.exitgames.cz/account/login"><i class="fa fa-user-o" aria-hidden="true"></i> Přihlásit</a></li>
                                                                                    <li class="languages-wrap">
    <form action="https://www.exitgames.cz/index.php?route=module/language" method="post" enctype="multipart/form-data">
        <div id="language">
                        <img src="./Seznam únikových her_files/gb.png" alt="English" title="English" onclick="$(&#39;input[name=\&#39;language_code\&#39;]&#39;).attr(&#39;value&#39;, &#39;en&#39;); $(this).parent().parent().submit();">
                        <input type="hidden" name="language_code" value="">
            <input type="hidden" name="redirect" value="https://www.exitgames.cz/seznam-unikovych-her">
        </div>
    </form>
</li>
                        </ul>
                                            </div>
                </div>

            </div>
        </div>
        <div class="notifications">
            <div class="container">
                                <div id="notification"></div>
            </div>
        </div>
<div class="main-content category-page ">
    <div class="container">
        <div class="breadcrumb">
            <div class="container" itemscope="" itemtype="http://schema.org/BreadcrumbList">
                                <span itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem"><a itemprop="item" href="https://www.exitgames.cz/"><span itemprop="name">Domů</span><meta itemprop="position" content="0"></a></span>
                                 &gt; <span itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem"><a itemprop="item" href="https://www.exitgames.cz/seznam-unikovych-her"><span itemprop="name">Seznam únikových her</span><meta itemprop="position" content="1"></a></span>
                            </div>
        </div>
         
                <div class="row">
            <div class="col-xs-12">
                <h2>Seznam únikových her</h2>
                <div></div><br>               
                
                <div class="google-maps category-map">
                    <div id="map_canvas"></div>
                </div>

                <!--<h3 class='text-center text-green'>Filtrovat dle:</h3>-->
                <form id="filter" action="https://www.exitgames.cz/seznam-unikovych-her">
                    <div class="row new-filter">
                        <div class="col-md-3 col-sm-6">
                            <div class="filter-map">
                                <label>Mapa</label>
                                <div class="google-maps-thumb">
                                    <img src="./Seznam únikových her_files/filter-map.png">
                                    <div class="map-hover text-center" data-open="Zobrazit hry na mapě" data-close="Skrýt mapu">
                                        <span class="orange">Zobrazit hry na mapě</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3 col-sm-6">
                            <div class="city-filter">
                                <label>Město</label>
                                <select name="city" class="ui-select not-auto-filter" id="ui-id-2" style="display: none;">
                                    <option value="" selected="selected">Nerozhoduje</option>
                                                                        <option data-url="praha" value="Praha">Praha</option>
                                                                        <option data-url="adamov" value="Adamov">Adamov</option>
                                                                        <option data-url="brno" value="Brno">Brno</option>
                                                                        <option data-url="cesky-krumlov" value="Český Krumlov">Český Krumlov</option>
                                                                        <option data-url="chomutov" value="Chomutov">Chomutov</option>
                                                                        <option data-url="varnsdorf" value="Varnsdorf">Varnsdorf</option>
                                                                        <option data-url="zlin" value="Zlín">Zlín</option>
                                                                    </select><span class="ui-selectmenu-button ui-widget ui-state-default ui-corner-all" tabindex="0" id="ui-id-2-button" role="combobox" aria-expanded="false" aria-autocomplete="list" aria-owns="ui-id-2-menu" aria-haspopup="true" style="width: 163px;"><span class="ui-icon ui-icon-triangle-1-s"></span><span class="ui-selectmenu-text">Nerozhoduje</span></span>
                            </div>
                            <div class="restaurant-filter">
                                <label>Operátor</label>
                                <select name="place" class="ui-select not-auto-filter" id="ui-id-3" style="display: none;">
                                    <option value="" selected="selected">Všichni operátoři</option>
                                                                        <option value="adrenalin-point">Adrenalin Point</option>
                                                                        <option value="chess-key-room">Chess KEY Room</option>
                                                                        <option value="coderoom">CodeRoom</option>
                                                                        <option value="decrypt">DeCrypt</option>
                                                                        <option value="endorfin-world">Endorfin World</option>
                                                                        <option value="escape-master">Escape Master</option>
                                                                        <option value="escape-mystery">Escape Mystery</option>
                                                                        <option value="escape-point">Escape Point</option>
                                                                        <option value="escape-the-room">Escape the room</option>
                                                                        <option value="escapecar">EscapeCar</option>
                                                                        <option value="escapex">EscapeX</option>
                                                                        <option value="esgame">EsGame</option>
                                                                        <option value="exit-room-prague">EXIT ROOM PRAGUE</option>
                                                                        <option value="exit-room-zlin">Exit Room Zlín</option>
                                                                        <option value="exitgameprague">ExitGamePrague</option>
                                                                        <option value="extremeescape">ExtremeEscape</option>
                                                                        <option value="fastout">Fastout</option>
                                                                        <option value="get-out-fun">Get Out Fun</option>
                                                                        <option value="hunter-games">Hunter Games</option>
                                                                        <option value="jakven">JakVen</option>
                                                                        <option value="krumlov-escape-game">Krumlov Escape Game</option>
                                                                        <option value="kryptograf">Kryptograf</option>
                                                                        <option value="leave-in-hour">Leave in hour</option>
                                                                        <option value="lost-exit">Lost Exit</option>
                                                                        <option value="lostrooms">Lostrooms</option>
                                                                        <option value="maphia">Maphia</option>
                                                                        <option value="mindmaze">Mindmaze</option>
                                                                        <option value="nitroadamov">NitroAdamov</option>
                                                                        <option value="puzzle-room">Puzzle Room</option>
                                                                        <option value="quest-adventure">Quest Adventure</option>
                                                                        <option value="questerland">Questerland</option>
                                                                        <option value="questroom">Questroom</option>
                                                                        <option value="riddle-twist">Riddle Twist</option>
                                                                        <option value="runaway-praha-6">RunAway Praha 6</option>
                                                                        <option value="runaway-praha-7">RunAway Praha 7</option>
                                                                        <option value="tajemstvi-hlavolamu">Tajemství hlavolamu</option>
                                                                        <option value="the-chamber">The Chamber</option>
                                                                        <option value="the-room">The Room</option>
                                                                        <option value="torch-vr">Torch VR</option>
                                                                        <option value="trap-catch">TRAP CATCH</option>
                                                                        <option value="trapasmamas">TrapAsMamas</option>
                                                                        <option value="unique-room">Unique Room</option>
                                                                        <option value="utekycz">Uteky.cz</option>
                                                                    </select><span class="ui-selectmenu-button ui-widget ui-state-default ui-corner-all" tabindex="0" id="ui-id-3-button" role="combobox" aria-expanded="false" aria-autocomplete="list" aria-owns="ui-id-3-menu" aria-haspopup="true" style="width: 217px;"><span class="ui-icon ui-icon-triangle-1-s"></span><span class="ui-selectmenu-text">Všichni operátoři</span></span>
                            </div>
                        </div>
                        <div class="visible-sm clearfix"></div>
                        <div class="col-md-3 col-sm-6">
                            <div class="row">
                                <div class="col-xs-12">
                                    <div class="game-type-filter">
                                        <label>Typ hry</label>
                                        <select name="game_type" class="ui-select not-auto-filter" id="ui-id-4" style="display: none;">
                                            <option value="" selected="selected">Nerozhoduje</option>
                                                                                        <option data-url="klasicka" value="1">klasická</option>
                                                                                        <option data-url="2-tymy" value="2">2 tymy</option>
                                                                                    </select><span class="ui-selectmenu-button ui-widget ui-state-default ui-corner-all" tabindex="0" id="ui-id-4-button" role="combobox" aria-expanded="false" aria-autocomplete="list" aria-owns="ui-id-4-menu" aria-haspopup="true" style="width: 149px;"><span class="ui-icon ui-icon-triangle-1-s"></span><span class="ui-selectmenu-text">Nerozhoduje</span></span>
                                    </div>
                                </div>
                                <div class="col-xs-6 pr-small">
                                    <div class="date-filter">
                                        <label>Dle přidání</label>
                                        <select name="date_added" class="ui-select" id="ui-id-5" style="display: none;">
                                            <option value="" selected="selected">Nerozhoduje</option>
                                            <option value="DESC">nejnovější</option>
                                            <option value="ASC">nejstarší</option>
                                        </select><span class="ui-selectmenu-button ui-widget ui-state-default ui-corner-all" tabindex="0" id="ui-id-5-button" role="combobox" aria-expanded="false" aria-autocomplete="list" aria-owns="ui-id-5-menu" aria-haspopup="true" style="width: 149px;"><span class="ui-icon ui-icon-triangle-1-s"></span><span class="ui-selectmenu-text">Nerozhoduje</span></span>
                                    </div>
                                </div>
                                <div class="col-xs-6 pl-small">
                                    <div class="price-filter">
                                        <label>Cena</label>
                                        <select name="price" class="ui-select" id="ui-id-6" style="display: none;">
                                            <option value="" selected="selected">Nerozhoduje</option>
                                            <option value="DESC">nejdražší</option>
                                            <option value="ASC">nejlevnější</option>
                                        </select><span class="ui-selectmenu-button ui-widget ui-state-default ui-corner-all" tabindex="0" id="ui-id-6-button" role="combobox" aria-expanded="false" aria-autocomplete="list" aria-owns="ui-id-6-menu" aria-haspopup="true" style="width: 149px;"><span class="ui-icon ui-icon-triangle-1-s"></span><span class="ui-selectmenu-text">Nerozhoduje</span></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3 col-sm-6">
                            <div class="row">
                                <div class="col-xs-12">
                                    <div class="search-filter">
                                        <label>Hledat dle názvu</label>
                                        <div class="input-search">
                                            <input type="text" name="filter_name" value="" placeholder="Zadej název hry/operátora" class="ui-autocomplete-input" autocomplete="off">
                                            <a href="javascript:;" title="Hledat"><i class="fa fa-search"></i></a>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xs-6 pr-small">
                                    <div class="rating-filter">
                                        <label>Hodnocení</label>
                                        <select name="rating_filter" class="ui-select" id="ui-id-7" style="display: none;">
                                            <option value="">Nerozhoduje</option>
                                            <option value="DESC">nejlepší</option>
                                            <option value="ASC">nejhorší</option>
                                        </select><span class="ui-selectmenu-button ui-widget ui-state-default ui-corner-all" tabindex="0" id="ui-id-7-button" role="combobox" aria-expanded="false" aria-autocomplete="list" aria-owns="ui-id-7-menu" aria-haspopup="true" style="width: 149px;"><span class="ui-icon ui-icon-triangle-1-s"></span><span class="ui-selectmenu-text">Nerozhoduje</span></span>
                                    </div>
                                </div>
                                <div class="col-xs-6 pl-small">
                                    <div class="difficulty-filter">
                                        <label>Obtížnost</label>
                                        <select name="difficulty_filter" class="ui-select" id="ui-id-8" style="display: none;">
                                            <option value="">Nerozhoduje</option>
                                            <option value="DESC">nejtežší</option>
                                            <option value="ASC">nejlehčí</option>
                                        </select><span class="ui-selectmenu-button ui-widget ui-state-default ui-corner-all" tabindex="0" id="ui-id-8-button" role="combobox" aria-expanded="false" aria-autocomplete="list" aria-owns="ui-id-8-menu" aria-haspopup="true" style="width: 149px;"><span class="ui-icon ui-icon-triangle-1-s"></span><span class="ui-selectmenu-text">Nerozhoduje</span></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </form>
                                <input type="hidden" id="page" value="2">
                                <div class="product-list items box-product">
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
                               <img src="./Seznam únikových her_files/dum-duchu-male-3-e1479292532150-280x210crop.jpg" alt="Dům duchů">
                            </a>
                        </div>
                        <div class="info">
                            <div class="name"><a href="https://www.exitgames.cz/praha-the-chamber-dum-duchu">Dům duchů</a></div>
                            <div class="partner"><a href="https://www.exitgames.cz/seznam-unikovych-her/the-chamber">The Chamber</a></div>
                            <div class="description">Ten dům byl téměř půl století opuštěný. Všichni se od něj drželi dál, mnozí neměli ani odvahu se podívat do zatažených oken. Stigma, které si nesl, bylo moc...</div>
                            <div class="btn-detail">
                                <div class="price">Cena od: <span class="value">1 590 Kč / skupina</span></div>
                                <a href="https://www.exitgames.cz/praha-the-chamber-dum-duchu" class="btn btn-small-filled" title="Dům duchů">zobrazit hru</a>
                            </div>
                        </div>
                    </div>
                                        <div class="product">
                                                <div class="flags">
                                                        <div class="flag-featured"><span>TOP</span></div>
                                                                                                                                            <div class="rating rating-small rating-5"></div>
                                                                                    <div class="difficulty difficulty-small difficulty-4">
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                                                <span class="icon-bulb-empty"></span>
                                                            </div>
                                                    </div>
                                                <div class="image">
                            <a href="https://www.exitgames.cz/praha-the-chamber-utek-ze-zalare" title="Útěk ze žaláře">
                               <img src="./Seznam únikových her_files/IMG_6509-edit-smaller-e1479295796281-280x210crop.jpg" alt="Útěk ze žaláře">
                            </a>
                        </div>
                        <div class="info">
                            <div class="name"><a href="https://www.exitgames.cz/praha-the-chamber-utek-ze-zalare">Útěk ze žaláře</a></div>
                            <div class="partner"><a href="https://www.exitgames.cz/seznam-unikovych-her/the-chamber">The Chamber</a></div>
                            <div class="description">Bezprostředně poté, co jste statečně rozkryli tajemství Karla IV., jste ve spánku uprostřed noci uneseni tajemnými muži v kápích. Probouzíte se v neznámé starobylé...</div>
                            <div class="btn-detail">
                                <div class="price">Cena od: <span class="value">1 290 Kč / skupina</span></div>
                                <a href="https://www.exitgames.cz/praha-the-chamber-utek-ze-zalare" class="btn btn-small-filled" title="Útěk ze žaláře">zobrazit hru</a>
                            </div>
                        </div>
                    </div>
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
                               <img src="./Seznam únikových her_files/Doupě neřesti_poháry-280x210crop.jpg" alt="Doupě neřesti (hra nejen pro páry)">
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
                                <a href="https://www.exitgames.cz/praha-chess-key-room-doupe-neresti" class="btn btn-small-filled" title="Doupě neřesti (hra nejen pro páry)">zobrazit hru</a>
                            </div>
                        </div>
                    </div>
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
                            <a href="https://www.exitgames.cz/praha-the-chamber-tajemstvi-cisare" title="Tajemství císaře">
                               <img src="./Seznam únikových her_files/pDSC_9789-e1478698161779-280x210crop.jpg" alt="Tajemství císaře">
                            </a>
                        </div>
                        <div class="info">
                            <div class="name"><a href="https://www.exitgames.cz/praha-the-chamber-tajemstvi-cisare">Tajemství císaře</a></div>
                            <div class="partner"><a href="https://www.exitgames.cz/seznam-unikovych-her/the-chamber">The Chamber</a></div>
                            <div class="description">Nejvýznamnější český panovník, Karel IV., je doposud obestřen mnoha nejasnostmi a tajemstvími, jež jsou předmětem Vašeho bádání v naší nové...</div>
                            <div class="btn-detail">
                                <div class="price">Cena od: <span class="value">1 190 Kč / skupina</span></div>
                                <a href="https://www.exitgames.cz/praha-the-chamber-tajemstvi-cisare" class="btn btn-small-filled" title="Tajemství císaře">zobrazit hru</a>
                            </div>
                        </div>
                    </div>
                                        <div class="product">
                                                <div class="flags">
                                                        <div class="flag-featured"><span>TOP</span></div>
                                                                                                                                            <div class="rating rating-small rating-5"></div>
                                                                                    <div class="difficulty difficulty-small difficulty-4">
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                                                <span class="icon-bulb-empty"></span>
                                                            </div>
                                                    </div>
                                                <div class="image">
                            <a href="https://www.exitgames.cz/Praha-Maphia-game" title="Maphia game">
                               <img src="./Seznam únikových her_files/ruka-280x210crop.jpg" alt="Maphia game">
                            </a>
                        </div>
                        <div class="info">
                            <div class="name"><a href="https://www.exitgames.cz/Praha-Maphia-game">Maphia game</a></div>
                            <div class="partner"><a href="https://www.exitgames.cz/seznam-unikovych-her/maphia">Maphia</a></div>
                            <div class="description">Don Katto se má sejít se svým dlouholetým přítelem Tomem Grahamem. Měli se potkat v opuštěném a zchátralém baru, za účelem velkého obchodu. Jelikož se Tom na výzvy...</div>
                            <div class="btn-detail">
                                <div class="price">Cena od: <span class="value">1 300 Kč / skupina</span></div>
                                <a href="https://www.exitgames.cz/Praha-Maphia-game" class="btn btn-small-filled" title="Maphia game">zobrazit hru</a>
                            </div>
                        </div>
                    </div>
                                        <div class="product">
                                                <div class="flags">
                                                        <div class="flag-featured"><span>TOP</span></div>
                                                                                                                                            <div class="rating rating-small rating-5"></div>
                                                                                    <div class="difficulty difficulty-small difficulty-4">
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                                                <span class="icon-bulb-empty"></span>
                                                            </div>
                                                    </div>
                                                <div class="image">
                            <a href="https://www.exitgames.cz/anonymous" title="Anonymous (venkovní mise)">
                               <img src="./Seznam únikových her_files/Anonymous hlavní-280x210crop.jpeg" alt="Anonymous (venkovní mise)">
                            </a>
                        </div>
                        <div class="info">
                            <div class="name"><a href="https://www.exitgames.cz/anonymous">Anonymous (venkovní mise)</a></div>
                            <div class="partner"><a href="https://www.exitgames.cz/seznam-unikovych-her/hunter-games">Hunter Games</a></div>
                            <div class="description">Určitě znáš ten tíživý pocit, že tě někdo sleduje. Rozhlížíš se kolem, nevidíš nic neobvyklého, ale ten pocit neklidu přesto zůstává...
Jenže ty se...</div>
                            <div class="btn-detail">
                                <div class="price">Cena od: <span class="value">900 Kč / skupina</span></div>
                                <a href="https://www.exitgames.cz/anonymous" class="btn btn-small-filled" title="Anonymous (venkovní mise)">zobrazit hru</a>
                            </div>
                        </div>
                    </div>
                                        <div class="product">
                                                <div class="flags">
                                                        <div class="flag-featured"><span>TOP</span></div>
                                                                                                                                            <div class="rating rating-small rating-5"></div>
                                                                                    <div class="difficulty difficulty-small difficulty-4">
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                                                <span class="icon-bulb-empty"></span>
                                                            </div>
                                                    </div>
                                                <div class="image">
                            <a href="https://www.exitgames.cz/muz-bez-minulosti" title="Muž bez minulosti (venkovní mise)">
                               <img src="./Seznam únikových her_files/muž bez minulosti hl.-280x210crop.jpeg" alt="Muž bez minulosti (venkovní mise)">
                            </a>
                        </div>
                        <div class="info">
                            <div class="name"><a href="https://www.exitgames.cz/muz-bez-minulosti">Muž bez minulosti (venkovní mise)</a></div>
                            <div class="partner"><a href="https://www.exitgames.cz/seznam-unikovych-her/hunter-games">Hunter Games</a></div>
                            <div class="description">Probral jsem se na lavičce uprostřed neznámého města. Vůbec nevím, kde jsem, kdo jsem, jak se jmenuji, ani jak jsem se tu octl. Vím jediné - ukrutně mě bolí hlava.
Podaří se mi zjistit, kdo jsem a...</div>
                            <div class="btn-detail">
                                <div class="price">Cena od: <span class="value">900 Kč / skupina</span></div>
                                <a href="https://www.exitgames.cz/muz-bez-minulosti" class="btn btn-small-filled" title="Muž bez minulosti (venkovní mise)">zobrazit hru</a>
                            </div>
                        </div>
                    </div>
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
                            <a href="https://www.exitgames.cz/praha-hunter-games-assassins-girl" title="Assassin´s girl (venkovní mise)">
                               <img src="./Seznam únikových her_files/Assassin_girl_ExitGames_1200-628_facebook-280x210crop.jpg" alt="Assassin´s girl (venkovní mise)">
                            </a>
                        </div>
                        <div class="info">
                            <div class="name"><a href="https://www.exitgames.cz/praha-hunter-games-assassins-girl">Assassin´s girl (venkovní mise)</a></div>
                            <div class="partner"><a href="https://www.exitgames.cz/seznam-unikovych-her/hunter-games">Hunter Games</a></div>
                            <div class="description">Proměň se v asasínku, členku cechu zabijáků. Čeká tě nemilosrdný boj na život a na smrt. Venkovní úniková hra Assassin´s Girl od Hunter Games tě zavede do Prahy roku 1588. Na cestě budeš...</div>
                            <div class="btn-detail">
                                <div class="price">Cena od: <span class="value">2 670 Kč / skupina</span></div>
                                <a href="https://www.exitgames.cz/praha-hunter-games-assassins-girl" class="btn btn-small-filled" title="Assassin´s girl (venkovní mise)">zobrazit hru</a>
                            </div>
                        </div>
                    </div>
                                        <div class="product">
                                                <div class="flags">
                                                        <div class="flag-featured"><span>TOP</span></div>
                                                                                                                                            <div class="rating rating-small rating-5"></div>
                                                                                    <div class="difficulty difficulty-small difficulty-4">
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                                                <span class="icon-bulb-empty"></span>
                                                            </div>
                                                    </div>
                                                <div class="image">
                            <a href="https://www.exitgames.cz/praha-hunter-games-kletba-vysehradu" title="Kletba Vyšehradu - venkovní mise (noční)">
                               <img src="./Seznam únikových her_files/PoselSmrti-280x210crop.jpg" alt="Kletba Vyšehradu - venkovní mise (noční)">
                            </a>
                        </div>
                        <div class="info">
                            <div class="name"><a href="https://www.exitgames.cz/praha-hunter-games-kletba-vysehradu">Kletba Vyšehradu - venkovní mise (noční)</a></div>
                            <div class="partner"><a href="https://www.exitgames.cz/seznam-unikovych-her/hunter-games">Hunter Games</a></div>
                            <div class="description">Smrtí děj nekončí, ale začíná. Venkovní úniková hra Kletba Vyšehradu od Hunter Games otestuje tvou bystrost, vytrvalost a odvahu. Dva bratři míří na Vyšehrad....</div>
                            <div class="btn-detail">
                                <div class="price">Cena od: <span class="value">2 670 Kč / skupina</span></div>
                                <a href="https://www.exitgames.cz/praha-hunter-games-kletba-vysehradu" class="btn btn-small-filled" title="Kletba Vyšehradu - venkovní mise (noční)">zobrazit hru</a>
                            </div>
                        </div>
                    </div>
                                        <div class="product">
                                                <div class="flags">
                                                        <div class="flag-featured"><span>TOP</span></div>
                                                                                                                                            <div class="rating rating-small rating-5"></div>
                                                                                    <div class="difficulty difficulty-small difficulty-4">
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                <span class="icon-bulb"></span>
                                                                                                <span class="icon-bulb-empty"></span>
                                                            </div>
                                                    </div>
                                                <div class="image">
                            <a href="https://www.exitgames.cz/praha-chesskeyroom-upiri-hrobka" title="Upíří hrobka">
                               <img src="./Seznam únikových her_files/Upíří hrobka Chess KEY Room interier 1-280x210crop.JPG" alt="Upíří hrobka">
                            </a>
                        </div>
                        <div class="info">
                            <div class="name"><a href="https://www.exitgames.cz/praha-chesskeyroom-upiri-hrobka">Upíří hrobka</a></div>
                            <div class="partner"><a href="https://www.exitgames.cz/seznam-unikovych-her/chess-key-room">Chess KEY Room</a></div>
                            <div class="description">Již samotný úvod této hry vrhá na hráče trochu jiný dojem než u ostatních her.
Do prostoru&nbsp; scházíte po schodech&nbsp;při rudém světle&nbsp;a room master vám po...</div>
                            <div class="btn-detail">
                                <div class="price">Cena od: <span class="value">900 Kč / skupina</span></div>
                                <a href="https://www.exitgames.cz/praha-chesskeyroom-upiri-hrobka" class="btn btn-small-filled" title="Upíří hrobka">zobrazit hru</a>
                            </div>
                        </div>
                    </div>
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
                            <a href="https://www.exitgames.cz/praha-trapasmamas-jumanji-jungle" title="Jumanji JUNGLE">
                               <img src="./Seznam únikových her_files/Jungle-800x800 (1)-280x210crop.jpg" alt="Jumanji JUNGLE">
                            </a>
                        </div>
                        <div class="info">
                            <div class="name"><a href="https://www.exitgames.cz/praha-trapasmamas-jumanji-jungle">Jumanji JUNGLE</a></div>
                            <div class="partner"><a href="https://www.exitgames.cz/seznam-unikovych-her/trapasmamas">TrapAsMamas</a></div>
                            <div class="description">Konečně hra také pro RODINY s dětmi!
JUNGLE je oblíbená a světově prověřená hra s velmi vysokým&nbsp;technickým zpracováním. Je postavena na skvělém...</div>
                            <div class="btn-detail">
                                <div class="price">Cena od: <span class="value">1 290 Kč / skupina</span></div>
                                <a href="https://www.exitgames.cz/praha-trapasmamas-jumanji-jungle" class="btn btn-small-filled" title="Jumanji JUNGLE">zobrazit hru</a>
                            </div>
                        </div>
                    </div>
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
                            <a href="https://www.exitgames.cz/zlodeji-snu" title="Zloději snů">
                               <img src="./Seznam únikových her_files/escapex-280x210crop.jpg" alt="Zloději snů">
                            </a>
                        </div>
                        <div class="info">
                            <div class="name"><a href="https://www.exitgames.cz/zlodeji-snu">Zloději snů</a></div>
                            <div class="partner"><a href="https://www.exitgames.cz/seznam-unikovych-her/escapex">EscapeX</a></div>
                            <div class="description">Máte rádi film Inception, postavený na více úrovních reality?
Tato úniková&nbsp;hra od EscapeX Vás dostane do snu světoznámého neurologa profesora Jeana Charcota...</div>
                            <div class="btn-detail">
                                <div class="price">Cena od: <span class="value">1 099 Kč / skupina</span></div>
                                <a href="https://www.exitgames.cz/zlodeji-snu" class="btn btn-small-filled" title="Zloději snů">zobrazit hru</a>
                            </div>
                        </div>
                    </div>
                                    </div>
                                <br><div class="text-center"><a href="javascript:;" id="next_products" class="btn btn-border">NAČÍST DALŠÍ</a></div>
                                <div class="pagination"></div>
                            </div>
        </div>
    </div>
</div>

<div class="footer-newsletter">
    <div class="container">
        <div class="newsletter-form row">
            <div class="col-md-4">
                <h4>Newsletter <small>1x měsíčně info o nových hrách a akcích!</small></h4>
            </div>
            <div class="col-md-4 form-mat">
                <div class="group">      
                    <input type="text" required="required" class="newsletter-email">
                    <span class="bar"></span>
                    <span class="message"></span>
                    <label>Váš email</label>
                </div>
            </div>
            <div class="col-md-4 text-right">
                <a class="button btn btn-border btn-small newsletter-send" href="javascript:;">Přihlásit k odběru</a>
            </div>
        </div>
    </div>
</div>
<div class="footer" id="footer">
    <div class="container">
        <div class="row">
            <div class="col-xs-12 text-center">
                <h3>Kontakty</h3>
            </div>
        </div>
        <div class="row footer-contacts">
            <div class="col-md-4 pt">
                <span class="icon-phone"></span><span><a href="tel:+420778001091" title="Zatelefonujte nám">+420 778 001 091</a><span><strong>Ověřování termínů</strong>, obecné dotazy</span></span>
            </div>
            <div class="col-md-4 pt">
                <span class="icon-email"></span><span><a href="mailto:info@exitgames.cz" title="Napište nám email">info@exitgames.cz</a><span>Obecné dotazy, spolupráce, teambuilding</span></span>
            </div>
            <div class="col-md-4 facebook">
                <div class="fb-page fb_iframe_widget" data-href="https://www.facebook.com/exitgamescz/timeline/" data-height="100" data-small-header="false" data-adapt-container-width="true" data-hide-cover="false" data-show-facepile="false" data-show-posts="false" fb-xfbml-state="rendered" fb-iframe-plugin-query="adapt_container_width=true&amp;app_id=470081443178894&amp;container_width=360&amp;height=100&amp;hide_cover=false&amp;href=https%3A%2F%2Fwww.facebook.com%2Fexitgamescz%2Ftimeline%2F&amp;locale=cs_CZ&amp;sdk=joey&amp;show_facepile=false&amp;show_posts=false&amp;small_header=false"><span style="vertical-align: bottom; width: 340px; height: 130px;"><iframe name="f18e1fae24c01d" width="1000px" height="100px" frameborder="0" allowtransparency="true" allowfullscreen="true" scrolling="no" allow="encrypted-media" title="fb:page Facebook Social Plugin" src="./Seznam únikových her_files/page.html" style="border: none; visibility: visible; width: 340px; height: 130px;" class=""></iframe></span></div>
            </div>
        </div>
    </div>
</div>
<footer>   
    <div class="container">
        <div class="row">
            <div class="col-md-3 copyright">
                © 2019 ExitGames.cz<span><br>Všechna práva vyhrazena</span>
            </div>
            <div class="col-md-6 footer-links text-center">
                                <a href="https://www.exitgames.cz/Obchodni-podminky-i2" title="Obchodní podmínky">Obchodní podmínky</a> | 
                                <a href="https://www.exitgames.cz/Casto-kladene-dotazy-i11" title="Často kladené dotazy">Často kladené dotazy</a> | 
                                <a href="https://www.exitgames.cz/admin" title="Přihlášení partnera">Přihlášení partnera</a>
            </div>
            <div class="col-md-3 footer-links text-right">
                <span>Created by</span> <a href="http://www.tsunamidigital.cz/" title="TsunamiDigital" target="_blank"><img src="./Seznam únikových her_files/tsunami-digital-logo-mini.png" class="tsunami-logo" alt="TsunamiDigital"></a> &amp; <a href="http://www.innoit.cz/" title="Tvorba e-shopů INNOIT" target="_blank">INNOIT</a>
            </div>
        </div>
    </div>
</footer>
<script type="text/javascript">
    /* <![CDATA[ */
    var google_conversion_id = 925928721;
    var google_custom_params = window.google_tag_params;
    var google_remarketing_only = true;
    /* ]]> */
</script>
<script type="text/javascript" src="./Seznam únikových her_files/f(1).txt">
</script>
<noscript>
<div style="display:inline;">
    <img height="1" width="1" style="border-style:none;" alt="" src="//googleads.g.doubleclick.net/pagead/viewthroughconversion/925928721/?guid=ON&amp;script=0"/>
</div>
</noscript>



    <script type="text/javascript"><!--
        
        var is_last_minute = '';
        
        function getFilterUrl(){
             var data = $('#filter').serializeArray();
             
             var url = '';
             
             if($('select[name="city"]').val()){
                 url += '/' + $('select[name="city"] option:selected').data('url');
             }
             
            if($('select[name="place"]').val()){
                 url += '/' + $('select[name="place"]').val();
            }
            
            if($('select[name="game_type"]').val() /*&& $('select[name="game_type"]').val() != '1'*/){
                 url += '/' + $('select[name="game_type"] option:selected').data('url');
            }
            
            if($('input[name="filter_name"]').val()){
                 url += '/' + $('input[name="filter_name"]').val();
            }
            
            index = 0;
            
             $(data).each(function(i, v){
                if(v.value != '' && v.name != 'city' && v.name != 'place' && v.name != 'game_type' && v.name != 'filter_name'){
                    if(v.name == 'zone'){
                        url += '/' + v.value;
                    }else{
                        url += (index++ == 0 ? '?' : '&') + v.name + '=' + v.value;
                    }
                 }
            });
            
            return $('#filter').attr('action') + url;
        }
        
        $(function () {
            var filterChange = function (event, ui) {
                $('.filter_by select:not(select[name="' + event.target.attributes.name.value + '"])').attr('disabled', 'disabled');
                window.location.href = getFilterUrl();
            };
            
            $('.search-filter a').click(function(){     
                if(searchResult !== null){
                    window.location.href = searchResult;
                }else{
                    window.location.href = getFilterUrl();
                }
            });
            
            $(".rating-select")
                .iconselectmenu({
                    change: filterChange,
                    create: function (event, ui) {
                        $('.rating-filter .ui-selectmenu-button').addClass('data-rate-' + $('.filter select[name=rating]').val());
                    }
                })
                .iconselectmenu("menuWidget")
                .addClass("ui-rating");
            $(".ui-select")
                .iconselectmenu({
                    change: filterChange
                })
                .iconselectmenu("menuWidget")
                .addClass("ui-styled");
        });


        var setting = new Array();
                                   
        $(document).ready(function () {
            $('.google-maps-thumb').click(function(){
                $('.category-map').toggleClass('active');
                if($('.category-map').hasClass('active')){
                    $('.map-hover span').text($('.map-hover').data('close'));
                    if(!$('#map_canvas .gm-style').length){
                        $('#map_canvas').slideToggle(300, function(){
                            inicializeMap(setting);
                        });
                    }else{
                        $('#map_canvas').slideToggle(300);
                    }
                }else{
                    $('#map_canvas').slideToggle();
                    $('.map-hover span').text($('.map-hover').data('open'));
                }
            });


            $("#next_products").on('click', function () {
                getProducts();
            });

            $("#filter").bind('keydown', function(e){
                
                if (e.keyCode == 13) {
                    e.preventDefault();
                    window.location.href = getFilterUrl();
                
                    return false;
                }
            });
            
            setting.markers = new Array();
                                    setting.markers[0] = { latitude:50.0917019,longitude:14.4294711, name: "Dům duchů",href:"https://www.exitgames.cz/praha-the-chamber-dum-duchu",town_detail: "Praha 1",street_detail: "Petrské nám. 1",restaurant_name_detail: "The Chamber - Petrské nám." };
                                    setting.markers[1] = { latitude:50.0917019,longitude:14.4294711, name: "Útěk ze žaláře",href:"https://www.exitgames.cz/praha-the-chamber-utek-ze-zalare",town_detail: "Praha 1",street_detail: "Petrské nám. 1",restaurant_name_detail: "The Chamber - Petrské nám." };
                                    setting.markers[2] = { latitude:50.0902529,longitude:14.4440041, name: "Doupě neřesti (hra nejen pro páry)",href:"https://www.exitgames.cz/praha-chess-key-room-doupe-neresti",town_detail: "Praha 8",street_detail: "Vítkova 244/8",restaurant_name_detail: "Chess Key Room" };
                                    setting.markers[3] = { latitude:50.0781872,longitude:14.419307, name: "Tajemství císaře",href:"https://www.exitgames.cz/praha-the-chamber-tajemstvi-cisare",town_detail: "Praha 1",street_detail: "Vodičkova 1",restaurant_name_detail: "The Chamber - Vodičkova" };
                                    setting.markers[4] = { latitude:50.08998,longitude:14.44919, name: "Maphia game",href:"https://www.exitgames.cz/Praha-Maphia-game",town_detail: "Praha 8",street_detail: "Pernerova 391/10",restaurant_name_detail: "Maphia.cz" };
                                    setting.markers[5] = { latitude:50.08533,longitude:14.44488, name: "Anonymous (venkovní mise)",href:"https://www.exitgames.cz/anonymous",town_detail: "Praha 3",street_detail: "Seifertova 559/51",restaurant_name_detail: "Hunter Games" };
                                    setting.markers[6] = { latitude:50.08536,longitude:14.42164, name: "Muž bez minulosti (venkovní mise)",href:"https://www.exitgames.cz/muz-bez-minulosti",town_detail: "Praha 1",street_detail: "Havelská 503/19",restaurant_name_detail: "Hunter Games" };
                                    setting.markers[7] = { latitude:50.0873882,longitude:14.4166422, name: "Assassin´s girl (venkovní mise)",href:"https://www.exitgames.cz/praha-hunter-games-assassins-girl",town_detail: "Praha 1",street_detail: "Jánská 238/4",restaurant_name_detail: "Hunter Games" };
                                    setting.markers[8] = { latitude:50.06535,longitude:14.41928, name: "Kletba Vyšehradu - venkovní mise (noční)",href:"https://www.exitgames.cz/praha-hunter-games-kletba-vysehradu",town_detail: "Praha 2, Vyšehrad",street_detail: "Cihelná Brána, V Pevnosti 46",restaurant_name_detail: "Hunter Games" };
                                    setting.markers[9] = { latitude:50.09048,longitude:14.44613, name: "Upíří hrobka",href:"https://www.exitgames.cz/praha-chesskeyroom-upiri-hrobka",town_detail: "Praha 8",street_detail: "Vítkova 244/8",restaurant_name_detail: "Chess KEY Room" };
                                    setting.markers[10] = { latitude:50.09024,longitude:14.44619, name: "Jumanji JUNGLE",href:"https://www.exitgames.cz/praha-trapasmamas-jumanji-jungle",town_detail: "Praha 8",street_detail: "Vítkova 244/8",restaurant_name_detail: "TrapAsMamas" };
                                    setting.markers[11] = { latitude:50.08108,longitude:14.42958, name: "Zloději snů",href:"https://www.exitgames.cz/zlodeji-snu",town_detail: "Praha 1",street_detail: "Opletalova 6",restaurant_name_detail: "EscapeX" };
                                    setting.markers[12] = { latitude:50.07716,longitude:14.42793, name: "Mind Horror (virtuální realita)",href:"https://www.exitgames.cz/praha-torch-vr-mind-horror",town_detail: "Praha 1",street_detail: "Žitná 44",restaurant_name_detail: "Torch VR" };
                                    setting.markers[13] = { latitude:50.07716,longitude:14.42793, name: "Cosmos (virtuální realita)",href:"https://www.exitgames.cz/praha-torch-vr-cosmos",town_detail: "Praha 1",street_detail: "Žitná 44",restaurant_name_detail: "Torch VR" };
                                    setting.markers[14] = { latitude:50.07886,longitude:14.42836, name: "Escape bar",href:"https://www.exitgames.cz/praha-escapetheroom-escape-bar",town_detail: "Praha 2",street_detail: "Bělehradská 42",restaurant_name_detail: "Escape The Room" };
                                    setting.markers[15] = { latitude:50.08797,longitude:14.38744, name: "Archimédovo tajemství",href:"https://www.exitgames.cz/praha-run-away-archimedovo-tajemstvi",town_detail: "Praha 6",street_detail: "Parléřova 74/7",restaurant_name_detail: "Run Away" };
                                    setting.markers[16] = { latitude:50.07897,longitude:14.42785, name: "ÚTĚK Z GUANTÁNAMA",href:"https://www.exitgames.cz/Utek-z-Guantanama",town_detail: "Praha 6",street_detail: "Parléřova 74/7",restaurant_name_detail: "Run Away" };
                                    setting.markers[17] = { latitude:50.077582,longitude:14.442593, name: "Hvězdný element",href:"https://www.exitgames.cz/praha-questerland-hvezdny-element",town_detail: "Praha 2",street_detail: "Mánesova 54",restaurant_name_detail: "Questerland" };
                                    setting.markers[18] = { latitude:50.08641,longitude:14.47153, name: "Escape Car",href:"https://www.exitgames.cz/praha-escapecar",town_detail: "Praha 3, Naproti domu č.15 v areálu A+R parking",street_detail: "Jana Želivského",restaurant_name_detail: "Escape Car" };
                                    setting.markers[19] = { latitude:50.06445,longitude:14.45222, name: "Saw",href:"https://www.exitgames.cz/praha-endorfin-saw",town_detail: "Praha 10",street_detail: "Petrohradská 216/3 ",restaurant_name_detail: "Endorfin World" };
                                    setting.markers[20] = { latitude:50.09517,longitude:14.45355, name: "Sirotčinec",href:"https://www.exitgames.cz/sirotcinec",town_detail: "Praha 8",street_detail: "Pobřežní 95/74",restaurant_name_detail: "Escape Mystery" };
                                    setting.markers[21] = { latitude:50.08543,longitude:14.41660, name: "Tajemství velkého magistra",href:"https://www.exitgames.cz/quest-adventure-tajemstvi-velkeho-magistra",town_detail: "Praha 1",street_detail: "Liliová 946/14",restaurant_name_detail: "" };
                                    setting.markers[22] = { latitude:50.10188,longitude:14.45596, name: "Mentor",href:"https://www.exitgames.cz/Praha-leave-in-hour-mentor",town_detail: "Praha 7",street_detail: "Jankovcova 13",restaurant_name_detail: "Leave in hour" };
                                    setting.markers[23] = { latitude:50.07886,longitude:14.42836, name: "Profesorova pracovna",href:"https://www.exitgames.cz/praha-escapetheroom-profesorova-pracovna",town_detail: "Praha 2",street_detail: "Bělehradská 42",restaurant_name_detail: "Escape The Room" };
                                    setting.markers[24] = { latitude:50.06397,longitude:14.45210, name: "Titanic",href:"https://www.exitgames.cz/praha-endorfin-titanic",town_detail: "Praha 10",street_detail: "Petrohradská 216/3 ",restaurant_name_detail: "Titanic" };
                                    setting.markers[25] = { latitude:50.0569475,longitude:14.4383978, name: "Psychiatrická léčebna: PAVILON č. 13 - hra o život",href:"https://www.exitgames.cz/praha-escape-master-pavilon-c-13-hra-o-zivot",town_detail: "Praha 4",street_detail: "Soudní 1515/8",restaurant_name_detail: "Escape Master - Soudní " };
                                    setting.markers[26] = { latitude:50.0873882,longitude:14.4166422, name: "Legenda o Golemovi (venkovní mise)",href:"https://www.exitgames.cz/praha-hunter-games-legenda-o-golemovi",town_detail: "Praha 1",street_detail: "Mariánské nám. 98/1",restaurant_name_detail: "Hunter Games" };
                                    setting.markers[27] = { latitude:50.07551,longitude:14.44107, name: "Zvláštní škola - případ zmizelých",href:"https://www.exitgames.cz/praha-lost-exit-zvlastni-skola",town_detail: "Praha 2 - Vinohrady",street_detail: "Korunní 18",restaurant_name_detail: "" };
                                    setting.markers[28] = { latitude:50.084082,longitude:14.454628, name: "Sherlockova kancelář (souboj 2 týmů)",href:"https://www.exitgames.cz/praha-exitgameprague-sherlockova-kancelar-souboj",town_detail: "Praha 3",street_detail: "Rokycanova 459/7",restaurant_name_detail: "ExitGamesPrague" };
                                    setting.markers[29] = { latitude:50.077582,longitude:14.442593, name: "Apocalypse Zombie 2213 ",href:"https://www.exitgames.cz/praha-apocalypse-zombie-2213",town_detail: "Praha 2",street_detail: "Mánesova 54",restaurant_name_detail: "Questerland" };
                                    setting.markers[30] = { latitude:50.10888,longitude:14.43811, name: "Gulliverova cesta",href:"https://www.exitgames.cz/praha-run-away-gulliverova-cesta",town_detail: "Praha 7",street_detail: "U Elektrárny",restaurant_name_detail: "Run Away" };
                                    setting.markers[31] = { latitude:50.07080,longitude:14.43167, name: "Xaverius",href:"https://www.exitgames.cz/praha-riddle-twist-xaverius",town_detail: "Praha 2",street_detail: "Wenzigova 1857/11",restaurant_name_detail: "Riddle Twist" };
                                    setting.markers[32] = { latitude:50.100734,longitude:14.421606, name: "Golemova skrýš",href:"https://www.exitgames.cz/Golemova-skrys-p19",town_detail: "Praha 7",street_detail: "Čechova 10",restaurant_name_detail: "Puzzle Room (Čechova)" };
                                    setting.markers[33] = { latitude:50.077582,longitude:14.442593, name: "Únik z čarodějnické školy Magie a Kouzel",href:"https://www.exitgames.cz/Unik-z-carodejnicke-skoly-Magie-a-Kouzel-p15",town_detail: "Praha 2",street_detail: "Mánesova 54",restaurant_name_detail: "Questerland" };
                                    setting.markers[34] = { latitude:50.1120274,longitude:14.4757813, name: "Psychiatrická léčebna: Pokoj č. 606 - posedlá",href:"https://www.exitgames.cz/praha-escape-master-psychiatricka-lecebna-posedla",town_detail: "Praha 8 - Libeň",street_detail: "Prosecká 524/26",restaurant_name_detail: "Escape Master" };
                                    setting.markers[35] = { latitude:50.0635573,longitude:14.4070029, name: "Tajemná laboratoř",href:"https://www.exitgames.cz/praha-coderoom-tajemna-laborator",town_detail: "Praha 5",street_detail: "Nádražní 740/56",restaurant_name_detail: "CodeRoom" };
                                    setting.markers[36] = { latitude:50.084082,longitude:14.454628, name: "Sherlockova kancelář",href:"https://www.exitgames.cz/praha-exitgameprague-sherlockova-kancelar",town_detail: "Praha 3",street_detail: "Rokycanova 459/7",restaurant_name_detail: "ExitGamesPrague" };
                                    setting.markers[37] = { latitude:50.086509,longitude:14.42928, name: "Únos (venkovní mise)",href:"https://www.exitgames.cz/Unos-venkovni-mise-p48",town_detail: "Praha 1",street_detail: "Senovážná 8",restaurant_name_detail: "Puzzle Room (Senovážná)" };
                                    setting.markers[38] = { latitude:50.10886,longitude:14.43814, name: "Kryštof Kolumbus",href:"https://www.exitgames.cz/praha-run-away-kryštof-kolumbus",town_detail: "Praha 7",street_detail: "U Elektrárny 6",restaurant_name_detail: "Run Away" };
                                    setting.markers[39] = { latitude:50.06397,longitude:14.45210, name: "Márnice",href:"https://www.exitgames.cz/praha-endorfin-marnice",town_detail: "Praha 10",street_detail: "Petrohradská 216/3 ",restaurant_name_detail: "Endorfin World" };
                                    setting.markers[40] = { latitude:50.0766782,longitude:14.4331464, name: "Tajemství hlavolamu",href:"https://www.exitgames.cz/Tajemstvi-hlavolamu-p49",town_detail: "Praha 2",street_detail: "Italská 8",restaurant_name_detail: "Tajemství hlavolamu" };
                                    setting.markers[41] = { latitude:50.0819276,longitude:14.4499552, name: "ÚTĚK Z ALCATRAZU",href:"https://www.exitgames.cz/praha-exit-room-prague-utek-z-alcatrazu",town_detail: "Praha 3",street_detail: "Čajkovského 15",restaurant_name_detail: "EXIT ROOM PRAGUE - Čajkovského" };
                                    setting.markers[42] = { latitude:50.0797897,longitude:14.4331585, name: "Tajný experiment",href:"https://www.exitgames.cz/praha-trapcatch-tajny-experiment",town_detail: "Praha 2",street_detail: "Na Smetance 4",restaurant_name_detail: "TRAP CATCH - Na Smetance" };
                                    setting.markers[43] = { latitude:50.073141,longitude:14.431107, name: "Enigma",href:"https://www.exitgames.cz/Enigma-p18",town_detail: "Praha 2",street_detail: "Tyršova 9",restaurant_name_detail: "Mindmaze" };
                                    setting.markers[44] = { latitude:49.2034774,longitude:16.6050462, name: "Vojákova cela",href:"https://www.exitgames.cz/Vojakova-cela-p32",town_detail: "Brno",street_detail: "Lidická 40",restaurant_name_detail: "Unique Room" };
                                    setting.markers[45] = { latitude:50.0711777,longitude:14.456027, name: "ČERNÝ POKOJ",href:"https://www.exitgames.cz/CERNY-POKOJ-p39",town_detail: "Praha 10",street_detail: "Žitomirská 38",restaurant_name_detail: "Lostrooms - Žitomirská" };
                                    setting.markers[46] = { latitude:50.0711777,longitude:14.456027, name: "HOTEL LE MARAIS",href:"https://www.exitgames.cz/HOTEL-LE-MARAIS-p38",town_detail: "Praha 10",street_detail: "Žitomirská 38",restaurant_name_detail: "Lostrooms - Žitomirská" };
                                    setting.markers[47] = { latitude:50.073141,longitude:14.431107, name: "Alchymistova komnata (souboj 2 týmů)",href:"https://www.exitgames.cz/praha-alchymistova-komnata-souboj-2-tymu",town_detail: "Praha 2",street_detail: "Tyršova 9",restaurant_name_detail: "Mindmaze" };
                                    setting.markers[48] = { latitude:50.07623,longitude:14.45352, name: "BOMBARDOVÁNÍ PRAHY",href:"https://www.exitgames.cz/praha-exitroomprague-bombardovani-prahy",town_detail: "Praha 3",street_detail: "Slezská 98",restaurant_name_detail: "EXIT ROOM PRAGUE" };
                                    setting.markers[49] = { latitude:50.46218,longitude:13.40109, name: "Masna - Bývalí lidé",href:"https://www.exitgames.cz/chomutov-jakven-masna-byvali-lide",town_detail: "Chomutov",street_detail: "Kadaňská 3744",restaurant_name_detail: "JakVen" };
                                    setting.markers[50] = { latitude:50.07908,longitude:14.42819, name: "Pokoj",href:"https://www.exitgames.cz/praha-escape-point-pokoj",town_detail: "Praha",street_detail: "Polská 1394/20",restaurant_name_detail: "" };
                                    setting.markers[51] = { latitude:50.1120274,longitude:14.4757813, name: "Psychiatrická léčebna: Pacient č. 27 - šílenec",href:"https://www.exitgames.cz/praha-escape-master-psychiatricka-lecebna-silenec",town_detail: "Praha 8 - Libeň",street_detail: "Prosecká 524/26",restaurant_name_detail: "Escape Master" };
                                    setting.markers[52] = { latitude:50.077582,longitude:14.442593, name: "Va-bank",href:"https://www.exitgames.cz/Va-bank-p14",town_detail: "Praha 2",street_detail: "Mánesova 54",restaurant_name_detail: "Questerland" };
                                    setting.markers[53] = { latitude:50.0740716,longitude:14.4125836, name: "Experiment",href:"https://www.exitgames.cz/Experiment-p33",town_detail: "Praha 2",street_detail: "Trojanova 355/6",restaurant_name_detail: "Questroom" };
                                    setting.markers[54] = { latitude:50.0796924,longitude:14.4218038, name: "NÁVRAT DO ROKU 1989",href:"https://www.exitgames.cz/praha-fastout-navrat-do-roku-1989",town_detail: "Praha 1",street_detail: "Školská 32",restaurant_name_detail: "Fastout" };
                                    setting.markers[55] = { latitude:50.10881,longitude:14.43797, name: "Buddhova stopa",href:"https://www.exitgames.cz/praha-run-away-buddhova-stopa",town_detail: "Praha 7",street_detail: "U Elektrárny",restaurant_name_detail: "Run Away" };
                                    setting.markers[56] = { latitude:50.079648,longitude:14.4160981, name: "PORTAL",href:"https://www.exitgames.cz/PORTAL-p45",town_detail: "Praha 1",street_detail: "Opatovická 18",restaurant_name_detail: "Lostrooms - Opatovická" };
                                    setting.markers[57] = { latitude:50.076237,longitude:14.4513323, name: "Strýček v ohrožení",href:"https://www.exitgames.cz/praha-trap-catch-mafianska-pomsta",town_detail: "Praha 3",street_detail: "Malešická 2178/20",restaurant_name_detail: "TRAP CATCH" };
                                    setting.markers[58] = { latitude:50.079648,longitude:14.4160981, name: "ZA HRANICEMI VĚDY",href:"https://www.exitgames.cz/ZA-HRANICEMI-VEDY-p44",town_detail: "Praha 1",street_detail: "Opatovická 18",restaurant_name_detail: "Lostrooms - Opatovická" };
                                    setting.markers[59] = { latitude:50.100734,longitude:14.421606, name: "Golemova skrýš (souboj 2 týmů)",href:"https://www.exitgames.cz/Golemova-skrys-souboj-2-tymu-p20",town_detail: "Praha 7",street_detail: "Čechova 10",restaurant_name_detail: "Puzzle Room (Čechova)" };
                                    setting.markers[60] = { latitude:49.2267248,longitude:17.6590666, name: "Joker Poker Club",href:"https://www.exitgames.cz/zlin-joker-poker-club",town_detail: "Zlín",street_detail: "Trávník 4451",restaurant_name_detail: "Exit Room Zlín" };
                                    setting.markers[61] = { latitude:49.2267248,longitude:17.6590666, name: "Ponorka",href:"https://www.exitgames.cz/exit-room-zlin-ponorka",town_detail: "Zlín",street_detail: "Trávník 4451",restaurant_name_detail: "Exit Room Zlín" };
                                    setting.markers[62] = { latitude:50.0797897,longitude:14.4331585, name: "Magický orloj",href:"https://www.exitgames.cz/praha-trap-catch-magicky-orloj",town_detail: "Praha 2",street_detail: "Na Smetance 4",restaurant_name_detail: "TRAP CATCH - Na Smetance" };
                                    setting.markers[63] = { latitude:50.08409,longitude:14.42063, name: "Occultica",href:"https://www.exitgames.cz/occultica",town_detail: "Praha 1",street_detail: "V Kotcích 2",restaurant_name_detail: "The Room - V Kotcích" };
                                    setting.markers[64] = { latitude:50.08615,longitude:14.40433, name: "Starý svět",href:"https://www.exitgames.cz/stary-svet",town_detail: "Praha 1 ",street_detail: "Karmelitská 16",restaurant_name_detail: "The Room - Karmelitská" };
                                    setting.markers[65] = { latitude:50.03958,longitude:14.41027, name: "Červená místnost",href:"https://www.exitgames.cz/praha-decrypt-cervena-mistnost",town_detail: "Praha 4",street_detail: "Branická 16",restaurant_name_detail: "DeCrypt" };
                                    setting.markers[66] = { latitude:50.100734,longitude:14.421606, name: "Stroj času",href:"https://www.exitgames.cz/praha-stroj-casu",town_detail: "Praha 7",street_detail: "Čechova 10",restaurant_name_detail: "Puzzle Room (Čechova)" };
                                    setting.markers[67] = { latitude:50.073141,longitude:14.431107, name: "Alchymistova komnata",href:"https://www.exitgames.cz/praha-mindmaze-alchymistova-komnata",town_detail: "Praha 2",street_detail: "Tyršova 9",restaurant_name_detail: "Mindmaze" };
                                    setting.markers[68] = { latitude:50.06397,longitude:14.45210, name: "Star Wars",href:"https://www.exitgames.cz/endorfin-star-wars",town_detail: "Praha 10",street_detail: "Petrohradská 216/3 ",restaurant_name_detail: "Endorfin World" };
                                    setting.markers[69] = { latitude:50.09478,longitude:14.45441, name: "Virus X",href:"https://www.exitgames.cz/escape-mystery-virus-x",town_detail: "Praha 8",street_detail: "Pobřežní 95/74",restaurant_name_detail: "Escape Mystery" };
                                    setting.markers[70] = { latitude:50.07424,longitude:14.44601, name: "Mozkomorovo Vězení",href:"https://www.exitgames.cz/mozkomorovo-vezeni",town_detail: "Praha 2",street_detail: "Chodská 16",restaurant_name_detail: "The Room - IMAGINATORIUM" };
                                    setting.markers[71] = { latitude:50.07424,longitude:14.44601, name: "Čarodějův Zámek",href:"https://www.exitgames.cz/carodejuv-zamek",town_detail: "Praha 2",street_detail: "Chodská 16",restaurant_name_detail: "The Room - IMAGINATORIUM" };
                                    setting.markers[72] = { latitude:50.0711777,longitude:14.456027, name: "Útěk z vězení",href:"https://www.exitgames.cz/praha-lostrooms-utek",town_detail: "Praha 10",street_detail: "Žitomirská 38",restaurant_name_detail: "Lostrooms - Žitomirská" };
                                    setting.markers[73] = { latitude:50.0711777,longitude:14.456027, name: "VELKÝ TŘESK",href:"https://www.exitgames.cz/praha-lostrooms-velky-tresk",town_detail: "Praha 10",street_detail: "Žitomirská 38",restaurant_name_detail: "Lostrooms - Žitomirská" };
                                    setting.markers[74] = { latitude:50.07424,longitude:14.44601, name: "Dračí Labyrint",href:"https://www.exitgames.cz/draci-labyrint",town_detail: "Praha 2",street_detail: "Chodská 16",restaurant_name_detail: "The Room - IMAGINATORIUM" };
                                    setting.markers[75] = { latitude:50.07863,longitude:14.44158, name: "Novinář",href:"https://www.exitgames.cz/praha-escape-point-novinar",town_detail: "Praha 2",street_detail: "Polská 1394/20",restaurant_name_detail: "" };
                                    setting.markers[76] = { latitude:50.12477,longitude:14.44965, name: "Bunkr",href:"https://www.exitgames.cz/praha-escape-point-bunkr",town_detail: "Praha 8",street_detail: " Čimická 6",restaurant_name_detail: "" };
                                    setting.markers[77] = { latitude:50.0752272,longitude:14.4153293, name: "Únos - zachraňte Elišku (venkovní mise)",href:"https://www.exitgames.cz/praha-unos-zachrante-elisku",town_detail: "Praha 2",street_detail: "Václavská 2073/20",restaurant_name_detail: "Kryptograf" };
                                    setting.markers[78] = { latitude:50.0752272,longitude:14.4153293, name: "Hra o pražské trůny (venkovní mise)",href:"https://www.exitgames.cz/praha-kryptograf-hra-o-prazske-truny",town_detail: "Praha 2",street_detail: "Václavská 2073/20",restaurant_name_detail: "Kryptograf" };
                                    setting.markers[79] = { latitude:50.0752272,longitude:14.4153293, name: "Kryptovirus - zachraňte svět (venkovní mise)",href:"https://www.exitgames.cz/praha-kryptograf-kryptovirus-zachrante-svet",town_detail: "Praha 2",street_detail: "Václavská 2073/20",restaurant_name_detail: "Kryptograf" };
                                    setting.markers[80] = { latitude:50.08766,longitude:14.42107, name: "Tour de pub",href:"https://www.exitgames.cz/praha-getoutfun-tour-de-pub",town_detail: "Praha 2",street_detail: "Náměstí Míru",restaurant_name_detail: "Get Out Fun" };
                                    setting.markers[81] = { latitude:50.09847,longitude:14.42510, name: "Technické muzeum",href:"https://www.exitgames.cz/praha-getoutfun-technicke-muzeum",town_detail: "Praha",street_detail: "Kostelní 1320/42,",restaurant_name_detail: "Get Out Fun" };
                                    setting.markers[82] = { latitude:50.08769,longitude:14.42100, name: "V zakletí času",href:"https://www.exitgames.cz/praha-getoutfun-v-zakleti-casu",town_detail: "Praha",street_detail: "Staroměstské náměstí",restaurant_name_detail: "Get Out Fun" };
                                    setting.markers[83] = { latitude:49.30141,longitude:16.65257, name: "Detektivní hra v Nitru",href:"https://www.exitgames.cz/brno-nitro-adamov-detektivni-hra-v-nitru",town_detail: "Adamov",street_detail: "Mírová 493",restaurant_name_detail: "Nitro" };
                                    setting.markers[84] = { latitude:48.8110955,longitude:14.3118137, name: "Čaroděj",href:"https://www.exitgames.cz/cesky-krumov-escape",town_detail: "Český Krumlov",street_detail: "Soukenická 40",restaurant_name_detail: "Krumlov Escape Game" };
                                    setting.markers[85] = { latitude:49.19094,longitude:16.61056, name: "Útěky.cz",href:"https://www.exitgames.cz/brno-uteky.cz",town_detail: "Brno",street_detail: "Bašty 4",restaurant_name_detail: "Útěky.cz" };
                                    setting.markers[86] = { latitude:49.2034774,longitude:16.6050462, name: "Záhada vinařství",href:"https://www.exitgames.cz/brno-unique-room-zahada-vinarstvi",town_detail: "Brno",street_detail: "Lidická 40",restaurant_name_detail: "Unique Room" };
                                    setting.markers[87] = { latitude:50.08090,longitude:14.48939, name: "Operace kasárna",href:"https://www.exitgames.cz/praha-esgame-operace-kasarna",town_detail: "Praha - Strašnice",street_detail: "Česká Námořní Plavba, Počernická 1a",restaurant_name_detail: "" };
                                    setting.markers[88] = { latitude:48.8110955,longitude:14.3118137, name: "Tortura",href:"https://www.exitgames.cz/cesky-krumlov-krumlov-escape-game-tortura",town_detail: "Český Krumlov",street_detail: "Soukenická 40",restaurant_name_detail: "Krumlov Escape Game" };
                                    setting.markers[89] = { latitude:50.07462,longitude:14.41567, name: "Alenka v říši divů",href:"https://www.exitgames.cz/alenka-v-risi-divu",town_detail: "Praha 2",street_detail: "Trojanova 355/6",restaurant_name_detail: "Questroom" };
                                    setting.markers[90] = { latitude:50.06397,longitude:14.45210, name: "Freddy Krueger",href:"https://www.exitgames.cz/endofin-freddy-krueger",town_detail: "Praha 10",street_detail: "Petrohradská 216/3 ",restaurant_name_detail: "Endorfin World" };
                    });

        function getProducts(clear) {
            /*var page = parseInt($('#page').val());*/
            var page = ($('.product-list .product').length / 12) + 1;

            $.ajax({
                url: 'index.php?route=product/category&ajax=1&page=' + page + '&' + $('#filter').serialize(),
                dataType: 'json',
                async: false,
                success: function (json) {
                    $('#page').val(page + 1);
                    if (clear) {
                        $('.product-list').html();
                    }
                    var num = $('.product-list .product').length;
                    $('.product-list').append(json.html);
                    slideTo($('.product-list .product').eq(num+1));

                    if (json.next_button == "0") {
                        $("#next_products").addClass('hidden');
                    } else {
                        $("#next_products").removeClass('hidden');
                    }
                }
            });
        }
        //-></script>
</div><ul class="ui-autocomplete ui-front ui-menu ui-widget ui-widget-content" id="ui-id-1" tabindex="0" style="display: none;"></ul><span role="status" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></span><div class="ui-selectmenu-menu ui-front"><ul aria-hidden="true" aria-labelledby="ui-id-2-button" id="ui-id-2-menu" class="ui-menu ui-widget ui-widget-content ui-corner-bottom ui-styled" role="listbox" tabindex="0"></ul></div><div class="ui-selectmenu-menu ui-front"><ul aria-hidden="true" aria-labelledby="ui-id-3-button" id="ui-id-3-menu" class="ui-menu ui-widget ui-widget-content ui-corner-bottom" role="listbox" tabindex="0"></ul></div><div class="ui-selectmenu-menu ui-front"><ul aria-hidden="true" aria-labelledby="ui-id-4-button" id="ui-id-4-menu" class="ui-menu ui-widget ui-widget-content ui-corner-bottom" role="listbox" tabindex="0"></ul></div><div class="ui-selectmenu-menu ui-front"><ul aria-hidden="true" aria-labelledby="ui-id-5-button" id="ui-id-5-menu" class="ui-menu ui-widget ui-widget-content ui-corner-bottom" role="listbox" tabindex="0"></ul></div><div class="ui-selectmenu-menu ui-front"><ul aria-hidden="true" aria-labelledby="ui-id-6-button" id="ui-id-6-menu" class="ui-menu ui-widget ui-widget-content ui-corner-bottom" role="listbox" tabindex="0"></ul></div><div class="ui-selectmenu-menu ui-front"><ul aria-hidden="true" aria-labelledby="ui-id-7-button" id="ui-id-7-menu" class="ui-menu ui-widget ui-widget-content ui-corner-bottom" role="listbox" tabindex="0"></ul></div><div class="ui-selectmenu-menu ui-front"><ul aria-hidden="true" aria-labelledby="ui-id-8-button" id="ui-id-8-menu" class="ui-menu ui-widget ui-widget-content ui-corner-bottom" role="listbox" tabindex="0"></ul></div></body></html>"""
    return BeautifulSoup(content, 'html.parser')
