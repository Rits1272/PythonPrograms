#Function for removing common characters
# with their respective occurences.

def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            # if common character is found
            # then remove that character
            # and return list of concatenated
            # list with True Flag.
            if list1[i] == list2[j]:
                c = list1[i]

                # remove character from the list
                list1.remove(c)
                list2.remove(c)

                # concatenation of two list elements with
                # * is act as a border mark here
                list3 = list1 + ["*"] + list2

                # return the concatenated list with True flag
                return [list3, True]

    # No common characters is found
    # return the concatenated list with
    # False flag
    list3 = list1 + ['*'] + list2
    return [list3, False]

# Driver code

if __name__ == '__main__':

    # take first name
    p1 = input("Player 1 name : ")
    p1 = p1.lower()
    p1.replace(" ",'')

    p1_list = list(p1)

    # take second name
    p2 = input('Player 2 name : ')
    p2 = p2.lower()
    p2.replace(" ",'')
    p2_list = list(p2)

    # Taking a flag as True initially.
    proceed = True

    # Keep calling remove_match_char function
    # until common characters is found or keep
    # looping until proceed flag becomes True

    while proceed:
        # function calling and store return value
        ret_list = remove_match_char(p1_list, p2_list)

        # take out concatenated list from return list
        con_list = ret_list[0]

        # take out the flag value
        proceed = ret_list[1]

        star_index = con_list.index('*')

        p1_list = con_list[:star_index]
        p2_list = con_list[star_index + 1:]

    # count remaining letters:
    count = len(p1_list) + len(p2_list)

    # list of FLAMES acronym
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    # Keeping looping until only one item
    # is not remaining in the remaining list.

    while(len(result) > 1):
        split_index = (count % len(result))

        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[:split_index]

            result = right + left
        else:
            result = result[:len(result)]
    # print final result
    print("Relationship status : ", result[0])


















            















        


        
        











    
    












    
