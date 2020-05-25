from random import randint
import random


def read_map():
    map = []
    with open('map.txt', 'r', encoding='utf-8') as r:
        size = int(r.readline().split('\n')[0])
        for i in range(size):
            map.append([int(x) for x in r.readline().split('\n')[0].split(' ')[:-1]])
        r.close()
    return size, map


class MonkeyOnTruck:
    
    def __init__(self, N, nCity, map):
        self.khoangCach = map
        
        self.N = N
        self.nghiem = []
        self.thichNghi = [0] * self.N
        self.nCity = nCity
        
        """tạo ngẫu nhiên tập nghiệm vs mổi tập gồm self.nCity"""
        for i in range(self.N):
            temp = [0] * self.nCity
            for j in range(self.nCity):
                temp[j] = randint(0, self.nCity - 1)
            self.nghiem.append(temp)
        
        self.top10_with_start = []
        self.top10 = []
        
        
        self.min = 10000000
        self.best = {}
        self.the_shorted_from = {}
        for i in range(nCity):
            self.the_shorted_from[i] = [self.min, []]
    
    def danh_gia(self):
        for i in range(self.N):
            self.thichNghi[i] = 0
            for j in range(self.nCity - 1):
                self.thichNghi[i] += self.khoangCach[self.nghiem[i][j]][self.nghiem[i][j + 1]]
            
            for j in range(self.nCity - 1):
                for t in range(j + 1, self.nCity):
                    if self.nghiem[i][j] == self.nghiem[i][t]:
                        self.thichNghi[i] += 100
    
    def chon_loc(self, choose_rate):
        temp = self.thichNghi.copy()
        temp.sort()
        nguong = temp[int(self.N * choose_rate)]
        
        for i in range(self.N):
            if self.thichNghi[i] > nguong:
                new_nghiem = [0] * self.nCity
                for j in range(self.nCity):
                    new_nghiem[j] = randint(0, self.nCity - 1)
                self.nghiem[i] = new_nghiem
    
    def lai_ghep(self, nLaighep):
        for i in range(nLaighep):
            cha = randint(0, self.N - 1)
            me = randint(0, self.N - 1)
            for j in range(0, len(self.nghiem[cha])):
                if randint(0, 1) == 1:
                    temp = self.nghiem[cha][j]
                    self.nghiem[cha][j] = self.nghiem[me][j]
                    self.nghiem[me][j] = temp
    
    def dot_bien(self, mutate_rate):
        num = int(mutate_rate * self.N)
        for i in range(num):
            index = randint(0, self.N - 1)
            something = randint(0, self.nCity - 1)
            self.nghiem[index][something] = randint(0, self.nCity - 1)
        
    
    def gen_sieu_nhan(self):
        temp = self.thichNghi.copy()
        temp.sort()
        best = temp[0]

        
        for i in range(len(self.thichNghi)):
            if self.thichNghi[i] == best:
                print(self.thichNghi[i])
                print(", ".join([str(j) for j in self.nghiem[i]]))
                print()
                with open("log_result.txt", 'a', encoding='utf-8') as w:
                    w.write("{}\n".format(self.thichNghi[i]))
                    w.write(", ".join([str(j) for j in self.nghiem[i]]))
                    w.write("\n")
                    w.close()

            
    def print_result(self):
        for i in self.best:
            print("best is: {} with\n{}".format(i, self.best[i]))
        print()



if __name__ == '__main__':
    size, map = read_map()
    man = MonkeyOnTruck(100, size, map)
    
    for i in range(1000):
        with open("log_result.txt", 'a', encoding='utf-8') as w:
            w.write("Đời {}\n".format(i))
            w.close()
        print('Đời {}'.format(i))
        man.danh_gia()
        man.gen_sieu_nhan()
        # man.duong_ngan_nhat_2()
        man.chon_loc(0.8)
        man.lai_ghep(20)
        man.dot_bien(0.01)
    
