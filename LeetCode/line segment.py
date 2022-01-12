def cross_product(a, b):
    return a[0]*b[1] - a[1]*b[0]


def verify(ab, cd):
    ac_vec = [cd[0][0]-ab[0][0], cd[0][1]-ab[0][1]]
    ad_vec = [cd[1][0]-ab[0][0], cd[1][1]-ab[0][1]]
    ab_vec = [ab[1][0]-ab[0][0], ab[1][1]-ab[0][1]]

    sign_ac = cross_product(ac_vec, ab_vec)
    sign_ad = cross_product(ad_vec, ab_vec)

    case1 = sign_ac * sign_ad
    if case1 > 0:
        return False
    ca_vec = [-num for num in ac_vec]
    cb_vec = [ab[1][0]-cd[0][0], ab[1][1]-cd[0][1]]
    cd_vec = [cd[1][0]-cd[0][0], cd[1][1]-cd[0][1]]
    sign_ca = cross_product(ca_vec, cd_vec)
    sign_cb = cross_product(cb_vec, cd_vec)

    case2 = sign_ca * sign_cb
    if case2 > 0:
        return False

    if case1 == case2 == 0:
        a = ab
        b = cd
        a.sort()
        b.sort()
        if b[0][0] < a[0][0] < b[1][0] or b[0][0] < a[1][0] < b[1][0] or \
            b[0][1] < a[0][1] < b[1][1] or b[1][1] < a[1][1] < b[1][1]:
            return True
        else:
            return False



    print()
    return True


if __name__ == '__main__':
    # a = [[0, 0], [1, 1]]
    # b = [[1, 0], [0, 1]]

    a = [[0, 0], [1, 0]]
    b = [[0.5, 0], [4, 0]]
    print(verify(a, b))