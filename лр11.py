pip install pytelegrambotapi

countries = [
  ['AFGHANISTAN','KABUL'],
  ['ALBANIA','TIRANA'],
  ['ALGERIA','ALGIERS'],
  ['ANDORRA','ANDORRA LA VELLA'],
  ['ANGOLA','LUANDA'],
  ['ANTIGUA & BARBUDA','SAINT JOHN\'S'],
  ['ARGENTINA','BUENOS AIRES'],
  ['ARMENIA','YEREVAN'],
  ['AUSTRALIA','CANBERRA'],
  ['AUSTRIA','VIENNA'],
  ['AZERBAIJAN','BAKU'],
  ['BAHAMAS, THE','NASSAU'],
  ['BAHRAIN','MANAMA'],
  ['BANGLADESH','DHAKA'],
  ['BARBADOS','BRIDGETOWN'],
  ['BELARUS','MINSK'],
  ['BELGIUM','BRUSSELS'],
  ['BELIZE','BELMOPAN'],
  ['BENIN','PORTO-NOVO'],
  ['BHUTAN','THIMPHU'],
  ['BOLIVIA','SUCRE'],
  ['BOSNIA & HERZEGOVINA','SARAJEVO'],
  ['BOTSWANA','GABORONE'],
  ['BRAZIL','BRASILIA'],
  ['BRUNEI','BANDAR SERI BEGAWAN'],
  ['BULGARIA','SOFIA'],
  ['BURKINA FASO','OUAGADOUGOU'],
  ['BURUNDI','BUJUMBURA'],
  ['CABO VERDE','PRAIA'],
  ['CAMBODIA','PHNOM PENH'],
  ['CAMEROON','YAOUNDE'],
  ['CANADA','OTTAWA'],
  ['CENTRAL AFRICAN REPUBLIC','BANGUI'],
  ['CHAD','N\'DJAMENA'],
  ['CHILE','SANTIAGO'],
  ['CHINA','BEIJING'],
  ['COLOMBIA','BOGOTÁ'],
  ['COMOROS','MORONI'],
  ['CONGO, DEMOCRATIC REPUBLIC OF THE','KINSHASA'],
  ['COSTA RICA','SAN JOSE'],
  ['CÔTE D\'IVOIRE','YAMOUSSOUKRO'],
  ['CROATIA','ZAGREB'],
  ['CUBA','HAVANA'],
  ['CYPRUS','NICOSIA'],
  ['CZECH REPUBLIC','PRAGUE'],
  ['DENMARK','COPENHAGEN'],
  ['DJIBOUTI','DJIBOUTI (CITY)'],
  ['DOMINICA','ROSEAU'],
  ['DOMINICAN REPUBLIC','SANTO DOMINGO'],
  ['ECUADOR','QUITO'],
  ['EGYPT','CAIRO'],
  ['EL SALVADOR','SAN SALVADOR'],
  ['EQUATORIAL GUINEA','MALABO'],
  ['ERITREA','ASMARA'],
  ['ESTONIA','TALLINN'],
  ['ESWATINI','MBABANE'],
  ['ETHIOPIA','ADDIS ABABA'],
  ['FEDERATED STATES OF MICRONESIA','PALIKIR'],
  ['FIJI','SUVA'],
  ['FINLAND','HELSINKI'],
  ['FRANCE','PARIS'],
  ['GABON','LIBREVILLE'],
  ['GAMBIA, THE','BANJUL'],
  ['GEORGIA','TBILISI'],
  ['GERMANY','BERLIN'],
  ['GHANA','ACCRA'],
  ['GREECE','ATHENS'],
  ['GRENADA','SAINT GEORGE\'S'],
  ['GUATEMALA','GUATEMALA CITY'],
  ['GUINEA','CONAKRY'],
  ['GUINEA-BISSAU','BISSAU'],
  ['GUYANA','GEORGETOWN'],
  ['HAITI','PORT-AU-PRINCE'],
  ['HONDURAS','TEGUCIGALPA'],
  ['HUNGARY','BUDAPEST'],
  ['ICELAND','REYKJAVIK'],
  ['INDIA','NEW DELHI'],
  ['INDONESIA','JAKARTA'],
  ['IRAN','TEHRAN'],
  ['IRAQ','BAGHDAD'],
  ['IRELAND','DUBLIN'],
  ['ISRAEL','JERUSALEM'],
  ['ITALY','ROME'],
  ['JAMAICA','KINGSTON'],
  ['JAPAN','TOKYO'],
  ['JORDAN','AMMAN'],
  ['KAZAKHSTAN','NUR-SULTAN'],
  ['KENYA','NAIROBI'],
  ['KIRIBATI','SOUTH TARAWA'],
  ['KOSOVO','PRISTINA'],
  ['KUWAIT','KUWAIT CITY'],
  ['KYRGYZSTAN','BISHKEK'],
  ['LAOS','VIENTIANE'],
  ['LATVIA','RIGA'],
  ['LEBANON','BEIRUT'],
  ['LESOTHO','MASERU'],
  ['LIBERIA','MONROVIA'],
  ['LIBYA','TRIPOLI'],
  ['LIECHTENSTEIN','VADUZ'],
  ['LITHUANIA','VILNIUS'],
  ['LUXEMBOURG','LUXEMBOURG'],
  ['MADAGASCAR','ANTANANARIVO'],
  ['MALAWI','LILONGWE'],
  ['MALAYSIA','KUALA LUMPUR'],
  ['MALDIVES','MALE'],
  ['MALI','BAMAKO'],
  ['MALTA','VALLETTA'],
  ['MARSHALL ISLANDS','MAJURO'],
  ['MAURITANIA','NOUAKCHOTT'],
  ['MAURITIUS','PORT LOUIS'],
  ['MEXICO','MEXICO CITY'],
  ['MOLDOVA','CHISINAU'],
  ['MONACO','MONACO'],
  ['MONGOLIA','ULAANBAATAR'],
  ['MONTENEGRO','PODGORICA'],
  ['MOROCCO','RABAT'],
  ['MOZAMBIQUE','MAPUTO'],
  ['MYANMAR','NAY PYI TAW'],
  ['NAMIBIA','WINDHOEK'],
  ['NAURU','YAREN DISTRICT'],
  ['NEPAL','KATHMANDU'],
  ['NETHERLANDS','AMSTERDAM'],
  ['NEW ZEALAND','WELLINGTON'],
  ['NICARAGUA','MANAGUA'],
  ['NIGER','NIAMEY'],
  ['NIGERIA','ABUJA'],
  ['NORTH KOREA','PYONGYANG'],
  ['NORTH MACEDONIA','SKOPJE'],
  ['NORWAY','OSLO'],
  ['OMAN','MUSCAT'],
  ['PAKISTAN','ISLAMABAD'],
  ['PALAU','NGERULMUD'],
  ['PALESTINE','EAST JERUSALEM'],
  ['PANAMA','PANAMA CITY'],
  ['PAPUA NEW GUINEA','PORT MORESBY'],
  ['PARAGUAY','ASUNCIÓN'],
  ['PERU','LIMA'],
  ['PHILIPPINES','MANILA'],
  ['POLAND','WARSAW'],
  ['PORTUGAL','LISBON'],
  ['QATAR','DOHA'],
  ['REPUBLIC OF THE CONGO','BRAZZAVILLE'],
  ['ROMANIA','BUCHAREST'],
  ['RUSSIA','MOSCOW'],
  ['RWANDA','KIGALI'],
  ['SAINT KITTS & NEVIS','BASSETERRE'],
  ['SAINT LUCIA','CASTRIES'],
  ['SAINT VINCENT & THE GRENADINES','KINGSTOWN'],
  ['SAMOA','APIA'],
  ['SAN MARINO','SAN MARINO'],
  ['SÃO TOMÉ & PRÍNCIPE','SÃO TOMÉ'],
  ['SAUDI ARABIA','RIYADH'],
  ['SENEGAL','DAKAR'],
  ['SERBIA','BELGRADE'],
  ['SEYCHELLES','VICTORIA'],
  ['SIERRA LEONE','FREETOWN'],
  ['SINGAPORE','SINGAPORE'],
  ['SLOVAKIA','BRATISLAVA'],
  ['SLOVENIA','LJUBLJANA'],
  ['SOLOMON ISLANDS','HONIARA'],
  ['SOMALIA','MOGADISHU'],
  ['SOUTH AFRICA','BLOEMFONTEIN, CAPE TOWN, PRETORIA'],
  ['SOUTH KOREA','SEOUL'],
  ['SOUTH SUDAN','JUBA'],
  ['SPAIN','MADRID'],
  ['SRI LANKA','COLOMBO, SRI JAYAWARDENEPURA KOTTE'],
  ['SUDAN','KHARTOUM'],
  ['SURINAME','PARAMARIBO'],
  ['SWEDEN','STOCKHOLM'],
  ['SWITZERLAND','BERN'],
  ['SYRIA','DAMASCUS'],
  ['TAJIKISTAN','DUSHANBE'],
  ['TANZANIA DODOMA'],
  ['THAILAND','BANGKOK'],
  ['TIMOR-LESTE','DILI'],
  ['TOGO','LOMÉ'],
  ['TONGA','NUKUʻALOFA'],
  ['TRINIDAD & TOBAGO','PORT OF SPAIN'],
  ['TUNISIA','TUNIS'],
  ['TURKEY','ANKARA'],
  ['TURKMENISTAN','ASHGABAT'],
  ['TUVALU','FUNAFUTI'],
  ['UGANDA','KAMPALA'],
  ['UKRAINE','KIEV'],
  ['UNITED ARAB EMIRATES','ABU DHABI'],
  ['UNITED KINGDOM*','LONDON'],
  ['UNITED STATES','WASHINGTON, D.C.'],
  ['URUGUAY','MONTEVIDEO'],
  ['UZBEKISTAN','TASHKENT'],
  ['VANUATU','PORT VILA'],
  ['VATICAN CITY','VATICAN CITY'],
  ['VENEZUELA','CARACAS'],
  ['VIETNAM','HANOI'],
  ['YEMEN','SANA\'A'],
  ['ZAMBIA','LUSAKA'],
  ['ZIMBABWE','HARARE']
]

