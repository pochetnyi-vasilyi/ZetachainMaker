REF_LINK = 'https://hub.zetachain.com/xp?code=YWRkcmVzcz0weDFiMUNCOWM4Nzg5MzJCMzkxZDlBNDkyNUMyQTA3OTQ0NDVFZjIwRjcmZXhwaXJhdGlvbj0xNzEzNDg4NjAxJnI9MHgyYjczMDZkN2VmNDE1OGFmYmM0ZWY5M2UxMWJkMmM2YWZhOTQwMDEzNzAyMGYwNDM2M2M5Mjg5MzM3NTE1ODA1JnM9MHg1OTMzNzBjYTdlNWViZWIzYWIzMTJlOWFiMzk3ZGE1YWUxNDgzNzhiY2FiNDE0MTEwOWY4NGVmNWZiOTBlNjVlJnY9Mjg%3D'

# api key native.org
NATIVE_API_KEY = "26c2aba2d146068846526054af86aaf71e6c9088"

# задержки
DELAY = {
    "account": (5, 10),       # Задержка в секундах между аккаунтами
    "transaction": (20, 30),  # Задержка в секундах между транзакциями
}

# апрувы. [x,y]. х - минимальное кол-во, у - максимальное кол-во. Рандом до 10 цифр после точки
APPROVES = {
    "bnb_approve": [11, 20],  # кол-во бнб для апрува
    "stzeta_approve": [12, 20],  # кол-во stzeta для апрува
    "wzeta_approve": [12, 20],   # кол-во wzeta для апрува
    "stzeta_accumulated_approve": [12, 20],  # кол-во stzeta для апрува
    "zetaswap_wzeta_approve": [12, 20]
}

# [x,y]. х - минимальное кол-во, у - максимальное кол-во. Рандом до 10 цифр после точки
SENDS_QUESTS = {
    "send_zeta": [0.001, 0.01],         # Сколько zeta отправить самому себе?
    "send_bnb":  [0.01, 0.002],     # Сколько zeta отправить для транзакции zeta->bnb.bsc (izumi)
    "send_eth":  [0.0001, 0.0002],    # Сколько zeta отправить для транзакции zeta->eth.rth (izumi)
    "send_btc":  [0.001, 0.002],     # Сколько zeta отправить для транзакции zeta->btc.btc (izumi)
}

# Чтобы отправлять в пулы указывать True/False в use.
POOLS = {
    "send_bnb": 0.00001,       # сколько отправлять бнб в пул
    "send_zeta": 0.0001,      # сколько отправлять zeta в пул

    # range pool
    "stzeta": 0.001  #должно быть меньше zeta_to_stzeta и zeta_to_wzeta с EDDY_SWAP
}

# свап на app.eddy.finance/swap
EDDY_SWAP = {
    "zeta_to_stzeta": 0.0013,  # кол-во zeta для свапа на stzeta
    "zeta_to_wzeta": 0.01,   # кол-во zeta для свапа на wzeta, можно не больше zeta_to_stzeta
}

# минт и стейк на Accumulated finance
ACCUMULATED_FINANCE = {
    "zeta_to_stzeta": 0.0001,     # кол-во zeta для свапа на stzeta на accumulated finance
    "stzeta_to_wstzeta": 0.0001  # кол-во stzeta для свапа на wstzeta на accumulated finance, должно быть не больше zeta_to_stzeta
}

# стейк на ZetaChain
STAKE_ZETACHAIN= {
    "zeta_count": 0.0011  # кол-во zeta для стейка. минимум 0.0011
}

# свап wzeta на ETH.ETH через zetaswap. [x,y]. х - минимальное кол-во, у - максимальное кол-во. Рандом до 5 цифр после точки
ZETASWAP = {
    "wzeta_count": [0.0001, 0.0002]
}

# рпц
RPCs = {
    "zetachain": "https://zetachain-evm.blockpi.network/v1/rpc/public"  # zetachain rpc
}
