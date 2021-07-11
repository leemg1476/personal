from pywinauto import Application
from pywinauto import keyboard

app = Application(backend='uia')
app.connect(title_re='.*Edge.*',found_index=0)
window = app.top_window()
window.set_focus()

# print(window.print_control_identifiers())
# for i in range(100):
#     wins = window.child_window(auto_id='res').child_window(control_type='Hyperlink',found_index=i)
#     print(wins.print_control_identifiers())
#     if i == 3:
#         wins.click_input()
# for i in range(5):
#
#     wins = window.child_window(auto_id='video-title',found_index=i)
#     print(wins.print_control_identifiers())
#     if i == 4:
#         wins.click_input()
# wins = window.child_window(title_re='.*아이유.*', found_index=0)
# wins.click_input()
#
#
# all_del='+{UP}{DEL}'
# s='hihi'
# text = window.child_window(control_type='ComboBox',auto_id='search')
# keyboard.send_keys(all_del)
# keyboard.send_keys(s)
# #