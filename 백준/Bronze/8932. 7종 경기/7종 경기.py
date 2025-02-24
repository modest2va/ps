import sys
def track_100(p):
    return int(9.23076*pow((26.7-p),1.835 ) )
def track_200(p):
    return int(4.99087*pow((42.5-p),1.81 ) )
def track_800(p):
    return int(0.11193*pow((254-p),1.88 ) )
def field_n(p):
    return int(1.84523 * pow((p-75), 1.348))
def field_p(p):
    return int(56.0211 * pow((p-1.5), 1.05))
def field_m(p):
    return int(0.188807 * pow((p-210), 1.41))
def field_c(p):
    return int(15.9803 * pow((p-3.8), 1.04))

for _ in range (int(sys.stdin.readline())):
    a,b,c,d,e,f,g=map(int, sys.stdin.readline().split())
    print((track_100(a)+field_n(b)+field_p(c)+track_200(d)+field_m(e)+field_c(f)+track_800(g)))

