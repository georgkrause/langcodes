# This is the list of language codes with the 'modern' level of support in CLDR
# (compared to 'full', which contains many more languages). We use this as the
# list of languages that we store specific name-to-code mappings for.

CLDR_LANGUAGES = {
    'af',
    'am',
    'ar',
    'az',
    'be',
    'bg',
    'bn',
    'bs',
    'ca',
    'cs',
    'cy',
    'da',
    'de',
    'el',
    'en',
    'es',
    'et',
    'eu',
    'fa',
    'fi',
    'fil',
    'fo',
    'fr',
    'ga',
    'gl',
    'gu',
    'he',
    'hi',
    'hr',
    'hu',
    'hy',
    'id',
    'is',
    'it',
    'ja',
    'ka',
    'kk',
    'km',
    'kn',
    'ko',
    'ky',
    'lo',
    'lt',
    'lv',
    'mk',
    'ml',
    'mn',
    'mr',
    'ms',
    'my',
    'nb',
    'ne',
    'nl',
    'pa',
    'pl',
    'pt',
    'ro',
    'ru',
    'si',
    'sk',
    'sl',
    'sq',
    'sr',
    'sv',
    'sw',
    'ta',
    'te',
    'th',
    'ti',
    'to',
    'tr',
    'uk',
    'und',
    'ur',
    'uz',
    'vi',
    'yue',
    'zh',
    'zu',
}


# These are the names languages that have the most entries on the English and
# German Wiktionaries. Wiktionary only consistently identifies languages by their
# name, making it important to be able to recognize the names.
#
# These lists of names are used in `tests/test_wikt_languages.py`.
WIKT_LANGUAGE_NAMES = {}

