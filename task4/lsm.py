def least_square_method(x_, y_):
    x_size = len(x_)
    if x_size != len(y_):
        print("wrong dementions!")
        return
    y_size = x_size
    x_mean = sum(x_)/x_size
    y_mean = sum(y_)/y_size
    xy_ = sum([x_[i] * y_[i] for i in range(x_size)])
    xx_ = sum([x_[i]**2 for i in range(x_size)])
    b = (xy_ - y_mean) / (xx_ - x_mean)
    a = y_mean - b * x_mean
    return {"a1": a, "a0": b}