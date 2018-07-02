from django.shortcuts import render, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_all_rows():             # получить все строки
    r = []
    g = 0
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('toha-pjt-e74ea53efb7f.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open('mysheet').sheet1
    print(wks.get_all_records())
    for i in wks.get_all_records():
        g += 1
        i['id'] = str(g)
        r.append(i)
    return r


def get_row(a):             # получить нужную строку со всеми данными в ключе [..., ..., ...]
    a += 1                  #делаю +1 чтобы выбрать нужную строку (отсчет идет с названия колонки)
    g = 0
    info = ['фамилия', 'имя', 'отчество', 'год_рождения', 'статус', 'дата_регистрации', 'город']
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('toha-pjt-e74ea53efb7f.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open('mysheet').sheet1
    x = wks.row_values(a)
    s = {info[0]: x[0],
         info[1]: x[1],
         info[2]: x[2],
         info[3]: x[3],
         info[4]: x[4],
         info[5]: x[5],
         info[6]: x[6]}
    return s


def all_all(request):               # получить все строки из таблицы, в ключе [{},{},{}, ...]
    if request.method == "GET":
        all_row = get_all_rows()
        context = {'posts': all_row}
        return render(request, 'home.html', context)
    elif request.method == "POST":          # при репосте отправляеться на заданную страницу по имени
        city = request.POST.get('город')
        status = request.POST.get('статус')
        return redirect(city + '_' + status)


def all_pass(request):
    if request.method == "GET":
        f_row = []
        row = get_all_rows()
        for i in row:
            if i['статус'] == 'прошел':
                f_row.append(i)
        context = {'posts': f_row}
        return render(request, 'home.html', context)
    elif request.method == "POST":
        city = request.POST.get('город')
        status = request.POST.get('статус')
        print(city + '_' + status)
        return redirect(city + '_' + status)


def all_block(request):
    if request.method == "GET":
        f_row = []
        row = get_all_rows()
        for i in row:
            if i['статус'] == 'не прошел':
                f_row.append(i)
        context = {'posts': f_row}
        return render(request, 'home.html', context)
    elif request.method == "POST":
        city = request.POST.get('город')
        status = request.POST.get('статус')
        print(city + '_' + status)
        return redirect(city + '_' + status)


def zt_all(request):
    if request.method == "GET":
        f_row = []
        row = get_all_rows()
        for i in row:
            if i['город'] == 'житомир':
                f_row.append(i)
        context = {'posts': f_row}
        return render(request, 'home.html', context)
    elif request.method == "POST":
        city = request.POST.get('город')
        status = request.POST.get('статус')
        print(city + '_' + status)
        return redirect(city + '_' + status)


def zt_pass(request):
    if request.method == "GET":
        f_row = []
        row = get_all_rows()
        for i in row:
            if i['статус'] == 'прошел' and i['город'] == 'житомир':
                f_row.append(i)
        context = {'posts': f_row}
        return render(request, 'home.html', context)
    elif request.method == "POST":
        city = request.POST.get('город')
        status = request.POST.get('статус')
        print(city + '_' + status)
        return redirect(city + '_' + status)


def zt_block(request):
    if request.method == "GET":
        f_row = []
        row = get_all_rows()
        for i in row:
            if i['статус'] == 'не прошел' and i['город'] == 'житомир':
                f_row.append(i)
        context = {'posts': f_row}
        return render(request, 'home.html', context)
    elif request.method == "POST":
        city = request.POST.get('город')
        status = request.POST.get('статус')
        print(city + '_' + status)
        return redirect(city + '_' + status)


def chr_all(request):
    if request.method == "GET":
        f_row = []
        row = get_all_rows()
        for i in row:
            if i['город'] == 'чернигов':
                f_row.append(i)
        context = {'posts': f_row}
        return render(request, 'home.html', context)
    elif request.method == "POST":
        city = request.POST.get('город')
        status = request.POST.get('статус')
        print(city + '_' + status)
        return redirect(city + '_' + status)


def chr_pass(request):
    if request.method == "GET":
        f_row = []
        row = get_all_rows()
        for i in row:
            if i['статус'] == 'прошел' and i['город'] == 'чернигов':
                f_row.append(i)
        context = {'posts': f_row}
        return render(request, 'home.html', context)
    elif request.method == "POST":
        city = request.POST.get('город')
        status = request.POST.get('статус')
        print(city + '_' + status)
        return redirect(city + '_' + status)


def chr_block(request):
    if request.method == "GET":
        f_row = []
        row = get_all_rows()
        for i in row:
            if i['статус'] == 'не прошел' and i['город'] == 'чернигов':
                f_row.append(i)
        context = {'posts': f_row}
        return render(request, 'home.html', context)
    elif request.method == "POST":
        city = request.POST.get('город')
        status = request.POST.get('статус')
        print(city + '_' + status)
        return redirect(city + '_' + status)


def user_info(request, go):
    if request.method == "GET":
        row = get_row(go)
        return render(request, 'info.html', row)