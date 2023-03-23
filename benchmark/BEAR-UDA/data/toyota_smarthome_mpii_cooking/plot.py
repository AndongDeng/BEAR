import numpy as np
import matplotlib.pyplot as plt

toyota_train = [300, 225, 116, 2008, 291, 254] # train
mpii_train = [93, 105, 481, 17, 78, 14]

toyota_test = [199, 133, 88, 1309, 203, 107] # test
mpii_test = [2, 1, 132, 4, 10, 6]



labels = ['stir', 'wash objects', 'cut', 'eat(drink)', 'pour', 'cleaning up']


toyota = np.array(toyota_train) + np.array(toyota_test)
mpii = np.array(mpii_train) + np.array(mpii_test)
print('========', np.sum(toyota), np.sum(mpii))

x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars

fig, ax = plt.subplots(figsize=(15, 10))

mod20_rects = ax.bar(x - width/2, toyota, width, label='Toyota Smarthome', color='cornflowerblue', edgecolor='black')
sports1m_rects = ax.bar(x + width/2, mpii, width, label='MPII-Cooking', color='lightsteelblue', edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Videos', size=28, weight='bold', fontproperties='Times New Roman')
ax.set_xlabel('Action Classes', size=38, weight='bold', fontproperties='Times New Roman')
# ax.set_title('Finetuning results based on supervised pretraining')
ax.set_xticks(x)
ax.set_xticklabels(labels, weight='bold', fontproperties='Times New Roman', rotation=45, fontsize=30)
# ax.set_yticks()
ax.legend(loc='best', ncol=1, prop={'size': 24, 'family': 'Times New Roman', 'weight': 'bold'})
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
plt.tick_params(labelsize=24)

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', 
                    size=20, fontproperties='Times New Roman')


autolabel(mod20_rects)
autolabel(sports1m_rects)

fig.tight_layout()
# plt.grid(axis='y')
plt.show()