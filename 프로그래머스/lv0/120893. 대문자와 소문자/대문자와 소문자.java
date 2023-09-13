//toLowerCase 메서드사용하기 위해 문자타입, Character 클래스 사용
class Solution {
    public String solution(String my_string) {
        String answer = "";
        for(int i=0; i < my_string.length(); i++){
            if(Character.isUpperCase(my_string.charAt(i))){
                answer += Character.toLowerCase(my_string.charAt(i));
            } else {
                answer += Character.toUpperCase(my_string.charAt(i));
            }
        }
        
        return answer;
    }
}