import math
import matplotlib.pyplot as plt

class Hangul:
    def __init__(self):
        #단위: mm
        #초성 모음
        self.g = [(0, 0, False), (0, 0, True), (1, 0, True), (1, 1, True), (1, 1, False)]
        self.kk = [(0, 0, False), (0, 0, True), (1*10/21, 0, True), (1*10/21, 1, True), (1*10/21, 1, False), (1*11/21, 0, False), (1*11/21, 0, True), (1, 0, True), (1, 1, True), (1, 1, False)]
        self.n = [(0, 0, False), (0, 0, True), (0, 1, True), (1, 1, True), (1, 1, False)]
        self.d = [(1, 0, False), (1, 0, True), (0, 0, True),(0, 1, True),(1, 1, True), (1, 1, False)]
        self.tt = [(1*10/21, 0, False), (1*10/21, 0, True), (0, 0, True), (0, 1, True), (1*10/21, 1, True), (1*10/21, 1, False), (1, 0, False), (1, 0, True), (1*11/21, 0, True), (1*11/21, 1, True), (1, 1, True), (1, 1, False)]
        self.r = [(0, 0, False), (0, 0, True), (1, 0, True), (1, 1/2, True), (0, 1/2, True), (0, 1, True), (1, 1, True), (1, 1, False)]
        self.m = [(0, 0, False), (0, 0, True), (1, 0, True), (1, 1, True), (0, 1, True), (0, 0, True), (0, 0, False)]
        self.b = [(0, 0, False), (0, 0, True), (0, 1, True), (1, 1, True), (1, 0, True), (1, 0, False), (0, 1/2, False), (0, 1/2, True), (1, 1/2, True), (1, 1/2, False)]
        self.pp = [(0, 0, False), (0, 0, True), (0, 1, True), (1*10/21, 1, True), (1*10/21, 0, True), (1*10/21, 0, False), (0, 1/2, False), (0, 1/2, True), (1*10/21, 1/2, True), (1*10/21, 1/2, False), (1*11/21, 0, False), (1*11/21, 0, True), (1*11/21, 1, True), (1, 1, True), (1, 0, True), (1, 0, False), (1*11/21, 1/2, False), (1*11/21, 1/2, True), (1, 1/2, True), (1, 1/2, False)]
        self.s = [(1/2, 0, False), (1/2, 0, True), (0, 1, True), (0, 1, False), (1/2, 0, False), (1/2, 0, True), (1, 1, True), (1, 1, False)]
        self.ss = [(1*5/21, 0, False), (1*5/21, 0, True), (0, 1, True), (0, 1, False), (1*5/21, 0, False), (1*5/21, 0, True), (1*10/21, 1, True), (1*10/21, 1, False), (1*16/21, 0, False), (1*16/21, 0, True), (1*11/21, 1, True), (1*11/21, 1, False), (1*16/21, 0, False), (1*16/21, 0, True), (1, 1, True), (1, 1, False)]
        self.sampling = list(range(0, 361, 1))
        self.ng = [(0, 1/2, False)] + [((1/2) + (1/2)*math.cos(math.radians(180-dot)), 1/2 + (1/2)*math.sin(math.radians(dot)), True) for dot in self.sampling] + [(0, 1/2, False)]
        self.j = [(0, 0, False),(0, 0, True),(1, 0, True),(1, 0, False),(1/2, 0, False), (1/2, 0, True), (0, 1, True),(0, 1, False),(1/2, 0, False),(1/2, 0, True),(1, 1, True),(1, 1, False)]
        self.jj = self.resize(self.j + self.offset(self.j, 1.1, 0), 10/21, 1)
        self.ch = [(1*1/5, 0, False),(1*1/5, 0, True),(1*4/5, 0, True),(1*4/5, 0, False),(0, 1*1/6, False),(0, 1*1/6, True),(1, 1*1/6, True),(1, 1*1/6, False),(1/2, 1*1/6, False), (1/2, 1*1/6, True), (0, 1, True),(0, 1, False),(1/2, 1*1/6, False),(1/2, 1*1/6, True),(1, 1, True),(1, 1, False)]
        self.k = [(0, 0, False), (0, 0, True), (1, 0, True),(1, 1, True),(1, 1, False),(0, 1/2, False),(0, 1/2, True),(1, 1/2, True),(1, 1/2, False)]
        self.t = [(1, 0, False), (1, 0, True), (0, 0, True),(0, 1, True),(1, 1, True),(1, 1, False),(0, 1/2, False),(0, 1/2, True),(1, 1/2, True),(1, 1/2, False)]
        self.p = [(0, 0, False), (0, 0, True), (0, 0, True),(1, 0, True),(1, 0, False),(0, 1, False),(0, 1, True),(1, 1, True),(1, 1, False),(1/3, 0, False),(1/3, 0, True),(1/3, 1, True),(1/3, 1, False),(1*2/3, 0, False),(1*2/3, 0, True),(1*2/3, 1, True),(1*2/3, 1, False)]
        self.h = [(1*1/5, 0, False),(1*1/5, 0, True),(1*4/5, 0, True),(1*4/5, 0, False),(0, 1*1/6, False),(0, 1*1/6, True),(1, 1*1/6, True),(1, 1*1/6, False)] + self.offset(self.resize(self.ng, 9/12, 9/12), 0.5 - 9/24, 3/12)
        self.CHOSUNGDICT = {'ㄱ':self.g, 'ㄴ':self.n, 'ㄷ':self.d, 'ㄸ':self.tt, 'ㄹ':self.r, 'ㅁ':self.m, 'ㅂ':self.b, 'ㅃ':self.pp, 'ㅅ':self.s, 'ㅆ':self.ss, 'ㅇ':self.ng, 'ㅈ':self.j, 'ㅉ':self.jj, 'ㅊ':self.ch, 'ㅋ':self.k, 'ㅌ':self.t, 'ㅍ':self.p, 'ㅎ':self.h}
        #중성 모음
        self.a = [(0, 0, False), (0, 0, True),(0, 1, True),(0, 1, False),(0, 1/2, False),(0, 1/2, True),(1, 1/2, True),(1, 1/2, False)]
        self.ae = [(0, 0, False), (0, 0, True), (0, 1, True),(0, 1, False),(1, 0, False),(1, 0, True),(1, 1, True),(1, 1, False),(0, 1/2, False),(0, 1/2, True),(1, 1/2, True),(1, 1/2, False)]
        self.ya = [(0, 0, False), (0, 0, True), (0, 1, True),(0, 1, False),(0, 1/3, False),(0, 1/3, True),(1, 1/3, True),(1, 1/3, False),(0, 1*2/3, False),(0, 1*2/3, True),(1, 1*2/3, True),(1, 1*2/3, False)]
        self.yae = [(0, 0, False), (0, 0, True), (0, 1, True),(0, 1, False),(1, 0, False),(1, 0, True),(1, 1, True),(1, 1, False),(0, 1/3, False),(0, 1/3, True),(1, 1/3, True),(1, 1/3, False),(0, 1*2/3, False),(0, 1*2/3, True),(1, 1*2/3, True),(1, 1*2/3, False)]
        self.eo = [(0, 1/2, False),(0, 1/2, True),(1, 1/2, True),(1, 1/2, False),(1, 0, False), (1, 0, True), (1, 1, True),(1, 1, False)]
        self.e = [(0, 1/2, False),(0, 1/2, True),(1/2, 1/2, True),(1/2, 1/2, False),(1/2, 0, False), (1/2, 0, True), (1/2, 1, True),(1/2, 1, False),(1, 0, False), (1, 0, True), (1, 1, True),(1, 1, False)]
        self.yeo = [(0, 1/3, False),(0, 1/3, True),(1, 1/3, True),(1, 1/3, False),(0, 1*2/3, False),(0, 1*2/3, True),(1, 1*2/3, True),(1, 1*2/3, False),(1, 0, False), (1, 0, True), (1, 1, True),(1, 1, False),]
        self. ye = [(0, 1/3, False),(0, 1/3, True),(1/2, 1/3, True),(1/2, 1/3, False),(0, 1*2/3, False),(0, 1*2/3, True),(1/2, 1*2/3, True),(1/2, 1*2/3, False),(1/2, 0, False), (1/2, 0, True), (1/2, 1, True),(1/2, 1, False),(1, 0, False), (1, 0, True), (1, 1, True),(1, 1, False),]
        self.o = [(1/2, 0, False), (1/2, 0, True),(1/2, 1, True),(1/2, 1, False),(0, 1, False),(0, 1, True),(1, 1, True),(1, 1, False)]
        self.wa = self.offset(self.resize(self.o, 4/5, 1/5), 0, 3/5) + self.offset(self.resize(self.a, 1/5, 1), 4/5, 0)
        self.wae = self.offset(self.resize(self.o, 4/5, 1/5), 0, 3/5) + self.offset(self.resize(self.ae, 1/5, 1), 4/5, 0)
        self.yo = [(1/3, 0, False), (1/3, 0, True),(1/3, 1, True),(1/3, 1, False),(1*2/3, 0, False), (1*2/3, 0, True),(1*2/3, 1, True),(1*2/3, 1, False),(0, 1, False),(0, 1, True),(1, 1, True),(1, 1, False)]
        self.u = [(0, 0, False),(0, 0, True),(1, 0, True),(1, 0, False),(1/2, 0, False), (1/2, 0, True),(1/2, 1, True),(1/2, 1, False)]
        self.wo = self.offset(self.resize(self.u, 4/5, 1/5), 0, 4/5) + self.offset(self.resize(self.offset(self.resize(self.offset(self.eo, 0, -1/4), 1/5, 2), 0, 1/2), 1, 1/2), 4/5, 0)
        self.we = self.offset(self.resize(self.u, 4/5, 1/5), 0, 4/5) + self.offset(self.resize(self.e, 1/5, 1), 4/5, 0)
        self.yu = [(0, 0, False), (0, 0, True),(1, 0, True),(1, 0, False),(1/3, 0, False), (1/3, 0, True),(1/3, 1, True),(1/3, 1, False),(1*2/3, 0, False), (1*2/3, 0, True),(1*2/3, 1, True),(1*2/3, 1, False)]
        self.eu = [(0, 1/2, False),(0, 1/2, True),(1, 1/2, True),(1, 1/2, False)]
        self.i = [(1/2, 0, False),(1/2, 0, True),(1/2, 1, True),(1/2, 1, False)]
        self.oe = self.offset(self.resize(self.o, 9/10, 1/5), 0, 3/5) + self.offset(self.resize(self.i, 1/5, 1), 4/5, 0)
        self.wi = self.offset(self.resize(self.u, 9/10, 1/5), 0, 4/5) + self.offset(self.resize(self.i, 1/5, 1), 4/5, 0)
        self.ui = self.offset(self.resize(self.eu, 9/10, 1/5), 0, 7/10) + self.offset(self.resize(self.i, 1/5, 1), 4/5, 0)
        self.JUNGSUNGDICT = {'ㅏ':self.a, 'ㅐ':self.ae, 'ㅑ':self.ya, 'ㅒ':self.yae, 'ㅓ':self.eo, 'ㅔ':self.e, 'ㅕ':self.yeo, 'ㅖ':self.ye, 'ㅗ':self.o, 'ㅘ':self.wa, 'ㅙ':self.wae, 'ㅚ':self.oe, 'ㅛ':self.yo, 'ㅜ':self.u, 'ㅝ':self.wo, 'ㅞ':self.we, 'ㅟ':self.wi, 'ㅠ':self.yu, 'ㅡ':self.eu, 'ㅢ':self.ui, 'ㅣ':self.i}
        #종성 모음
        self.gs = self.resize(self.g + self.offset(self.s, 1.1, 0), 10/21, 1)
        self.nj = self.resize(self.n + self.offset(self.j, 1.1, 0), 10/21, 1)
        self.nh = self.resize(self.n + self.offset(self.h, 1.1, 0), 10/21, 1)
        self.rg = self.resize(self.r + self.offset(self.g, 1.1, 0), 10/21, 1)
        self.rm = self.resize(self.r + self.offset(self.m, 1.1, 0), 10/21, 1)
        self.rb = self.resize(self.r + self.offset(self.b, 1.1, 0), 10/21, 1)
        self.rs = self.resize(self.r + self.offset(self.s, 1.1, 0), 10/21, 1)
        self.rt = self.resize(self.r + self.offset(self.t, 1.1, 0), 10/21, 1)
        self.rp = self.resize(self.r + self.offset(self.p, 1.1, 0), 10/21, 1)
        self.rh = self.resize(self.r + self.offset(self.h, 1.1, 0), 10/21, 1)
        self.bs = self.resize(self.b + self.offset(self.s, 1.1, 0), 10/21, 1)
        self.JONGSUNGDICT = {'ㄳ':self.gs, 'ㄵ':self.nj, 'ㄶ':self.nh, 'ㄺ':self.rg, 'ㄻ':self.rm, 'ㄼ':self.rb, 'ㄽ':self.rs, 'ㄾ':self.rt, 'ㄿ':self.rp, 'ㅀ':self.rh, 'ㅄ':self.bs, 'ㄱ':self.g, 'ㄴ':self.n, 'ㄷ':self.d, 'ㄸ':self.tt, 'ㄹ':self.r, 'ㅁ':self.m, 'ㅂ':self.b, 'ㅃ':self.pp, 'ㅅ':self.s, 'ㅆ':self.ss, 'ㅇ':self.ng, 'ㅈ':self.j, 'ㅉ':self.jj, 'ㅊ':self.ch, 'ㅋ':self.k, 'ㅌ':self.t, 'ㅍ':self.p, 'ㅎ':self.h}

    def shower(self, word):
        x = []
        y = []
        z = []
        for dot in word:
            x.append(dot[0])
            y.append(dot[1])
            z.append(dot[2])
        ax = plt.figure(figsize=(5,5)).add_subplot(projection='3d')
        ax.axis([0, 1, 1, 0])
        ax.plot(x, y, z)
        ax.set_title('word trajectory 3d plot')

    def stringShower(self, size, wordnum, string):
        x = []
        y = []
        z = []
        for dot in string:
            x.append(dot[0])
            y.append(dot[1])
            z.append(dot[2])
        ax = plt.figure().add_subplot(projection='3d')
        ax.axis([0, size*0.7*wordnum, size*wordnum, 0])
        ax.plot(x, y, z)
        ax.set_title('string trajectory 3d plot')

    def offset(self, word, x, y):
        word = word.copy()
        for dot in range(0,len(word)):
            word[dot] = list(word[dot])
        for dot in range(0, len(word)):
            word[dot][0] = word[dot][0] + x
            word[dot][1] = word[dot][1] + y
        for dot in range(0,len(word)):
            word[dot] = tuple(word[dot])
        return word
    
    def resize(self, word, xscale, yscale):
        word = word.copy()
        for dot in range(0,len(word)):
            word[dot] = list(word[dot])
        for dot in range(0, len(word)):
            word[dot][0] = word[dot][0] * xscale
            word[dot][1] = word[dot][1] * yscale
        for dot in range(0,len(word)):
            word[dot] = tuple(word[dot])
        return word
    
    def string_dot(self, size, chars):
        string_dot_list = []
        i = 0
        for char in chars:
            char = self.offset(char, i*size, 0)
            string_dot_list = string_dot_list + char
            i = i + 0.7
        return string_dot_list

    def Type1(self, size, word1, word2):
        word1 = self.resize(word1, size*55/100, size*4/5)
        word2 = self.resize(word2, size*35/100, size*1)
        word1 = self.offset(word1, 0, size*1/10)
        word2 = self.offset(word2, size*65/100, 0)
        return self.resize(word1+word2, 0.6, 1)

    def Type2(self, size, word1, word2, word3):
        temp = self.Type1(size, word1, word2)
        temp = self.resize(temp, size, size*55/100)
        word3 = self.resize(word3, size*0.6, size*35/100)
        word3 = self.offset(word3, 0, size*65/100)
        return self.resize(temp+word3, 1, 1)

    def Type3(self, size, word1, word2):
        word1 = self.resize(word1, size*4/5, size*55/100)
        word2 = self.resize(word2, size*1, size*35/100)
        word1 = self.offset(word1, size*1/10, 0)
        word2 = self.offset(word2, 0, size*65/100)
        return self.resize(word1+word2, 0.6, 1)
    
    def Type4(self, size, word1, word2, word3):
        temp = self.Type3(size, word1, word2)
        temp = self.resize(temp, size, size*65/100)
        word3 = self.resize(word3, size*4/5*0.6, size*25/100)
        word3 = self.offset(word3, size*1/10, size*75/100)
        return self.resize(temp+word3, 1, 1)

    def Type5(self, size, word1, word2):
        pass
    
    def Type6(self, size, word1, word2):
        pass
    
    def TrajectoryMaker(self, size, dividedHangul):
        Hangul.TrajectoryList = []
        for word in dividedHangul:
            if word[0] == 'Type1':
                Hangul.TrajectoryList.append(self.Type1(size, self.CHOSUNGDICT[word[1]], self.JUNGSUNGDICT[word[2]]))
            elif word[0] == 'Type2':
                Hangul.TrajectoryList.append(self.Type2(size, self.CHOSUNGDICT[word[1]], self.JUNGSUNGDICT[word[2]], self.JONGSUNGDICT[word[3]]))
            elif word[0] == 'Type3':
                Hangul.TrajectoryList.append(self.Type3(size, self.CHOSUNGDICT[word[1]], self.JUNGSUNGDICT[word[2]]))
            elif word[0] == 'Type4':
                Hangul.TrajectoryList.append(self.Type4(size, self.CHOSUNGDICT[word[1]], self.JUNGSUNGDICT[word[2]], self.JONGSUNGDICT[word[3]]))
            elif word[0] == 'Type5':
                Hangul.TrajectoryList.append(self.Type5(size, self.CHOSUNGDICT[word[1]], self.JUNGSUNGDICT[word[2]]))
            elif word[0] == 'Type6':
                Hangul.TrajectoryList.append(self.Type6(size, self.CHOSUNGDICT[word[1]], self.JUNGSUNGDICT[word[2]], self.JONGSUNGDICT[word[3]]))
        return self.string_dot(size, Hangul.TrajectoryList)

