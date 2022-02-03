import random
import telebot;

bot = telebot.TeleBot('TOKEN')
d = '''Если бы вам навсегда запретили заниматься вашей нынешней работой, какую новую профессию вы бы выбрали?
Если бы у вас была возможность больше никогда не работать, вы бы ею воспользовались?
Снились ли вам сны, которые вы запомнили на всю жизнь?
Каким человеком вы восхищаетесь?
Хотели бы вы дружить с таким человеком, как вы?
Каким было самое красивое место, в котором вам довелось побывать?
Если бы вы могли поехать куда угодно, в какую точку планеты вы бы отправились?
Если бы вы могли жить где угодно, что за место это было бы?
Если бы список 7 чудес света нужно было составить заново, что бы вы в него включили?
Что именно каждый человек должен хотя бы раз испытать в своей жизни?
Чего вы боитесь больше всего на свете?
Было ли у вас в жизни событие, когда казалось, что все плохо, а потом выяснилось, что все к лучшему?
Есть ли фильмы или книги, которыми все восхищаются, а вы терпеть их не можете, и наоборот?
Вы когда-нибудь плакали над книгой или фильмом? Какие книги и фильмы это были?
Если бы вы могли стать персонажем книги или фильма, то каким?
Если бы ваша жизнь была фильмом, как бы он назывался?
Какой самый странный комплимент вам когда-либо говорили?
Какая самая неловкая ситуация была у вас в жизни?
У вас есть какие-нибудь «постыдные удовольствия», которые, однако, дают вам ощущение счастья и полноты жизни?
Если бы вы могли изменить какую-то одну вещь в своем прошлом, что бы это было?
А если бы вы могли изменить какую-то одну вещь в мире, что бы вы выбрали?
Если бы вы до конца жизни должны были есть только один продукт, что бы это было?
Если бы вы должны были проживать один и тот же день снова и снова, какой день в своей жизни вы бы выбрали?
Хотели бы вы стать бессмертным?
Если бы вам осталось жить год, как бы вы его провели?
Если бы вы могли дать совет самому себе в 15 лет, что бы это было?
Какое ваше лучшее воспоминание из детства?
Если бы в детстве вы могли положить все свои самые любимые вещи в капсулу времени и отправить в будущее, какие предметы бы там оказались?
Как вы представляете свой идеальный день?
Если бы вы могли иметь в собственности только 5 вещей, какие бы вещи это были?
Какова самая мудрая мысль, которую вы когда-либо слышали?
Если бы у вас была возможность за полчаса научиться чему угодно, чему бы вы научились?
Если бы у вас была возможность навсегда остаться в каком-то возрасте, какой возраст вы бы выбрали?
Если бы можно было вновь начать свою жизнь с 10-летнего возраста, но при этом сохранив весь ваш опыт и знания, вы бы сделали это?
Если бы вы могли выбирать эпоху, в которой жить, какая подошла бы вам лучше всех?
Если бы вы могли своими глазами увидеть любое событие из прошлого, настоящего или будущего, что бы вы выбрали?
Какую сверхспособность вам хотелось бы иметь?
Если нужно было бы выбрать только один вариант, вы бы хотели, чтобы ваш ребенок вырос умным или добрым?
Если бы вам предложили вечную молодость и кучу денег с условием, что у вас никогда не будет любви и семьи, вы бы согласились?
Есть какая-то информация или теория, в которую вы просто верите, так как у нее нет доказательств? Почему?
Нравится ли вам тот человек, которым вы стали?
Что люди скажут о вас на ваших похоронах?
О чем вы будете сожалеть, что не сделали в своей жизни?
Какова самая мудрая мысль, которую вы когда-либо слышали?
Чему вас научил ваш личный горький опыт?
Как часто реализуются ваши самые сильные тревоги и страхи?
Если бы вам осталось жить год, чего бы вы попытались достичь?
Вы служите деньгам, или деньги — на службе у вас?
Боитесь ли вы быть самим собой в кругу других людей? Почему?
За что вы благодарны?
Сделали ли вы недавно что-то, чем гордитесь?
Сделали ли вы недавно что-то доброе?
Если бы вы знали, что завтра умрете, какие бы вопросы задали себе?
Если бы сбылись ваши худшие страхи, имело бы это значение пять лет спустя?
Как бы вы описали себя?
16. Пользуетесь ли вы чужими советами?
Вы быстро обижаетесь?
Считаете ли вы себя приятным человеком?
«То, что мы получаем, обеспечивает нам существование. То, что мы отдаем, творит нашу жизнь» – Что эти слова Уинстона Черчилля значат для вас?
Обогащаете ли вы чем-то жизнь других?
Живете ли вы осмысленной жизнью?
Что такое осмысленная жизнь?
Отдали бы вы свою жизнь, чтобы спасти жизнь другого человека?
Многим ли вы готовы пожертвовать ради людей, оказавшихся в нищете?
Если бы вы могли проживать один и тот же день снова и снова, что бы вы предпочли сделать в этот день?
Считаете ли вы себя человеком важным и достойным привязанности и любви?
Что поможет вам чувствовать себя более достойным человеком? Что в вас должно стать иначе?
Что вас чаще всего расстраивает?
Согласились бы вы работать меньше (и заниматься любимыми делами) и меньше зарабатывать?
Что приносит вам мир?
Каково главное качество, которое вы ищете в других?
Какова ваша главная мечта?
Каков ваш главный страх?
Как изменился бы мир, если бы вы не родились?
Какие жизненные уроки вы хотели бы знать десять лет назад?
Если бы вы могли сказать самому себе в молодости что-то одно, что бы это могло быть?
Если бы ваша жизнь была фильмом, как бы он назывался?
Если бы ваша жизнь была фильмом, понравилось бы вам его смотреть?
Что для вас значит успех?
Если бы вы могли стать другим человеком, то каким бы стали?
Каким был лучший день вашей жизни? Почему вы так считаете?
Чего вы больше всего ждете в жизни?
От каких дурных привычек вы хотели бы отказаться?
Кто для вас авторитет и почему?
Знаете ли вы язык любви своего партнера?
Знают ли люди, которых вы любите больше всего, как вы их любите?
Удовлетворены ли вы глубиной своих отношений с людьми?
Что вы должны себе?
Учитывая вашу нынешнюю повседневную жизнь, чего вы рассчитываете добиться через пять лет?
Часто ли вы говорите «да», хотя на самом деле хотите сказать «нет»? Почему?
Что вы узнали вчера?
Что вам нравится в себе?
Назвали бы вы себя щедрым человеком?
Когда люди с вами говорят, вы действительно слушаете?
Что самое главное, что вам нужно изменить в своей жизни в этом году?
Сколько часов в неделю вы проводите в интернете?
Каковы ваши самые распространенные негативные мысли? Есть ли в них логика?
Считаете ли вы, что за некоторые вещи вам уже поздно браться? Почему?
Если бы вы могли стать самым влиятельным человеком в мире, что бы вы изменили?
Сколько времени вы проводите с семьей и друзьями?
Где вы хотите оказаться через пять лет?
Осложняют ли вашу жизнь вещи, в которых нет необходимости?
Как вы могли бы упростить свою жизнь и сосредоточиться на самом важном?
Что вызывает у вас стресс?
Что делает вашу жизнь проще?
Как часто вы делитесь чем-то, не ожидая получить что-то в ответ?
Каков главный вызов в вашей жизни?
Что самое главное для вас в жизни? Уделяете ли вы этому достаточно времени?
Если бы вы могли отправить всему миру послание, что бы вы сказали за 30 секунд?
О чем вы никому не рассказываете и очень сожалеете об этом?
Когда вы в последний раз попробовали что-то новое?
Боитесь ли вы выражать собственное мнение?
Не слишком ли часто вы поддаетесь на уговоры других, а потом чувствуете обиду и сожаление?
Держитесь ли вы за что-то, что нужно оставить позади?
Как часто вы позволяете своим страхам удержать вас от действий?
Помогают ли люди в вашей жизни вам проявить себя с лучшей стороны?
Как часто вы отделываетесь от других оправданиями?
Какую ошибку вы больше никогда не повторите?
Что хуже — потерпеть неудачу или вовсе не пробовать?
Что больше помогло вашему личному росту — вызовы и испытания или приятные и уютные мгновения жизни?
Если бы вы могли сделать так, чтобы в вашей жизни больше не было вызовов и препятствий, согласились бы вы на это?
Что стоит между вами и вашей самой главной целью? Дайте ответ одним словом.
Как часто вы ложитесь спать с ощущением злобы или гнева?
Плохо ли красть, чтобы накормить голодного ребенка?
Если бы вы уделяли больше внимания грустным аспектам жизни, испытывали бы вы больше внутренних конфликтов?
Если на ошибках учатся, почему так плохо терпеть поражение?
Чему в жизни вы могли бы уделять больше внимания?
Почему мы больше всего думаем о других людях, когда их нет рядом?
Что это значит — выжать из вашей жизни максимум?
В чем вы сдались, опустили руки?
Сколько людей вы действительно любите и что вы делаете для них?
Достаточно ли вы задаете вопросов, или вы счастливы и тем, что и так уже знаете?
Что вы делали в последний раз, когда потеряли счет времени?
Будете ли вы счастливы, если вам больше не придется работать?
Если бы вы могли попросить об исполнении одного желания, каким бы оно было?
Что вдохновляет вас в жизни?
Без чего вы больше всего не можете жить?
Что вам нравится делать снова и снова?
Когда вы в последний раз смеялись до боли в животе?
Что мешает вам жить той жизнью, какой вы хотите жить? '''.split('\n')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Вопрос":
        bot.send_message(message.from_user.id, random.choice(d))
    else:
        keyboard = telebot.types.InlineKeyboardMarkup();  # наша клавиатура
        key_yes = telebot.types.InlineKeyboardButton(text='Да', callback_data='yes');  # кнопка «Да»
        keyboard.add(key_yes)
        bot.send_message(message.from_user.id, "Хочешь вопрос?", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        keyboard = telebot.types.InlineKeyboardMarkup();  # наша клавиатура
        key_yes = telebot.types.InlineKeyboardButton(text='еще', callback_data='yes');  # кнопка «Да»
        keyboard.add(key_yes)
        bot.send_message(call.message.chat.id, random.choice(d), reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)