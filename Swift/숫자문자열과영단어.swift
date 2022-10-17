/* 중간고사 시험 대비를 위한 스위프트 문제 연습 
프로그래머스 숫자문자열과 영단어 */
import Foundation
let line: Dictionary<String,String> = ["zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"]
//일단 편안한 접근을 위해 딕셔너리를 생성
func solution(_ s:String) -> Int { //기본 설정 함수
    var result: String="" //문자열 형태로 담는 결과
    var word="" // 문자열을 숫자로 바꾸기 위한 temp변수
    for i in s.indices{ //숫자를 뽑아낸다.
        if s[i]>="0" && s[i]<="9"{ 
            result.append(s[i]) //결과값에 먼저 추가해줌. String형태라도 append형태로 추가가능
        }
        else{
            word.append(s[i]) //일단 word에 한글자씩 추가해주고
            for (key,value) in line{ //그 단어가 딕셔너리에 있는지 탐색
                if key==word{ //만약 단어가 존재하면
                    result.append(value) //그 단어를 result에 추가하고
                    word=""//temp변수는 초기화해준다.
                }
            }
            
        }
    }
    print(result) //확인 위한 출력
    var results=Int(result) //String->Int로 바꾸는 작업
    return results! //강제 추출 해야한다고 해서 ! 
}
