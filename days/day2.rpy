label day2_exit_hell:
    scene black with fade
    show text "День 2"
    pause 2.0
    scene bg roomgg with dissolve
    pause 0.2
    $ qm_togle = True
    """Прекрасное пробуждение от карканья под окном. Что за птица издает такие мерзкие звуки?
    Хм, какой-то странный ворон. Стоило на него посмотреть, как он сразу же умолк. Чего он хочет?
    Да как-то все равно, я дальше спать.
    """
    "..."
    "Видимо на сегодня я выспался – уснуть никак не получается."
    "Ладно, от лежания в кровати жизнь лучше не станет."
    "Пойду прогуляюсь."
    scene street1 with dissolve
    "Прекрасное утро прекрасного дня. Кажется, ничего не способно его испортить."
    show krisa with moveinright
    krisa "Здравствуй, [odaname]"
    "Этот противный голос можно узнать из тысячи."
    oda "И тебе не хворать, старик."
    krisa "Не настолько я стар, мелочь."
    oda "Конечно-конечно, можешь обманывать себя так дальше. Но, как бы ни приятно было называть тебя чем попало, но у тебя ведь и имя есть?"
    krisa "Есть конечно, но тебе явно о нем знать не надо. Но можешь звать меня… Хм… Крысоловом, да."
    oda "Ты это на ходу придумал?"
    krisa "Это правда важно?"
    oda "Мне все равно, старик"
    krisa "Тогда вернемся туда, с чего начали. В общем, мелкий, мне нужно, чтобы ты взял посылку из одной точки и доставил ее в другую. Легко, правда?"
    "Сомневаюсь в легальности всего этого. Что там вообще должно быть? Дурман?"
    oda"Где-то же есть подвох?"
    krisa "Вау, ты можешь замечать самые очевидные вещи, молодец. Конечно, есть подвох, спрашиваешь еще."
    oda "Объяснить не хочешь?"
    show krisa at right
    krisa "Не особо."
    "Ну надо же. Как-то я р
    азмечтался, что он хотя бы чуть-чуть доброжелателен."
    oda "Понял тебя."
    krisa "Ах да, постарайся одеться как можно неприметнее, ну или хотя бы голову скрой полностью."
    "Чем больше я узнаю подробностей, тем меньше мне это все нравится."
    oda "Понял, от тебя помощи хотя бы в этом ждать не стоит?"
    krisa "А ты схватываешь на лету."
    "Кто бы сомневался."
    oda "Что делать и куда идти?"
    krisa """Повезло тебе. Забрать посылочку нужно будет в переулке рядом. Как только увидишь, что укутанный парень бросит деревянную шкатулку, ждешь пока посыльный скроется, и хватаешь ее. Оставишь ее у кабака на рынке. 
    Просто брось в переулок и прячься как можно быстрее. Запомнил?"""
    oda "Конечно"
    krisa "Вот и отлично, у тебя еще есть время… Добыть маскировку. А на этом я с тобой прощаюсь, постарайся не попасться."
    hide krisa with moveoutleft
    "Вот так он и ушел."
    "Ну, делать нечего. Надо бы найти чем прикрыться."
    "..."
    "Стащив чей-то сушащийся плащ, который, очень удивительно, мне как раз, я снова встал за угол, и поглядываю на переулок."
    "Долго ждать не пришлось, и какой-то человек в плаще быстрым шагом зашел в переулок и положил ту самую шкатулку у стены. Так же быстро зайдя, он быстро ушел. Теперь моя очередь."
    "Времени оглядывать посылку нет, быстро хватаю и выхожу из переулка."
    "Того парня нигде не видно, но, наверное, это к лучшему. Чем меньше подозрительных людей рядом, тем меньше вероятность что до нас докопаются."
    "Иду по улице в сторону городской площади, ничего не предвещает беды."
    show guard with dissolve
    guard "Добрый день, молодой человек, а что это вы несете?"
    oda "И вам добрый день, молодой человек. А это иван-чай для душевнобольных, хотите?"
    guard "Нет, спасибо, пожалуй…"
    oda "Ну раз так, то на этом я откланяюсь, не болейте!"
    hide guard with moveoutright
    """Человек явно непростой, раз интересуется посылкой. 
    Нырнув в ближайший переулок, привычными путями ухожу подальше от места встречи. 
    Надеюсь, что он не так хорошо знает эти закоулки."""
    scene st4 with fade
    show guard at right
    guard "Добрый день. Слышал, у вас есть иван-чай. Я хороший знаток таких целебных трав…"
    oda "Добрый день, поздравляю вас. Я тороплюсь, так что окончим разговор."
    "Откуда он взялся?! Ладно, не важно, нужно лишь еще быстрее добраться до места."
    "Забежав в другой переулок, я не стал тут долго задерживаться."
    "..."
    scene rt with dissolve
    pause 0.3
    "Наконец-то городская площадь. Не хочу держать при себе хотя бы лишнюю секунду это посылку."
    "Нужный кабак был тут рядом. Так, где же переулок?"
    """Как будто бы отвечая мне, раздается тоже самое противное карканье, что и утром. 
    Поворачиваю голову в сторону звука, и вижу: нужный мне переулок, и тот же подозрительный ворон. Так, не важно."""
    scene st2 with fade
    "Забегаю в переулок, кладу шкатулку, и иду обратно на выход. Отлично, доставка прошла успешно."
    scene st3 with dissolve
    "Заворачиваю за угол, чтобы выйти на одну из главных улиц."
    show guard at center
    show guard2 at right
    guard "Добрый день, гонец. Бегать не устал?"
    "Еще один мужик, но этот видимо по умнее будет, раз взял с собой еще и пару стражников."
    oda "Добрый день, не думаю, что знаю вас. Вы что-то хотели?"
    guard "Да, хотели бы узнать, где твоя посылочка."
    oda "О, какое совпадение, я бы тоже хотел это знать."
    guard "И правда, какое совпадение. Ну что ж, думаю, вместе мы найдем твои травы быстрее, чем по отдельности."
    oda "Как мило с вашей стороны, господа, заботиться о таком обычном посыльном. Полагаю, что вы можете потратить свое время полезнее, чем искать какой-то иван-чай."
    guard "Ну что ты, юноша, нам не сложно."
    "Так просто, как прошлые он не отстанет. Ну что ж, надеюсь бегают они не так быстро, как я."
    hide guard with moveoutright
    hide guard2 with moveoutright
    "Без лишних слов, а точнее без них совсем, я, что есть сил, развернулся и побежал в противоположную от них сторону."
    "Словно ожидая такого исхода, эта троица не сильно отставала."
    "..."
    scene st2 with fade
    pause 0.2
    "Свернув в какой-то случайный переулок уже, бог знает, какой раз, я спрятался за угол, и высматривал ситуацию. Эти трое пробежали мимо."
    "Наконец-то эта погоня закончилась. Можно и пойти домой."
    scene door2 with dissolve
    "Ну, если бы все было так просто. Проходя мимо ничем не примечательной двери, она открылась и меня втащили внутрь. Все осознал я уже только хорошенько приложившись о пол."
    scene twohome with fade 
    show krisa 
    krisa "Надо же, это какая-то судьба, мелкий."
    "Тот же противный голос, что приветствовал меня утром. И нет, это не ворон."
    krisa "Представь себе, из всех посыльных не поймали только тебя, да и еще от погони ты оторвался именно у этого убежища!"
    oda "Надо же, как интересно."
    krisa "Ну точно, кому я это говорю, как будто ты вообще в этом что-то понимаешь."
    oda "Наконец-то ты понял."
    krisa "Да-да, мелочь. Ну, тебе очень повезло, даже удивительно насколько."
    oda "Засмущаешь меня сейчас своим вниманием."
    krisa "Ага, как же."
    oda "Но все же, мне интересно, а что будет с остальными?"
    krisa "С другими посыльными? Они вообще никому не нужны. Ну, попытают немного, может даже пару пальцев отрежут, потом отпустят. Никто не собирается тратиться на их содержание."
    oda "Какая незавидная судьба."
    krisa "Ну, спешу тебя обрадовать, если бы тебя поймали, то именно тебе бы и отрезали пальцы, потому что ты полезнее тех идиотов будешь."
    oda "Раз уж я такой полезный, то может и награда будет получше?"
    krisa "Моя похвала уже достаточная награда, разве не так?"
    oda "Нет."
    krisa "Какой неблагодарный ребенок мне попался. Ну ладно, давай так, сделаешь для меня еще что-нибудь, и так уж и быть, получишь мою услугу."
    oda "Ничего себе, это ведь так полезно."
    krisa "Рад что ты понял. Так, посиди тут, и выбрось этот кусок ткани. А мне ты уже надоел, так что я пойду."
    oda "Ага, не споткнись."
    "Наконец-то он ушел. Последую его совету, и пережду тут немного."
    "..."
    "Просто сидеть и ждать в этой халупе уже надоело. Думаю, все улеглось и можно пойти домой. Ну в этот раз меня точно не оставят сидеть в чьем-то доме."
    scene st3 with dissolve
    pause 0.3
    "Быстрым шагом отойдя от развалин, которые еще чудом держаться, я наконец-то могу и спокойно пройтись."
    "Ну и денек, знал бы что такое со мной произойдет, ни за что бы не полез в тот подвал."
    "Меня могли поймать, и сидел бы я в грязной, холодной камере, с отрубленными пальцами. Брр, даже представлять противно. Сейчас я хотя бы прохлаждался на каком-то подобии кровати."
    show inq at right
    inq "Здравствуйте!"
    "Откуда?!"
    "А, это он."
    oda "Здравствуйте."
    "Тот самый инквизитор. Ну, он то точно не знает, что я тут бегал с каким-то подозрительным грузом."
    show inq
    inq "Представьте себе, молодой человек, мне тут такое рассказали. Вы знали, что сегодня гонялись за какими-то бандитами по всему городу."
    inq "Они с какой-то важной шкатулкой бегали. Всех переловили, а одному удалось сбежать!"
    show inq at left
    inq "Вот так у него ноги быстрые, нам такого в гонцы, тогда я бы мог быстрее согласовывать с начальством казни!"
    "Я все еще надеюсь, что он ничего не знает."
    oda "Надо же, он мог бы помогать совершать благое дело, а вместо этого бегает со шкатулками какими-то."
    inq "Вот-вот, я о том же! Ну ладно, ведьмы все еще портят этот город своим существованием, так что я пойду блюсти порядок дальше!"
    hide inq with moveoutleft
    "Откуда он такой вообще взялся?"
    "..."
    "Следующий путь до дома прошел без происшествий."
    scene bg roomgg with fade
    "Дом, милый дом."
    "Хм, Кара не дома?"
    "Ну, ушла, наверное, куда-то."
    "Так, что-то я притомился бегать по городу, прилягу поспать"
    jump day3
    return
