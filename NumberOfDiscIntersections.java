// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");
import java.util.*;

class NumberOfDiscIntersections {

    public int solution(int[] A) {
        ArrayList<Pair<Long, String>> arr = new ArrayList<Pair<Long, String>>();
        for(int i = 0; i < A.length; i++) {
            arr.add(new Pair<Long, String>(i - Long.valueOf(A[i]), "start"));
            arr.add(new Pair<Long, String>(i + Long.valueOf(A[i]), "end"));
        }
        Collections.sort(arr);
        int active_discs = 0;
        int intersect_sum = 0;
        for(int i = 0; i < arr.size(); i++) {
            Pair<Long, String> pair = arr.get(i);
            if (pair.value.equals("start")) {
                intersect_sum += active_discs;
                active_discs++;
            } else {
                active_discs--;
            }
        }
        return intersect_sum > 10000000 ? -1 : intersect_sum;  //stupid codility task requirement
    }

    class Pair<K extends Comparable<? super K>,V> implements Comparable<Pair<K,?>>{
        public K key;
        public V value;
        
        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }
        
        public String toString() {
            return "[ " + key + ", " + value + " ]";
        }
        public int compareTo(Pair<K,?> other) {
            int result = this.key.compareTo(other.key);
            if (result < 0) {
                return -1;
            } else if (result > 0) {
                return 1;
            }
            else if (this.value.equals(other.value)) {
                return 0;
            }
            else if (this.value.equals("start")) {
                    return -1;
            }
            else {
                return 1;
            }
            
        }
    }
}