if __name__ == '__main__':
    H = Hangul()
    # Combine
    #H.stringShower(3, H.string_dot(1, [H.Type2(1, H.k, H.eo, H.m), H.Type3(1, H.p, H.yu), H.Type1(1, H.t, H.eo)]))
    #H.stringShower(2, H.string_dot(1, [H.Type2(1, H.j, H.eo, H.r), H.Type1(1, H.d, H.ae)]))
    #H.stringShower(2, H.string_dot(1, [H.Type1(1, H.ng, H.a), H.Type1(1, H.h, H.a)]))
    #H.stringShower(4, H.string_dot(1, [H.Type1(1, H.d, H.i), H.Type1(1, H.j, H.i), H.Type3(1, H.s, H.eu), H.Type3(1, H.t, H.eu)]))
    #H.stringShower(4, H.string_dot(1, [H.Type3(1, H.s, H.u), H.Type4(1, H.n, H.eu, H.ng), H.Type4(1, H.t, H.eu, H.g), H.Type2(1, H.g, H.a, H.ng)]))
    #H.stringShower(len([['Type2', 'ㅂ', 'ㅐ', 'ㄱ'], ['Type2', 'ㅁ', 'ㅣ', 'ㄴ'], ['Type2', 'ㅎ', 'ㅕ', 'ㄱ']]), H.TrajectoryMaker(1, [['Type2', 'ㅂ', 'ㅐ', 'ㄱ'], ['Type2', 'ㅁ', 'ㅣ', 'ㄴ'], ['Type2', 'ㅎ', 'ㅕ', 'ㄱ']]))