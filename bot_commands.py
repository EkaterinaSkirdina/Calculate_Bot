from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def log(data):
    with open('logger.txt', 'a+', encoding='utf-8') as file:
        file.write(f'{data}')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!\
         Я Бот калькулятор. Для рассчетов введи команду /calc')



def calc(my_list):

    while '*' in my_list or '/' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '*':
                result = my_list.pop(i+1) * my_list.pop(i-1)
                my_list[i-1] = result
                break
            elif my_list[i] == '/':
                result = my_list.pop(i-1) / my_list.pop(i)
                my_list[i-1] = result
                break

    while '+' in my_list or '-' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '-':
                result = my_list.pop(i-1) - my_list.pop(i)
                my_list[i-1] = result
                break
            elif my_list[i] == '+':
                result = my_list.pop(i+1) + my_list.pop(i-1)
                my_list[i-1] = result
                break
   
    return my_list

async def calculate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):  
    await update.message.reply_text(f'Введите выражение')
   
async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):  
    s = update.message.text
    log(f'Введено выражение {s};')
    print(s)
    old_list = s.replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')\
        .replace('(', '( ')\
        .replace(')', ' )').split()
    old_list = [int(elem) if elem.isdigit() else elem for elem in old_list]
   
    while '(' in old_list:
        first_i = len(old_list) - old_list[::-1].index('(') - 1
        second_i = first_i + old_list[first_i + 1:].index(')') + 1

        old_list = old_list[:first_i] + calc(old_list[first_i + 1:second_i]) + old_list[second_i+1:]
    
    old_list = calc(old_list)
    await update.message.reply_text(*old_list)
    log(f'Получен результат {old_list}\n')