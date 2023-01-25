import numpy as np
import matplotlib.pyplot as plt

mod20_train = [83, 102, 90, 76, 77, 74, 79, 83, 107, 73, 73, 79, 76, 80, 78]  # train
sports1m_train = [80, 120, 40, 120, 40, 40, 40, 160, 80, 40, 160, 80, 240, 40, 40]
labels = ['backpacking', 'diving', 'cycling', 'boxing', 'figure skating', 'jetsprint', 'kayaking', 'motor biking', 
          'football', 'rock climbing', 'running', 'skateboarding', 'skiing', 'surfing', 'windsurfing']
mod20_test = [37, 44, 39, 34, 34, 33, 34, 36, 46, 32, 32, 34, 33, 35, 34]  # test
# sports1m_test = [80, 120, 40, 120, 40, 40, 40, 160, 80, 40, 160, 80, 240, 40, 40]

mod20 = np.array(mod20_train) + np.array(mod20_test)
sports1m = np.array(sports1m_train) * 5 // 4
print('========', np.sum(mod20), np.sum(sports1m))
x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars

fig, ax = plt.subplots(figsize=(20, 12))

mod20_rects = ax.bar(x - width/2, mod20, width, label='MOD20', color='cornflowerblue', edgecolor='black')
sports1m_rects = ax.bar(x + width/2, sports1m, width, label='Mini-Sports1M', color='lightsteelblue', edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Videos', size=38, weight='bold', fontproperties='Times New Roman')
ax.set_xlabel('Action Classes', size=38, weight='bold', fontproperties='Times New Roman')
# ax.set_title('Finetuning results based on supervised pretraining')
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=40, weight='bold', fontproperties='Times New Roman', rotation=45)
# ax.set_yticks()
ax.legend(loc='best', ncol=4, prop={'size': 24, 'family': 'Times New Roman', 'weight': 'bold'})
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