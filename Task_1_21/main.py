# -*- coding: utf-8 -*-

# main module
import sys
import utils
import logic

if __name__ == "__main__":
    # input
    try:
        if len(sys.argv) < 2:
            print("Enter the first list : ")
            nums1 = utils.getfrominput()
            print("Enter the second list : ")
            nums2 = utils.getfrominput()
        else:
            nums1, nums2 = utils.loadfromfile(sys.argv[1])
    except Exception as e:
        print("Data load error. Exception : " + str(e))
        exit()

    # logic
    try:
        print(logic.createlist(nums1, nums2))
    except Exception as e:
        print("Invalid data processing. May be data was corrupt. Exception : " + str(e))
