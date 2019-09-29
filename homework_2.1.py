def check_text(text):
    text=text.lower()
    error=0
    if text.count('ш')==0 and text.count('ж')==0 and text.count('ч')==0 and  text.count('щ')==0:
        print('Буквосочетания жи, ши, ча и ща отстутствуют')
    else:
        for i in range(len(text)-1):
            if text[i]=='ж' and text[i+1]=='ы':
                error=+1
                print('Ошибка в написании буквосочетания ЖИ')
            elif text[i]=='ш'  and text[i+1]=='ы':
                error=+1
                print('Ошибка в написании буквосочетания ШИ')
            elif text[i]=='ч' and  text[i+1]=='я':
                error=+1
                print('Ошибка в написании буквосочетания ЧА')
            elif text[i]=='щ' and text[i+1]=='я':
                error=+1
                print('Ошибка в написании буквосочетания ЩА')
    if error ==0:
        print('Ошибок нет')
text=str(input('Введите текст:'))
check_text(text)
