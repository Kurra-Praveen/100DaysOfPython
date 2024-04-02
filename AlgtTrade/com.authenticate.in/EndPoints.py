import MyUtils

BASE_URL: str = "apiconnect.angelbroking.com"
LOGIN_ENDPOINT: str = "/rest/auth/angelbroking/user/v1/loginByPassword"
PROFILE_ENDPOINT: str = "/rest/secure/angelbroking/user/v1/getProfile"
FUNDS_ENDPOINT: str = "/rest/secure/angelbroking/user/v1/getRMS"
LOGOUT_ENDPOINT: str = "/rest/secure/angelbroking/user/v1/logout"
HOLDINGS_ENDPOINT: str = "/rest/secure/angelbroking/portfolio/v1/getHolding"
HISTORICAL_ENDPOINT: str = "/rest/secure/angelbroking/historical/v1/getCandleData"


def getHeaders():
    headers = {
        'Authorization': MyUtils.getValue("AUTHORIZATION_TOKEN"),
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-UserType': 'USER',
        'X-SourceID': 'WEB',
        'X-ClientLocalIP': MyUtils.getValue("CLIENT_LOCAL_IP"),
        'X-ClientPublicIP': MyUtils.getValue("CLIENT_PUBLIC_IP"),
        'X-MACAddress': MyUtils.getValue("MAC_ADDRESS"),
        'X-PrivateKey': MyUtils.getValue("api_key")
    }
    return headers
