from ClientInfo import Client

# client = Client()
# MyProfileInfo = client.getProfileInfo()
# print(MyProfileInfo)
# historicData = {
#     "exchange": "NSE",
#     "symboltoken": "15083",
#     "interval": "FIFTEEN_MINUTE",
#     "fromdate": "2023-09-11 09:15",
#     "todate": "2023-09-11 09:45"
# }
#
# data = client.getHistoricData(historicData)
# print(data)
# logiut = client.logOut()
# print(logiut)

d = {'status': True, 'message': 'SUCCESS', 'errorcode': '',
     'data': [['2023-09-11T09:15:00+05:30', 840.0, 846.35, 836.4, 842.55, 1240205],
              ['2023-09-11T09:30:00+05:30', 842.75, 847.9, 841.35, 847.9, 495736],
              ['2023-09-11T09:45:00+05:30', 847.7, 857.5, 847.7, 856.4, 1396051]]}

original_data = d["data"]
open_price = original_data[0][1]
closed_price = original_data[-1][-2]
print(open_price, closed_price)
