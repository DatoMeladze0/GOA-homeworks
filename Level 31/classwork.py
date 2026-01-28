string = "StRing1 string2 string3"
# 1)
print(string.upper())
# 2)
print(string.lower())
# 3)
print(string.capitalize())
# 4)
print(string.title())
# 5)
print(string.find("2"))
print(string.find("ing", 10))
print(string.find("string4"))

#find() ფუნქცია მიუთითებს კონკრეტული სიმბოლოს ინდექსს string-ში. თუ მივუთითებთ ისეთ სიმბოლოს, რომელიც არაერთხელ მეორდება, მაშინ ფუნქცია გამოიტანს უმცირეს ინდექსზე მყოფ 
# მნიშვნელობას ამ სიმბოლოთი. ასევე შეგვიძლია მივუთითოთ მეორე არგუმენტი თუ საიდან დაიწყოს ათვლა იმ შემთხვევაში თუ არ გვინდა რომ გამოვიტანოთ პირველივე შემხვედრი ეს სიმბოლო.