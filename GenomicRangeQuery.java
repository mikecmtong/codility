// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");
import java.util.HashMap;
import java.util.Arrays;
class GenomicRangeQuery {
    public static int[] solution(String S, int[] P, int[] Q) {
        // write your code in Java SE 8
    int N = S.length();
    int M = P.length;
    int[][] impact = new int[4][N];
    HashMap<Character, Integer> genome_map = new HashMap<Character, Integer>();
    //initial values
    genome_map.put('A', 0);
    genome_map.put('C', 1);
    genome_map.put('G', 2);
    genome_map.put('T', 3);

    //load sums
    impact[genome_map.get(S.charAt(0))][0] = 1; 
    for (int j = 1; j < N; j++) {
        for (int i = 0; i < 4; i++) {
            if (genome_map.get(S.charAt(j)) == i) {
                impact[i][j] = impact[i][j-1] + 1;
            } else {
                impact[i][j] = impact[i][j-1];
            }
        }
    }

    //queries
    int[] out_array = new int[M];
    for (int k = 0; k < M; k++) {
        for (int i = 0; i < 4; i++) {
            int lower_value = P[k]-1>=0 ? impact[i][P[k]-1] : 0;
            if (impact[i][Q[k]] - lower_value > 0) {
                out_array[k] = i+1;
                break;
            }
        }
    }
    return out_array;
    }

    public static void main(String[] args) {
        String S = "CAGCCTA"; System.out.println("String: " + S);
        int[] P = new int[]{2, 5, 0}; 
        int[] Q = new int[]{4, 5, 6};
        System.out.println(Arrays.toString(solution(S, P, Q)));
    }
}