from __future__ import print_function
from django.shortcuts import render, redirect
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login


SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(
        'client_secret_218841006699-5a5vh0bg9l86hlf2ud0o3s6nnhr807jf.apps.googleusercontent.com.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))
SPREADSHEET_ID = '1NH6MN8TOdOC8ujc2mwidtNTlgsW12y2pxjb1Cgo4kT4'


def get_all_rows():             # получить все строки
    all = []
    count = 0
    RANGE_NAME = 'Ответы на форму (1)!A2:AN'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        for row in values:
            count += 1
            # Print columns A and E, which correspond to indices 0 and 4.
            inis = '{} {} {}'.format(row[1], row[2], row[3])
            time = row[0]
            try:
                city = row[38]
            except IndexError:
                city = 'пусто'
            try:
                status = row[39]
            except IndexError:
                status = 'пусто'
            g = {'time': time, 'name': inis, 'id': str(count), 'status': status, 'city': city}
            all.append(g)
            all.reverse()
    return all


def get_row(a):             # получить нужную строку со всеми данными в ключе [..., ..., ...]
    a += 1
    di_all = {}
    count = 0
    RANGE_NAME = 'Ответы на форму (1)!A{0}:AN{0}'.format(a)
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', {})
    if not values:
        print('No data found.')
    else:
        for i in values[0]:
            count += 1
            if i == '':
                i = '-'
            di_all[str(count)] = i
    return di_all


def update_cell(a, b, c):
    print(a)
    print(b)
    print(c)
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=SPREADSHEET_ID, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Ответы на форму (1)!{}{}".format(a, int(b) + 1),
             "majorDimension": "ROWS",
             # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
             "values": [[c]]}]}).execute()
    return {}


def logout_to(request):
    logout(request)
    return redirect('log_in')


def log_in(request):
    if request.user.is_authenticated:
        return redirect('all_all')
    else:
        if request.method == 'GET':
            return render(request, 'log_in.html')
        elif request.method == 'POST':
            name = request.POST.get('Login')
            password = request.POST.get('Password')
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('all_all')
            else:
                context = {'error': 'неправельный логин или пароль'}
                return render(request, 'log_in.html', context)




def all_all(request):               # получить все строки из таблицы, в ключе [{},{},{}, ...]
    if request.user.is_authenticated:
        if request.method == "GET":
            all_row = get_all_rows()
            context = {'posts': all_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":          # при репосте отправляеться на заданную страницу по имени
            city = request.POST.get('город')
            status = request.POST.get('статус')
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def all_schedule(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == '(Запланирован на СБ':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def all_directed(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == 'Направлен СБ':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def all_pass(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == 'Одобрен СБ':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def all_reject(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == 'Отклонен СБ':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def all_reinviw(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == 'Дополнительная проверка СБ':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def zt_all(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['city'] == 'Житомир':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def zt_schedule(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == '(Запланирован на СБ' and i['city'] == 'Житомир':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def zt_directed(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == 'Направлен СБ' and i['city'] == 'Житомир':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')

def zt_pass(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == 'Одобрен СБ' and i['city'] == 'Житомир':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def zt_reject(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == 'Отклонен СБ' and i['city'] == 'Житомир':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def zt_reinviw(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == 'прошел' and i['city'] == 'Житомир':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def chr_all(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['city'] == 'Чернигов':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def chr_schedule(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == '(Запланирован на СБ' and i['city'] == 'Чернигов':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def chr_directed(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == 'Направлен СБ' and i['city'] == 'Чернигов':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def chr_pass(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == 'Одобрен СБ' and i['city'] == 'Чернигов':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def chr_reject(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == 'Отклонен СБ' and i['city'] == 'Чернигов':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def chr_reinviw(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            f_row = []
            row = get_all_rows()
            for i in row:
                if i['status'] == 'не прошел' and i['city'] == 'Чернигов':
                    f_row.append(i)
            context = {'posts': f_row}
            return render(request, 'home.html', context)
        elif request.method == "POST":
            city = request.POST.get('город')
            status = request.POST.get('статус')
            print(city + '_' + status)
            return redirect(city + '_' + status)
    else:
        return redirect('log_in')


def user_info(request, go, repage):
    if request.user.is_authenticated:
        repage = repage * -1
        if request.method == "GET":
            row = get_row(go)
            context = {'info': row, 'repage': repage, 'go': go}
            return render(request, 'info.html', context)
        elif request.method == "POST":
            name_info = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                         'H', 'I', 'J', 'K', 'L', 'M',
                         'N', 'O', 'P', 'Q', 'R',
                         'S', 'T', 'U', 'V', 'W',
                         'X', 'Y', 'Z', 'AA', 'AB', 'AC',
                         'AD', 'AE', 'AF', 'AG', 'AH', 'AI',
                         'AJ', 'AK', 'AL', 'AM', 'AN']
            for i in name_info:
                if request.POST.get(i) != None:
                    print('commit important info')
                    print(request.POST.get(i))
                    update_cell(i, go, request.POST.get(i))
                else:
                    pass
            print(request.POST.get(i), i)
            row = get_row(go)
            repage -= 1
            context = {'info': row, 'repage': repage, 'go': go}
            return render(request, 'info.html', context)
    else:
        return redirect('log_in')


if __name__ == '__main__':
    update_cell('E', 8, 'збс я обновил все')
    print('good')