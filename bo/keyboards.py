
import re
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def genmarkup(ot):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for i in ot:
        markup.add(InlineKeyboardButton(f'{i[0]}. Оценка: {i[3]}/5', callback_data=f'ot_{i[0]}'))
    return markup



menu = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='История заказов', callback_data='history_offers')
btn2 = InlineKeyboardButton(text='Пополнить баланс', callback_data='+balance')
btn3 = InlineKeyboardButton(text='Заработать', callback_data='earn')
btn4 = InlineKeyboardButton(text='Активировать купон', callback_data='activate_cupon')
menu.row(btn1)
menu.row(btn2)
menu.row(btn3)
menu.row(btn4)


location = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='Москва', callback_data='moscow')
btn2 = InlineKeyboardButton(text='Челябинск', callback_data='chelyaba')
btn3 = InlineKeyboardButton(text='Ростов-на-Дону', callback_data='rostov')
btn4 = InlineKeyboardButton(text='Ярославль', callback_data='yaroslavl')
btn5 = InlineKeyboardButton(text='Екатеринбург', callback_data='ekb')
btn6 = InlineKeyboardButton(text='Санкт-Петербург', callback_data='spb')
btn7 = InlineKeyboardButton(text='Новосибирск', callback_data='novosibirsk')
btn8 = InlineKeyboardButton(text='Тула', callback_data='tula')
btn9 = InlineKeyboardButton(text='Краснодарский край', callback_data='krasnodarskiy')
#btn10 = InlineKeyboardButton(text='Москвская область', callback_data='moscow_oblast')
btn11 = InlineKeyboardButton(text='Самара', callback_data='samara')
btn12 = InlineKeyboardButton(text='Воронеж', callback_data='voronej')
btn13 = InlineKeyboardButton(text='Иваново', callback_data='ivanovo')
btn14 = InlineKeyboardButton(text='Красноярск', callback_data='krasnoyarsk')
btn15 = InlineKeyboardButton(text='Саратов', callback_data='saratov')
btn16 = InlineKeyboardButton(text='Краснодар', callback_data='krasnodar')
btn17 = InlineKeyboardButton(text='Омск', callback_data='omsk')
btn18 = InlineKeyboardButton(text='Нижний Новгород', callback_data='novgorod')
btn19 = InlineKeyboardButton(text='Владимир', callback_data='vladimir')
btn20 = InlineKeyboardButton(text='Вологда', callback_data='vologda')
btn21 = InlineKeyboardButton(text='Тверь', callback_data='tver')
btn22 = InlineKeyboardButton(text='Рязань', callback_data='ryazan')
btn23 = InlineKeyboardButton(text='Волгоград', callback_data='volgograd')
btn24 = InlineKeyboardButton(text='Кострома', callback_data='kostroma')
btn25 = InlineKeyboardButton(text='Волжский', callback_data='voljskiy')
btn26 = InlineKeyboardButton(text='Краснотуринск', callback_data='krasnoturinsk')
btn27 = InlineKeyboardButton(text='Оренбург', callback_data='orenburg')
location.row(btn1)
location.row(btn2)
location.row(btn3)
location.row(btn4)
location.row(btn5)
location.row(btn6)
location.row(btn7)
location.row(btn8)
location.row(btn9)
#location.row(btn10)
location.row(btn11)
location.row(btn12)
location.row(btn13)
location.row(btn14)
location.row(btn15)
location.row(btn16)
location.row(btn17)
location.row(btn18)
location.row(btn19)
location.row(btn20)
location.row(btn21)
location.row(btn22)
location.row(btn23)
location.row(btn24)
location.row(btn25)
location.row(btn26)
location.row(btn27)

moscow = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='Депозит', callback_data='deposit')
btn2 = InlineKeyboardButton(text='Амфетамин', callback_data='amf')
btn3 = InlineKeyboardButton(text='Мефедрон кристалл', callback_data='mef_cristall')
btn4 = InlineKeyboardButton(text='Мефедрон мука', callback_data='mef_myka')
moscow.row(btn1)
moscow.row(btn2)
moscow.row(btn3)
moscow.row(btn4)

perm = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Мефедрон кристалл', callback_data='mef_cristall')
btn2 = InlineKeyboardButton(text='Мефедрон мука', callback_data='mef_myka')
btn3 = InlineKeyboardButton(text='Гашиш', callback_data='gashish')
perm.row(btn2)
perm.row(btn1)
perm.row(btn3)

