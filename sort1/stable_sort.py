def is_stable_sort(original, sorted):
    for sorted1 in sorted:
        for sorted2 in sorted:
                for original1 in original:
                        for original2 in original:
                            if sorted1.value == sorted2.value and original1 == sorted2 and original2 == sorted1:
                                return False
