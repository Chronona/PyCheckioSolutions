#!/usr/local/bin/checkio --domain=py run flatten-list

# 
# END_DESC
#%%
der flat_list(array):
    array = [i for i in str(array) if i.isnumeric() or i == "-"]
    minus
    for i in array:
        if i == "-"
#%%
if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
# %%
flat_list([-1, [1, [-2], 1], -1])
# %%
"[1".isnumeric()
# %%
str([1])
# %%
