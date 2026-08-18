import java.util.Scanner;

public class question_26229 {
	public static int turnCount(int from, int to) {
		return (to - from + 4) % 4;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++) {
			int n = sc.nextInt();
			int[][] board = new int[n][n];
			int[][] apples = new int[11][2];
			int maxApple = 0;
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					int num = sc.nextInt();
					if(num > 0) {
						apples[num][0] = i;
						apples[num][1] = j;
						maxApple += 1;
					}
					board[i][j] = num;
				}
			}
			int x = 0; int y=0;
			// 각 위치 돌면서 체크하기
			int turn = 0; // 누적 값 계산
 			int dir = 0;  // 현재 방향
			int vertical;
			int horizontal;
			
			for(int i=1; i<=maxApple; i++) {
				//위치에서 먼저 목표값을 가져온다.
				int targetX = apples[i][0];
				int targetY = apples[i][1]; 
				
				// 어떤 방향으로 이동시키는 것이 좋을까?
				if(targetX > x) {
					vertical = 1; // 아래
				} else {
					vertical = 3; // 위
				}
				
				if(targetY > y) {
					horizontal = 0; // 오른쪽
					
				} else {
					horizontal = 2; // 왼쪽
				}
				
				int cost1 = turnCount(dir, vertical) + turnCount(vertical, horizontal);
				int cost2 = turnCount(dir, horizontal) + turnCount(horizontal, vertical);
				
				if(cost1 < cost2) {
					turn += cost1;
					dir = horizontal;
					
				} else {
					turn += cost2;
					dir = vertical;
				}
				
				//처리 후 현재 값을 이전으로 이동시킴
				x = targetX;
				y = targetY;
				
			}
		System.out.println("#" + test_case + " " + turn);
		}
		
	}
}
