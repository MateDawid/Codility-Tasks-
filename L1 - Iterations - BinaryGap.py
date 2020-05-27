#https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
def solution(N):
    return len(max(format(N,'b').strip('0').split('1')))  #format() określa, na jaki format ma być zamieniona liczba

#test
binary = "1000000010000000000000001000000000000001000"
print(binary)
print(binary.strip('0')) #.strip() usuwa znak "0" z przestrzeni graniczących ze spacją
print(binary.strip('0').split('1')) #.split() tworzy ze stringu listę, których elementy rozgranicza podany w nawiasie znak
print(max(binary.strip('0').split('1'))) #w przypadku stringów funkcja max() wskazuje najdłuższy element
