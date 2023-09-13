class Solution {
    public int solution(int[] box, int n) {
        int answer = 0;
        
        int a = 0;
        int b = 0;
        int c = 0;
        
        a = box[0] / n;
        b = box[1] / n;
        c = box[2] / n;
        
        answer = a*b*c;
        
        return answer;
    }
}