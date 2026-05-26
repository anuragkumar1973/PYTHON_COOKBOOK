import itertools
import pandas as pd

# /Users/anuragkumar1973/Downloads/book_py_cookbk/chapter2/rec2_5.py
# Recipe 2.5. Find Ramanujan numbers between 1 and 30 using pandas to identify duplicates.

def find_max(df):
    df_max = pd.DataFrame()
    df_max['max_value'] = [df['array'].max()] if not df.empty else [None]
    print(f"Max Ramanujan value found between 1 and 30 : {df_max['max_value'].iloc[0]}")
    return df_max

def find_min(df):
    df_min = pd.DataFrame()
    df_min['min_value'] = [df['array'].min()] if not df.empty else [None]
    print(f"Min Ramanujan value found between 1 and 30: {df_min['min_value'].iloc[0]}")    
    return df_min


def main():
    # create list of sums of cubes for all 2-number combinations from 1..30 (a < b)
    arr = [a**3 + b**3 for a, b in itertools.combinations(range(1, 31), 2)]

    # use the provided pandas code to find duplicates
    df_arry = pd.DataFrame()
    df_arry['array'] = arr
    duplicates = df_arry[df_arry['array'].duplicated()]

    # print results
    print(f"Total combinations: {len(arr)}")
    print(f"Number of duplicate entries (excluding first occurrences): {len(duplicates)}")
    if not duplicates.empty:
        # show one example of duplicated values and how many times they occur in total
        dup_counts = df_arry['array'].value_counts()
        dup_values = dup_counts[dup_counts > 1]
        print("Values that occur more than once with their total counts:")
        print(dup_values)
        print("\nRows that are flagged as duplicated (exclude first occurrence):")
        print(duplicates.head(20))
    else:
        print("No duplicates found.")

    # find max and min using provided functions for Recipe 2.6
    df_max = find_max(duplicates)
    df_min = find_min(duplicates)  


if __name__ == "__main__":
    main()

main()