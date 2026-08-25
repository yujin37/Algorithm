package study;

import java.util.Arrays;
import java.util.Scanner;

public class question_25679 {
	
	static int N;
	static int[][] board;
	static int poX, poY;
	static int result;
	static boolean[][] found;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};

	public static void main(String[] args) throws Exception {

	    Scanner sc = new Scanner(System.in);

	    int T = sc.nextInt();

	    for (int test_case = 1; test_case <= T; test_case++) {

	        N = sc.nextInt();
	        board = new int[N][N];
	        found= new boolean[N][N];
	        result = 0;

	        for (int i = 0; i < N; i++) {
	            for (int j = 0; j < N; j++) {

	                board[i][j] = sc.nextInt();

	                if (board[i][j] == 2) {
	                    poX = i;
	                    poY = j;
	                }
	            }
	        }

	        dfs(poX, poY, 0);
	        System.out.println("#" + test_case + " " + result);
	       
	        
	    }
	}

	

	static void dfs(int x, int y, int depth) {

	    if (depth == 3) {
	        return;
	    }

	    for (int d = 0; d < 4; d++) {

	        boolean jumped = false;

	        int nx = x + dx[d];
	        int ny = y + dy[d];

	        while (nx >= 0 && nx < N && ny >= 0 && ny < N) {

	            // 첫 번째 알
	            if (board[nx][ny] == 1) {

	                // 이미 하나 넘었다면
	                // 이 알은 잡을 수 있는 알
	                if (jumped) {

	                    if (!found[nx][ny]) {
	                        found[nx][ny] = true;
	                        result++;
	                    }
	                    board[nx][ny] = 0;
	                    dfs(nx, ny, depth + 1);
	                    board[nx][ny] = 1;
	                    break;
	                }

	                // 첫 번째 알을 넘음
	                jumped = true;
	            }

	            // 빈칸
	            else if (board[nx][ny] == 0) {

	                if (jumped) {

	                	
	                    dfs(nx, ny, depth + 1);
	                }
	            }

	            nx += dx[d];
	            ny += dy[d];
	        }
	    }
	}

}
