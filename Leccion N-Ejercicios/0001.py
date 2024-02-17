# Solution number: 0001 

def make_histograms(numbers: list[int]) -> int:
    for number in numbers:
        print(f"{number} -> {number*'#'}")
              

make_histograms([1, 2, 3, 4, 5, 6, 7, 8, 9])              

