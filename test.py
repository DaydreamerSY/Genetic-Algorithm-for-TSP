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
            
    # def nghiem_hop_le(self, nghiem):
    #     for i in range(len(nghiem) - 1):
    #         for j in range(i+1, len(nghiem)):
    #             if nghiem[i] == nghiem[j]:
    #                 return False
    #     return True
    #     # r = sum(range(len(nghiem)))
    #     # s = sum(nghiem)
    #     # if r == s:
    #     #     return True
    #     # return False
        
        
    
    def gen_sieu_nhan(self):
        temp = self.thichNghi.copy()
        temp.sort()
        best = temp[0]
        # if best <= self.min and self.nghiem_hop_le(self.nghiem[self.thichNghi.index(best)]):
        #     print("best is: {} with".format(best))
        #     self.min = best
        #     print(self.nghiem[self.thichNghi.index(best)])
        #     self.best.clear()
        #     self.best[best] = self.nghiem[self.thichNghi.index(best)]
        #     print()
        
        for i in range(len(self.thichNghi)):
            if self.thichNghi[i] == best:
                print(self.thichNghi[i])
                print(", ".join([str(j) for j in self.nghiem[i]]))
                print()
    
    # def duong_ngan_nhat_2(self):
    #     for city in self.the_shorted_from:
    #         temp_nghiem = []
    #         temp_thichNghi = []
    #         for i in range(self.N):
    #             if self.nghiem[i][0] == city:
    #                 temp_nghiem.append(self.nghiem[i])
    #                 temp_thichNghi.append(self.thichNghi[i])
    #
    #         temp = temp_thichNghi.copy()
    #         temp.sort()
    #         best = temp[0]
    #         if best <= self.the_shorted_from[city][0] and self.nghiem_hop_le(temp_nghiem[temp_thichNghi.index(best)]):
    #             self.the_shorted_from[city][0] = best
    #             self.the_shorted_from[city][1] = temp_nghiem[temp_thichNghi.index(best)]
    
            
    def print_result(self):
        for i in self.best:
            print("best is: {} with\n{}".format(i, self.best[i]))
        print()
        # for i in self.the_shorted_from:
        #     print("Start at {} cost {}:\n{}".format(i, self.the_shorted_from[i][0], self.the_shorted_from[i][1]))
        #     print()


if __name__ == '__main__':
    size, map = read_map()
    man = MonkeyOnTruck(100000, size, map)
    
    for i in range(100):
        print('Đời {}'.format(i))
        man.danh_gia()
        man.gen_sieu_nhan()
        # man.duong_ngan_nhat_2()
        man.chon_loc(0.8)
        man.lai_ghep(20)
        man.dot_bien(0.01)
    
    # man.print_result()
    
    # print(man.nghiem)
    # print(man.thichNghi)
