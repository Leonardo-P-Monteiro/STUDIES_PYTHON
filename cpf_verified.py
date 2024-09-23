# FIRST DIGIT
cpf = input('Provide a CPF: ').strip().replace('.', '').replace('-', '')
cpf_nine = cpf[0:9]
multiplier = 10
total_first_number = 0
cpf_nine_number = 0


for i in cpf_nine:

    if multiplier >= 2:
        total_first_number += int(i)*multiplier
        multiplier -= 1
    
total_first_number = (total_first_number * 10) % 11

if total_first_number > 9:
    cpf_nine_number = 0
else:
    cpf_nine_number = total_first_number

# SECOND DIGIT

cpf_ten = cpf[0:10]
multiplier = 11
total_second_number = 0
cpf_eleven_number = None

for i in cpf_ten:

    if multiplier >= 2:
        total_second_number += int(i)*multiplier
        multiplier -= 1
    

total_second_number = (total_second_number * 10) % 11

if total_second_number > 9:
    cpf_eleven_number = 0
else:
    cpf_eleven_number = total_second_number

cpf_attached = cpf_ten + str(cpf_eleven_number)

verifier = 'This CPF is OK.' if cpf_attached == cpf else 'This CPF is not '\
'correct.'


print(verifier)