label day2ykral_obed:
    scene black with fade
    show text "День 2"
    pause 2.0
    scene bg roomgg with dissolve
    pause 0.2
    "Прекрасное утро прекрасного дня."
    "Чем же мне заняться?"
    "Стоит навестить Кэрол, мало ли она что-нибудь разузнала."
    "..."
    scene znaxr with fade
    oda "Доброе утро."
    show kerol1 at right
    kerol "Доброе утро, [odaname]"
    "В этот раз ждать не придется."
    oda "Вы что-нибудь узнали?"
    kerol "Особо интересных записей не было, только то, что мы и так знаем. Книг содержит секрет создания панацеи, на этом все."
    oda "Абсолютно ничего?"
    kerol "Да, ну, если это тебя успокоит, то есть вероятность, что эта книга и правда существует, раз даже у моей семьи есть о ней записи."
    oda "Особо не помогло."
    show kerol1 at left
    kerol "Так, ты давай не жалуйся. Это все что мы можем узнать."
    oda "Хорошо-хорошо."
    kerol "Всё, давай, уходи."
    oda "Да-да, увидимся."
    hide kerol1 with moveoutleft
    "Так, хотя бы немного хорошие новости."
    "Ну, думаю, после такого стоит подышать свежим воздухом."
    jump day2_centergoroda_obed_and_obed_kara