samara = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Мефедрон мука', callback_data='mef_myka')
btn2 = InlineKeyboardButton(text='Альфа-ПВП кристалл', callback_data='alfapvp')
samara.row(btn1, btn2)

voronej = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Мефедрон кристалл', callback_data='mef_myka')
btn2 = InlineKeyboardButton(text='Альфа-ПВП кристалл', callback_data='alfapvp')
voronej.row(btn1, btn2)

chelyaba = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='Мефедрон мука', callback_data='mef_myka')
chelyaba.row(btn1)

rostov = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='Мефедрон кристалл', callback_data='mef_cristall')
rostov.row(btn1)

yaroslavl = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='Мефедрон мука', callback_data='mef_myka')
yaroslavl.row(btn1)

ekb = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='Мефедрон мука', callback_data='mef_myka')
ekb.row(btn1)

spb = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='Мефедрон кристалл', callback_data='mef_cristall')
btn2 = InlineKeyboardButton(text='Мефедрон мука', callback_data='mef_myka')
btn3 = InlineKeyboardButton(text='Бошки', callback_data='boshki')
btn4 = InlineKeyboardButton(text='Альфа-ПВП кристалл', callback_data='alfapvp_cristall')
spb.row(btn1)
spb.row(btn2)
spb.row(btn3)
spb.row(btn4)

novosib = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='Мефедрон мука', callback_data='mef_myka')
spb.row(btn1)

tula = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='Мефедрон кристалл', callback_data='mef_cristall')
tula.row(btn1)

krasnodarskiy = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='Анапа', callback_data='anapa')
btn2 = InlineKeyboardButton(text='Сочи', callback_data='sochi')
krasnodarskiy.row(btn1)
krasnodarskiy.row(btn2)

ivanovo = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='Альфа-ПВП кристалл', callback_data='alfapvp_cristall')
ivanovo.row(btn1)

krasnodar = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='Мефедрон кристалл', callback_data='mef_cristall')
krasnodar.row(btn1)

voljskiy = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='Альфа-ПВП кристалл', callback_data='alfapvp_cristall')
voljskiy.row(btn1)


deposit = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='1.00 шт - от 1 000 руб', callback_data='deposit_1')
btn2 = InlineKeyboardButton(text='2.00 шт - от 2 000 руб', callback_data='deposit_2')
btn3 = InlineKeyboardButton(text='3.00 шт - от 3 000 руб', callback_data='deposit_3')
btn4 = InlineKeyboardButton(text='5.00 шт - от 5 000 руб', callback_data='deposit_5')
deposit.row(btn1)
deposit.row(btn2)
deposit.row(btn3)
deposit.row(btn4)

amf = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='1.00 г - от 1 700 руб', callback_data='amf_1')
btn2 = InlineKeyboardButton(text='2.00 г - от 2 450 руб', callback_data='amf_2')
amf.row(btn1)
amf.row(btn2)

mefcristall = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='1.00 г - от 2 300 руб', callback_data='mef_cristall_1')
btn2 = InlineKeyboardButton(text='2.00 г - от 4 600 руб', callback_data='mef_cristall_2')
btn3 = InlineKeyboardButton(text='3.00 г - от 6 900 руб', callback_data='mef_cristall_3')
btn4 = InlineKeyboardButton(text='5.00 г - от 11 500 руб', callback_data='mef_cristall_5')
mefcristall.row(btn1)
mefcristall.row(btn2)
mefcristall.row(btn3)
mefcristall.row(btn4)

mefmyka = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='1.00 г - от 2 000 руб', callback_data='amf_myka_1')
btn2 = InlineKeyboardButton(text='3.00 г - от 6 000 руб', callback_data='amf_myka_3')
btn3 = InlineKeyboardButton(text='5.00 г - от от 10 000 руб', callback_data='amf_myka_5')
mefmyka.row(btn1)
mefmyka.row(btn2)
mefmyka.row(btn3)

alfapvp = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='0.30 г - от 1 000 руб', callback_data='alfapvp_1')
alfapvp.row(btn1)

boshki = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='1.01 г - от 1 800 руб', callback_data='boshki_1')
boshki.row(btn1)

gashish = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='1.00 г - от 1 600 руб', callback_data='gashish_1')
btn2 = InlineKeyboardButton(text='2.00 г - от 3 200 руб', callback_data='gashish_2')
gashish.add(btn1, btn2)
