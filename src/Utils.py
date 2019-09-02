import telegram
from datetime import datetime, date

class Utils:

    @staticmethod
    def getChatId(bot, update):
        chatId = None
        try:
            chatId = update.message.chat_id
        except:
            chatId = update['callback_query']['message']['chat']['id']
        return chatId

    @staticmethod
    def getUsername(bot, update):
        username = None
        try:
            username = update.message.from_user.first_name + ' '
            if update.message.from_user.last_name: username += update.message.from_user.last_name
        except:
            username = update['callback_query']['message']['chat']['first_name'] + ' ' 
            if update['callback_query']['message']['chat']['last_name']: username+= update['callback_query']['message']['chat']['last_name']
        return username
    
    @staticmethod
    def getWeekNumber():
        return datetime.today().isocalendar()[1]

    @staticmethod
    def showStartMenu(bot, update):
        bot.send_message(
            chat_id = Utils.getChatId(bot, update),
            text = '*\nSelecione uma opção para continuar...*',
            parse_mode = 'Markdown',
            reply_markup = Utils.getMainMenuMarkup()
        )

    @staticmethod
    def showStartMenuInExistingMsg(bot, update):
        bot.editMessageText(
            message_id = update.callback_query.message.message_id,
            chat_id = update.callback_query.message.chat.id,
            text = '*Olá!\nSelecione uma opção para continuar...*',
            parse_mode = 'Markdown',
            reply_markup = Utils.getMainMenuMarkup()
        )

    @staticmethod
    def getMainMenuMarkup():
        keyboard = [
            [
                telegram.InlineKeyboardButton('Cardápio RU', callback_data = 'menu-ru'),
                telegram.InlineKeyboardButton('Cardápio Cantina', callback_data = 'menu-canteen')
            ],
            [
                telegram.InlineKeyboardButton('Horário ônibus', callback_data = 'bus-schedules'),
                telegram.InlineKeyboardButton('Calendário acadêmico', callback_data = 'academic-calendar')
            ],
            [
                telegram.InlineKeyboardButton('Próximos Eventos', callback_data = 'events-schedules'),
                telegram.InlineKeyboardButton('Datas Importantes', callback_data = 'academic-date')
            ],
            [
                telegram.InlineKeyboardButton('Cardápio Automático', callback_data = 'auto-menu')
            ]
        ]
        return telegram.InlineKeyboardMarkup(keyboard)