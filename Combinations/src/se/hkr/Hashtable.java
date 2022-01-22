package se.hkr;

import java.util.Arrays;

public class Hashtable <T,K>{
    T[] keys;
    K[] values;
    private int index = 0;

    @SuppressWarnings("unchecked")
    public Hashtable(){
        keys = (T[]) new Object[10];
        values = (K[]) new Object[10];
    }

    public void put(T key, K value){

        if((index == 10)){
            grow();
        }
        keys[index] = key;
        values[index] = value;

        index++;

    }

    public void grow(){
        keys = Arrays.copyOf(keys, keys.length);
        values = Arrays.copyOf(values, values.length);
    }


    public K getValue(T key){
        K value = null;
        try{
            if(values[Arrays.asList(keys).indexOf(key)] != null){
                value = values[Arrays.asList(keys).indexOf(key)];
            }
        }catch(IndexOutOfBoundsException e){
            e.printStackTrace();
        }
        return value;
    }

    public T getKey(K value){
        T key = null;
        try{
            if(keys[Arrays.asList(values).indexOf(value)]!= null){
                key = keys[Arrays.asList(values).indexOf(value)];
            }
        }catch(IndexOutOfBoundsException e){
            e.printStackTrace();
        }
        return key;
    }
}
