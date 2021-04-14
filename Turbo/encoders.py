import numpy as np
from Turbo.helpers import bi2de,de2bi, size

def rsc_encoder(input,gen_func,trunc):
    n=gen_func.shape[0]
    K=gen_func.shape[1]
    init_state=np.arange(K-1)*0
    N=0
    p_b=[]
    tb=[]
    while N<=len(input)-1:
        ip=input[N]
        n_ip=np.mod(np.sum(np.append(ip,init_state)*gen_func[0]),2)

        for i in range(1,n):
            parity=np.mod(np.sum(np.append(n_ip,init_state)*gen_func[i]),2)
            p_b.append(parity)

        ns=np.append(n_ip,init_state[0:len(init_state)-1])
       
        init_state=ns
        
        
        N+=1
 
        
    padding=0
    if trunc==0:
        while bi2de(init_state)!=0 | N<len(input)+(K-1):

            ip=np.mod(np.sum(init_state*gen_func[0][1:K]),2)
            n_ip=np.mod(sum(np.append(ip,init_state)*gen_func[0]),2)
            for i in range(1,n):
                parity=np.mod(np.sum(np.append(n_ip,init_state)*gen_func[i]),2)
                p_b.append(parity)

            ns=np.append(n_ip,init_state[0:len(init_state)-1])
    
            init_state=ns 
            tb.append(ip)
            padding+=1
            N=N+1        
        
        input=np.append(input, tb)
    return input,p_b,init_state


def state_table(gen_func):
    k=1
    n,K=size(gen_func)
    M=K-1
    
    #generate 0/1 inputs
    inputs=np.arange(2**K)*0
    inputs[1::2] = 1
    
    
    newInputs=np.arange(2**K)*0
    
    #generate current states
    cs=np.floor(np.arange(2**(k*(K)))/2)
    cs=cs.astype(int)
    #print(cs)
    currentStates=de2bi(cs)
    nextStates=de2bi(cs.astype(int))
       
    #generate next states
    
    for j in range(2**K):
        asd=np.append(inputs[j], currentStates[j])
        zz=np.mod(np.sum(asd*gen_func[0]),2)
        newInputs[j]=zz
        nextStates[j]=np.append(newInputs[j], currentStates[j][0:(M-1)])
    
    #generate outputs
    #print(currentStates)
    outputs=np.zeros((2**K,2),dtype=int)
    #print(outputs)
    
    for i in range(1,n):
        for j in range(len(inputs)):
            op=np.mod(np.sum(gen_func[i]*np.append(newInputs[j], currentStates[j])),2)
            outputs[j] =np.append(inputs[j], op)  
     
    return {"ip":inputs,"cs":currentStates,"ns":nextStates,"op":outputs}

def state_transitions(gen_func):
    n,K=size(gen_func)
    #node_transitions=np.zeros((2**K,2))
    st=state_table(gen_func)
    current=bi2de(st['cs'],'left-msb')
    next_state=bi2de(st['ns'],'left-msb')
    node_transitions=np.concatenate((current,next_state),axis=1)
    return node_transitions
    
        
   

        