label day2ykral_obed_kara:
    scene black with fade
    show text "День 2"
    pause 2.0
    scene bg roomgg with dissolve
    pause 0.2
    "Прекрасное утро прекрасного дня."
    "Чем же мне заняться?"
    "Позволю сердцу направлять меня."
    "Звучит еще глупее, чем есть на самом деле, хорошо, что это всего лишь в моих мыслях."
    "Так, куда бы сходить?"
    "Ну, центр города звучит как хорошая идея. Может быть, сегодня там найдется работенка."
    jump day2_centergoroda_obed_and_obed_kara

label day2_centergoroda_obed_and_obed_kara:
    scene rt with fade
    "Хм, еще более пустая, чем обычно. Сегодня день какой-то особенный, или что?"
    "Работу такими темпами я не найду."
    "Присяду что ли, делать все равно нечего."
    "..."
    "Даже смотреть не на что, людей настолько мало, что это не смешно."
    scene rtvo with dissolve
    "Хм, ворон? Тоже решил присесть отдохнуть?"
    "Еще и смотрит так. Эта игра в гляделки не принесет мне ничего хорошего."
    "Что он делает?"
    scene rt
    show voronleft at right
    oda "Эй, отпусти меня."
    "Зачем он дергает мою одежду? Зовет куда-то?"
    oda "Всё-всё, пойду я с тобой, хватит тянуть меня."
    "Мда, разговариваю как идиот с птицей. Еще и иду за ней. Что может пойти не так?"
    hide voronleft
    scene st2 with fade 
    show voronright 
    #Здесь желательно отрисовать шкатулку и воткнуть ее на фон вместе с вороном
    "И куда ты меня привел?"
    "На что я надеюсь? Как будто он мне ответит."
    "Что это? Какой-то чудак в темном плаще забежал в переулок и бросил деревянную шкатулку, ну явно не обронил, раз так быстро выбежал."
    oda "Ой, отстань, тупая птица."
    "Зачем он ткнул меня в ногу? Хм? Указывает на шкатулку."
    oda "Там драгоценности какие-то? Ты сорока что ли?"
    "Ну, что упало – то пропало. Хотя мне явно не стоит этого делать."
    "Подняв шкатулку, смотрю на ворона, он смотрит на меня."
    oda "Что мне с этим делать?"
    "Мне кажется, рядом с этой птицей я тупею. Он же мне явно не ответит. Ну, он же меня привел, надеюсь покажет куда это нести."
    "Ну, хотя бы в этом я оказался прав. Он полетел куда-то. Пойду за ним."
    "..."
    "В какие дебри я вообще попал? Не знал, что в этом городе даже есть такие переулки. Шляюсь возле каких-то ветхим домов. Один ветерок, и половину домов сдует."
    "Эта птица даже не думает останавливаться. Ведет меня куда-то, бог знает куда."
    "Сердце, куда ты меня привело?"
    "..."
    "Наконец-то мы дошли куда-то. А, собственно говоря, куда?"
    hide voronright with fade
    "Смотрю на ворона… Так, а где он? Только что тут был."
    show krisa at left
    krisa "Так-так-так, кто это тут у нас?"
    "Кто?!"
    krisa "Эй, мальчик, знаешь, что у тебя в руках?"
    "Что это за лысый подозрительный тип?"
    oda "Э, нет?"
    "Даже не сказать, что меня сюда привел ворон. Тупая птица, во что я ввязал"
    krisa "Надо же, посылка сама пришла ко мне в руки. Ну, малыш, не хочешь отдать?"
    oda "Нет, почему я тебе должен ее отдать?"
    krisa "Ну, чтобы стражники тебя не отпинали, а? Как тебе такая сделка?"
    oda "Пусть сначала догонят."
    show krisa at right
    krisa "Ой, какой самоуверенный. Ладно, мелочь, поиграли и хватит, отдавай шкатулку."
    oda "И почему я должен ее тебе отдавать, она твоя что ли?"
    krisa "Как ты узнал? Там вроде не подписано."
    oda "..."
    krisa "Ладно, мальчик, у меня дел по горло."
    oda "Я ее в канаву выброшу, если подойдешь."
    "В доказательство своих слов, я протянул руку над дырой в земле."
    krisa "Хорошо-хорошо, мальчик, давай быстрее, что ты хочешь взамен этой шкатулки, содержимое которой ты даже не знаешь?"
    oda "Так я могу посмотреть и узнать."
    krisa "Нет, не можешь."
    "При попытке открыть, шкатулка не открывается. Похоже и правда не могу."
    oda "Хорошо, но что ты можешь предложить за нее."
    show krisa
    krisa "Могу тебе предложить поработать на меня, как тебе, нравится? Знаю-знаю, это очень щедро с моей стороны, но сегодня у меня настроение хорошее."
    oda "И где моя выгода?"
    krisa "Это же очевидно, ты установишь со мной связь. А это дорогого стоит."
    oda "Откуда мне знать?"
    krisa "Слишком много вопросов, ты мне надоел. Ты согласен или нет?"
    "Не думаю, что отказ принесет хоть что-нибудь."
    oda "Последний вопрос. Ты поможешь мне найти кое-что?"
    krisa "Что: брата, сестру, игрушку, потерянную в детстве? Будь конкретнее."
    oda "Легендарный манускрипт – «Книгу Огненных Звёзд»."
    krisa "О, звучит гораздо интереснее, еще один мальчишка в поисках сказки. Хорошо, малыш, ты меня заинтриговал."
    oda "Какой-то подозрительный блеск в его глазах. Для него это все игра что ли?"
    krisa "Ладно, мелкий, мне интересно, насколько далеко ты зайдешь. Ну все, отдавай шкатулку."
    "Бросаю шкатулку ему в руки. С довольной улыбкой, этот подозрительный тип разворачивается и уходит."
    oda " Как тебя звать, старик?"
    krisa "Ммм… Крысолов, да. Зови меня так."
    hide krisa
    "И после этих слов он скрылся за углом. Что это сейчас вообще было?"
    "Тупая птица, привела меня куда-то, к какому-то странному человеку, еще я и подписался на него работать. Ну что за день."
    "Так, не стоит мне тут задерживаться. Я вообще хотел отдохнуть на площади."
    "Ну вот и вернусь туда."
    scene rt with dissolve
    "..."
    "Хм, откуда взялась эта толпа? "
    "А, кого-то сегодня казнят. Ну, на это зрелище я смотреть не собираюсь. Думаю, лучше пойду домой."
    "Ой, в кого-то врезался."
    show inq at right 
    inq "Здравствуйте!"
    oda "Здравствуйте. Ваша работа?"
    "О, инквизитор. А почему он здесь, а не на эшафоте?"
    inq "Конечно! Благодаря моему упорному труду смогли поймать этих ужасных ведьм и сегодня их сожгут! И город станет еще чуточку чище от их грязного присутствия."
    "Какой странный человек он всё-таки."
    oda "Спасибо за ваш тяжелый труд."
    "Нет, по какому признаку он понял, что они ведьмы?"
    inq "О, ради таких слов я и продолжаю работать. Ну, молодой человек, мне пора."
    hide inq
    "И ушел. Откуда он такой вообще взялся?"
    "Ладно, хватит на сегодня приключений, теперь точно домой."
    "..."
    "Путь до дома прошел без происшествий."
    scene bg roomgg with fade
    "Дом, милый дом."
    "Хм, Кара не дома?"
    "Ну, ушла, наверное, куда-то."
    "Так, что-то я притомился бегать по городу, прилягу поспать."
    jump day3
    return