WIKT_LANGUAGE_NAMES['en'] = [
    "Spanish",
    "French",
    "Latvian",
    "Latin",
    "English",
    "Mandarin",
    "Italian",
    "Portuguese",
    "Cantonese",
    "Japanese",
    "German",
    "Swedish",
    "Korean",
    "Serbo-Croatian",
    "Serbian",
    "Croatian",
    "Bosnian",
    "Finnish",
    "Vietnamese",
    "Dutch",
    "Galician",
    "Catalan",
    "Polish",
    "Danish",
    "Norwegian Nynorsk",
    "Turkish",
    "Romanian",
    "Lithuanian",
    "Ido",
    "Old French",
    "Czech",
    "Norwegian",
    # Jèrriais -- same as Norman
    "Esperanto",
    "Icelandic",
    # Old Armenian
    "Norwegian Bokmål",
    "Asturian",
    "Hungarian",
    "Proto-Germanic",
    "Russian",
    "Slovene",
    "Min Nan",
    "Scottish Gaelic",
    "Greek",
    "Irish",
    "Lojban",
    "Middle French",
    "Malay",
    "Luxembourgish",
    "Slovak",
    "Estonian",
    "Persian",
    "Venetian",
    "Old English",
    "Volapük",
    "Ladin",
    "Faroese",
    "Scots",
    "Interlingua",
    "Romansch",
    "Urdu",
    # Middle Chinese
    "Indonesian",
    "Swahili",
    "Middle English",
    "Occitan",
    "Welsh",
    "Old Norse",
    "Albanian",
    "Old Irish",
    "Old Saxon",
    "Lower Sorbian",
    "Afrikaans",
    "Ukrainian",
    "Proto-Slavic",
    "Ancient Greek",
    "Gothic",
    "Hawaiian",
    "Kurdish",
    "Tagalog",
    "Old High German",
    "Crimean Tatar",
    "Manx",
    "Sanskrit",
    "Hiligaynon",
    "West Frisian",
    "Hebrew",
    "Tok Pisin",
    "Proto-Indo-European",
    "Macedonian",
    "Novial",
    "Armenian",
    "Arabic",
    "Maltese",
    "Hakka",
    "Sicilian",
    # "Ladino", -- same as Ladin
    "Basque",
    "Breton",
    # Guernésiais -- same as Norman
    "Vai",
    "Navajo",
    "Azeri",
    "Vilamovian",
    # Tarantino
    "Maori",
    "Friulian",
    "Hausa",
    "Haitian Creole",
    "Yiddish",
    "Tatar",
    "Proto-Malayo-Polynesian",
    "Aromanian",
    "Ottoman Turkish",
    "Old Provençal",
    "Northern Sami",
    "Dalmatian",
    "Bulgarian",
    "Neapolitan",
    "Cornish",
    "Middle Dutch",
    "Rapa Nui",
    # Old Portuguese
    "Egyptian Arabic",
    "Romani",
    "Tahitian",
    "Thai",
    "Limburgish",
    "Karelian",
    "Tajik",
    "Turkmen",
    "Kabardian",
    "Uzbek",
    "Samoan",
    "Mongolian",
    "Zulu",
    "Upper Sorbian",
    "Walloon",
    # Proto-Finnic
    "Frankish",
    "Mapudungun",
    "Pashto",
    "Low German",
    "Bashkir",
    "Kashubian",
    "Sranan Tongo",
    "Proto-Sino-Tibetan",
    "Norman",
    "Proto-Austronesian",
    "Marathi",
    "Rohingya",
    "Classical Nahuatl",
    # Proto-Malayic
    # German Low German
    "Fijian",
    "Zazaki",
    "Proto-Italic",
    "Old Dutch",
    "Egyptian",
    "Old Frisian",
    "Greenlandic",
    "Burmese",
    "Votic",
    "Ewe",
    "Cherokee",
    "Old Church Slavonic",
    "Quechua",
    "Mirandese",
    "Livonian",
    "Bengali",
    "Skolt Sami",
    # Proto-Balto-Slavic
    "Pitjantjatjara",
    "Georgian",
    "North Frisian",
    "Tetum",
    "Tongan",
    # Mauritian Creole
    "Torres Strait Creole",
    "Papiamentu",
    "Lao",
    "Malagasy",
    "Interlingue",
    "Aragonese",
    "Istriot",
    "Sumerian",
    "Proto-Celtic",
    "Võro",
    # Proto-Polynesian
    "Nepali",
    "Chickasaw",
    "Akkadian",
    "Middle Armenian",
    "Cimbrian",
    "Somali",
    "Sardinian",
    "Tocharian B",
    "Telugu",
    "Javanese",
    "Taos",
    "Proto-Semitic",
    # Old Prussian
    "Kyrgyz",
    "Corsican",
    "Veps",
    "Baluchi",
    "Middle Low German",
    "Middle High German",
    "Uyghur",
    # Dutch Low Saxon
    "Belarusian",
    "Guaraní",
    "Undetermined",
    "Inuktitut",
    "Tocharian A",
    "Nigerian Pidgin",
    # Gallo
    # Saterland Frisian
    "Punjabi",
    "Proto-Algonquian",
    # Istro-Romanian
    "Wiradhuri",
    "Sichuan Yi",
    "Wu",
    # White Hmong
    "Ugaritic",
    "Sundanese",
    # Old East Slavic
    # Fala
    # Elfdalian
    "Tamil",
    "Pijin",
    "Okinawan",
    "Kazakh",
    "Hindi",
    "Tuvan",
    "Polabian",
    "Aramaic",
    "Malayalam",
    "Kumyk",
    "Inari Sami",
    "Ilocano",
    "Tswana",
    "Libyan Arabic",
    "Latgalian",
    "Yakut",
    "Sindhi",
    "Khmer",
    "Gamilaraay",
    "Ojibwe",
    "Choctaw",
    "Chinese",
    "Chamorro",
    "Yucatec Maya",
    "Picard",
    "Ngarrindjeri",
    "Kott",
    "Ingrian",
    # Crimean Gothic
    "Chamicuro",
    "Rajasthani",
    # Old Tupi
    "Old Spanish",
    "Gagauz",
    "Extremaduran",
    "Chinook Jargon",
    "Cahuilla",
    "Kannada",
    "Iban",
    "American Sign Language",
    "Adyghe",
    "Warlpiri",
    "Tibetan",
    "Ossetian",
    "Meriam",
    "Marshallese",
    "Khakas",
    "Balinese",
    "Zhuang",
    "Tuvaluan",
    "Niuean",
    "Martuthunira",
    "Guugu Yimidhirr",
    "Chechen",
    "Campidanese Sardinian",
    "Tolai",
    # Old Javanese
    "Nahuatl",
    "Lombard",
    "West Coast Bajau",
    "Romagnol",
    "Middle Irish",
    "Yoruba",
    "Wangaaybuwan-Ngiyambaa",
    # Old Swedish
    "Lingala",
    "Fiji Hindi",
    "Shabo",
    "Sasak",
    "Judeo-Arabic",
    "Central Kurdish",
    "Bislama",
]

