import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PE052 {
    public static void main (String [] args)
    {
        for(int i=1; ; i++){
            List<Character> L = new ArrayList<Character>();
            String s = (new Integer(i)).toString();
            for(int k=0; k < s.length(); k++) {
                L.add(s.charAt(k));
            }
            Collections.sort(L);
            int j;
            for(j = 2; j <= 6; j++){
                s = new Integer(i*j).toString();
                List<Character> l = new ArrayList<Character>();
                for(int k=0; k < s.length(); k++) {
                    l.add(s.charAt(k));
                    
                }
                Collections.sort(l);
                if(!l.equals(L)){
                    break;
                }
            }
            if(j == 7){
                System.out.println(i);
                break;
            }
        }
    }
}
