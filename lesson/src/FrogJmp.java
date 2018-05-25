public class FrogJmp {
    public static void main(String[] args) {
        System.out.println(solution(10,85, 30));
    }
    static int solution(int X, int Y, int D){
        return (Y-X)/D;
    }
}
