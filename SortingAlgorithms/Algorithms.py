
# Bubble Sort Algorithm Function

def bubbleSort(array, ascending=False, steps=False):

    if ascending == True and steps == True:
        for i in range(len(array)):
            print("step {}:-" .format(i+1))
            for j in range(0, len(array) - i - 1):
                print("j = {} : {} ".format(j, array))
                # sorting in ascending order
                if array[j] > array[j + 1]:
                    # swapping
                    array[j], array[j + 1] = array[j + 1], array[j]
                    print("Swapping: {} with {} ".format(array[j], array[j+1]))
            print("\n")
        else:
            return array

    elif ascending == False and steps == True:
        for i in range(len(array)):
            print("step {}:-" .format(i+1))
            for j in range(0, len(array) - i - 1):
                print("j = {} : {} ".format(j, array))
                # sorting in descending order
                if array[j] < array[j + 1]:
                    # swapping
                    array[j], array[j + 1] = array[j + 1], array[j]
                    print("Swapping: {} with {} ".format(array[j], array[j+1]))
            print("\n")
        else:
            return array

    elif ascending == True and steps == False:
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):

                # sorting in ascending order
                if array[j] > array[j + 1]:

                    # swapping
                    array[j], array[j + 1] = array[j + 1], array[j]
        else:
            return array

    else:
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):

                # sorting in descending order
                if array[j] < array[j + 1]:

                    # swapping
                    array[j], array[j + 1] = array[j + 1], array[j]
        else:
            return array


# Selection Sort Algorithm Function


def selectionSort(array, ascending=False, steps=False):
    size = len(array)
    if ascending == True and steps == True:
        for i in range(size):
            min_index = i
            print("step {}:-" .format(i+1))

            for j in range(i + 1, size):

                print("j = {} : {} , Min Value Index: {} ".format(
                    j, array, min_index))

                # sorting in ascending order
                if array[j] < array[min_index]:
                    min_index = j
            # swapping
            array[i], array[min_index] = array[min_index], array[i]
            print("Swapping: {} with {} ".format(array[i], array[min_index]))
            print("\n")
        else:
            return array

    elif ascending == True and steps == False:
        for i in range(size):
            min_index = i
            for j in range(i + 1, size):

                # sorting in ascending order
                if array[j] < array[min_index]:
                    min_index = j
            # swapping
            array[i], array[min_index] = array[min_index], array[i]
        else:
            return array

    elif ascending == False and steps == True:
        for i in range(size):
            max_index = i
            print("step {}:-" .format(i+1))
            for j in range(i + 1, size):

                print("j = {} : {} , Max Value Index: {} ".format(
                    j, array, max_index))

                # sorting in descending order
                if array[j] > array[max_index]:
                    max_index = j
            print("\n")
            # swapping
            array[i], array[max_index] = array[max_index], array[i]
        else:
            return array

    else:
        for i in range(size):
            min_index = i
            for j in range(i + 1, size):

                # sorting in descending order
                if array[j] > array[min_index]:
                    min_index = j
            # swapping
            array[i], array[min_index] = array[min_index], array[i]
        else:
            return array

# Insertion Sort Algorithm Function


def insertionSort(array, ascending=False, steps=False):

    if ascending == True and steps == True:
        for i in range(1, len(array)):
            print("step {}:-" .format(i))
            key = array[i]
            j = i - 1

            while j >= 0 and key < array[j]:
                print("{} ".format(array))

                array[j + 1] = array[j]
                j = j - 1

            array[j + 1] = key
            print("Key = {} ".format(key))

            print("\n")
        else:
            return array

    elif ascending == True and steps == False:
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1

            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key
        else:
            return array

    elif ascending == False and steps == True:
        for i in range(1, len(array)):
            print("step {}:-" .format(i))
            key = array[i]
            j = i - 1

            while j >= 0 and key > array[j]:
                print("{} ".format(array))

                array[j + 1] = array[j]
                j = j - 1
            else:
                print(array)

            array[j + 1] = key
            print("Key = {} ".format(key))
            print("\n")
        else:
            return array

    else:
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1

            while j >= 0 and key > array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key
        else:
            return array
