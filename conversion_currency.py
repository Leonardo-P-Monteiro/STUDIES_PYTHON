import locale

# Define a localidade para português do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

valor = 1234.56
moeda_formatada = locale.currency(valor, grouping=True)
print(moeda_formatada)  # Saída: R$ 1.234,56