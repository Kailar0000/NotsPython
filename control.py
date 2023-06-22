import view as f
import ui


def start():
    while True:
        input_from_user = ''
        ui.menu()
        input_from_user = input().strip()
        match input_from_user:
            case '1':
                f.show('all')
            case '2':
                f.add()
            case '3':
                f.show('all')
                f.id_edit_del_show('del')
            case '4':
                f.show('all')
                f.id_edit_del_show('edit')
            case '5':
                f.show('date')
            case '6':
                f.show('id')
                f.id_edit_del_show('show')
            case '7':
                ui.goodbuy()
                break