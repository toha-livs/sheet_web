import gspread
from oauth2client.client import OAuth2WebServerFlow


flow = OAuth2WebServerFlow(client_id='218841006699-5bb07b75p44uaqcvrm2to4sg44h5vjn2.apps.googleusercontent.com',
                           client_secret='IT7vC8UOpKjIBR_WCVjpEZ6w',
                           scope='https://www.googleapis.com/auth/calendar',
                           redirect_uri='https://docs.google.com/spreadsheets/d/1NH6MN8TOdOC8ujc2mwidtNTlgsW12y2pxjb1Cgo4kT4/edit#gid=1003512965')






def gogo():
    #g = 0
    #info = ['фамилия', 'имя', 'отчество', 'год рождения', 'статус', 'дата регистрации', 'город']
    #scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    #credentials = ServiceAccountCredentials.from_json_keyfile_name('sheets-5a6614c399fb.json', scope)
    #gc = gspread.authorize(credentials)
    wks = flow.open('КопияSS').sheet1
    #x = wks.row_values(go)
    #s = {info[0]: x[0],
     #    info[1]: x[1],
     #    info[2]: x[2],
     #    info[3]: x[3],
     #    info[4]: x[4],
     #    info[5]: x[5],
     #    info[6]: x[6]}
    # for i in wks.row_values(4):
    #     n = {info[g]: i}
    #     g += 1
    #     r.append(n)
    #return s
    return wks.get_all_rows()


if __name__ == '__main__':
    print(gogo())
    # print(are())

# wks.append_row(['sdjknsfl', 'adijaskdka', 'aujksnad', 'ajskdjas'])

# wks.update_cell(3, 5, 'не прошел')