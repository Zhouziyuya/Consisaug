import numpy as np

def f1(precision, recall):
    f1_score = (2*precision*recall)/(precision+recall)
    return f1_score


def f2(precision, recall):
    f2_score = (5*precision*recall)/(4*precision+recall)
    return f2_score

def l1_norm(x):
    norm = np.abs(x).sum()
    if norm == 0:
        return x
    else:
        return x / norm

if __name__ == "__main__":
    a = f2(0.557, 0.395)
    print(a)
    # print(l1_norm([5, 1, 1, 10]))