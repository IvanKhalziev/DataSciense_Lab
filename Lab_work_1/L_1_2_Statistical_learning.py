# ------------------------ Statistical learning: regression models  -------------------------------

'''

Статистичне навчання:
 - визначення параметрів поліноміальної / моделі за статистичною дискретною навчальною вибіркою;
 - побудова лінії тренду;
 - прогнозування динаміки розвитку статистичного ряду.

Склад етапів:
1. Тестова аддитивна модель: квадратичний тренд + нормальна + аномальна помилки;
2. Парсінг реальних даних https://www.oschadbank.ua/rates-archive, Oschadbank (USD).xls;
3. Визначення статистичних характеристик навчальної вибірки;
4. Детекція та очищення навчальної вибірки від аномалій;
5. Статистичне навчання парамерів поліноміальної моделі за МНК - бібліотека numpy;
6. Прогнозування динаміки розвитку статистичного ряду за МНК.


Package                      Version
---------------------------- -----------
pip                          23.1
numpy                        1.23.5
pandas                       1.5.3
xlrd                         2.0.1
matplotlib                   3.6.2

'''

import numpy as np
import math as mt
import matplotlib.pyplot as plt
import pandas as pd

# ------------------------ ФУНКЦІЯ парсингу реальних даних --------------------------

def file_parsing (URL, File_name, Data_name):
    d = pd.read_excel(File_name)
    for name, values in d[[Data_name]].items():
        print(values)
    S_real = np.zeros((len(values)))
    for i in range(len(values)):
        S_real[i] = values[i]
    print('Джерело даних: ', URL)
    return S_real

# ---------------------- ФУНКЦІЇ тестової аддитивної моделі -------------------------

# ----------- рівномірний закон розводілу номерів АВ в межах вибірки ----------------
def randomAM (n, iter):
    SAV = np.zeros((nAV))
    S = np.zeros((n))
    for i in range(n):
        S[i] = np.random.randint(0, iter)  # параметри закону задаются межами аргументу
    mS = np.median(S)
    dS = np.var(S)
    scvS = mt.sqrt(dS)
    # -------------- генерація номерів АВ за рівномірним законом  -------------------
    for i in range(nAV):
        SAV[i] = mt.ceil(np.random.randint(1, iter))  # рівномірний розкид номерів АВ в межах вибірки розміром 0-iter
    print('номери АВ: SAV=', SAV)
    print('----- статистичны характеристики РІВНОМІРНОГО закону розподілу ВВ -----')
    print('матиматичне сподівання ВВ=', mS)
    print('дисперсія ВВ =', dS)
    print('СКВ ВВ=', scvS)
    print('-----------------------------------------------------------------------')
    # гістограма закону розподілу ВВ
    plt.hist(S, bins=20, facecolor="blue", alpha=0.5)
    plt.show()
    return SAV

# ------------------------- нормальний закон розводілу ВВ ----------------------------
def randoNORM (dm, dsig, iter):
    S = np.random.normal(dm, dsig, iter)  # нормальний закон розподілу ВВ з вибіркою єбємом iter та параметрами: dm, dsig
    mS = np.median(S)
    dS = np.var(S)
    scvS = mt.sqrt(dS)
    print('------- статистичны характеристики НОРМАЛЬНОЇ похибки вимірів -----')
    print('матиматичне сподівання ВВ=', mS)
    print('дисперсія ВВ =', dS)
    print('СКВ ВВ=', scvS)
    print('------------------------------------------------------------------')
    # гістограма закону розподілу ВВ
    plt.hist(S, bins=20, facecolor="blue", alpha=0.5)
    plt.show()
    return S

# ------------------- модель ідеального тренду (квадратичний закон)  ------------------
def Model (n):
    S0=np.zeros((n))
    for i in range(n):
        S0[i]=(0.0000005*i*i)    # квадратична модель реального процесу
    return S0

# ---------------- модель виміру (квадратичний закон) з нормальний шумом ---------------
def Model_NORM (SN, S0N, n):
    SV=np.zeros((n))
    for i in range(n):
        SV[i] = S0N[i]+SN[i]
    return SV

# ----- модель виміру (квадратичний закон) з нормальний шумом + АНОМАЛЬНІ ВИМІРИ
def Model_NORM_AV (S0, SV, nAV, Q_AV):
    SV_AV = SV
    SSAV = np.random.normal(dm, (Q_AV * dsig), nAV)  # аномальна випадкова похибка з нормальним законом
    for i in range(nAV):
        k=int (SAV[i])
        SV_AV[k] = S0[k] + SSAV[i]        # аномальні вимірів з рівномірно розподіленими номерами
    return SV_AV

