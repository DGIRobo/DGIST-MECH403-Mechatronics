class HangulDivider:
    def __init__(self):
        # Type 1: 가
        # Type 2: 각
        # Type 3: 고
        # Type 4: 곡
        # Type 5: 과
        # Type 6: 곽
        # 초성 리스트. 00 ~ 18
        self._CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        # 중성 리스트. 00 ~ 20
        self._JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
        # 종성 리스트. 00 ~ 27 + 1(1개 없음)
        self._JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    def Korean_String_Separater(self, korean_string):
        Seperated_korean_string = []
        for korean_word in list(korean_string.strip()):
            ## 들어온 문자가 한글일 경우에만 실행하도록 함. 
            if ord('가')<=ord(korean_word)<=ord('힣'): ## 한글 유니코드는 가~힣까지 존재함.
                ## 한글 유니코드는 588개 마다 초성이 바뀜. 
                CHOSUNG = (ord(korean_word) - ord('가'))//588
                ## 한글 유니코드는 같은 초성일 때 28개마다 중성이 바뀜.
                JUNGSUNG = ((ord(korean_word) - ord('가')) - (588*CHOSUNG)) // 28
                ## 한글 유니코드는 같은 초성, 같은 중성일 때 28개의 종성을 가짐.
                JONGSUNG = (ord(korean_word) - ord('가')) - (588*CHOSUNG) - 28*JUNGSUNG
                if JONGSUNG == 0:
                    if 0<=JUNGSUNG<8 or JUNGSUNG == 20:
                        Seperated_korean_string.append(['Type1', self._CHOSUNG_LIST[CHOSUNG], self._JUNGSUNG_LIST[JUNGSUNG]])
                    elif 9<=JUNGSUNG<12 or 14<=JUNGSUNG<17 or JUNGSUNG==19:
                        Seperated_korean_string.append(['Type5', self._CHOSUNG_LIST[CHOSUNG], self._JUNGSUNG_LIST[JUNGSUNG]])
                    else:
                        Seperated_korean_string.append(['Type3', self._CHOSUNG_LIST[CHOSUNG], self._JUNGSUNG_LIST[JUNGSUNG]])
                else: 
                    if 0<=JUNGSUNG<8 or JUNGSUNG == 20:
                        Seperated_korean_string.append(['Type2', self._CHOSUNG_LIST[CHOSUNG], self._JUNGSUNG_LIST[JUNGSUNG], self._JONGSUNG_LIST[JONGSUNG]])
                    elif 9<=JUNGSUNG<12 or 14<=JUNGSUNG<17 or JUNGSUNG==19:
                        Seperated_korean_string.append(['Type6', self._CHOSUNG_LIST[CHOSUNG], self._JUNGSUNG_LIST[JUNGSUNG], self._JONGSUNG_LIST[JONGSUNG]])
                    else:
                        Seperated_korean_string.append(['Type4', self._CHOSUNG_LIST[CHOSUNG], self._JUNGSUNG_LIST[JUNGSUNG], self._JONGSUNG_LIST[JONGSUNG]])
            else:
                Seperated_korean_string.append(['Space', korean_word])
        return Seperated_korean_string

if __name__ == '__main__':
    Separater = HangulDivider()
    print(Separater.Korean_String_Separater("백민혁 어디가"))
    print(Separater.Korean_String_Separater("돔황차"))