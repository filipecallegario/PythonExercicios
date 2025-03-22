

def voto(a):
    from datetime import date
    idade = date.today().year - a
    if idade < 16:
        return f'Com {idade}. NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade}. VOTO OPCIONAL!'
    else:
        return f'Com {idade}. VOTO OBRIGATÓRIO!'

ano = int(input('Em que ano nasceu? '))
print(voto(ano))