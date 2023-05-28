import pytest
import sort_algo as s
import search_algo as se


# Используем декоратор для функции test_sorting_algo чтобы
# поочередно протестировать функции указанные в декораторе
@pytest.mark.parametrize('sorting_function', [
    s.selection_sort,
    s.insertion_sort,
    s.merge_sort,
    s.bubble_sort,
    s.cocktail_sort,
    s.shell_sort,
    s.quicksort
])
def test_sorting_algo(sorting_function):
    arr = [5, 3, 11, 24, 6, 3, 10]
    sorted_arr = sorting_function(arr)
    assert sorted_arr == [3, 3, 5, 6, 10, 11, 24]


# Используем декоратор для функции test_searching_algo чтобы
# поочередно протестировать функции указанные в декораторе
@pytest.mark.parametrize('searching_function', [
    se.binary_search,
    se.fibonacci_search,
    se.interpolation_search
])
def test_searching_algo(searching_function):
    value1 = 7
    value2 = -1
    arr = [1, 3, 5, 7, 9]
    res_ind1 = searching_function(arr, value1)
    res_ind2 = searching_function(arr, value2)
    assert res_ind1 == 3
    assert res_ind2 is None
