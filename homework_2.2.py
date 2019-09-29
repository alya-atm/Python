def distance(n):
    all_way=0
    dist_home=0
    for i in range(1,n+1):
        all_way=all_way+1/i
        dist_home=dist_home+(-1)**(i+1)/i
    print('Пройденный путь',all_way,'км')
    print('Расстояние до дома км',dist_home,'км')
distance(10)