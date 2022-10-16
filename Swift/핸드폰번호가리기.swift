/* 중간고사 시험 대비를 위한 스위프트 문제 연습 
프로그래머스 핸드폰번호 가리기 */
func solution(_ phone_number:String) -> String {
    var n: Int = phone_number.count
    n-=4

    var phone=Array(phone_number)
    for i in 0..<n{
        phone[i]="*"
    }

    return String(phone)
}
