from fake_useragent import UserAgent


cookies = {
    '__ddg9_': '85.143.146.47',
    '__ddg1_': 'M18Ky98Fk3PMNNPE1wfR',
    'ab2_90': 'ab2_90old90',
    'ab2_33': 'ab2_33new33',
    'ab2_50': '44',
    'ab3_75': 'ab3_75new20',
    'ab3_33': 'ab3_33new17',
    'ab3_20': 'ab3_20_20_0',
    'web_proxy': 'old',
    'cc': '0',
    'uid': 'CtIBN2g/LcwZXwFtC4ptAg==',
    '_gid': 'GA1.2.274123874.1748970984',
    'uxs_uid': '79a43360-409e-11f0-b484-e7ebe8e552fa',
    '_sp_ses.2b21': '*',
    'dmuid': '968f4249-070e-4916-ad2b-09d2d3dc2810',
    'rsid': 'b9bfc2bf9b759f0207097815a05666bab73d12b4',
    'JSESSIONID': '9f256fa3-6a3b-4688-a545-2a55b6e3acce',
    'detmir-cart': 'e7a7553f-7c0d-4eba-b0d6-430a18138815',
    'detmir-buy_now-cart': 'b04307cc-6f54-494b-aec0-824ef6e18fa3',
    'auid': 'e579aea4-9770-4594-bd47-3883c85a914e',
    'srv_id': 'cubic-front11-prod',
    '_gcl_au': '1.1.423201650.1748970984',
    'geoCityDMCode': '',
    'oneTimeSessionId': 'd070705e-76eb-479f-b7b7-3fe0bd8d228d',
    '_ym_uid': '1748970986114862546',
    '_ym_d': '1748970986',
    '_ym_isad': '1',
    'geoCityDMIso': 'RU-SPE',
    'dm_s': 'L-9f256fa3-6a3b-4688-a545-2a55b6e3acce|kHe7a7553f-7c0d-4eba-b0d6-430a18138815|Vje579aea4-9770-4594-bd47-3883c85a914e|gqcubic-front11-prod|qae7a7553f-7c0d-4eba-b0d6-430a18138815|-N1748970984028|RK1748971005957|XJb9bfc2bf9b759f0207097815a05666bab73d12b4|tUb04307cc-6f54-494b-aec0-824ef6e18fa3#aOUi1Tn00oqkky9OhTN_rQhC6FO8oA_s52ugVRbeXPU',
    'geoCityDM': '%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%20%D0%B8%20%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C',
    'cto_bundle': 'ynibX19RcE5ZeiUyQmM5SDlCbCUyRml0VEFtSXdDalRjdlFzaXVob3piT0t3Nkh4dVRrUnh5Y2ZyQkVETEdYRmxuUnd4JTJGdE9HNXBwWndEM1FqcEs1VE9id1ZHNENKUlRyeVZlSE1veXpwcDRzSklJcmJCNFVqeGNOYlFaNm1oOE5RZ2FLUGpoSE9QRGUzSk96dVp6bjdZVTBxOElFOEElM0QlM0Q',
    'mindboxDeviceUUID': 'f9ef1fa4-f863-49c3-b9e2-2336290be3b2',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22f9ef1fa4-f863-49c3-b9e2-2336290be3b2%22%7D',
    '_gat': '1',
    '_sp_id.2b21': '560f514e-89a3-4b8d-9787-224ba07fcf6f.1748970984.1.1748972538..fce60b60-fb87-4405-a033-f9fcec2092bc..88cd4c6b-bf94-42ba-bb4c-22da65b9eb20.1748970984202.259',
    '_gat_UA-7115391-1': '1',
    '_ga_MW06XXV5JP': 'GS2.1.s1748970985$o1$g1$t1748972539$j58$l0$h0',
    '_ga': 'GA1.1.2010760760.1748970984',
    '_ga_87D5G6Z6JP': 'GS2.1.s1748970986$o1$g1$t1748972539$j48$l0$h0',
    '__ddg10_': '1748972539',
    '__ddg8_': 'zUMZfhu7CqJFaxTT',
}


def get_headers() -> dict:
    """
    Создает fake user agent, вставляет его в заголовок

    :return: словарь headers, в котором указан fake ua
    """
    ua = UserAgent()

    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'origin': 'https://www.detmir.ru',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.detmir.ru/',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': ua.random,
        'x-img-platform': 'm/1',
        'x-requested-with': 'detmir-ui-vip3'
    }
    return headers
