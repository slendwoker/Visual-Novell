label day4:
    scene black with fade
    show text "День 4"
    pause 1.0
    scene black with fade
    show text "Это что? конец? хе хе хе :)"
    pause 2.0
    scene bg roomgg with dissolve
    pause 0.2
    $ qm_togle = True
    "Прекрасное утро, прекрасного дня. Могло бы быть, если бы я проснулся позже. Но, этого не случилось, так что придется работать с тем, что имеем."
    "Хм, Кара спит, ну ладно, не буду ее беспокоить, ей лучше поспать. Да и рано еще. Это я что-то проснулся. Так, аккуратно выйду из дома, лишь бы Кара не проснулась."
    "Ну, вроде получилось."
    scene znaxr with fade
    show kerol1
    oda "Доброе утро."
    kerol "Доброе утро, [odaname]"
    oda "Я вчера хотел кое-что спросить. Состояние Кары ухудшается, да?"
    kerol """Ты ведь это и так понял. 
    Да, с каждым днем ей хуже, сейчас более-менее, но кто знает, что произойдет, допустим, завтра.
    Я даже не могу примерно сказать, сколько Каре осталось."""
    """Ситуация хреновая. Максимально. Я даже не знаю, что делать. На ум приходит только уговор с Чумным Доктором. 
    Похоже он моя единственная надежда. Даже если и ложная, я не могу просто сидеть сложа руки."""
    oda "Вы что-нибудь знаете о Чумном Докторе?"
    kerol "М? Чумной Доктор? Ну, только, что он помогает больным чумой. Как и я, собственно говоря. А что, меня уже недостаточно, думаешь?"
    oda "Нет-нет, что вы, вы самая ценная в этом городе, если не в стране."
    kerol "То-то же. Это все, что ты хотел спросить?"
    oda "Хотел бы знать, можно ли ему доверять. Но вы о нем ничего не знаете."
    kerol "Ну, тут я тебе не помощница."
    oda "Я это уже понял. Но все равно спасибо, за Кару."
    kerol "Принимаю твою благодарность. Можешь не беспокоиться."
    oda "Тогда я пойду, прощайте."
    kerol "Да-да, береги себя."
    hide kerol1
    "Так, с целью определились, теперь пора идти. Как он говорил, сходить к Священнику надо."
    scene st3 with dissolve
    # Мб на фон вставить персов для вида
    # Nvl делаю
    """Откуда Чумной Доктор взялся. Как будто из ниоткуда появился. 
    Такой человек явно привлекает много внимания. Так бы или иначе я бы услышал о нем. Но даже сейчас, информации очень мало. 
    Ни слухов, ничего. И почему он явился ко мне пару дней назад. Эх, какие же проблемные люди, которые знают очень много. 
    Почему меня окружают только такие люди. Хотя бы Кара может меня утешить своим присутствием."""
    "Что мне должен сказать Священник? Ну, должно быть очень важное."
    "Как сказать, сердце направляет меня по этому пути. Эх, все так же глупо звучит."
    """Стражи как будто больше стало, к чему это? Хотя, какая разница. 
    Главное, чтобы делали свою работу. Но в этом я сомневаюсь. Просто еще больше бездельников на улицах города. Бесполезная массовка, в случае чего, они даже пальцем не пошевелят. 
    Иногда, они, конечно, что-то делают, но насколько это редко. 
    Может, в стражники надо было пойти? Ходил бы улицам и получал за это деньги. Мечта просто.""" 
    "Ну ладно, это, явно, не вся их работа"
    "Надеюсь, прихожан не будет, а то ждать еще, пока они разойдутся, пока они поговорят со Священником. Ну ждать совсем не хочется, да и интересно, что же он все-таки скажет."
    show chel1 at left
    chel1 "Эй, парень!"
    "Хм, ну, а когда я был прав. Видимо, даже большое количество стражи все так же бесполезно."
    chel1 "Эй, постой."
    hide chel1
    "О, ну это явно не мне. Пойду-ка я побыстрее, а то не очень интересно."
    "И так дел полно, не хватало еще слушать бредни всяких там."
    """Ну и все же, почему стража позволяет таким людям ходить среди бела дня. 
    Неужели с таким количеством они не могут переловить всех и заключить в темницу. 
    Да даже если не всех, то хотя самых наглых, которые на улице прямо докапываются до прохожих. Не по переулку же прогуливаюсь."""
    "Да даже если он платит страже. Все-то патрули не подкупишь."
    "Хотя он может скрытый умник."
    "Ну, пока я плакался и сокрушался о безопасности в этом городе, уже дошел до церкви. Ну, давайте послушаем, что Чумной Доктор хочет, чтобы я услышал."
    scene ch with fade
    "Мне повезло, в церкви пусто. Ну, Священник-то тут."
    scene bg church with dissolve
    show priest
    oda "Здравствуйте, отец."
    pri "Здравствуй, сын мой. Вижу, сердце твоё направило тебя на путь к цели, которой ты желаешь."
    "Надеюсь он и правда знает, о чем говорит."
    oda "Да, отец. На днях я встретил человека, который поможет мне найти."
    pri "А еще много чего натворил ты."
    "О чем он?"
    pri "Не беспокойся, сын мой, Бог милостив и простит тебя, если ты будешь искренен."
    "Да ну сколько можно, еще один все знающий мужик, сколько вас еще будет?"
    pri "Можешь быть спокоен, никто за тобой за это не придет."
    oda "Благодарю, отец. Вы меня успокоили."
    "Да ничего подобного. Это у них игры такие веселые?"
    pri "Вижу, что нет. Но, время придет, и ты все поймешь."
    oda "Я вас понял, отец."
    pri "Это же не все, что ты хочешь услышать, не так ли, сын мой?"
    "Он же и так все понимает, зачем только спрашивает?"
    oda "Да, отец, я хотел бы услышать то, что должен."
    pri "Ты услышал, то что должен, ступай."
    "И это все? "
    oda "Хм, отец, вы уверены, что я услышал все, что должен был?"
    pri "Да-да, сын мой, можешь быть свободен, ступай."
    "Издевается?"
    oda "Ну, тогда я пойду, отец?"
    pri "Конечно."
    "Ну, делать нечего."
    pri "Сын мой, на самом деле, это еще не все."
    "Так и знал, старик, глумишься надо мной."
    oda "Слушаю вас, отец."
    pri "Слушай внимательно, мрачный мужчина с вороном на плече заслуживает достаточно доверия, можешь следовать за ним, и тогда ты найдешь, что ищешь."
    "И он тоже знает. Хм, ну, надеюсь и в этот раз Священник поможет мне в поисках, в прошлый то раз не соврал"
    oda "Благодарю вас, за ваше наставление, отец."
    pri "Ступай, сын мой. И храни тебя Господь."
    hide priest
    "Ну, теперь Чумному Доктору можно верить чуточку больше. В прошлый раз, наставления Священника привели меня, через обходные пути, правда, но привели к Чумному Доктору."
    "Ладно, думаю, можно и домой. Как он говорил? Даст мне знать, вроде бы."
    scene st3 with fade
    # NVL текст делать
    "И вот, с новыми силами, с намеченной целью, со спокойной душой, я иду домой. Это того стоило."
    "Почаще к нему ходить, что ли. Ну, это мне подумать на будущее."
    "Даже теперь не так тошно от этих теневых элементов. Хотя, стража, как по мне, все так же бесполезна. Ну все, хватит думать о них на сегодня."
    "Что же такого может попросить Чумной Доктор? Сомневаюсь, что ему нужна помощь именно меня, все-таки он знаком с Крысоловом, а по этому старику сразу видно, что не последний человек в городе."
    "Но все же, подозрения меня так просто не отпускают, Священник сказал, что доверять можно, но можно ли доверять Священнику? Ну, главное вслух такое не говорить, а то еще повесят."
    "Надеюсь, обойдется все без происшествий, а то хватит с меня приключений. "
    "Хотя, даже как-то странно, никого не встретил, слишком спокойно сегодня как-то. Ну, за исключением того придурка из переулка. Он явно не заслуживает ни капельки доверия."
    "Ну, надо не жаловаться, а наслаждаться невиданным спокойствием, в последнее время это редкость."
    show inq at right 
    inq "Здравствуйте!"
    "Я уже не удивлен, он всегда подкрадывается в такие моменты, когда его не ждешь."
    oda "Здравствуйте."
    inq "Не заметили, что сегодня как-то тихо?"
    oda "Да, приметил что-то подобное. И стражи стало как-то больше."
    inq "Вот-вот, верхушка тоже заметила, что как-то подозрительно тихо, и увеличила количество патрулей."
    inq "Но! Не только преступники попрятались, но и эти чертовы дьяволопоклонники."
    inq "Нигде не могу найти сегодня ни одной ведьмы, эти слуги сатаны будто попрятались вместе с преступниками. Я чувствую, будто день прошел напрасно, я не вздернул ни одного сатаниста."
    inq "Ни сжег ни одной ведьмы. Это ужас, надеюсь Господь не разочаруется во мне, за то, что я плохо выполняю свою работу."
    oda "Не беспокойтесь, Бог милостив, главное, чтобы вы были искренни."
    inq "Точно, и все же, какой вы мудрый молодой человек. Но, мой долг не ждет, я надеюсь, что найду хотя бы одну ведьму! Прощайте, молодой человек!"
    hide inq
    "И снова его этот фирменный салют."
    "Интересная личность, этот инквизитор. Насколько интересный, настолько же и странный. Надеюсь, он один такой. Не хотелось бы, чтобы по городу бегали сотни таких фанатиков."
    "Ну, дело не мое, мое дело – идти домой."
    "Сейчас-то уж точно должно все пройти без происшествий."
    "Самое большое происшествия за сегодня уже произошло."
    "..."
    scene st3 with dissolve
    "Хм, попробую сократить через этот переулок."
    scene st2 with fade
    "Так, сейчас побыстрее уйти отсюда, что-то мне здесь не нравиться."
    "Ну, конечно, все не могло быть так просто."
    show vor1 at right
    band "Здарова, мелочь, куда-то торопишься?"
    "Двое спереди. Трое сзади. Ситуация хреновая."
    oda "На самом деле да, могу я пройти?"
    band "Можешь, но, если выложишь все ценное."
    oda "Так у меня даже ничего нет."
    band "Ага-ага, все вы так говорите. Давай доставай и можешь быть свободен."
    oda "Да нет у меня ничего!"
    "Я уже даже начинаю злиться. Вот он, дом, прямо передо мной, буквально дорогу перейти, и я выполню задание. А они тут хотят меня ограбить, а у меня даже ничего нет."
    band2 "Да что ты с ним церемонишься?"
    "Человек сзади подошел, и я почувствовал, как меня проткнуло ножом в спину. После этого меня толкнули, и я упал на живот."
    band "Ну и нужно ли было его убивать?"
    band2 "Тебя забыл спросить, давай, обыщи его и пойдем уже, не терпится напиться."
    band "Ладно-ладно."
    "Я чувствую, как чьи-то руки роются в моих карманах."
    band "У него и правда ничего нет."
    band2 "Цк, зря только время потратили."
    hide vor1
    "Серьезно? Меня пырнули ножом в подворотне какие-то алкаши? И вот так все закончится? "
    "Надо попытаться встать. "
    "Полностью встать не получилось, но я хотя бы прилег у стены, а не валяюсь мордой в пол."
    "Ужасная ситуация. Я умру. Выжить без чужой помощи невозможно."
    doc "И снова здравствуй, юноша."
    "Этот голос…"
    oda "И вам не хворать."
    show docktor with dissolve
    "Чумной Доктор во всей красе."
    doc "Вид твой какой-то не очень."
    oda "Во мне всего лишь лишняя дырка."
    doc "Ну, не все после такого выживут."
    oda "Я знаю, знаю. Вы поглумиться пришли, или как?"
    doc "Даже не надейся, спасать я тебя не буду."
    "Мудак."
    oda "Тогда зачем вы здесь?"
    doc "Знаешь, ты устроил для меня интересное представление. Мне было очень весело наблюдать, как ты, словно таракан, бегаешь туда-сюда, в надежде найти мифическую книгу."
    doc "Но знаешь, что? Книга эта все время была у меня. Все время ты бегал в надежде найти книгу, которая была у меня."
    oda "Говорили же, что глумиться не будете."
    doc "Я такого не говорил. Но не суть. Мне было очень весело, так что в награду, я спасу ту девчонку. Очень уж мне понравилось, что ты для нее делал."
    doc "Веселее было бы, если бы она умерла на твоих глазах, но, не судьба."
    doc "Так что, юноша, можешь спокойно покинуть этот бренный мир."
    "Как жаль, что я не смогу увидеть, правду ли он только что сказал. Но что мне остается? Видимо, на этом все. Сожалений особых нет, кроме Кары, конечно."
    "Хотелось бы увидеть ее перед уходом на тот свет. Ну, нищие не выбирают.Что тешит меня перед смертью, так это хотя бы то, что Кара будет жить."
    "Можно уйти спокойно."
    doc "На этом все, юноша. Ты подарил мне прекрасное представление, я подарю твоей девчонке исцеление. А теперь, прощай."
    oda "Увидимся в аду"
    doc "Не дождешься."
    hide docktor with fade
    "Прощай, этот бренный мир…"
    scene bg roomgg
    pause 0.5
    "Неизвестное количество времени спустя"
    "Кара открыла свои глаза. Внешне с ней все в порядке. На самом деле, болезнь ушла, как будто ее никогда и не было."
    show kerol1 at right
    show karanew at left
    kerol "Доброе утро, Кара."
    kara "Доброе утро, Кэрол. А где [odaname]?"
    kerol "Его нет."
    kara "Что?"
    kerol "Оды, здесь нет. [odaname], ушел. Он исчез."
    pause 0.5
    $ qm_togle = False
    scene end1 with fade
    pause 2.0
    scene end2 with fade
    pause 3.0
    scene end3 with fade
    pause 3.0
    scene end4 with fade
    pause 3.0
    return
