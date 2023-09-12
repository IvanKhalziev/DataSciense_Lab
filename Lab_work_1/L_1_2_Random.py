# ------------------------ Statistical learning: regression models  -------------------------------

'''

МОДЕЛЬ:
законів розподілу випадкових величин (ВВ).

Довідковий матеріал:
https://numpy.org/doc/stable/reference/random/generator.html
https://www.w3schools.com/python/numpy/numpy_random_exponential.asp
https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html
https://www.geeksforgeeks.org/numpy-random-exponential-in-python/
https://numpy.org/doc/stable/reference/random/generated/numpy.random.chisquare.html

Package                      Version
---------------------------- -----------
pip                          23.1
numpy                        1.23.5
matplotlib                   3.6.2

'''

import numpy as np
import math as mt
import matplotlib.pyplot as plt



# ----------- рівномірний закон розводілу номерів АВ в межах вибірки ----------------
def random_uniform (a, b, iter):
    S = np.zeros((iter))
    for i in range(iter):
        S[i] = np.random.uniform(a, b)  # параметри закону задаются межами аргументу
    mS = np.mean(S)
    dS = np.var(S)
    # dS = ((a-b)**2)/12
    scvS = mt.sqrt(dS)
    print('------- статистичны характеристики РІВНОМІРНОГО закону розподілу ВВ -----')
    print('матиматичне сподівання ВВ=', mS)
    print('дисперсія ВВ =', dS)
    print('СКВ ВВ=', scvS)
    print('--------------------------------------------------------------------------')
    # гістограма закону розподілу ВВ
    plt.hist(S, bins=20, facecolor="blue", alpha=0.5)
    plt.show()
    return S

# ------------------------- нормальний закон розводілу ВВ ----------------------------
def rando_norm (dm, dsig, iter):
    S = np.random.normal(dm, dsig, iter)  # нормальний закон розподілу ВВ з вибіркою єб'ємом iter та параметрами: dm, dsig
    mS = np.mean(S)
    dS = np.var(S)
    scvS = mt.sqrt(dS)
    print('------- статистичны характеристики НОРМАЛЬНОГО закону розподілу ВВ -----')
    print('матиматичне сподівання ВВ=', mS)
    print('дисперсія ВВ =', dS)
    print('СКВ ВВ=', scvS)
    print('------------------------------------------------------------------------')
    # гістограма закону розподілу ВВ
    plt.hist(S, bins=20, facecolor="blue", alpha=0.5)
    plt.show()
    return S

# ------------------------- експоненційний закон розводілу ВВ ----------------------------
def rando_exponential (alfa, iter):
    S = np.random.exponential(alfa, iter)  # експоненційний закон розподілу ВВ з вибіркою єб'ємом iter та параметрами: dsig
    mS = np.mean(S)
    dS = np.var(S)
    scvS = mt.sqrt(dS)
    print('------- статистичны характеристики ЕКСПОНЕНЦІЙНОГО закону розподілу ВВ -----')
    print('матиматичне сподівання ВВ=', mS)
    print('дисперсія ВВ =', dS)
    print('СКВ ВВ=', scvS)
    print('----------------------------------------------------------------------------')
    # гістограма закону розподілу ВВ
    plt.hist(S, bins=20, facecolor="blue", alpha=0.5)
    plt.show()
    return S


# ------------------------- хі квадрат закон розводілу ВВ ----------------------------
def rando_chisquare (k, iter):
    S = np.random.chisquare(k, iter)  # хі квадрат закон розподілу ВВ з вибіркою єб'ємом iter та параметрами: dsig
    mS = np.mean(S)
    dS = np.var(S)
    scvS = mt.sqrt(dS)
    print('-------- статистичны характеристики ХІ КВАДРАТ закону розподілу ВВ ---------')
    print('матиматичне сподівання ВВ=', mS)
    print('дисперсія ВВ =', dS)
    print('СКВ ВВ=', scvS)
    print('----------------------------------------------------------------------------')
    # гістограма закону розподілу ВВ
    plt.hist(S, bins=20, facecolor="blue", alpha=0.5)
    plt.show()
    return S

if __name__ == '__main__':

    print('Оберіть закон розподілу ВВ:')
    print('1 - рівномірний')
    print('2 - нормальний')
    print('3 - експоненційний')
    print('4 - хі квадрат')
    mode = int(input('mode:'))


    if (mode == 1):
        print(' ---------------- Обрано: рівномірний закон розподілу ВВ -----------------')
        print('------------------ ВХІДНІ параметри законі розподілу ВВ:------------------')
        a = 0
        b = 10
        iter = 10000
        print('початок інтервал =', a)
        print('кінцевий інтервал=', b)
        print('розмір вибірки ВВ =', iter)
        random_uniform(a, b, iter)

    if (mode == 2):
        print('------------------ Обрано: нормальний закон розподілу ВВ -----------------')
        print('------------------- ВХІДНІ параметри законі розподілу ВВ:-----------------')
        dm = 0
        dsig = 5
        iter = 10000
        print('матиматичне сподівання ВВ=', dm)
        print('СКВ ВВ=', dsig)
        print('розмір вибірки ВВ =', iter)
        rando_norm(dm, dsig, iter)

    if (mode == 3):
        print('----------------- Обрано: експоненційний закон розподілу ВВ --------------')
        print('------------------- ВХІДНІ параметри законі розподілу ВВ:-----------------')
        alfa = 1
        iter = 10000
        print('параметр alfa =', alfa)
        print('розмір вибірки ВВ =', iter)
        rando_exponential(alfa, iter)

    if (mode == 4):
        print('-------------------- Обрано: хі квадрат закон розподілу ВВ ---------------')
        print('--------------------- ВХІДНІ параметри законі розподілу ВВ: --------------')
        k = 1
        iter = 10000
        print('ступінь вільності k =', k)
        print('розмір вибірки ВВ =', iter)
        rando_chisquare(k, iter)
