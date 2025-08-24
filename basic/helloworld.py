fruits = ['apple', 'banana', 'orange']

for fruit in fruits[:]:
    print(f'あなたの好きなフルーツは{fruit}ですか？')
    user = input('(y/n): ')
    if user == 'y':
        fruits.remove(fruit)
        print(f'{fruit}を差し上げます。')
    else:
        continue


print(fruits)
