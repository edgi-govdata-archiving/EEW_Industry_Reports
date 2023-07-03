#[plot_visual_data_box_plot] creates a box plot given the the argument needed (tbl_arg)
#such as echoFAC_QTRS_WITH_NC.NOT A STRING with the titles and axis labels
def plot_visual_data_box_plot(tbl_arg, title, x_axis_title, y_axis_title):
  import math
  import numpy as np
  import matplotlib.pyplot as plt
  arr = []
  for x in tbl_arg:
    if math.isnan(x)== False:
      arr += [x]
  np_arr = np.array(arr)
  fig = plt.figure()
  fig.suptitle(title, fontsize=14, fontweight='bold')
  ax = fig.add_subplot(111)
  ax.boxplot(np_arr)
  ax.set_xlabel(x_axis_title)
  ax.set_ylabel(y_axis_title)
  plt.show()