# --------------- графіки тренда, вимірів з нормальним шумом  ---------------------------
def Plot_AV (S0_L, SV_L, Text):
    plt.clf()
    plt.plot(SV_L)
    plt.plot(S0_L)
    plt.ylabel(Text)
    plt.show()
    return

# ----- Коефіцієнт детермінації - оцінювання якості моделі --------
def r2_score(SL, Yout, Text):
    # статистичні характеристики вибірки з урахуванням тренду
    iter = len(Yout)
    numerator = 0
    denominator_1 = 0
    for i in range(iter):
        numerator = numerator + (SL[i] - Yout[i, 0]) ** 2
        denominator_1 = denominator_1 + SL[i]
    denominator_2 =  0
    for i in range(iter):
        denominator_2 = denominator_2 + (SL[i] - (denominator_1 / iter)) ** 2
    R2_score_our = 1 - (numerator / denominator_2)
    print('------------', Text, '-------------')
    print('кількість елементів вбірки=', iter)
    print('Коефіцієнт детермінації (ймовірність апроксимації)=', R2_score_our)

    return R2_score_our


# ----- статистичні характеристики вхідної вибірки  --------
def Stat_characteristics_in (SL, Text):
    # статистичні характеристики вибірки з урахуванням тренду
    Yout = MNK_Stat_characteristics(SL)
    iter = len(Yout)
    SL0 = np.zeros((iter ))
    for i in range(iter):
        SL0[i] = SL[i] - Yout[i, 0]
    mS = np.median(SL0)
    dS = np.var(SL0)
    scvS = mt.sqrt(dS)
    print('------------', Text ,'-------------')
    print('кількість елементів вбірки=', iter)
    print('матиматичне сподівання ВВ=', mS)
    print('дисперсія ВВ =', dS)
    print('СКВ ВВ=', scvS)
    print('-----------------------------------------------------')
    return

# ----- статистичні характеристики лінії тренда  --------
def Stat_characteristics_out (SL_in, SL, Text):
    # статистичні характеристики вибірки з урахуванням тренду
    Yout = MNK_Stat_characteristics(SL)
    iter = len(Yout)
    SL0 = np.zeros((iter ))
    for i in range(iter):
        SL0[i] = SL[i,0] - Yout[i, 0]
    mS = np.median(SL0)
    dS = np.var(SL0)
    scvS = mt.sqrt(dS)
    # глобальне лінійне відхилення оцінки - динамічна похибка моделі
    Delta = 0
    for i in range(iter):
        Delta = Delta + abs(SL_in[i] - Yout[i, 0])
    Delta_average_Out = Delta / (iter + 1)
    print('------------', Text ,'-------------')
    print('кількість елементів ивбірки=', iter)
    print('матиматичне сподівання ВВ=', mS)
    print('дисперсія ВВ =', dS)
    print('СКВ ВВ=', scvS)
    print('Динамічна похибка моделі=', Delta_average_Out)
    print('-----------------------------------------------------')
    return

# ----- статистичні характеристики екстраполяції  --------
def Stat_characteristics_extrapol (koef, SL, Text):
    # статистичні характеристики вибірки з урахуванням тренду
    Yout = MNK_Stat_characteristics(SL)
    iter = len(Yout)
    SL0 = np.zeros((iter ))
    for i in range(iter):
        SL0[i] = SL[i,0] - Yout[i, 0]
    mS = np.median(SL0)
    dS = np.var(SL0)
    scvS = mt.sqrt(dS)
    #  довірчий інтервал прогнозованих значень за СКВ
    scvS_extrapol = scvS * koef
    print('------------', Text ,'-------------')
    print('кількість елементів ивбірки=', iter)
    print('матиматичне сподівання ВВ=', mS)
    print('дисперсія ВВ =', dS)
    print('СКВ ВВ=', scvS)
    print('Довірчий інтервал прогнозованих значень за СКВ=', scvS_extrapol)
    print('-----------------------------------------------------')
    return

# ------------- МНК згладжуваннядля визначення стат. характеристик -------------
def MNK_Stat_characteristics (S0):
    iter = len(S0)
    Yin = np.zeros((iter, 1))
    F = np.ones((iter, 3))
    for i in range(iter):  # формування структури вхідних матриць МНК
        Yin[i, 0] = float(S0[i])  # формування матриці вхідних даних
        F[i, 1] = float(i)
        F[i, 2] = float(i * i)
    FT=F.T
    FFT = FT.dot(F)
    FFTI=np.linalg.inv(FFT)
    FFTIFT=FFTI.dot(FT)
    C=FFTIFT.dot(Yin)
    Yout=F.dot(C)
    return Yout


