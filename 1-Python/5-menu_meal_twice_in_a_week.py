def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
     index=0
     result = False
     for elem_primary in meals:
         print("Indice primario: " + str(index))
         index += 1
         if index == len(meals):
             break
         for index_second in range(index,len(meals)):
             print("Indice secundario: " + str(index_second))
             if elem_primary == meals[index_second]:
                 result = True
    
    
     return result
        
