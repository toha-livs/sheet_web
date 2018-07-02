import gspread
from oauth2client.service_account import ServiceAccountCredentials
r = []


def are():
    d = []
    n = [3, 5, 6]
    x = [4, 7, 4]
    for i, s in n, x:
        print(i, r)
        d.append(i + s)
    return d


def gogo():
    g = 0
    info = ['фамилия', 'имя', 'отчество', 'год рождения', 'статус', 'дата регистрации', 'город']
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('toha-pjt-e74ea53efb7f.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open('mysheet').sheet1
    x = wks.row_values(go)
    s = {info[0]: x[0],
         info[1]: x[1],
         info[2]: x[2],
         info[3]: x[3],
         info[4]: x[4],
         info[5]: x[5],
         info[6]: x[6]}
    # for i in wks.row_values(4):
    #     n = {info[g]: i}
    #     g += 1
    #     r.append(n)
    return s
    # return wks.get_row(4)


if __name__ == '__main__':
    print(gogo())
    # print(are())

# wks.append_row(['sdjknsfl', 'adijaskdka', 'aujksnad', 'ajskdjas'])

# wks.update_cell(3, 5, 'не прошел')