# ------------------------------ МНК згладжування -------------------------------------
def MNK (S0):
    iter = len(S0)
    Yin = np.zeros((iter, 1))
    F = np.ones((iter, 3))
    for i in range(iter):  # формування структури вхідних матриць МНК
        Yin[i, 0] = float(S0[i])  # формування матриці вхідних даних
        F[i, 1] = float(i)
        F[i, 2] = float(i * i)
    FT=F.T
    FFT = FT.dot(F)
    FFTI=np.linalg.inv(FFT)
    FFTIFT=FFTI.dot(FT)
    C=FFTIFT.dot(Yin)
    Yout=F.dot(C)
    print('Регресійна модель:')
    print('y(t) = ', C[0,0], ' + ', C[1,0], ' * t', ' + ', C[2,0], ' * t^2')
    return Yout

# ------------------------ МНК детекція та очищення АВ ------------------------------
def MNK_AV_Detect (S0):
    iter = len(S0)
    Yin = np.zeros((iter, 1))
    F = np.ones((iter, 3))
    for i in range(iter):  # формування структури вхідних матриць МНК
        Yin[i, 0] = float(S0[i])  # формування матриці вхідних даних
        F[i, 1] = float(i)
        F[i, 2] = float(i * i)
    FT=F.T
    FFT = FT.dot(F)
    FFTI=np.linalg.inv(FFT)
    FFTIFT=FFTI.dot(FT)
    C=FFTIFT.dot(Yin)
    return C[1,0]

# ---------------------------  МНК ПРОГНОЗУВАННЯ -------------------------------
def MNK_Extrapol (S0, koef):
    iter = len(S0)
    Yout_Extrapol = np.zeros((iter+koef, 1))
    Yin = np.zeros((iter, 1))
    F = np.ones((iter, 3))
    for i in range(iter):  # формування структури вхідних матриць МНК
        Yin[i, 0] = float(S0[i])  # формування матриці вхідних даних
        F[i, 1] = float(i)
        F[i, 2] = float(i * i)
    FT=F.T
    FFT = FT.dot(F)
    FFTI=np.linalg.inv(FFT)
    FFTIFT=FFTI.dot(FT)
    C=FFTIFT.dot(Yin)
    print('Регресійна модель:')
    print('y(t) = ', C[0, 0], ' + ', C[1, 0], ' * t', ' + ', C[2, 0], ' * t^2')
    for i in range(iter+koef):
        Yout_Extrapol[i, 0] = C[0, 0]+C[1, 0]*i+(C[2, 0]*i*i)   # проліноміальна крива МНК - прогнозування
    return Yout_Extrapol


# ------------------------------ Виявлення АВ за алгоритмом sliding window -------------------------------------
def Sliding_Window_AV_Detect_sliding_wind (S0, n_Wind):
    # ---- параметри циклів ----
    iter = len(S0)
    j_Wind=mt.ceil(iter-n_Wind)+1
    S0_Wind=np.zeros((n_Wind))
    Midi = np.zeros(( iter))
    # ---- ковзне вікно ---------
    for j in range(j_Wind):
        for i in range(n_Wind):
            l=(j+i)
            S0_Wind[i] = S0[l]
        # - Стат хар ковзного вікна --
        Midi[l] = np.median(S0_Wind)
    # ---- очищена вибірка  -----
    S0_Midi = np.zeros((iter))
    for j in range(iter):
        S0_Midi[j] = Midi[j]
    for j in range(n_Wind):
        S0_Midi[j] = S0[j]
    return S0_Midi

# -------------------------------- БЛОК ГОЛОВНИХ ВИКЛИКІВ ------------------------------

