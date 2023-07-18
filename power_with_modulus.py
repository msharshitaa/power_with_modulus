def power_with_modulus(A,B,C):
    val=1
    for i in range(B):
        val=(val*A)%C
    return val%C
A=int(input())
B=int(input())
C=int(input())
print(power_with_modulus(A,B,C))
