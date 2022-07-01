import java.io.*;
import java.util.*;

class Node {
	int data;
	Node next;
	Node(int d) {
        data = d;
        next = null;
    }
}

class Main {
    public static  Node insert(Node head, int data) {
    	Node topHead;
    	if (head == null) {
    		topHead = head = new Node(data);
    	} else {
    		topHead = head;
	    	while (head.next != null) {
	    		head = head.next;
	    	}
	    	head.next = new Node(data);
	    	head.next.next = null;
    	}
    	return topHead;
    }

	public static void display(Node head) {
        Node start = head;
        while(start != null) {
            System.out.print(start.data + " ");
            start = start.next;
        }
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Node head = null;
        int N = sc.nextInt();

        while(N-- > 0) {
            int ele = sc.nextInt();
            head = insert(head,ele);
        }
        display(head);
        sc.close();
    }
}