if __name__ == '__main__':

    # ------------------------------ Джерело вхідних даних ---------------------------

    print('Оберіть джерело вхідних даних та подальші дії:')
    print('1 - модель')
    print('2 - реальні дані')
    Data_mode = int(input('mode:'))

    if (Data_mode == 1):
        # ------------------------------ сегмент констант ---------------------------
        n = 10000
        iter = int(n)  # кількість реалізацій ВВ
        Q_AV = 3  # коефіцієнт переваги АВ
        nAVv = 10
        nAV = int((iter * nAVv) / 100)  # кількість АВ у відсотках та абсолютних одиницях
        dm = 0
        dsig = 5  # параметри нормального закону розподілу ВВ: середне та СКВ

        # ------------------------------ сегмент даних ---------------------------
        # ------------ виклики функцій моделей: тренд, аномального та нормального шуму  ----------
        S0 = Model(n)  # модель ідеального тренду (квадратичний закон)
        SAV = randomAM(n, iter)  # модель рівномірних номерів АВ
        S = randoNORM(dm, dsig, iter)  # модель нормальних помилок
        # ----------------------------- Нормальні похибки ------------------------------------
        SV = Model_NORM(S, S0, n)  # модель тренда + нормальних помилок
        Plot_AV(S0, SV, 'квадратична модель + Норм. шум')
        Stat_characteristics_in(SV, 'Вибірка + Норм. шум')
        # ----------------------------- Аномальні похибки ------------------------------------
        SV_AV = Model_NORM_AV(S0, SV, nAV, Q_AV)  # модель тренда + нормальних помилок + АВ
        Plot_AV(S0, SV_AV, 'квадратична модель + Норм. шум + АВ')
        Stat_characteristics_in(SV_AV, 'Вибірка з АВ')

    if (Data_mode == 2):

        # SV_AV = file_parsing('https://www.oschadbank.ua/rates-archive', 'Oschadbank (USD).xls', 'Купівля')  # реальні дані
        SV_AV = file_parsing('https://www.oschadbank.ua/rates-archive', 'Oschadbank (USD).xls', 'Продаж')  # реальні дані
        # SV_AV = file_parsing('https://www.oschadbank.ua/rates-archive', 'Oschadbank (USD).xls', 'КурсНбу')  # реальні дані

        S0 = SV_AV
        n = len(S0)
        iter = int(n)  # кількість реалізацій ВВ
        Plot_AV(SV_AV, SV_AV, 'Коливання курсу USD в 2022 році за даними Ощадбанк')
        Stat_characteristics_in(SV_AV, 'Коливання курсу USD в 2022 році за даними Ощадбанк')


    # ------------------- вибір функціоналу статистичного навчання -----------------------

    print('Оберіть функціонал процесів навчання:')
    print('1 - МНК згладжування')
    print('2 - МНК прогнозування')
    mode = int(input('mode:'))

    if (mode == 1):
        print('MNK згладжена вибірка очищена від АВ алгоритм sliding_wind')
        # --------------- Очищення від аномальних похибок sliding window -------------------
        n_Wind = 5  # розмір ковзного вікна для виявлення АВ
        S_AV_Detect_sliding_wind = Sliding_Window_AV_Detect_sliding_wind(SV_AV, n_Wind)
        Stat_characteristics_in(S_AV_Detect_sliding_wind, 'Вибірка очищена від АВ алгоритм sliding_wind')
        # --------------------------- МНК згладжування -------------------------------------
        Yout_SV_AV_Detect_sliding_wind = MNK(S_AV_Detect_sliding_wind)
        Stat_characteristics_out(SV_AV, Yout_SV_AV_Detect_sliding_wind,
                             'MNK згладжена, вибірка очищена від АВ алгоритм sliding_wind')
        # --------------- Оцінювання якості моделі та візуалізація -------------------------
        r2_score(S_AV_Detect_sliding_wind, Yout_SV_AV_Detect_sliding_wind, 'MNK_модель_згладжування')
        Plot_AV(Yout_SV_AV_Detect_sliding_wind, S_AV_Detect_sliding_wind,
                'MNK Вибірка очищена від АВ алгоритм sliding_wind')

    if (mode == 2):
        print('MNK ПРОГНОЗУВАННЯ')
        # --------------- Очищення від аномальних похибок sliding window -------------------
        n_Wind = 5  # розмір ковзного вікна для виявлення АВ
        koef_Extrapol = 0.5  # коефіціент прогнозування: співвідношення інтервалу спостереження до  інтервалу прогнозування
        koef = mt.ceil(n * koef_Extrapol)  # інтервал прогнозу по кількісті вимірів статистичної вибірки
        S_AV_Detect_sliding_wind = Sliding_Window_AV_Detect_sliding_wind(SV_AV, n_Wind)
        Stat_characteristics_in(S_AV_Detect_sliding_wind, 'Вибірка очищена від АВ алгоритм sliding_wind')
        # --------------------------- МНК екстраполяція -------------------------------------
        Yout_SV_AV_Detect_sliding_wind = MNK_Extrapol(S_AV_Detect_sliding_wind, koef)
        # --------- Статистичні характеристики екстраполяції та візуалізація ---------------
        Stat_characteristics_extrapol(koef, Yout_SV_AV_Detect_sliding_wind,
                             'MNK ПРОГНОЗУВАННЯ, вибірка очищена від АВ алгоритм sliding_wind')
        Plot_AV(Yout_SV_AV_Detect_sliding_wind, S_AV_Detect_sliding_wind,
                'MNK ПРОГНОЗУВАННЯ: Вибірка очищена від АВ алгоритм sliding_wind')



