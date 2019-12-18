import re
'''file = open("New_python_text.txt","r")
text = file.readlines()

x = 0
for i in range(150):
    if i == 108:
        x = x-1
        result = re.sub(r'<question>  ','',text[x])
        text[x] = result
        x = x+7
    else:
        result = re.sub(r'<question> ', '', text[x])
        text[x] = result
        x=x+7

file = open("New_python_text.txt","w+")
file.writelines(text)
file.close()'''

'''
for i in text:
    if re.findall(r'<question>',i):
        result = re.sub(r'<question> \w+. ','',i)
        test_text = result
    elif re.findall(r'<variant>',i):
        result = re.sub(r'<variant> ','',i)
        test_text = test_text + result
    else:
        test_question.append(test_text)
        test_text = '' 
'''

'''
pattern = re.compile(r'<question> \w+. |<variant> ')
result = pattern.split(test_question[0])
for i in range(1,len(result)):
        print(result[i].rstrip())
'''

variant = '<variant> Джангода  HTML, JSON, XML сияқты форматтармен жұмыс істейді.\n<variant> Джангоға көп веб-түйіндерді қосуға болады\n<variant> Windows, Linux и MacOS сияқты әртүрлі платформаларға ауысуы\n<variant> Джанго кейбір қауіпсіздік шараларын қолданады\n<variant> Джангода көптеген қосымша пакеттер бар'
result = re.split(r'\n<variant>\s+',variant)
print(result[0])