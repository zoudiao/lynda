package generics;


/**
 * Created by eyifang on 2017/10/24.
 * @param <K>
 * @param <V>
 * generic class
 */

public class OrderedPair<K,V> implements Pair<K,V> {
    private final K key;
    private final V value;

    public OrderedPair(K key, V value) {
        this.key = key;
        this.value = value;
    }
    public K getKey() {return key;}
    public V getValue() {return value;}

}