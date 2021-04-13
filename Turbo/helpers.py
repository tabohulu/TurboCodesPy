import numpy as np
    
def generator_function(num,denum):
    gen_funcs_octal=np.array([[denum],[num]],dtype=int)
    gen_funcs_dec=(np.floor(gen_funcs_octal/10)*8+(np.remainder(gen_funcs_octal,10))).astype(int)
    return bi2de(gen_funcs_dec)

def bi2de(decimal_vector):
    binary_repr_v=np.vectorize(np.binary_repr)
    gen_func=binary_repr_v(np.array(decimal_vector,dtype=int)).astype(int)
    bin_list=[]
    
    for i in range(decimal_vector.shape[0]):
        for j in range(decimal_vector.shape[1]):
            bin_list.append(list(map(int,str(gen_func[i][j])))) 
    return np.array(bin_list)

def de2bi(binary_vector):
    decimal_vector=np.zeros((binary_vector.shape[0],1),dtype=int)
    for row in range(binary_vector.shape[0]):
        dec_num=0

        for col in range(binary_vector.shape[1]-1,-1,-1):
            dec_num+=binary_vector[row][col]*2**col
        decimal_vector[row][0]=dec_num
    return decimal_vector    
            