import telebot
import random
bot = telebot.TeleBot("1138006818:AAEqGOJQfmwR2ut9edPrX4fYJVSda53AQeo")
usergames = dict()
answers = dict()
start_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
start_keyboard.row("Грати","Відповідь","Стоп")
@bot.callback_query_handler(func=lambda query: query.data)
def process_callback(query):
  if query.message.chat.id in usergames:
      if usergames[query.message.chat.id][1] == query.data:
        bot.send_message(query.message.chat.id,"Вірно! Так тримати!",reply_markup=start_keyboard)  
        start_game(query.message)
      else:
        bot.send_message(query.message.chat.id,"Ні( Спробуй ще!",reply_markup=start_keyboard) 
  else:
      bot.send_message(query.message.chat.id,"Ти вже не граєш!",reply_markup=start_keyboard) 
@bot.message_handler(commands=['start'])
def handle_start_command(message):
  bot.send_message(message.chat.id, "Вітаю, " + message.chat.first_name + ". Ти зареєструвався в грі \"Вгадай столицю\". Натисни \"Грати\".",reply_markup=start_keyboard)
@bot.message_handler(content_types=['text'])
def handle_text(message):
  if message.text.lower() == 'грати':
    if message.chat.id in usergames:
      bot.send_message(message.chat.id,"Ти вже граєш!",reply_markup=start_keyboard) 
    else:
      start_game(message)
      bot.send_message(message.chat.id,"Чекаємо на твою відповідь!",reply_markup=start_keyboard)  
  elif message.text.lower() == 'відповідь':
    if message.chat.id in usergames:
      bot.send_message(message.chat.id,"Правильна відповід = \""+usergames[message.chat.id][1]+"\"",reply_markup=start_keyboard)  
      bot.send_message(message.chat.id,"Продовжуємо!",reply_markup=start_keyboard)  
      start_game(message)
    else:
      bot.send_message(message.chat.id,"Ти ще не граєш!",reply_markup=start_keyboard) 
  elif message.text.lower() == 'стоп':
    if message.chat.id in usergames:
      usergames.pop(message.chat.id, None)
      answers.pop(message.chat.id, None)
      bot.send_message(message.chat.id,"Гру зупинено!",reply_markup=start_keyboard) 
    else:
      bot.send_message(message.chat.id,"Ти ще не граєш!",reply_markup=start_keyboard) 
  else:
    bot.send_message(message.chat.id, "Вибач, я тебе не розумію!",reply_markup=start_keyboard)
def start_game(message):
  usergames[message.chat.id] = random.choice(countries)
  answers[message.chat.id] = [
    usergames[message.chat.id][1],
    random.choice(countries)[1],
    random.choice(countries)[1],
    random.choice(countries)[1]        
  ]
  random.shuffle(answers[message.chat.id])
  keyboard = telebot.types.InlineKeyboardMarkup()
  for country in answers[message.chat.id]:
    keyboard.add(telebot.types.InlineKeyboardButton(text=country,callback_data=country))
  bot.send_message(message.chat.id, "Яка столиця \""+usergames[message.chat.id][0]+"\"?", reply_markup=keyboard)
bot.polling()

