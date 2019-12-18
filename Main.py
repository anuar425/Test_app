import re,codecs,random

test_question = []
test_variant = []
file = codecs.open("New_python_text.txt","r",'utf_8_sig')
text = file.readlines()
text_question = ''
text_variant = ''
for i in text:
    if re.findall(r'<question>',i):
        text_question = i
    elif re.findall(r'<variant>',i):
        text_variant = text_variant + i
    else:
        test_question.append(text_question.rstrip())
        test_variant.append(text_variant.rstrip())
        text_question = ''
        text_variant = ''

for i in range(len(test_question)):
    test_question[i] = re.sub(r'<question>+[\s\d]+[.\s]+','',test_question[i])
    variant = re.split(r'\n<variant>\s+',test_variant[i])
    for x in range(len(variant)):
        variant[x] = re.sub(r'<variant>\s+','',variant[x])
    test_variant[i] = variant

rand_var = random.sample(range(0,len(test_variant[0])),len(test_variant[0]))
print(rand_var)

print(test_question[0])
for i in range(len(test_variant[0])):
    print(test_variant[0][rand_var[i]])










'''for i in range(len(test_question)):
    result = re.split(r'<question> \w+. \b',test_question[i])
    for x in range(len(result)):
        print(result[x].rstrip())'''



















