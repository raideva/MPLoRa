from image_classification.main import cal_obs

def add_loss(st:str, d, hr, ht, di):
    # q = ['distance_from_receiver','height', 'no_walls']
    a = 0
    w = cal_obs(st)
    # print(w)
    for i in range(len(w)):
        h = (hr * di[i] + ht * (d - di[i])) / d
        if h <= w[i][0]:
            a += (w[i][1] * 1.57) / 10
    return a