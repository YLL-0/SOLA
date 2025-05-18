def absolutno(seznam):
   
    return list(map(abs, seznam))
    """ return [abs(x) for x in seznam] """

seznam = [-1, -2, 0, 1, 2]
rezultat = absolutno(seznam)
print(rezultat)  

  
