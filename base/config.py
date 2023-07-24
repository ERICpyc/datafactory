import logging

def logger():
    logger = logging.getLogger()
    if len(logger.handlers) == 0:  # 只添加一个输出到控制台的handler
        logger.setLevel('DEBUG')
        BASIC_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"
        DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)
        chlr = logging.StreamHandler()  # 输出到控制台的handler
        chlr.setFormatter(formatter)
        chlr.setLevel('INFO')  # 也可以不设置，不设置就默认用logger的level
        logger.addHandler(chlr)
    return logger

vmp_tcookie = 'appid=xp_entrance; uid=2000002; cookieVersion=; userName=%E7%AE%A1%E7%90%86%E5%91%98; oauthCookie=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; freshTime=1690188454617; deviceId=59fa5d477725cd1cef825c3cdcfb9f1e'
vmp_pcookie = 'deviceId=23a8f1bc792a26e1103bdaae24e46a78; 84eafaa69d23412f_gdp_user_key=; 84eafaa69d23412f_gdp_cs1=gioenc-qdofxb0; 84eafaa69d23412f_gdp_gio_id=gioenc-qdofxb0; gdp_user_id=gioenc-1gc31608%2Cga5a%2C5766%2C8507%2Cd67g59e49979; 84eafaa69d23412f_gdp_session_id_sent=f3d33fad-053c-404c-a654-b9411f7034e7; 84eafaa69d23412f_gdp_sequence_ids={%22globalKey%22:30%2C%22VISIT%22:5%2C%22PAGE%22:4%2C%22LOGIN_USER_ATTRIBUTES%22:2%2C%22CUSTOM%22:8%2C%22VIEW_CHANGE%22:2%2C%22VIEW_CLICK%22:16}; appid=xp_entrance; cookieVersion=; freshTime=1690184555814; uid=2000002; userName=%E6%B5%8B%E8%AF%95; oauthCookie=Wn2lfkdvx1ubY40/DV/SNeMW65CVKwZJZK92Cuck91AavJcBkxmgp27LdrJJrmx+ibHBdv6RN1jNREMVkxm89ytVbo45Q4cn0Aj2q8ceEx6pSK1j4hay0UYNn8XzwvFiGtuG84UWlg+ZJvrSWQHPF7iPmQuLU1OOd54SnUccn5ldGGgtsEOB1jrXFK/sExHDj3swa3GjCleSfzrWCwEXto2ukr5jzusHa+/bc5XgbqV0HRXwQ0X6PjnGzGWjeUq0PFiNNsGFka95YIZZ9BjgONm9OHzEpEOPHIq+Bm9JZ3135YjVlRD9zUwKQBiOD3qZONPRTEzdBcliOAF4ynvP9308ec+tZZ28PByWFRTPUYXGkPJnISpo33rEOG1ydTct0WSexKLC3qVP/QCsrcgBwsHHjxA/TAvSW27uCcO5ItRP4NFCUNT6mxeowPwFw4sJNTH8H2+WHtU7FD/be2cxV83uQd75ks0vr/HPldbuCQg3KRQFacagL/gYOzA54gzyhp6LZPOIuaKjHC+Hh2NJ5ZS+vVL8GfIB8sM1MHvIkwH98oObiNv9k7K6Jb1zSxNVYBPtKvOm7NB5ShIp7gRbQBLJW7lQkvLzl/psUz0OdNyyTB0WYyFTY432ULGYUPjEObE6y0IDp4/krbH6lQ47ryEMszrh0+6Toto5spzo+24MghCIoAgK8LE1dhpZJqAocRx7j0JqvyktStduHybHgMon1KkrII78X6LYM9Z1p5WS8mRdEQuTTATxkMs/BcGXLt1GEMkNPDFp5KER9Sk/UtvYHlhYTeh6PMnTokG4IbQLL+v3sdOLf+ZSjPYy511/pOWQHf8U6FwWP+Xqlw6fF0N1zi2t9MS5h0lTRQeD66HwRV9hbu/rNTeeQDo9eftWIPSskc0fpSfngpkIwjysFHaQDHhwoo9B7/gWhroJYckq5juHXLlnR5n4znIOpiXlkaJB+KbvZepeTPmx4nd5mlw3Xmo7HZi9GtEGPGeBUlnxgsYeFM+efe7ZvsO7+8zZZKggzw6GjZg1cq3naRqFijpbPNYPiP3Oqw8OC8rQso5B7tRvF900gKL4/GrdKNzVGhpm2DTTeHcIJyARaVfXmC92aIHoZIFV7psuX0H42zmEkLh3Hi87iO4l1uAMrNYVZ1j308Mm7S+OjaXuMyglRYWxKWpC2LL/HGJ/rz4miAxiykV0Ll3ql+eGyUKszzcIefSTe+TPZsgv3C/Cdu4WtR8xbU5JrRv4zI0OFS4XhIBdZ2Yk19LopuipggimgYIrUwfqgFCcb5iVV6hzCd7FEua5UdkAMC00H9vrNdYe3Ohdecit9dRwQ5bUf2gS7h2t+u6ugHmiQCdk18fJsE4tNx53oIMSuQ7qIOL6ihsu8Nfl18BNx1TCim119Rm+pLDscRgul+31mIcuvrVgs1PA28qE0wt1ByLiLF/mcts/bMiGN4ZUKQx4BgjJc/vkgdZlQ47hwzd7qCCLm16V/mZurabIgqKZ/Zkbnpg5r6rGKVE7jjN1lMqbdSRWjYfdxRJcBCSUDuKmq7iriohRMqhiFc8YCRCAf762Mku4khzBZ/P36VIrmcfHwePbr5D+XorwLY0EzYsjBN6cV8q4WN11Ti5LDQPxPH2DnGhASyXDkpg8LgUuOF51kQx9GqPqEiW9xyfBiUCUcxjlQ80yK+Si394zmcSTSGIU8ICCaiwMjVxHap+eGuC0hSrDG2G8bNlJXmODnVR3ZD10zdaqu8QL4HWzJm7ds+KWMx0QN7uV9mtoBfLV04V6U5gz0dll4siphHXepP7N+cboqQMZ+iJm10a26ESPbkHJHEceyQycFJG1YqM96hGIy3fL7IjjBWbWbzkUfitK380B10Xg+/tFa0eqKEeaS1AIGibwQsKhWLj7tDMcmeNO2d1V0gKkLMeO3bRnFoXdvHZ/AAYucTcpo/Ht9H+B7OEcUq9dC5xTvmFUWEGGJiSsf6AXBSLb4UG8gK/qVVn2UUH+ymg/aVuiIVy/ycWGOtEshvaez+d1r7SLvjyOtWDS0jTcxgetBhN6HwexrV6bJdj6UTe3EEW/4kEDWsxmMn613RGcreUHSdNJQMkXdX4gjm2aNJjjCbVY129R02GlacIgYd4YOM4CP1fV1ssp46Mp3d8hzp2psnS8yr93AiDYmkNmqX5pxqsBu0FXmZlmfgaTzEZ+pGOKfgHlLLdGyJgTwOBXFL82fHYhCIhaBQ9HuScqZ/ZApo460P6r8kdNlzF0coRdl2Ic9X8o4RZOSxNlqLLSGzyVu+o35xl+97339HjDgQd13qUHT01CbQRop2MgHE+jGuEplkxxo/hGtaSXhRXk8u1f6dbzmu+GWs7U3hOvj/Nb4fPtVYKMa0GqwUV4IHPyCD3IKHehbYFGharuPb/rBcj6Wp6DbxMuY8GSxDD2i4SzKdVhB3YXT2h9PV6pwEawCSdpgmpCyx5o35l8fKGgbocJ4cUcvbnNnCQy0Vm6gRDqEVclPpLMOJ49NHbj3dkux0J2G4IkTMkBNNwe+YwtStspmZq8R6C79MXiaKnvG5YIIKyPbKGWUhApgc9erzQhft9MAwcD3pwXp9CRbIlRab+D85Lpb2D3n7bVwYpcnzbj8wf2FC45YymS5mkVsSgiJiN30R4A80Qt/XMkmIY7T5yrngr5BDJ5u0URwfwaW0A74qzj0yM96oK99qopiaqKpq8V08sv28e5Kxn18Sj1Y5TsJHRLnIgHnqKKY7RDw7v79SYJCIisCkqj7PxSDLTHSLrsb32ycsROuGKwlJhSfAfnzNIG/TZRoDzLc9jw22oCYcQpEhdmEcIu+64Nq+ztGu66h03hK7GPYQygrrQX2x6Ah0gUMvYQTGw97AxE/hcXSzxdoCWFSo4JZ9cJboMoJl460z3u2HxdDVcvXggOyju6BHlKAJLsjaDM4lSrBQwYsyOdIqUn3J7rqbvjcwCgLiXz7sqOxAI3oWK8lvIbbSwAbUFRJOxctF0xaX3YYzzk/e4+yGO8ExYJGNKDzukm71CaB0LzfnZ0TZhmlrg1E7tfUFMUU6Kt6fUUwSW0hyXHkVqvNKs97MFFrtJFE7mLLviFy+8v4Y3DjQtkVr8AFowZ8kAIQw923WFvX6/NQB6Hb1nfouwz51b3Th7oOnhT6hnIckwRbyT/n7UFSTNKrUBSBYu5GlDGny5yeSYNRGuolnpZzSmM1inn3Az0s0H7HrIaxbjwlD8BgYwZj4dP0tEPA+xXzxrxTv//b52bqVmiTRK0QqxShlfKZuxar3TBMQ0d18FbsjPAIxK83snjhDlciSyP3WOGdoX5JxG8aCK61e12'
header_js = {"Content-Type":"application/json"}