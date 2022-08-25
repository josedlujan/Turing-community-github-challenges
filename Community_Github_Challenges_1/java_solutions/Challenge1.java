package Community_Github_Challenges_1.java_solutions;

public class Challenge1{
    public static int highestDigit(int num){
        int result = 0;
        while(num>0){
            if(num % 10 > result){
                result = num % 10;
            }
            num = num / 10;
        }
        return result;
    }
}