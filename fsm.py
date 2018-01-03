from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def where_to_go(self, update):
        text = update.message.text
        return text.lower() == 'hi,我最近想出國玩'

    def is_going_to_europe(self, update):
        text = update.message.text
        return text.lower() == '歐洲?'

    def is_going_to_asia(self, update):
        text = update.message.text
        return text.lower() == '亞洲?'

    def is_going_to_northamerica(self, update):
        text = update.message.text
        return text.lower() == '美洲?'

    def is_going_to_england(self, update):
        text = update.message.text
        return text.lower() == '那就去英國玩吧'

    def is_going_to_taiwan(self, update):
        text = update.message.text
        return text.lower() == '那就去台灣玩吧'

    def is_going_to_usa(self, update):
        text = update.message.text
        return text.lower() == '那就去美國玩吧'

    def is_going_to_bigben(self, update):
        text = update.message.text
        return text.lower() == '倫敦的大笨鐘!'

    def is_going_to_mount_ali(self, update):
        text = update.message.text
        return text.lower() == '阿里山!'

    def is_going_to_statue_of_liberty(self, update):
        text = update.message.text
        return text.lower() == '紐約的自由女神像!'


    def on_enter_user(self, update):
        update.message.reply_text("Hello,你最近想去哪裡玩?")

    def on_exit_user(self, update):
        print('88')

    def on_enter_europe(self, update):
        update.message.reply_text("那英國是個不錯的選擇!")
    
    def on_exit_europe(self, update):
        print('Leaving europe')

    def on_enter_asia(self, update):
        update.message.reply_text("那台灣是個不錯的選擇!")

    def on_exit_asia(self, update):
        print('Leaving asia')

    def on_enter_northamerica(self, update):
        update.message.reply_text("那美國是個不錯的選擇!")

    def on_exit_northamerica(self, update):
        print('Leaving northamerica')

    def on_enter_england(self, update):
        update.message.reply_text("有心目中必去的英國景點嗎?")

    def on_exit_england(self, update):
        print('Leaving england')

    def on_enter_taiwan(self, update):
        update.message.reply_text("有心目中必去的台灣景點嗎?")

    def on_exit_taiwan(self, update):
        print('Leaving taiwan')

    def on_enter_usa(self, update):
        update.message.reply_text("有心目中必去的美國景點嗎?")

    def on_exit_usa(self, update):
        print('Leaving usa')

    def on_enter_bigben(self, update):
        update.message.reply_text("ok,馬上為你安排去英國的行程")

    def on_exit_bigben(self, update):
        print('Leaving bigben')

    def on_enter_mount_ali(self, update):
        update.message.reply_text("ok,馬上為你安排去台灣的行程")

    def on_exit_mount_ali(self, update):
        print('Leaving mount_ali')

    def on_enter_statue_of_liberty(self, update):
        update.message.reply_text("ok,馬上為你安排去美國的行程")

    def on_exit_statue_of_liberty(self, update):
        print('Leaving statue_of_liberty')