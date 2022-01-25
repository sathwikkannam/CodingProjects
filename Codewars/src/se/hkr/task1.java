package se.hkr;

import java.util.Hashtable;
import java.util.Map;

public class task1 {
    public StringBuilder getTranslated(String dna){
        Hashtable<String, String> map = new Hashtable<>();
        map.put("A", "T");
        map.put("C", "G");
        StringBuilder translated = new StringBuilder();
        for (int i = 0; i < dna.length(); i++) {
            String hash_value = map.get(String.valueOf(dna.charAt(i)));
            if(hash_value != null){
                translated.append(hash_value);
            }else {
                for (Map.Entry<String, String> keys : map.entrySet()) {
                    if(map.get(keys.getKey()).equals(String.valueOf(dna.charAt(i)))){
                        translated.append(keys.getKey());
                        break;
                    }
                }
            }
        }

        return translated;
    }
}
