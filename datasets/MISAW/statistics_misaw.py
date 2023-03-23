import os

root = 'MISAW-Test-data/Procedural decription/'

ann_list_dir = os.listdir(root)
action_set = set()
state_shift = 0
pre_action = ''
num_frame = 0
action_dict = dict()
for annotation_file in ann_list_dir:
# annotation_file = '1_1_annotation.txt'

    ann_file = open(os.path.join(root, annotation_file), 'r')
    ann_content = ann_file.readlines()

    # print(len(ann_content))
    num_frame += len(ann_content)


    for line in ann_content:
        v_left = line.split('\t')[2]
        t_left = line.split('\t')[3]

        action = v_left + t_left
        action_set.add(action)



        if action != pre_action:
            state_shift += 1
            pre_action = action

            if action not in action_dict.keys():
                action_dict[action] = 1
            else:
                action_dict[action] += 1


print(len(action_set))
print(state_shift)
print(num_frame//30/3600)
print(num_frame//30/state_shift)

print('max: ', max(action_dict.values()))
print('min: ', min(action_dict.values()))

print(action_dict)


print(sum(action_dict.values()))
