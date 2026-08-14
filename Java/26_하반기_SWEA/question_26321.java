package study;

import java.util.Arrays;
import java.util.Scanner;

public class question_26321 {
	static boolean[] monsterVisited;
	static boolean[] customerVisited;
	static int[][] board;
	static int[][] monster;
	static int[][] customer;
	static int result;
	
	public static void dfs(int x, int y, int time) {
		
		boolean allVisited = true;

		for(int i = 1; i <= 4; i++) {
		    if(!monsterVisited[i] || !customerVisited[i]) {
		        allVisited = false;
		        break;
		    }
		}

		if(allVisited) {
		    result = Math.min(result, time);
		    return;
		}
		
		for(int i=1; i<=4; i++) {
			if(!monsterVisited[i]) {
				monsterVisited[i] = true;
				int dist = Math.abs(x-monster[i][0]) + 
						Math.abs(y-monster[i][1]);
				dfs(monster[i][0], monster[i][1], time+dist);
				monsterVisited[i] = false;
			} 
			if(monsterVisited[i] && !customerVisited[i]) {
				customerVisited[i] = true;
				
				int dist = Math.abs(x - customer[i][0])
				         + Math.abs(y - customer[i][1]);

				dfs(customer[i][0], customer[i][1], time + dist);
				customerVisited[i] = false;
			}
		}
		
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int test_case=1; test_case <= T; test_case++) {
			int n = sc.nextInt();
			result = Integer.MAX_VALUE;
			
			board = new int[n][n];
			monster = new int[5][2];
			customer = new int[5][2];
			
			monsterVisited = new boolean[5];
			customerVisited = new boolean[5];
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					board[i][j] = sc.nextInt();
					
					if(board[i][j] > 0) {
						int num = board[i][j];
						monster[num][0] = i;
						monster[num][1] = j;
					} else if (board[i][j] < 0) {
					    int num = -board[i][j];
					    customer[num][0] = i;
					    customer[num][1] = j;
					}
				}
			}
			
			dfs(0,0, 0);
			System.out.println("#" + test_case + " " + result);
		}
	}

}
