import numpy as np
    
def generator_function(num,denum):
    gen_funcs_octal=np.array([[denum],[num]],dtype=int)
    gen_funcs_dec=(np.floor(gen_funcs_octal/10)*8+(np.remainder(gen_funcs_octal,10))).astype(int)
    return de2bi(gen_funcs_dec.astype(int))

def de2bi(decimal_vector):
    aa=np.max(decimal_vector)
    binary_repr_v=np.vectorize(np.binary_repr)
    ab=binary_repr_v(aa)
    #binary_repr_v(a,4)
    width=int(len(str(ab)))
    gen_func=binary_repr_v(decimal_vector,width)
    #print(gen_func)
    
    
    bin_list=[]
    
    for i in range(decimal_vector.shape[0]):
        if decimal_vector.ndim > 1:
            #print('we here')
            for j in range(decimal_vector.shape[1]):
                bin_list.append(list(map(int,str(gen_func[i][j]))))
        else:
            #print('nah fam')
            bin_list.append(list(map(int,str(gen_func[i]))))
    
    aa=np.array(bin_list)

    return aa

def bi2de(binary_vector,significant_bit='right-msb'):
    #print(significant_bit)
    if significant_bit=='right-msb' and binary_vector.ndim>1:
        rr=range(binary_vector.shape[1]-1,-1,-1)
        decimal_vector=np.zeros((binary_vector.shape[0],1),dtype=int)
        for row in range(binary_vector.shape[0]):
            dec_num=0
            index=binary_vector.shape[1]-1
            for col in rr:
                dec_num+=binary_vector[row][index]*2**col
                index-=1
                #print(binary_vector[row][col],2,col)
            decimal_vector[row][0]=dec_num
    elif significant_bit=='left-msb' and binary_vector.ndim>1:
        rr=range(0,binary_vector.shape[1])
        decimal_vector=np.zeros((binary_vector.shape[0],1),dtype=int)
        for row in range(binary_vector.shape[0]):
            dec_num=0
            index=binary_vector.shape[1]-1
            for col in rr:
                dec_num+=binary_vector[row][index]*2**col
                index-=1
            decimal_vector[row][0]=dec_num
    elif significant_bit=='right-msb' and binary_vector.ndim==1:
        rr=range(binary_vector.shape[0]-1,-1,-1)
        decimal_vector=np.arange(1)*0
        dec_num=0
        index=0
        for row in rr:
            
            dec_num+=binary_vector[row]*2**index
            #print(binary_vector[row],2,index)
            index+=1
        decimal_vector[0]=dec_num
    elif significant_bit=='left-msb' and binary_vector.ndim==1:
        rr=range(0,binary_vector.shape[0])
        decimal_vector=np.arange(1)*0
        dec_num=0
        index=binary_vector.shape[0]-1
        for row in rr:
            
            dec_num+=binary_vector[row]*2**index
            #print(binary_vector[row],2,index)
            index-=1
        decimal_vector[0]=dec_num    
    

    
        

    #print(decimal_vector,binary_vector)
    return decimal_vector

def size(array):
    if array.ndim >1:
        return array.shape[0],array.shape[1]
    else:
        return 1, array.shape[0]            
            


