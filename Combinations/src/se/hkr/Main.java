package se.hkr;

import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        ArrayList<String> combinations = new ArrayList<>();
        Hashtable<String, String> map = new Hashtable<>();
        Main app = new Main();
        map.put("2", "abc");
        map.put("3", "def");
        map.put("4", "ghi");
        map.put("5", "jkl");
        map.put("6", "mno");
        map.put("7", "pqrs");
        map.put("8", "tuv");
        map.put("9", "wxyz");

        ArrayList<String> allWords = app.readWords("src/se/hkr/words.txt");

        Scanner input = new Scanner(System.in);
        System.out.print("Enter a number: ");

        String checkedInput = app.checkInput(input.nextInt());

        app.findCombo(checkedInput, map, combinations, 0, "");

        System.out.printf("%s : %d%n%s%n", "Combinations", combinations.size(), "Possible Words:");
        for (String word: app.checkPossibleWords(combinations, allWords)) {
            System.out.println(word);

        }

    }

    public String checkInput(int input) {
        String strInput = String.valueOf(input);
        strInput = strInput.replaceAll("0", "");
        strInput = strInput.replaceAll("1", "");

        return strInput;

    }



    public void findCombo(String number, Hashtable<String, String> map, ArrayList<String> combinations, int index, String oldCombinations){
        if((number.length() == 0) || index == number.length()){
            combinations.add(oldCombinations);
            return;

        }

        String currentAlphabets = map.getValue(String.valueOf(number.charAt(index)));

        for (int i = 0; i < currentAlphabets.length(); i++) {
            findCombo(number, map, combinations, index+1, oldCombinations+currentAlphabets.charAt(i));

        }

    }

    public ArrayList<String> checkPossibleWords(ArrayList<String> combinations, ArrayList<String> words){
        ArrayList<String> checkedWords = new ArrayList<>();
        for (String combination: combinations) {
            for (String word: words) {
                if(combination.contains(word) && combination.length() == word.length()){
                    checkedWords.add(word);
                }

            }
        }
        return checkedWords;
    }

    public ArrayList<String> readWords(String path){
        ArrayList<String> words = new ArrayList<>();
        File file = new File(path);

        try(BufferedReader reader = new BufferedReader(new FileReader(file))){
            String i;
            while((i = reader.readLine()) !=null){
                words.add(i);
            }
        }catch(IOException e){
            e.printStackTrace();
        }

        return words;

    }
}