WIKT_LANGUAGE_NAMES['de'] = [
    "Deutsch",
    "Englisch",
    "Polnisch",
    "Italienisch",
    "Französisch",
    "Esperanto",
    "Schwedisch",
    "Lateinisch",
    "Tschechisch",
    "Katalanisch",
    "Spanisch",
    "Okzitanisch",
    "Ungarisch",
    "Litauisch",
    "Finnisch",
    "Russisch",
    "Altgriechisch",
    "Niederländisch",
    "Kurdisch",
    "Baskisch",
    "Armenisch",
    "Isländisch",
    "Bulgarisch",
    "Färöisch",
    "Dänisch",
    "Portugiesisch",
    "Slowakisch",
    "Türkisch",
    "Maori",
    "Albanisch",
    "Japanisch",
    "Norwegisch",
    "Irisch",
    "Koreanisch",
    "Chinesisch",
    "Venezianisch",
    "Friaulisch",
    "Serbisch",
    "Indonesisch",
    "Walisisch",
    "Arabisch",
    "Zentral-Nahuatl",
    "Neugriechisch",
    "Sumerisch",
    "Obersorbisch",
    "Sesotho",
    "Rumänisch",
    "Suaheli",
    "Persisch",
    "Krimtatarisch",
    "Plattdeutsch",
    "Prußisch",
    "Thai",
    "Bosnisch",
    "Sardisch",
    "Maltesisch",
    "Akkadisch",
    "Hawaiianisch",
    "Hebräisch",
    "Gotisch",
    "Afrikaans",
    "Rätoromanisch",
    "Tamil",
    "Bretonisch",
    "Ukrainisch",
    "Hindi",
    "Georgisch",
    "Panjabi",
    "Papiamentu",
    "Slowenisch",
    "Nauruisch",
    "Schottisch-Gälisch",
    "Balinesisch",
    "Estnisch",
    "Manx",
    "Korsisch",
    # "Frühneuhochdeutsch",
    "Lettisch",
    "isiZulu",
    "Tagalog",
    "Tok Pisin",
    # "Südpikenisch",
    "Kroatisch",
    "Niedersorbisch",
    "Kannada",
    "Guanche",
    "Belarussisch",
    "Sanskrit",
    "Aserbaidschanisch",
    "Mittelhochdeutsch",
    "Laotisch",
    "Altnordisch",
    "Altenglisch",
    "Vietnamesisch",
    "Tadschikisch",
    "Samoanisch",
    "Mazedonisch",
    "Luxemburgisch",
    "Hethitisch",
    # "Yukatekisch",
    "Kaschubisch",
    "Wallonisch",
    # "Klassisches Nahuatl",
    "Telugu",
    "Rapanui",
    "Jiddisch",
    "Ido",
    # "Galicisch",
    "Volapük",
    "Bengalisch",
    "Mapudungun",
    "Lojban",
    "Tuvaluisch",
    "Gujarati",
    "Assamesisch",
]
