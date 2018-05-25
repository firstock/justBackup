import java.util.Scanner;
import javax.script.ScriptEngineManager;
import javax.script.ScriptEngine;

public class SameZero {
    public static void main(String[] args) throws Exception{
        Scanner reader= new Scanner(System.in);
        ScriptEngineManager mgr= new ScriptEngineManager();
        ScriptEngine engine= mgr.getEngineByName("JavaScript");


        int[] test= new int[10];

        int m= reader.nextInt();
        for(int i=0; i<m; i++){
            test[i]= reader.nextInt();
        }


        System.out.println(m);
        for(int i=0; i<m; i++){
            //System.out.println(test[i]);
            String formular= "";
            for(int j=1; j<= test[i]; j++){
                //System.out.println(j);
                formular+= j;
                if(j== test[i]) break;

            }
        }

        String calZero= "40 2";
        calZero= calZero.replaceAll("\\s+","");
        System.out.println(engine.eval(calZero));

        reader.close();
    }

    static String[] formularRet(int n){
        String[] res= new String[6561];
        final String[] OPER= {"+", "-", " "};
        for(int i= 1; i<=6561; i++){
            for(int j= 1; j< n; j++){
                res[i]+= j;
                for(String oper: OPER){
//                    res[i]+=
                }
            }
        }

        return res;
    }
}
