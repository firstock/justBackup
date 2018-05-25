import java.util.Scanner;

public class Test1 {
//    000~222, 0000 ~ 2222, ... , 00000000 ~ 22222222
//    1st, easy case
    public static void main(String[] args) {
        Scanner reader= new Scanner(System.in);
        int n= reader.nextInt();


//        for(int i=0; i<n; i++){
//            for(int j=0; j<=2; j++){
//                System.out.print(j);
//            }
//            System.out.println();
//        }

        int num= (int)(Math.pow(3.0, n)) - 1;
        System.out.println(num);

//        for(int i=0; i<= num; i++){
//            System.out.print((int)(i/3/3)%3);
//            System.out.print((int)(i/3)%3);
//            System.out.print(i%3);
//            System.out.println();
//        }

        for(int i=0; i<= num; i++){
            System.out.println(convert3(i));
        }


    }

    static int convert3(int m){
        int[] T= {0,1,2};
        int q= (m/3);
        int r= m%3;

        if(0== q)
            return T[r];
        else
            return convert3(q)+T[r];
    }
}
