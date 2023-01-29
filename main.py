from statisfy import Statify


A = Statify()
B = Statify()


print(A.mean())
print(B.mean())
print(A.median())
print(B.median())
print(A.mode())
print(B.mode())
print(A.midpoint())
print(B.midpoint())
print(A.standard_deviation())
print(B.standard_deviation())
A.display_data()
B.display_data()
print(A.covariance(B))
print(A.correlation_coefficient(B))

C = A + B
C.display_data()
print(C.mean())
print(C.median())
print(C.mode())
print(C.midpoint())
print(C.standard_deviation())
print(C.covariance(B))
print(C.correlation_coefficient(B))
print(C.covariance(A))
print(C.correlation_coefficient(A))

A.histogram()
B.histogram()
C.histogram()
A.box_plot()
B.box_plot()
C.box_plot()
