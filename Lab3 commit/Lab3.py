import numpy as np
from scipy.stats import t,f

def table_student(prob, f3):
    x_vec = [i*0.0001 for i in range(int(5/0.0001))]
    par = 0.5 + prob/0.1*0.05
    for i in x_vec:
        if abs(t.cdf(i, f3) - par) < 0.000005:
            return i


def table_fisher(prob, d, f3):
    x_vec = [i*0.001 for i in range(int(10/0.001))]
    for i in x_vec:
        if abs(f.cdf(i, 4-d, f3)-prob) < 0.0001:
            return i

def make_norm_plan_matrix(plan_matrix, matrix_of_min_and_max_x):
    X0 = np.mean(matrix_with_min_max_x, axis=1)
    interval_of_change = np.array([(matrix_of_min_and_max_x[i, 1] - X0[i]) for i in range(len(plan_matrix[0]))])
    X_norm = np.array(
        [[round((plan_matrix[i, j] - X0[j]) / interval_of_change[j], 3) for j in range(len(plan_matrix[i]))]
         for i in range(len(plan_matrix))])
    return X_norm


def cochran_check(Y_matrix):
    fisher = table_fisher(0.95, 1, (m - 1) * 4)
    mean_Y = np.mean(Y_matrix, axis=1)
    dispersion_Y = np.mean((Y_matrix.T - mean_Y) ** 2, axis=0)
    Gp = np.max(dispersion_Y) / (np.sum(dispersion_Y))
    if Gp < fisher/(fisher+(m-1)-2):
        return True
    return False


def students_t_test(norm_matrix, Y_matrix):
    mean_Y = np.mean(Y_matrix, axis=1)
    dispersion_Y = np.mean((Y_matrix.T - mean_Y) ** 2, axis=0)
    mean_dispersion = np.mean(dispersion_Y)
    sigma = np.sqrt(mean_dispersion / (N * m))
    betta = np.mean(norm_matrix.T * mean_Y, axis=1)
    f3 = (m - 1) * 4
    t = np.abs(betta) / sigma
    return np.where(t > table_student(0.95, f3))


def phisher_criterion(Y_matrix, d):
    if d == N:
        return False
    Sad = m / (N - d) * np.mean(check1 - mean_Y)
    mean_dispersion = np.mean(np.mean((Y_matrix.T - mean_Y) ** 2, axis=0))
    Fp = Sad / mean_dispersion
    f3 = (m - 1) * 4
    if Fp > table_fisher(0.95, d, f3):
        return False
    return True

def final():
    if cochran_check(Y_matrix):
        b_natura = np.linalg.lstsq(plan_matr, mean_Y, rcond=None)[0]
        b_norm = np.linalg.lstsq(norm_matrix, mean_Y, rcond=None)[0]
        check1 = np.sum(b_natura * plan_matr, axis=1)
        check2 = np.sum(b_norm * norm_matrix, axis=1)
        indexes = students_t_test(norm_matrix, Y_matrix)
        print("Матриця плану експерименту: \n", plan_matr)
        print("Нормована матриця: \n", norm_matrix)
        print("Матриця відгуків: \n", Y_matrix)
        print("Середні значення У: ", mean_Y)
        print("Натуралізовані коефіціенти: ", b_natura)
        print("Нормовані коефіціенти: ", b_norm)
        print("Перевірка 1: ", check1)
        print("Перевірка 2: ", check2)
        print("Індекси коефіціентів, які задовольняють критерію Стьюдента: ", np.array(indexes)[0])
        print("Критерій Стьюдента: ", np.sum(np.sum(b_natura[indexes] * plan_matr[:, indexes], axis=1), axis=1))
        if phisher_criterion(Y_matrix, np.size(indexes)):
            print("Рівняння регресії адекватно оригіналу.")
        else:
            print("Рівняння регресії неадекватно оригіналу.")
    else:
        global m
        m = m+1
        final()


matrix_with_min_max_x = np.array([[-40, 20], [5, 40], [-40, -20]])
m = 6
N = 4
plan_matr = np.array(
    [np.random.randint(-40, 20, size=N), np.random.randint(5, 40, size=N), np.random.randint(-40, -20, size=N)]).T
norm_matrix = make_norm_plan_matrix(plan_matr, matrix_with_min_max_x)
plan_matr = np.insert(plan_matr, 0, 1, axis=1)
norm_matrix = np.insert(norm_matrix, 0, 1, axis=1)
Y_matrix = np.random.randint(200 + np.mean(matrix_with_min_max_x, axis=0)[0],
                             200 + np.mean(matrix_with_min_max_x, axis=0)[1], size=(N, m))
mean_Y = np.mean(Y_matrix, axis=1)
final()

