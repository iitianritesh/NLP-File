
import re
chat1 = 'codebasics: you ask to lot of questions  1235434347, abcA@xyz.com,9334538905'
chat2 = 'codebasics: here it is (123)-133-4544, abc@xyz.com'
chat3 = 'codebasics: yes, phone:1235434347 email:abc@gmail.com'
pattern = '[a-z0-9A-Z_]*@[a-z0-9A-Z]*\.[a-z0-9A-Z]*'
matches = re. findall(pattern, chat2)
print(matches)