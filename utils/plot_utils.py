import matplotlib.pyplot as plt

def plot_loss(losses, epoch):
  plt.plot(losses)
  plt.title("losses epoch %d" % (epoch))
  plt.show()
