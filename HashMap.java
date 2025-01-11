import java.util.LinkedList;
public class HashMap<K, V> {
    // Node class to represent the key-value pair
    private class Node{
        K key;
        V value;

        Node(K key, V value){
            this.key = key;
            this.value = value;
        }
    }

    // Array of LinkedList to serve as buckets
    private LinkedList<Node>[] table;
    private int size;

    // Constructor to initialize the hash table
    @SuppressWarnings("unchecked")
    public HashMap(int tableSize){
        size = tableSize;
        table = new LinkedList[tableSize];
    
        // initialize each bucket as empty LinkedList
        for(int i = 0; i < size; i++){
            table[i] = new LinkedList<>();
        }
    }

    // Hash function to compute the index
    private int hashFunction(K key){
        return Math.abs(key.hashCode()) % size;
    }

    // Insert a key-value pair into the hash table
    public void put(K key, V value){
        int index = hashFunction(key);
        LinkedList<Node> bucket = table[index];

        // Check if the key already exists
        for(Node node : bucket){
            if(node.key.equals(key)){
                // Update the value if the key already exists
                node.value = value;
                return;
            }
        }

        // Add the key-value pair to the bucket
        bucket.add(new Node(key, value));
    }

    // Retrive the value associated with the key
    public V get(K key){
        int index = hashFunction(key);
        LinkedList<Node> bucket = table[index];

        // Search for the key in the bucket
        for(Node node : bucket){
            if(node.key.equals(key)){
                return node.value;
            }
        }

        // Return null if the key is not found
        return null;
    }

    // Remove the key-value pair from the hash table
    public void remove(K key){
        int index = hashFunction(key);
        LinkedList<Node> bucket = table[index];

        for(Node node : bucket){
            if(node.key.equals(key)){
                bucket.remove(node);
                return;
            }
        }

        System.out.println("Key not found, cannot remove");
    }

    public void display() {
        for (int i = 0; i < size; i++) {
            System.out.print("Bucket " + i + ": ");
            for (Node node : table[i]) {
                System.out.print("[" + node.key + ": " + node.value + "] ");
            }
            System.out.println();
        }
    }

    // Main function for demonstration
    public static void main(String[] args) {
        // Create a HashMap with 10 buckets
        HashMap<Integer, String> hashMap = new HashMap<>(10);

        // Insert key-value pairs
        hashMap.put(1, "Value1");
        hashMap.put(2, "Value2");
        hashMap.put(11, "CollisionValue"); // This will collide with key 1
        hashMap.put(3, "Value3");

        // Display the hash table
        System.out.println("Hash Table Contents:");
        hashMap.display();

        // Retrieve values by keys
        System.out.println("Get key 1: " + hashMap.get(1));
        System.out.println("Get key 2: " + hashMap.get(2));
        System.out.println("Get key 11: " + hashMap.get(11));

        // Remove a key
        hashMap.remove(2);
        System.out.println("After removing key 2:");
        hashMap.display();
    }
}
