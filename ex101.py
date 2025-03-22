def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade}: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade}: VOTO OPCIONAL!'
    elif 18 <= idade < 65:
        return f'Com {idade}: VOTO OBRIGATÓRIO!'



ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))