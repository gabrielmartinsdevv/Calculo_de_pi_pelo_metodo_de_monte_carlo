import random
import math
import matplotlib.pyplot as plt

def estimate_pi(n):
    inside = 0
    xs_inside, ys_inside = [], []
    xs_out, ys_out = [], []
    for _ in range(n):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            inside += 1
            xs_inside.append(x)
            ys_inside.append(y)
        else:
            xs_out.append(x)
            ys_out.append(y)
    pi_est = (inside / n) * 4
    return pi_est, xs_inside, ys_inside, xs_out, ys_out


def plot_samples(xs_in, ys_in, xs_out, ys_out):
    plt.figure(figsize=(6,6))
    plt.scatter(xs_in, ys_in, color='blue',s=1,label='inside')
    plt.scatter(xs_out, ys_out, color='red',s=1,label='outside')
    circle = plt.Circle((0,0),1,color='green',fill=False)
    plt.gca().add_patch(circle)
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.gca().set_aspect('equal','box')
    plt.legend()
    plt.title('Monte Carlo PI estimation (quarter circle in first quadrant)')
    plt.show()


if __name__ == '__main__':
    n = 10000
    pi_est, xs_in, ys_in, xs_out, ys_out = estimate_pi(n)
    print(f"Estimated PI with n={n}: {pi_est}")
    print(f"Actual PI value: {math.pi}")
    plot_samples(xs_in, ys_in, xs_out, ys_out)