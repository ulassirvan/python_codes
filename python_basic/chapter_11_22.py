import numpy as np




pi = 3.14
def area_of_circle(radius):
    return pi * radius ** 2
print(f"yarı çapı 0.5 olan dairenin alanı {area_of_circle(0.5)}")





def investment_calculator(interest, year_of_investment, adding_each_of_end_year, starting_capital=1000):
    for _ in (np.arange(year_of_investment)):
        starting_capital = starting_capital + interest / 100 * starting_capital
        starting_capital = starting_capital + adding_each_of_end_year
    return starting_capital


print(investment_calculator(3, 5, 0))





def parabol_delta_finder(a,b,c):
    return b**2 - 4*a*c


print(parabol_delta_finder(3,-4,1))





def aritmatic_series_formula(first_term,last_term,n):
    return (first_term+last_term)/2*n

print(aritmatic_series_formula(14,50,10))





def geometric_series_calculator(first_term,n,r):
    return first_term*((1-(r**n))/(1-r))
print(geometric_series_calculator(8,6,2))





def parabol_kokler_toplam_çarpımı(a,b,c):
    print(f"x1+x2={-b/a}")
    print(f"x1*x2={c/a}")
parabol_kokler_toplam_çarpımı(1,5,4)



def line_mid_point_finder(a,b):
    return ((a[0]+b[0])/2 ,(a[1]+b[1])/2)
print(line_mid_point_finder((2,4),(-4,6)))



def distiance_btv_2_point(a,b):
    return np.sqrt(((a[0]-b[0])**2)+(a[1]-b[1])**2)
print(distiance_btv_2_point((3,2),(-1,-1)))


def parbol_kok_bulma(a,b,c):


    return ((((-1*b)+((parabol_delta_finder(a,b,c))**(1/2)))/2*a),(((-1*b)-((parabol_delta_finder(a,b,c))**(1/2)))/2*a))

print(parbol_kok_bulma(1,-7,10))


def geomtric_mean(sayılar):
    tüm_sayıların_çarpımı=1
    for a in sayılar:
        tüm_sayıların_çarpımı*=a
    return tüm_sayıların_çarpımı**(1/len(sayılar))


print(geomtric_mean((4,10,16,24)))



def mean(a):
    return sum(a)/len(a)




#standart sapma kodu yaz.....